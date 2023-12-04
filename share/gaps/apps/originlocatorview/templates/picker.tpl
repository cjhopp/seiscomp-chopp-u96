<div class="panel pad">
	<div class="vl full-height">
		<div class="top toolbar" style="flex-grow:0;flex-shrink:0">
			<select name="Picking" class="item" ng-init="pickMode=''" ng-model="pickMode" ng-change="setPickMode(pickMode)">
				<option value="" selected="selected">No picking</option>
				<option value="{{ph}}" ng-repeat="ph in config.phases">{{ph}}</option>
			</select>
			<button class="item" ng-click="deletePh()" title="Delete currently selected phase on current trace">X</button>
			<div class="separator item"></div>
			<button class="item" ng-click="alignOT()" title="Align traces on origin time">OT</button>
			<button class="item" ng-click="alignOnPhase('P')" title="Align traces on P onset">P</button>
			<button class="item" ng-click="alignOnPhase('S')" title="Align traces on S onset">S</button>
			<div class="separator item"></div>
			<select name="Filter" class="item" ng-init="cf=defaultFilter()+''" ng-model="cf" ng-change="applyFilter(cf)">
				<option value="-1" ng-selected="cf==-1">No filter</option>
				<option value="{{$index}}" ng-selected="cf==$index" ng-repeat="f in config.filters">{{f[0]}}</option>
			</select>
			<div class="separator item"></div>
			<button class="item" ng-click="activateData(0)" title="Active vertical component">Z</button>
			<button class="item" ng-click="activateData(1)" title="Active 1st horizontal (N) component">1(N)</button>
			<button class="item" ng-click="activateData(2)" title="Active 2nd horizontal (E) component">2(E)</button>
			<div class="separator item"></div>
			<select class="item" ng-model="currentTTable" ng-options="t[0] for t in config.ttables" ng-change="applyTT()">
			</select>
			<div class="item">&gt;</div>
			<select class="item" ng-model="currentTProfile" ng-options="p for p in currentTTable[1]" ng-change="applyTP()">
			</select>
			<div class="separator item"></div>
			<input class="item" type="checkbox" ng-model="options.view.showTT"></input>
			<span class="item">Show TT</span>
			<div class="separator item"></div>
			<input class="item" type="number" min="1" max="20000" step="1" ng-model="stationRange"></input>
			<span class="item">km</span>
			<button class="item" ng-click="loadStationsInRange()" title="Load additional stations in defined range (km)">+</button>
			<button class="pull-right item" ng-click="apply()" title="Apply picks">OK</button>
		</div>
		<div id="zoomtrace" class="rel" style="flex-grow:0;flex-shrink:0">
			<div class="vl full-height" context-menu data-target="ctx-menu-trace" context-menu-close="closeContextMenu()" context-menu-disabled="hasContextMenu()">
				<div class="trace"
				     style="flex-grow:1"
				     timeseries
				     options="options.ctrace"
				     markers="ctrace.markers"
				     data="ctrace.data"
				     status="ctraceStatus"
				     api="zoomTrace"
				     tabindex="0">
				</div>
				<div class="trace-label">
					<div><strong>{{ctrace.asid}}</strong></div>
					<div class="left-text">{{ctrace.dist|number:2}}&deg; ({{ctrace.distKM|number:1}}km)</div>
					<div class="right-text">{{ctrace.azi|number:0}}&deg;</div>
				</div>
				<div class="dropdown outset fixed" id="ctx-menu-trace">
					<ul>
						<li ng-repeat="opt in contextOptions">
							<a ng-click="call(opt)">{{ opt[0] }}</a>
						</li>
					</ul>
				</div>
			</div>
		</div>
		<vsplitter class="vsplit" style="flex-grow:0;flex-shrink:0"></vsplitter>
		<div id="traces" style="flex-grow:1" tabindex="1">
			<div class="tracearea" auto-height-no-scope min-height="40" children=".row" rows="traces.length">
				<div class="row" ng-repeat="trace in traces" last-update-layout auto-scroll="trace==ctrace"
					 ng-class="{'active':trace===ctrace}"
					 ng-click="setCurrentTrace(trace)">
					<div class="trace"
						 timeseries
						 options="trace.options"
						 markers="trace.markers"
						 data="trace.data"
						 api="trace.api">
					</div>
					<div class="trace-label">
						<div><strong>{{trace.asid}}</strong></div>
						<div class="left-text">{{::trace.dist|number:2}}&deg; ({{::trace.distKM|number:1}}km)</div>
						<div class="right-text">{{::trace.azi|number:0}}&deg;</div>
					</div>
				</div>
			</div>
			<div class="ruler" timeseries
				 options="options.ruler"
				 status="tracesStatus">
			</div>
		</div>
	</div>
</div>
