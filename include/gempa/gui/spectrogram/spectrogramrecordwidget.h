/***************************************************************************
 * Copyright (C) 2011 by gempa GmbH
 *
 * Author: Jan Becker
 * Email: jabe@gempa.de
 ***************************************************************************/


#ifndef __GEMPA_SPECTROGRAM_SPECTROGRAMRECORDWIDGET_H__
#define __GEMPA_SPECTROGRAM_SPECTROGRAMRECORDWIDGET_H__


#include <seiscomp3/gui/core/recordwidget.h>
#ifndef Q_MOC_RUN
#include <gempa/gui/spectrogram/spectrogram.h>
#endif
#include <gempa/gui/spectrogram/image.h>


// Required for g++ 4.4.7
#if SC_API_VERSION >= SC_API_VERSION_CHECK(13,0,0)
using Seiscomp::Core::intrusive_ptr_release;
#endif


namespace Gempa {
namespace Gui {


class SpectrogramRecordWidget : public Seiscomp::Gui::RecordWidget {
	Q_OBJECT

	public:
		SpectrogramRecordWidget(QWidget *parent=0);
		SpectrogramRecordWidget(const Seiscomp::DataModel::WaveformStreamID& streamID,
		                        QWidget *parent=0);


	public:
		void setSpectrogramSettings(double fromPeriod, double toPeriod,
		                            int ranges, int bandCount);
		void setSpectrogramSettings(const SpectrogramSettings &settings);

		void setColorLUT(const ColorLUT *lut);
		void setSpectrogramSlot(int slot);

		int spectrogramSlot() const { return _specSlot; }

		void useFilteredRecords(bool);
		bool filteredRecordsUsed() const { return _useFilteredRecords; }

		void fed(int slot, const Seiscomp::Record *rec);

		void clearSpectrogramImages();

		double minimumSpecValue() const { return _range.first; }
		double maximumSpecValue() const { return _range.second; }

		bool isSpectrogramEnabled() const;
		bool isSpectrogramDisplayEnabled() const;


	public slots:
		//! Force a complete update of the spectrogram
		void recordsChanged();

		void setSpectrogramEnabled(bool);
		void setSpectrogramDisplayEnabled(bool);

		void setDrawSpectrogramInFront(bool);


	protected:
		void changedRecords(int slot, Seiscomp::RecordSequence *seq);
		void customPaintTracesBegin(QPainter &painter);
		void customPaintTracesEnd(QPainter &painter);

		virtual void drawSpectrogram(QPainter &painter);


	private:
		void init();
		void feedSpectrogram(int slot, const Seiscomp::Record *rec);


	private:
		struct SpectrogramItem {
			SpectrogramItem() : startIndex(-1), scale(0) {}
			SpectrogramItem(RecordSpectrogramF *s) : spec(s), startIndex(-1), scale(0) {}

			RecordSpectrogramFPtr spec;
			QImage                img;
			int                   startIndex;
			double                scale;
		};

		typedef std::deque<SpectrogramItem> SpectrogramSequence;
		SpectrogramSequence    _specs;
		QPair<double,double>   _range;
		const ColorLUT        *_colorLUT;

		bool                   _drawSpecOnTop;
		bool                   _enableSpecDisplay;
		bool                   _enableSpec;
		bool                   _useFilteredRecords;

		SpectrogramSettings    _specSettings;
		int                    _specSlot;
};


}
}


#endif
