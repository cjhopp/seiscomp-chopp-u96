/***************************************************************************
 * Copyright (C) 2011 by gempa GmbH
 *
 * Author: Jan Becker
 * Email: jabe@gempa.de
 ***************************************************************************/


#ifndef __GEMPA_SPECTROGRAM_SPECTROGRAM_H__
#define __GEMPA_SPECTROGRAM_SPECTROGRAM_H__


#include <seiscomp3/core/typedarray.h>
#include <seiscomp3/core/record.h>
#include <seiscomp3/math/filter.h>


namespace Gempa {
namespace Gui {


template <typename T> class Spectrogram;
template <typename T> class RecordSpectrogram;

typedef Spectrogram<float> SpectrogramF;
TYPEDEF_SMARTPOINTER(SpectrogramF);
TYPEDEF_CONST_SMARTPOINTER(SpectrogramF);

typedef Spectrogram<double> SpectrogramD;
TYPEDEF_SMARTPOINTER(SpectrogramD);
TYPEDEF_CONST_SMARTPOINTER(SpectrogramD);


struct SpectrogramSettings {
	enum Unit {
		Hz,
		Seconds
	};

	SpectrogramSettings();

	bool fromString(const std::string &def);

	double bandStart;   // Start of (freq or period) band
	double bandEnd;     // End of (freq or period) band
	Unit   bandUnit;    // Unit of start/end (frequenz or period)

	int    ranges;      // Number of ranges to subdivide the band
	int    bands;       // Number of overlapping bands

	bool   logarithmic; // logarithmic ranges
};


template <typename T>
class Spectrogram : public Seiscomp::Core::BaseObject {
	public:
		typedef Seiscomp::TypedArray<T> DataArray;
		typedef typename Seiscomp::Core::SmartPointer<DataArray>::Impl DataArrayPtr;


	public:
		Spectrogram();
		Spectrogram(const SpectrogramSettings &settings);
		~Spectrogram();


	public:
		void init(const SpectrogramSettings &settings);
		void initFrom(const Spectrogram<T> &other);

		void setMaximumSeconds(double secs);

		void setSamplingFrequency(double fsamp);
		double samplingFrequency() const;

		void pushData(int n, const T *data);

		void reset();

		virtual void trimData(int start, int end, int *cutOffset = NULL);

		const T *data() const;
		int columns() const;
		int rows() const;
		double minimum() const;
		double maximum() const;
		bool isNull() const;


	protected:
		virtual void resetted();


	private:
		void resetData();
		void clearData();

		void initFilters();
		void addFilter(double loFreq, double hiFreq, double maxPeriod);


	protected:
		typedef SpectrogramSettings Settings;
		typedef Seiscomp::Math::Filtering::InPlaceFilter<T> Filter;
		std::vector<Filter*> _filters;

		T       *_data;
		int      _maxColumns;
		int      _columns;
		int      _startColumn;
		int      _endColumn;
		int      _rows;

		double   _fsamp;
		double   _maxSeconds;

		double   _min, _max;

		Settings _settings;
};



typedef RecordSpectrogram<float> RecordSpectrogramF;
TYPEDEF_SMARTPOINTER(RecordSpectrogramF);
TYPEDEF_CONST_SMARTPOINTER(RecordSpectrogramF);

typedef RecordSpectrogram<double> RecordSpectrogramD;
TYPEDEF_SMARTPOINTER(RecordSpectrogramD);
TYPEDEF_CONST_SMARTPOINTER(RecordSpectrogramD);


template <typename T>
class RecordSpectrogram : public Spectrogram<T> {
	public:
		typedef Spectrogram<T> Base;

		RecordSpectrogram();
		RecordSpectrogram(const SpectrogramSettings &settings);


	public:
		const Seiscomp::Core::Time &startTime() const;
		const Seiscomp::Core::Time &endTime() const;

		int mapTime(const Seiscomp::Core::Time &t) const;

		void feed(const Seiscomp::Record *rec);

		virtual void trimData(int start, int end, int *cutOffset = NULL);
		void trim(const Seiscomp::Core::Time &start, const Seiscomp::Core::Time &end);


	protected:
		virtual void resetted();


	private:
		bool                 _initialized;
		Seiscomp::Core::Time _startTime;
		Seiscomp::Core::Time _endTime;
};



#include <gempa/gui/spectrogram/spectrogram.ipp>


}
}


#endif
