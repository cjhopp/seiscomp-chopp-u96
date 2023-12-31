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


#ifndef SEISCOMP_DATAMODEL_TYPES_H__
#define SEISCOMP_DATAMODEL_TYPES_H__


#include <seiscomp/core/enumeration.h>


namespace Seiscomp {
namespace DataModel {



MAKEENUM(
	OriginUncertaintyDescription,
	EVALUES(
		HORIZONTAL,
		ELLIPSE,
		ELLIPSOID,
		PDF
	),
	ENAMES(
		"horizontal uncertainty",
		"uncertainty ellipse",
		"confidence ellipsoid",
		"probability density function"
	)
);


MAKEENUM(
	MomentTensorStatus,
	EVALUES(
		CMT_S,
		CMT_Q
	),
	ENAMES(
		"standard CMT solution",
		"quick CMT solution"
	)
);


MAKEENUM(
	OriginDepthType,
	EVALUES(
		FROM_LOCATION,
		FROM_MOMENT_TENSOR_INVERSION,
		BROAD_BAND_P_WAVEFORMS,
		CONSTRAINED_BY_DEPTH_PHASES,
		CONSTRAINED_BY_DIRECT_PHASES,
		OPERATOR_ASSIGNED,
		OTHER_ORIGIN_DEPTH
	),
	ENAMES(
		"from location",
		"from moment tensor inversion",
		"from modeling of broad-band P waveforms",
		"constrained by depth phases",
		"constrained by direct phases",
		"operator assigned",
		"other"
	)
);


MAKEENUM(
	OriginType,
	EVALUES(
		HYPOCENTER,
		CENTROID,
		AMPLITUDE,
		MACROSEISMIC,
		RUPTURE_START,
		RUPTURE_END
	),
	ENAMES(
		"hypocenter",
		"centroid",
		"amplitude",
		"macroseismic",
		"rupture start",
		"rupture end"
	)
);


MAKEENUM(
	EvaluationMode,
	EVALUES(
		MANUAL,
		AUTOMATIC
	),
	ENAMES(
		"manual",
		"automatic"
	)
);


MAKEENUM(
	EvaluationStatus,
	EVALUES(
		PRELIMINARY,
		CONFIRMED,
		REVIEWED,
		FINAL,
		REJECTED,
		REPORTED
	),
	ENAMES(
		"preliminary",
		"confirmed",
		"reviewed",
		"final",
		"rejected",
		"reported"
	)
);


MAKEENUM(
	PickOnset,
	EVALUES(
		EMERGENT,
		IMPULSIVE,
		QUESTIONABLE
	),
	ENAMES(
		"emergent",
		"impulsive",
		"questionable"
	)
);


MAKEENUM(
	MomentTensorMethod,
	EVALUES(
		CMT_0,
		CMT_1,
		CMT_2,
		TELESEISMIC,
		REGIONAL
	),
	ENAMES(
		"CMT - general moment tensor",
		"CMT - moment tensor with zero trace",
		"CMT - double-couple source",
		"teleseismic",
		"regional"
	)
);


MAKEENUM(
	DataUsedWaveType,
	EVALUES(
		BODY_WAVES,
		P_BODY_WAVES,
		LONG_PERIOD_BODY_WAVES,
		SURFACE_WAVES,
		INTERMEDIATE_PERIOD_SURFACE_WAVES,
		LONG_PERIOD_MANTLE_WAVES,
		UNKNOWN_WAVETYPE
	),
	ENAMES(
		"body waves",
		"P body waves",
		"long-period body waves",
		"surface waves",
		"intermediate-period surface waves",
		"long-period mantle waves",
		"unknown"
	)
);


MAKEENUM(
	EventDescriptionType,
	EVALUES(
		FELT_REPORT,
		FLINN_ENGDAHL_REGION,
		LOCAL_TIME,
		TECTONIC_SUMMARY,
		NEAREST_CITIES,
		EARTHQUAKE_NAME,
		REGION_NAME
	),
	ENAMES(
		"felt report",
		"Flinn-Engdahl region",
		"local time",
		"tectonic summary",
		"nearest cities",
		"earthquake name",
		"region name"
	)
);


MAKEENUM(
	EventType,
	EVALUES(
		NOT_EXISTING,
		NOT_LOCATABLE,
		OUTSIDE_OF_NETWORK_INTEREST,
		EARTHQUAKE,
		INDUCED_EARTHQUAKE,
		QUARRY_BLAST,
		EXPLOSION,
		CHEMICAL_EXPLOSION,
		NUCLEAR_EXPLOSION,
		LANDSLIDE,
		ROCKSLIDE,
		SNOW_AVALANCHE,
		DEBRIS_AVALANCHE,
		MINE_COLLAPSE,
		BUILDING_COLLAPSE,
		VOLCANIC_ERUPTION,
		METEOR_IMPACT,
		PLANE_CRASH,
		SONIC_BOOM,
		DUPLICATE,
		OTHER_EVENT,
		NOT_REPORTED,
		ANTHROPOGENIC_EVENT,
		COLLAPSE,
		CAVITY_COLLAPSE,
		ACCIDENTAL_EXPLOSION,
		CONTROLLED_EXPLOSION,
		EXPERIMENTAL_EXPLOSION,
		INDUSTRIAL_EXPLOSION,
		MINING_EXPLOSION,
		ROAD_CUT,
		BLASTING_LEVEE,
		INDUCED_OR_TRIGGERED_EVENT,
		ROCK_BURST,
		RESERVOIR_LOADING,
		FLUID_INJECTION,
		FLUID_EXTRACTION,
		CRASH,
		TRAIN_CRASH,
		BOAT_CRASH,
		ATMOSPHERIC_EVENT,
		SONIC_BLAST,
		ACOUSTIC_NOISE,
		THUNDER,
		AVALANCHE,
		HYDROACOUSTIC_EVENT,
		ICE_QUAKE,
		SLIDE,
		METEORITE,
		CALVING,
		FROST_QUAKE,
		TREMOR_PULSE,
		SUBMARINE_LANDSLIDE,
		ROCKET_LAUNCH,
		ROCKET,
		ROCKET_IMPACT,
		ARTILLERY_STRIKE,
		BOMB_DETONATION,
		MOVING_AIRCRAFT,
		ATMOSPHERIC_METEOR_EXPLOSION
	),
	ENAMES(
		"not existing",
		"not locatable",
		"outside of network interest",
		"earthquake",
		"induced earthquake",
		"quarry blast",
		"explosion",
		"chemical explosion",
		"nuclear explosion",
		"landslide",
		"rockslide",
		"snow avalanche",
		"debris avalanche",
		"mine collapse",
		"building collapse",
		"volcanic eruption",
		"meteor impact",
		"plane crash",
		"sonic boom",
		"duplicate",
		"other",
		"not reported",
		"anthropogenic event",
		"collapse",
		"cavity collapse",
		"accidental explosion",
		"controlled explosion",
		"experimental explosion",
		"industrial explosion",
		"mining explosion",
		"road cut",
		"blasting levee",
		"induced or triggered event",
		"rock burst",
		"reservoir loading",
		"fluid injection",
		"fluid extraction",
		"crash",
		"train crash",
		"boat crash",
		"atmospheric event",
		"sonic blast",
		"acoustic noise",
		"thunder",
		"avalanche",
		"hydroacoustic event",
		"ice quake",
		"slide",
		"meteorite",
		"calving",
		"frost quake",
		"tremor pulse",
		"submarine landslide",
		"rocket launch",
		"rocket",
		"rocket impact",
		"artillery strike",
		"bomb detonation",
		"moving aircraft",
		"atmospheric meteor explosion"
	)
);


MAKEENUM(
	EventTypeCertainty,
	EVALUES(
		KNOWN,
		SUSPECTED,
		DAMAGING,
		FELT
	),
	ENAMES(
		"known",
		"suspected",
		"damaging",
		"felt"
	)
);


MAKEENUM(
	SourceTimeFunctionType,
	EVALUES(
		BOX_CAR,
		TRIANGLE,
		TRAPEZOID,
		UNKNOWN_FUNCTION
	),
	ENAMES(
		"box car",
		"triangle",
		"trapezoid",
		"unknown"
	)
);


MAKEENUM(
	PickPolarity,
	EVALUES(
		POSITIVE,
		NEGATIVE,
		UNDECIDABLE
	),
	ENAMES(
		"positive",
		"negative",
		"undecidable"
	)
);


MAKEENUM(
	StationGroupType,
	EVALUES(
		DEPLOYMENT,
		ARRAY
	),
	ENAMES(
		"deployment",
		"array"
	)
);



}
}


#endif
