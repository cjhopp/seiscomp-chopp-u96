/***************************************************************************
 * Copyright (C) 2011 by gempa GmbH
 *
 * Author: Jan Becker
 * Email: jabe@gempa.de
 ***************************************************************************/


#ifndef __GEMPA_SPECTROGRAM_IMAGE_H__
#define __GEMPA_SPECTROGRAM_IMAGE_H__


#include <seiscomp3/gui/core/gradient.h>
#include <gempa/utils/lut.h>
#include <gempa/gui/api.h>

#include <QImage>


namespace Gempa {
namespace Gui {


template <typename T> class Spectrogram;

typedef Gempa::Utils::LUT<double,QRgb> ColorLUT;

template <int N>
class StaticColorLUT : public Gempa::Utils::StaticLUT<double,QRgb,N> {
	public:
		StaticColorLUT() {}
		StaticColorLUT(const Seiscomp::Gui::Gradient &gradient) {
			generateFrom(gradient);
		}

	public:
		bool setRangeFrom(const Seiscomp::Gui::Gradient &gradient) {
			if ( gradient.empty() ) return false;

			double lower =  gradient.begin().key();
			double upper = (--gradient.end()).key();
			Gempa::Utils::StaticLUT<double,QRgb,N>::setRange(lower, upper);

			return true;
		}

		void generateFrom(const Seiscomp::Gui::Gradient &gradient) {
			if ( !setRangeFrom(gradient) ) return;
			for ( int i = 0; i < N; ++i )
				Utils::StaticLUT<double,QRgb,N>::_staticLUT[i] =
					gradient.colorAt(Utils::StaticLUT<double,QRgb,N>::indexToKey(i)).rgba();
		}
};


template <typename T>
bool generateImageCW(QImage &img, const Spectrogram<T> *spec, const ColorLUT *lut,
                     int width, int height, int columnOffset = 0,
                     int columnWidth = -1);

template <typename T>
bool generateImagePPS(QImage &img, const Spectrogram<T> *spec, const ColorLUT *lut,
                      int width, int height, int columnOffset = 0,
                      double pixelPerSecond = 1.0);


}
}

#endif
