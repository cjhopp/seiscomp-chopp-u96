<div class="modal" id="dlg-commit">
	<div class="dialog window" style="max-width: 444px">
		<div class="title">
			<div title="Close dialog" class="button" close data-target="dlg-commit">x</div>
			Commit with additional options
		</div>
		<div class="panel pad">
			<div class="row"><input type="checkbox" ng-model="commitOpts.update"><span>Update origin</span></div>
			<div class="row"><input type="checkbox" ng-model="commitOpts.associate"><span>Force association with event {{ced.event.publicID}}</span></div>
			<div class="row"><span>&nbsp;&nbsp;</span><input ng-disabled="!commitOpts.associate" type="checkbox" ng-model="commitOpts.fix"><span>Fix this origin as preferred location</span></div>
			<table>
				<tr class="row">
					<td>Set event type to</td>
					<td>
						<select ng-options="t for t in eventTypes" ng-model="commitOpts.eventType"/>
					</td>
				</tr>
				<tr class="row">
					<td>Set event type certainty to</td>
					<td>
						<select ng-options="t for t in eventTypeCertainties" ng-model="commitOpts.eventTypeCertainty"/>
					</td>
				</tr>
				<tr class="row">
					<td>Set origin status to</td>
					<td>
						<select ng-options="t for t in originStatus" ng-model="commitOpts.originStatus"/>
					</td>
				</tr>
			</table>
			<hr/>
			<strong>NOTE</strong> To fix the origin involves that successive origins are
			not considered as preferred origins by the event associator (scevent) until
			another origin is fixed again. Fixing an origin overrides the automatic rules
			of setting an origin as preferred origin.
			<hr/>
			<p>Earthquake name:</p>
			<input class="full-width" ng-model="commitOpts.name"></input>
			<p>Comment:</p>
			<input class="full-width" ng-model="commitOpts.comment"></input>
			<hr/>
			<div class="row"><input type="checkbox" ng-model="commitOpts.eventList"><span>Return to event list after commit</span></div>
			<div class="compact toolbar">
				<div class="spacer item"></div>
				<button class="item pull-right" close data-target="dlg-commit">Cancel</button>
				<button class="item pull-right" ng-click="commitWithOptions()" close data-target="dlg-commit">OK</button>
			</div>
		</div>
	</div>
</div>
