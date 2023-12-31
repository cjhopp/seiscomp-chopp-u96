/***************************************************************************
 * Copyright (C) gempa GmbH                                                *
 * All rights reserved.                                                    *
 * Contact: gempa GmbH (seiscomp-dev@gempa.de)                             *
 *                                                                         *
 * GNU Affero General Public License Usage                                 *
 * This file may be used under the terms of the GNU Affero                 *
 * Public License version 3.0 as published by the Free Software Foundation *
 * and appearing in the file LICENSE included in the packaging of this     *
 * file. Please review the following information to ensure the GNU Affero  *
 * Public License version 3.0 requirements will be met:                    *
 * https://www.gnu.org/licenses/agpl-3.0.html.                             *
 *                                                                         *
 * Other Usage                                                             *
 * Alternatively, this file may be used in accordance with the terms and   *
 * conditions contained in a signed written agreement between you and      *
 * gempa GmbH.                                                             *
 ***************************************************************************/


#ifndef SEISCOMP_SEISMOLOGY_LOCSAT_H
#define SEISCOMP_SEISMOLOGY_LOCSAT_H


#include <seiscomp/core/exceptions.h>
#include <seiscomp/datamodel/origin.h>
#include <seiscomp/datamodel/arrival.h>
#include <seiscomp/datamodel/pick.h>
#include <seiscomp/datamodel/station.h>
#include <seiscomp/seismology/locatorinterface.h>
#include <seiscomp/core.h>


#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <map>


namespace Seiscomp{


namespace Internal {

struct Locator_params;
class LocSAT;
class Loc;

}


struct SC_SYSTEM_CORE_API LocSATErrorEllipsoid {
	LocSATErrorEllipsoid() {
		sxx=syy=szz=stt=sxy=sxz=syz=stx=sty=stz=sdobs=smajax=sminax=strike=sdepth=stime=conf=0.;
	}

	float   sxx;
	float   syy;
	float   szz;
	float   stt;
	float   sxy;
	float   sxz;
	float   syz;
	float   stx;
	float   sty;
	float   stz;
	float   sdobs;
	float   smajax;
	float   sminax;
	float   strike;
	float   sdepth;
	float   stime;
	float   conf;
};


class SC_SYSTEM_CORE_API LocSAT : public Seismology::LocatorInterface {
	public:
		LocSAT();
		virtual ~LocSAT();

		virtual bool init(const Config::Config &config);

		//! Returns supported parameters to be changed.
		virtual IDList parameters() const;

		//! Returns the value of a parameter.
		virtual std::string parameter(const std::string &name) const;

		//! Sets the value of a parameter.
		virtual bool setParameter(const std::string &name,
		                          const std::string &value);

		virtual IDList profiles() const;
		virtual void setProfile(const std::string &name);

		static void setDefaultProfile(const std::string &name);
		static std::string currentDefaultProfile();

		void setNewOriginID(const std::string& newOriginID);

		int capabilities() const;

		DataModel::Origin* locate(PickList& pickList);
		DataModel::Origin* locate(PickList& pickList,
		                          double initLat, double initLon, double initDepth,
		                          const Seiscomp::Core::Time& initTime);

		DataModel::Origin* relocate(const DataModel::Origin* origin);

		const LocSATErrorEllipsoid &errorEllipsoid() const {
			return _errorEllipsoid;
		}

	private:
		void setLocatorParams(int param, const char* value);
		std::string getLocatorParams(int param) const;
		void setDefaultLocatorParams();

		bool loadArrivals(const DataModel::Origin* origin);
		DataModel::Origin *fromPicks(PickList& pickList);
		DataModel::Origin *loc2Origin(Internal::Loc* loc);

		double stationCorrection(const std::string &staid, const std::string &stacode,
		                         const std::string &phase) const;


	private:
		typedef std::map<std::string, double> PhaseCorrectionMap;
		typedef std::map<std::string, PhaseCorrectionMap> StationCorrectionMap;

		static std::string        _defaultTablePrefix;
		static IDList             _allowedParameters;

		StationCorrectionMap      _stationCorrection;
		std::string               _newOriginID;
		std::string               _tablePrefix;
		bool                      _computeConfidenceEllipsoid;
		Internal::LocSAT         *_locateEvent;
		Internal::Locator_params *_locator_params;
		double                    _minArrivalWeight{0.5};
		double                    _defaultPickUncertainty;
		bool                      _usePickUncertainties{false};
		bool                      _usePickBackazimuth{true};
		bool                      _usePickSlowness{true};

		bool                      _enableDebugOutput;

		IDList                    _profiles;

		LocSATErrorEllipsoid      _errorEllipsoid;
};


}// of namespace Seiscomp

#endif
