/***************************************************************************
 * Copyright (C) 2011 by gempa GmbH
 *
 * Author: Jan Becker
 * Email: jabe@gempa.de
 ***************************************************************************/


template <typename T>
inline double Spectrogram<T>::samplingFrequency() const {
	return _fsamp;
}

template <typename T>
inline const T *Spectrogram<T>::data() const {
	return _data;
}


template <typename T>
inline int Spectrogram<T>::columns() const {
	return _columns;
}


template <typename T>
inline int Spectrogram<T>::rows() const {
	return _rows;
}


template <typename T>
inline double Spectrogram<T>::minimum() const {
	return _min;
}


template <typename T>
inline double Spectrogram<T>::maximum() const {
	return _max;
}
