<table>
	<thead>
		<tr>
			<th ng-click="set('weight')">Used<div ng-class="{'glyphicon-chevron-down':reverse && col == 'weight', 'glyphicon-chevron-up':!reverse && col == 'weight'}"></div></th>
			<th>Status<div></div></th>
			<th ng-click="set('phase.code')">Phase<div ng-class="{'glyphicon-chevron-down':reverse && col == 'phase.code', 'glyphicon-chevron-up':!reverse && col == 'phase.code'}"></div></th>
			<th>Polarity<div></div></th>
			<th>Takeoff<div></div></th>
			<th ng-click="set('_net')">Net<div ng-class="{'glyphicon-chevron-down':reverse && col == '_net', 'glyphicon-chevron-up':!reverse && col == '_net'}"></div></th>
			<th ng-click="set('_sta')">Sta<div ng-class="{'glyphicon-chevron-down':reverse && col == '_sta', 'glyphicon-chevron-up':!reverse && col == '_sta'}"></div></th>
			<th ng-click="set('_cha')">Loc/Cha<div ng-class="{'glyphicon-chevron-down':reverse && col == '_cha', 'glyphicon-chevron-up':!reverse && col == '_cha'}"></div></th>
			<th ng-click="set('timeResidual')">Res<div ng-class="{'glyphicon-chevron-down':reverse && col == 'timeResidual', 'glyphicon-chevron-up':!reverse && col == 'timeResidual'}"></div></th>
			<th ng-click="set('distance')">Dist<div ng-class="{'glyphicon-chevron-down':reverse && col == 'distance', 'glyphicon-chevron-up':!reverse && col == 'distance'}"></div></th>
			<th ng-click="set('azimuth')">Az<div ng-class="{'glyphicon-chevron-down':reverse && col == 'azimuth', 'glyphicon-chevron-up':!reverse && col == 'azimuth'}"></div></th>
			<th>Time<div></div></th>
		</tr>
	</thead>
	<tbody context-menu data-target="ctx-menu-artable">
		<tr ng-repeat="ar in tableItems" ng-click="select(ar, $event)" ng-class="{'active':ar._selected}">
			<td class="{{::ar.pick.evaluationMode[0].toUpperCase()}}"><input type="checkbox" ng-checked="ar._used" ng-click="toggleArrival(ar);$event.stopPropagation()"></input></td>
			<td>{{::ar.pick.evaluationMode[0].toUpperCase()}}&lt;{{ar.pick.methodID[0].toUpperCase()}}&gt;</td>
			<td>{{::ar.phase.code}}</td>
			<td>{{::ar.pick.polarity}}</td>
			<td>{{::ar.pick.takeOffAngle}}</td>
			<td>{{::ar._net}}</td>
			<td>{{::ar._sta}}</td>
			<td>{{::ar._chaid}}</td>
			<td>{{::ar.timeResidual.toFixed(1)}}</td>
			<td>{{::ar.distance.toFixed(2)}}</td>
			<td>{{::ar.azimuth.toFixed(0)}}</td>
			<td>{{::ar.pick.time.value|strftime}}</td>
		</tr>
	</tbody>
</table>
