<div class="fade hotkeys" ng-class="{in: helpVisible}">
	<div class="pad wrapper full-height">
		<div class="window full-height">
			<div class="title">
				<div title="Close this window." class="button" ng-click="toggleCheatSheet()">x</div>
				Help
			</div>
			<div class="panel pad full-height">
				<div class="full-width full-height rel">
					<div class="tabcontent outset">
						<div class="full-height">
							<div ng-show="tab==='sc'" class="full-width full-height pad">
								<div class="inset scroll full-width full-height area">
									<table class="styled">
										<tr ng-repeat="hotkey in hotkeys | filter:{ description: '!$$undefined$$' }">
											<td class="keys"><span ng-repeat="key in hotkey.format() track by $index" class="key">{{ key }}</span></td>
											<td class="text">{{ hotkey.description }}</td>
										</tr>
									</table>
								</div>
							</div>
							<div ng-show="tab==='help'" class="full-width full-height pad">
								<div class="inset scroll help area full-height pad">
									<help></help>
								</div>
							</div>
						</div>
					</div>
					<div class="tabheader" ng-init="tab='events'">
						<div ng-click="tab='sc'" ng-class="{'active':tab==='sc'}">Shortcuts</div>
						<div ng-click="tab='help'" ng-class="{'active':tab==='help'}">Help</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
