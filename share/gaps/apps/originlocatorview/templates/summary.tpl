<div style="line-height:2em">
	<div class="nowrap highlight">{{ces.otime|strfdatetime}}</div>
	<div>{{ces.otime|ago}}</div>
	<div class="highlight">{{ces.magType}} {{ces.mag|mag}}</div>
	<div class="highlight">{{ces.region}}</div>
	<div class="highlight">Depth {{ces.depth.toFixed(0)}} km</div>
	<div>
		<div class="pull-left"><strong>{{ces.lat|lat}}</strong></div>
		<div class="pull-right"><strong>{{ces.lon|lon}}</strong></div>
	</div>
	<div style="clear:both"></div>
	<div class="square">
		<map-ll options="options.map" events="mapSummaryEvents" class="full-width full-height"></map-ll>
	</div>
	<table style="width:100%">
		<tr>
			<td colspan="2"><hr/></td>
		</tr>
		<tr>
			<td style="padding-right:1em">Phases:</td>
			<td style="width:100%"><strong>{{ces.phaseCount}}</strong></td>
		</tr>
		<tr>
			<td colspan="2"><hr/></td>
		</tr>
		<tr>
			<td class="nowrap" style="padding-right:1em">Event ID:</td>
			<td><strong>{{ces.eventID}}</strong></td>
		</tr>
		<tr>
			<td class="nowrap" style="padding-right:1em">Agency ID:</td>
			<td><strong>{{ces.agency}}</strong></td>
		</tr>
	</table>
</div>
