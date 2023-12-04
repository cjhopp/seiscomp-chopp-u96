<table>
	<tbody>
		<tr>
			<td>Time:</td>
			<td colspan="3"><strong>{{corg.time.value|strfdatetime}}</strong></td>
		</tr>
		<tr>
			<td>Depth:</td>
			<td><strong>{{corg.depth.value|number:0}}</strong></td>
			<td>km</td>
			<td>{{corg.depth|kmerr}}</td>
		</tr>
		<tr>
			<td>Lat:</td>
			<td><strong>{{corg.latitude.value|lat}}</strong></td>
			<td>&deg;</td>
			<td>{{corg.latitude|kmerr}}</td>
		</tr>
		<tr>
			<td>Lon:</td>
			<td><strong>{{corg.longitude.value|lon}}</strong></td>
			<td>&deg;</td>
			<td>{{corg.longitude|kmerr}}</td>
		</tr>
		<tr>
			<td>Phases:</td>
			<td><strong>{{corg.quality.usedPhaseCount|number:0}}</strong></td>
			<td align="center">/</td>
			<td>{{corg.quality.associatedPhaseCount|number:0}}</td>
		</tr>
		<tr>
			<td>RMS Res.:</td>
			<td><strong>{{corg.quality.standardError|number:1}}</strong></td>
			<td>s</td>
			<td></td>
		</tr>
		<tr>
			<td>Az. Gap:</td>
			<td><strong>{{corg.quality.azimuthalGap|number:0}}</strong></td>
			<td>&deg;</td>
			<td></td>
		</tr>
		<tr>
			<td>Min. Dist.:</td>
			<td><strong>{{corg.quality.minimumDistance|number:2}}</strong></td>
			<td>&deg</td>
			<td></td>
		</tr>
	</tbody>
	<tbody>
		<tr>
			<td colspan="4"><hr/></td>
		</tr>
	</tbody>
	<tbody>
		<tr>
			<td>EventID:</td>
			<td colspan="3">{{ced.event.publicID}}</td>
		</tr>
		<tr>
			<td>Agency:</td>
			<td colspan="3"><strong>{{corg.creationInfo.agencyID}}</strong></td>
		</tr>
		<tr>
			<td>Author:</td>
			<td colspan="3"><strong>{{corg.creationInfo.author}}</strong></td>
		</tr>
		<tr>
			<td>Evaluation:</td>
			<td colspan="3">{{corg.evaluationStatus[0].toUpperCase()}} ({{corg.evaluationMode[0].toUpperCase()}})</td>
		</tr>
		<tr>
			<td>Earth model:</td>
			<td colspan="3">{{corg.earthModelID}}</td>
		</tr>
		<tr>
			<td>Updated:</td>
			<td colspan="3" ng-class="{'emph':isLocalOrigin}">{{corg.creationInfo|ciup|strfdatetime}}</td>
		</tr>
	</tbody>
</table>
