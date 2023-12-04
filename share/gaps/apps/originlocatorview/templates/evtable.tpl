<table>
	<thead>
		<tr>
			<th ng-click="set('otime')">OT ({{config.useUTC?'GMT':'Localtime'}})<div ng-class="{'glyphicon-chevron-down':reverse && col == 'otime', 'glyphicon-chevron-up':!reverse && col == 'otime'}"></div></th>
			<th ng-click="set('type')">Type<div ng-class="{'glyphicon-chevron-down':reverse && col == 'type', 'glyphicon-chevron-up':!reverse && col == 'type'}"></div></th>
			<th ng-click="set('mag')">M<div ng-class="{'glyphicon-chevron-down':reverse && col == 'mag', 'glyphicon-chevron-up':!reverse && col == 'mag'}"></div></th>
			<th ng-click="set('magType')">TP<div ng-class="{'glyphicon-chevron-down':reverse && col == 'magType', 'glyphicon-chevron-up':!reverse && col == 'magType'}"></div></th>
			<th ng-click="set('phaseCount')">Phases<div ng-class="{'glyphicon-chevron-down':reverse && col == 'phaseCount', 'glyphicon-chevron-up':!reverse && col == 'phaseCount'}"></div></th>
			<th ng-click="set('lat')">Lat<div ng-class="{'glyphicon-chevron-down':reverse && col == 'lat', 'glyphicon-chevron-up':!reverse && col == 'lat'}"></div></th>
			<th ng-click="set('lon')">Lon<div ng-class="{'glyphicon-chevron-down':reverse && col == 'lon', 'glyphicon-chevron-up':!reverse && col == 'lon'}"></div></th>
			<th ng-click="set('depth')">Depth<div ng-class="{'glyphicon-chevron-down':reverse && col == 'depth', 'glyphicon-chevron-up':!reverse && col == 'depth'}"></div></th>
			<th ng-click="set('status')">Stat<div ng-class="{'glyphicon-chevron-down':reverse && col == 'status', 'glyphicon-chevron-up':!reverse && col == 'status'}"></div></th>
			<th>FM<div></div></th>
			<th ng-click="set('agency')">Agency<div ng-class="{'glyphicon-chevron-down':reverse && col == 'agency', 'glyphicon-chevron-up':!reverse && col == 'agency'}"></div></th>
			<th ng-click="set('region')">Region<div ng-class="{'glyphicon-chevron-down':reverse && col == 'region', 'glyphicon-chevron-up':!reverse && col == 'region'}"></div></th>
			<th ng-click="set('eventID')">ID<div ng-class="{'glyphicon-chevron-down':reverse && col == 'eventID', 'glyphicon-chevron-up':!reverse && col == 'eventID'}"></div></th>
		</tr>
	</thead>
	<tbody>
		<tr ng-repeat="evt in tableItems track by evt.eventID" ng-click="select(evt)" ng-class="{'active':ces==evt}">
			<td>{{evt.otime|strfdatetime}}</td>
			<td>{{evt.type}}</td>
			<td>{{evt.mag|mag}}</td>
			<td>{{evt.magType}}</td>
			<td>{{evt.phaseCount}}</td>
			<td>{{evt.lat|lat}}</td>
			<td>{{evt.lon|lon}}</td>
			<td>{{evt.depth.toFixed(0)}} km</td>
			<td class="{{evt.status}}">{{evt.status}}</td>
			<td>{{evt.fm?"Yes":""}}</td>
			<td>{{evt.agency}}</td>
			<td>{{evt.region}}</td>
			<td>{{evt.eventID}}</td>
		</tr>
	</tbody>
</table>
