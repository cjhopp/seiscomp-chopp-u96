<div class="help">
	<header>
		<h1>OriginLocatorView</h1>
	</header>

	<section>
	<h2>Table of contents</h2>
	<ul class="toc">
		<li>
			<a href="#overview">Overview</a>
		</li>
		<li>
			<a href="#event-list">Event list</a>
		</li>
		<li>
			<a href="#locator-perspective">Locator perspective</a>
			<ul>
				<li><a href="#locator-map">Map</a></li>
				<li><a href="#locator-info">Info</a></li>
				<li><a href="#locator-plots">Plots</a></li>
				<li><a href="#locator-arrivals">Arrival table</a></li>
				<li><a href="#relocate">Relocate</a></li>
				<li><a href="#locator-commit">Commit</a></li>
				<li><a href="#locator-waveforms">Checking waveforms</a></li>
			</ul>
		</li>
		<li>
			<a href="#picker">Picker perspective</a>
			<ul>
				<li><a href="#picker-layout">Layout</a></li>
				<li><a href="#picker-navigation">Navigation</a></li>
				<li><a href="#picker-filtering">Filtering</a></li>
				<li><a href="#picker-markers">Trace markers</a></li>
				<li><a href="#picker-align">Alignment</a></li>
				<li><a href="#picker-assoc">Associations</a></li>
				<li><a href="#picker-picking">Picking</a></li>
				<li><a href="#picker-more-stations">More stations</a></li>
				<li><a href="#picker-confirm">Confirming</a></li>
			</ul>
		</li>
	</ul>
	</section>

	<section>
	<h2 id="overview">Overview</h2>
	<p>
	The origin locator view allows to analyse events of a SeisComP system
	with a web browser. It allows interactive modifications of bound phases
	as well as waveform review existing phases and picking of new phases.
	</p>

	<div class="gallery col_3 ratio_5_4">
		<div class="item">
			<div class="itemw">
				<a class="fancybox" href="assets/images/startup.png" target="_blank">
					<div class="img">
						<img src="assets/images/startup.png"/>
						<p>Initial view after startup</p>
					</div>
				</a>
			</div>
		</div>
		<div class="item">
			<div class="itemw">
				<a class="fancybox" href="assets/images/event.png" target="_blank">
					<div class="img">
						<img src="assets/images/event.png"/>
						<p>Locator perspective</p>
					</div>
				</a>
			</div>
		</div>
		<div class="item">
			<div class="itemw">
				<a class="fancybox" href="assets/images/picker.png" target="_blank">
					<div class="img">
						<img src="assets/images/picker.png"/>
						<p>Picker perspective</p>
					</div>
				</a>
			</div>
		</div>
	</div>

	<p>
	The application is organized in two main perspectives:
	the <a href="assets/images/event.png" target="_blank">locator perspective</a>
	and the <a href="assets/images/picker.png" target="_blank">picker perspective</a>.
	After the application has started and initialized it shows the
	<a href="assets/images/startup.png" target="_blank">initial view</a> with
	the latest located events. Selecting an event will load it and switch
	to the locator perspective.
	</p>

	<p>
	The origin locator view is a client-server application. Information that are
	shown in the various perspectives are either local or committed data.
	</p>

	<p>
	<strong>Committed data</strong> refers to data that are stored in the
	database and available to other clients as well.
	</p>

	<p>
	<strong>Local data</strong> refers to data that are only processed in the
	local client (your webbrowser) and not yet committed back to the server.
	For example if an origin is relocated the updated time is show as bold
	red text which means that origin is a local origin and not yet committed.
	If the webpage is reloaded that data will be lost.
	</p>

	<p class="note">
	Note that local modifications of arrival weights won't have any effect until
	<a href="#relocate">Relocate</a> is pressed.
	</p>
	</section>

	<section>
	<h2 id="event-list">Event list</h2>
	<p>
	The event list shows by default the events of the last 24 hours or the last
	day in a list. This initial time span can be configured in <em>gaps.cfg</em> with
	the parameter <em>apps.scolv.loadEventDB</em>.
	</p>
	<a class="img" href="assets/images/startup_map.png" target="_blank">
		<img src="assets/images/startup_map.png"/>
		<p>Map view of all events listed.</p>
	</a>
	<p>
	Alternatively the events can be shown in a map. In the upper right corner
	are two tab headers and activating the globe will switch to a map view. A
	click on an event symbol will open that event in the
	<a href="#locator-perspective">locator perspective</a>.
	</p>
	<p>
	The controls for the event list are in the bottom panel. The first (left)
	<button>Read</button> button will re-read the event list with the given
	number of days entered in the <em>Last days:</em> box. The second (right)
	<button>Read</button> button will re-reade the event list for the given
	time span entered in the <em>From:</em> and <em>To:</em> fields.
	</p>
	<p class="note">
	Note that times entered in the corresponding fields are either in GMT/UTC or
	local time depending on the configuration of GAPS. What time zone is expected
	is written in the label next to the <em>To:</em> field.
	</p>
	<p>
	The filter can toggle visible events. By default all events are being shown.
	There are three options to chose from:
	<ul>
		<li>
			<strong>Show all events </strong> shows all events regardless of
			their status.
		</li>
		<li>
			<strong>Hide rejected events </strong> hides all events with status
			<span class="fg X">X</span>.
		</li>
		<li>
			<strong>Show only rejected events </strong> hides all events
			that don't have status <span class="fg X">X</span> or to put it in
			other words: it shows only rejected events.
		</li>
	</ul>
	</p>
	</section>

	<section>
	<h2 id="locator-perspective">Locator perspective</h2>
	<p>
	The locator perspective is devided into two panels: the left panel with the
	event summary that shows the latest committed event information of the
	event currently loaded and the right main panel which shows the detailed
	location parameters and phase associations.
	</p>

	<h3 id="locator-map">Map</h3>
	<p>
	In the upper left corner of the main panel is the map display showing the
	epicenter as a coloured circle. The diameter corresponds to the magnitude
	and the colour encodes the depths. The following mapping is used:

	<div><span style="background-color: #f00">&nbsp;&nbsp;</span> &lt;= 50km</div>
	<div><span style="background-color: #f80">&nbsp;&nbsp;</span> &lt;= 100km</div>
	<div><span style="background-color: #ff0">&nbsp;&nbsp;</span> &lt;= 250km</div>
	<div><span style="background-color: #0f0">&nbsp;&nbsp;</span> &lt;= 600km</div>
	<div><span style="background-color: #00f">&nbsp;&nbsp;</span> &gt; 600km</div>
	</p>

	In addition to the epicenter associated stations are plotted. The color of
	the circle encodes if a phase has been picked <span class="fg M">manually</span>
	or <span class="fg A">automatically</span>. Hovering a station symbol with
	the mouse will open a popup with the station and channel identifier as well
	as the phase code. Clicking on a station symbol will activate that trace
	in the <a href="#picker">picker perspective</a> if opened otherwise no action is
	triggered.

	<h3 id="locator-info">Info</h3>
	<p>
	The info panel in the middle of the upper half of the main panel shows
	detailed origin information. The single values are self explaining. The
	<strong>Evaluation</strong> value again is a combination of evaluation
	mode (automatic, manual) and evaluation status (preliminary, confirmed,
	reviewed, final, rejected, reported). It is composed of the first character
	of the evaluation mode converted to uppercase following the first character
	of evaluation status converted to uppercase in parenthesis. If any of the
	values is not set, &quot;-&quot; is used instead.
	</p>
	<p>
	Another specially displayed value is <strong>Updated</strong> which reflects
	the timestamp when the origin has been created or updated. If the origin
	is a local object then the timestamp is rendered as e.g.
	<span class="emph">2015-02-20 13:37:02</span>.

	<h3 id="locator-plots">Plots</h3>

	<p>
	The upper right corner of the main panel shows different plots or different
	views on the arrival table (see below). Currently two plots are shown:
	residual vs. distance and redidual vs. azimuth. Clicking on a plot symbol
	will activate that trace in the <a href="#picker">picker perspective</a> if
	opened otherwise no action is triggered. Double clicking will toggle the
	weight of that arrival. If an arrival is enabled then a double click will
	disable it. If disabled, a double click will enable it.
	</p>

	<p>
	To activate a set of arrival a box can be drawn covering the desired arrivals.
	To draw the rubberband the mouse cursor must be moved inside the plot area
	and the left mouse button has to be pressed and held at the desired start
	position. Then move the mouse and still hold the mouse button (dragging).
	The rubberband is finished when the mouse button is released again. Holding
	a modification key changes the operation applied to the arrivals inside the
	rubberband. To cancel the rubberband selection move the mouse cursor back
	to the start position until the box disappears and release the mouse button.
	</p>

	<p>There are three modes:</p>

	<ul>
		<li>
			<strong>Set</strong> the arrivals inside the rubberband as active
			and deactivate all others. This is the default operation if no
			modification key (<span class="key">Shift</span> or <span class="key">Ctrl</span>)
			is pressed.
		</li>
		<li>
			<strong>Activate</strong> the arrivals inside the rubberband and
			leave the arrivals outside the rubberband untouched. That operation
			is activated by holding the <span class="key">Shift</span> key during
			the mouse button release.
		</li>
		<li>
			<strong>Deactivate</strong> the arrivals inside the rubberband and
			leave the arrivals outside the rubberband untouched. That operation
			is activated by holding the <span class="key">Ctrl</span> key during
			the mouse button release.
		</li>
	</ul>

	<p>
	<strong>Zooming</strong> into the plot can be helpful sometimes.
	To zoom into the activated values, e.g. to remove some outliers from the plot,
	the context menu offers an option to <i>Zoom into selected values</i>.
	To reset the zoom again choose <i>Reset zoom</i> from the context menu.
	The context menu can be opened by clicking with the right mouse button
	into the plot area.
	</p>

	<h3 id="locator-arrivals">Arrival table</h3>
	<p>
	The table in the main panel shows all associated picks with the origin. The
	table can be sorted by clicking on the table section headers. Clicking again
	toggles the order ascending/descending.
	</p>
	<p>
	The first column contains check boxes for each row. Unchecking it will set
	the associated pick weight to 0. Checking the box sets the weight to 1.
	The background color reflects the pick evaluation mode:
	<span style="color:white" class="bg A">&nbsp;automatic&nbsp;</span>,
	<span style="color:white" class="bg M">&nbsp;manual&nbsp;</span> or
	<span style="color:white" class="bg C">&nbsp;confirmed&nbsp;</span>.
	</p>
	<p>
	The status (second) column shows the status of each pick. The first character
	encodes the evaluation mode: automatic (A) or manual (M). If followed by
	a character in arrow brackets, this character corresponds the the uppercase
	first character of the methodID, e.g. an automatic AIC pick is shown as &quot;A&lt;A&gt;&quot;.
	</p>
	<p>
	Clicking on a row will select the corresponding row in the
	<a href="#picker">picker perspective</a> if opened otherwise no action is
	triggered.
	</p>
	<p>
	The arrival table supports multiselection of rows. Mulitple rows can be
	selected via <span class="key">Shift</span> or <span class="key">Ctrl</span>
	in combination with a click of the left mouse button. <span class="key">Shift</span>
	selects all rows between the last selected row and the current.
	<span class="key">Ctrl</span> toggles the selection of the current row without
	changing the other rows. Via the context menu different action can be triggered
	for the set of selected rows:
	</p>
	<ul>
		<li>
			<strong>Delete selected arrivals </strong> deletes all selected arrivals
			from the origin without relocating it.
		</li>
		<li>
			<strong>Activate selected arrivals </strong> activates all
			selected arrivals which is equal to ticking the first column of
			each selected arrival individually.
		</li>
		<li>
			<strong>Deactivate selected arrivals </strong> deactivates all
			selected arrivals which is equal to un-ticking the first column of
			each selected arrival individually.
		</li>
	</ul>

	<h3 id="relocate">Relocate</h3>
	<p>
	To relocate an origin with a given locator and profile press the button
	<button>Relocate</button>. Relocation is done at server side. The GUI
	collects all local picks and uses the current set of arrivals (see
	<a href="#locator-arrivals">Arrival table</a>). That data are sent to gaps
	which in turn locates the origin as SeisComP would do it and returns the
	result as local object. Note that no information is sent to the SeisComP
	messaging system during a relocation. The whole process is a private
	communication between gaps and the webbrowser.
	</p>
	<p class="warning note">
	To relocate the user must authenticate against gaps. Only authenticated
	users are allowed to relocate origins. Also the user must be part of
	group <strong>staff</strong>.
	</p>
	<p>
	On server side gaps uses the same configurations as <i>scolv</i> or
	<i>screloc</i> for different locators such as NonLinLoc or HYPO71.
	Additional SeisComP locator plugins can be added to gaps and made available
	to the GUI.
	</p>
	<p>
	Because the relocation process may take a while the button
	<button disabled title="Waiting for result">Relocate</button> is locked until
	a response or an error is received. Once a response was received a notification
	pops up in the upper right corner. In case of an error, it is an error box (red),
	in case of success, a success box (green).
	</p>
	<p>
	The origin returned by gaps is a local object. Only shared picks from
	earlier revisions exist already in the SeisComP database. All
	picks made locally in the picker are not yet committed to the messaging
	system and not persistently stored in the database. The solution must first
	be <a href="#locator-commit">committed</a>.
	</p>

	<h3 id="locator-commit">Commit</h3>

	<h4>Quick commit</h4>

	<p>
	To commit a solution back to gaps which in turn
	sends it to the SeisComP messaging as the desktop version of scolv would do
	press the button <button>Commit</button>. Note that the same security policy
	as with <a href="#relocate">Relocate</a> take effect.
	</p>

	<h4>Commit with additional options</h4>

	<div class="img">
		<a href="assets/images/commit-with-options-button.png" target="_blank">
			<img src="assets/images/commit-with-options-button.png"/>
			<p>Button to activate <em>Commit with additional options</em></p>
		</a>
		<a href="assets/images/commit-with-options.png" target="_blank">
			<img src="assets/images/commit-with-options.png"/>
			<p><em>Commit with additional options</em> dialog</p>
		</a>
	</div>

	<p>
	To commit with additional
	option press the right mouse button on button <button>Commit</button>. A
	context menu will open and the option <em>With additional options ...</em>
	will bring up a dialog where several options can be set.
	</p>

	<ul>
		<li>
			<strong>Update origin</strong> will update the origin if checked.
			Local origins are always committed regardless of the state of this
			option. If a remote origin is committed it is usually tagged as
			<em>confirmed</em>. To avoid that, uncheck this option.
		</li>
		<li>
			<strong>Force association with event ...</strong> will associate
			the committed origin with the current event. This is the normal
			operation because the origin has been revised in the context of
			the event loaded. A remote origin is always associated with the
			event and cannot be deassociated by unchecking the option. A local
			origin can just be sent to the messaging and scevent will decide
			which event to associate the origin with. If unsure, keep that
			option checked.
		</li>
		<li>
			<strong>Fix this origin as preferred location</strong> will fix
			the committed origin as preferred location. That means that subsequent
			origins will not become preferred unless fixed again.
		</li>
		<li>
			<strong>Set event type to</strong> one of the enumerations available.
			This will cause an event update if changed.
		</li>
		<li>
			<strong>Set event type certainty to</strong> one of the enumerations
			available. This will cause an event update if changed.
		</li>
		<li>
			<strong>Set origins status to</strong> one the the enumerations
			available. The default is to set the status to <em>confirmed</em>
			but that can be changed. This will cause an origin update for
			remote origins.
		</li>
		<li>
			<strong>Earthquake name</strong> sets the name of the earthquake.
			This adds another event description with type <em>earthquake name</em>
			or updates the existing. Event descriptions are part of an event.
		</li>
		<li>
			<strong>Comment</strong> adds an operator comment to the event or
			updates the existing. The id of the comment is <em>Operator</em>.
			This comment will show up in scolv as well and can be used to
			communicate with other operators in a simple way.
		</li>
		<li>
			<strong>Return to event list after commit</strong> does what is says.
			After committing the event list is activated to select another
			event to work on.
		</li>
	</ul>

	<h3 id="locator-waveforms">Checking waveforms</h3>
	<p>
	To open the picker perspective either press button <i>Picker</i> or hit
	<span class="key">P</span> on the keyboard.
	</p>
	<div style="clear:both"></div>
	</section>

	<section>
	<h2 id="picker">Picker perspective</h2>

	<a class="img" href="assets/images/picker-layout.png" target="_blank">
		<img src="assets/images/picker-layout.png"/>
		<p>Picker perspective layout</p>
	</a>

	<h3 id="picker-layout">Layout</h3>

	<p>
	The picker perspective is devided into 4 areas that are vertically layouted.
	The upper area is the toolbar which contains several buttons to trigger
	actions.
	</p>
	<p>
	The second row (blue area) is the zoomtrace. It is a zoomed copy of the
	selected trace and shows all 3 components instead of only the currently
	activated trace and can be zoomed independently of trace list. The zoomtrace
	is the only place where picks are set and removed.
	</p>
	<p>
	The third row (green area) is the trace list. Here all stations that
	contribute to the current solution are shown sorted by distance in
	ascending order. To activate a trace, click on it. It will then be shown
	in the zoomtrace and made available for <a href="#picker-assoc">Association</a>
	or <a href="#picker-picking">Picking</a>.
	</p>
	<p>
	An interactive splitter (purple area) separates the zoomtrace and the
	trace list. This splitter can be touched with the mouse and moved to
	change the vertical sizes of the zoomtrace and the trace list to fit
	personal preferences.
	</p>

	<div style="clear:both"></div>

	<h3 id="picker-navigation">Navigation</h3>

	<p>
	To navigate through the streams either the cursor keys can be used to scroll
	the zoomtrace and to select the next or previous stream. Alternatively a
	stream in the list can be selected with the mouse by clicking into it.
	</p>

	<p>
	To zoom traces the mousewheel can be used. This works in the zoomtrace as
	well in the ruler area (last row of the trace list). The latter will zoom
	the trace list horizontally. If the horizontal zoom of the zoomtrace and
	the trace list is different the dark bar in the currently selected trace
	(trace list) represents the area currently shown in the zoomtrace.
	</p>

	<h3  id="picker-filtering">Filtering</h3>

	<a class="img" href="assets/images/toolbar-filter.png" target="_blank">
		<img src="assets/images/toolbar-filter.png"/>
		<p>Toolbar filter selection</p>
	</a>
	<p>
	To filter waveform data in a specific frequency band is a fundamental
	requirement of earthquake analysis. All selectable filters are listed
	in the combo box in the toolbar (blue area).
	</p>
	<p class="note">
	When the filter is changed it can take some time until it is applied since
	all filtering is executed client side in the webbrowser.
	</p>
	<p>
	The available filters are configured on server side with gaps. To change
	the filter list, reconfigure gaps. The configuration parameter is <emph>picker.filters</emph>
	and of the same format as described in the SeisComP documentation.
	</p>
	<p>
	To apply a filter just select it from the list of available filters. The
	first entry <i>No filter</i> is a special entry and shows raw data if selected.
	To toggle between filtered and raw data, key <span class="key">f</span>
	can be used.
	</p>
	<p class="note">
	If a filter has been choosen from the drop down list the list receives the
	focus from the browser and handles all subsequent keypresses. To continue
	to work with the picker hotkeys, click into the zoomtrace to release the
	focus from the filter list. Usually focused controls have a smart outline.
	</p>

	<h3 id="picker-markers">Trace markers</h3>

	<p>
	Each trace in the trace list and the zoomtrace contain markers, vertical
	coloured lines with annotations. The position of the marker reflects the
	timestamp of the corresponding measurement.

	There are three types of markers:
	</p>

	<ul>
		<li><strong>Predicted arrival times</strong> with annotations bottom aligned</li>
		<li><strong>Arrivals</strong> with annotations top aligned and darker colours</li>
		<li><strong>Picks</strong> with annotations top aligned and lighter colours</li>
	</ul>

	<p>
	Picks and arrivals can be either local or origin. Local picks/arrivals are
	not yet part of an origin and just exist in the picker session. Origin
	picks/arrival are part of the origin for that the picker was loaded.
	</p>

	<p>
	Clicking on a marker brings up a notification with information about the type.
	When the mouse pointer hovers a marker it will be highlighted. That indicates
	that the marker is now hit by the mouse and subject to further actions.

	</p>

	<h3 id="picker-align">Alignment</h3>

	<a class="img" href="assets/images/toolbar-align.png" target="_blank">
		<img src="assets/images/toolbar-align.png"/>
		<p>Toolbar align options</p>
	</a>
	<p>
	By default traces in the list are aligned by origin time (OT).
	That alignment can be changed to:

	<ul>
		<li><strong>Origin time</strong> (OT)</li>
		<li><strong>P</strong> is the reference which is either the first picked
		P onset or the first associated P onset. Local picks take precedence over
		arrivals. If neither a pick nor an arrival is available the first
		predicted P onset is taken.
		</li>
		<li><strong>S</strong> is the reference which is either the first picked
		S onset or the first associated S onset. Local picks take precedence over
		arrivals. If neither a pick nor an arrival is available the first
		predicted S onset is taken.
		</li>
	</ul>
	</p>

	<h3 id="picker-assoc">Associations</h3>

	<p>
	When the waveform perspective is opened phases are most likely already
	associated with the origin. After checking the waveforms it might be
	desirable to remove a mispicked phase or to disable it. Sometimes phases
	are automatically disabled by the locator because it constrained the location
	or depth in a bad way. Then an operator might want to reactivate that phase.
	To do that hover a marker that should be activated/deactivated with the
	mouse. Hitting <span class="key">del</span> will set the arrival weight to 0
	and thus disable the phase. <span class="key">ins</span> in turn sets the
	arrival weight to 1 and enables the phase.
	</p>

	<p>
	More operations are available through the context menu of a marker. Pressing
	the right mouse button while hovering a marker brings up several options
	depending on the marker type:
	</p>

	<ul>
		<li>
			<strong>Delete arrival</strong> deletes the arrival state and converts
			the marker to a pick. Picks are not part of the origin new created when
			accepting the solution.
		</li>
		<li>
			<strong>Declare XX phase</strong> changes the phase of the arrival.
			This option is only available if the current pick mode is different
			than the arrivals phase. Note that an arrivals phase can be different
			than the phase hint of the pick itself. This operation implies
			activating the arrival.
		</li>
		<li>
			<strong>Deactivate arrival</strong> sets the weight of the association
			to 0. This option is only available for arrival markers.
		</li>
		<li>
		<strong>Activate arrival</strong> sets the weight of the association
		to 1. This option is only available for arrival markers.
		</li>
		<li>
			<strong>Declare XX arrival</strong> binds a pick with the given phase
			to the solution and creates an arrival. The phase is either the
			currently active pick mode or the phase of the pick if picking is
			not active.
		</li>
		<li>
			<strong>Delete pick</strong> deletes a locally made pick from the
			trace. If the pick is an arrival, the arrival is deleted as well.
		</li>
	</ul>

	<h3 id="picker-picking">Picking</h3>

	<a class="img" href="assets/images/toolbar-picking.png" target="_blank">
		<img src="assets/images/toolbar-picking.png"/>
		<p>Toolbar picking actions</p>
	</a>
	<p>
	Beside modification of the association weights one can also pick new phases
	or correct existing ones. Manually picked phases take always precedence
	over already associated phases. E.g. if an origin has an arrival with phase
	P and the user picks phase P on the same trace the latter is taken into
	account when <a href="#picker-confirm">confirming</a> the solution.
	</p>
	<p>
	Picking can only be done in the zoomtrace. By default picking is disabled
	and it must be enabled for a particular phase. To that a phase must be
	selected from the picking list. There are also hotkeys defined for each
	available phase, see <i>Shortcuts</i> help in the picker perspective.
	If a phase has been selected the cursor of the zoomtrace will change to a
	vertical line with the phase printed at the top and the current time under
	the cursor at the bottom. In addition to the current time the hovered
	component code is also shown after the <i>#</i> character.
	</p>
	<p>
	To set a pick move the cursor to the desired position and double click. A
	new marker appears with the picked phase printed at the top. If the same
	phase is picked again on the same trace the marker will be updated and
	moved to the new position. It is not possible to pick one phase at two
	different positions.
	</p>
	<p>
	To delete a manual pick, press <span class="key">del</span> or press button
	<button >X</button>.
	That will remove a manual pick for the currenly picked phase. If there is no
	manual pick the arrival matching that phase will be deactivated (see
	<a href="#picker-assoc">Association</a>).
	</p>

	<h3 id="picker-more-stations">More stations</h3>
	<a class="img" href="assets/images/toolbar-stations.png" target="_blank">
		<img src="assets/images/toolbar-stations.png"/>
		<p>Toolbar add stations actions</p>
	</a>
	<p>
	Initially the trace list shows only associated stations and in particular
	the picked channels. To show also unassociated stations in a certain
	distance the button <button>+</button> in the toolbar is available. It load
	all stations in the range given in the text input next to it. The unit of
	the distance value is km.
	</p>
	<p>
	Added are stations that are not yet associated and not yet part of the trace
	list. Furthermore a detection stream must be defined in the configuration.
	To define the time window the predicted P arrival is required. Instead of
	requesting a travel time from gaps (which can lead to an empty response) a
	P velocity of 8 km/s is being assumed. The requested data time window should
	be large enough to equalize regional errors of that assumption.
	</p>

	<h3 id="picker-confirm">Confirming</h3>
	<p>
	Once all picks have been set the solution is passed back to the locator
	perspective by pressing button <button>OK</button>. That will create a
	new origin without modifying the location but arrivals. A relocation based
	on the new set of arrivals needs to be issued in the locator perspective
	(see <a href="#relocate">Relocate</a>).
	</p>
	</section>

	<footer>
	Copyright &copy; 2015 by <a href="http://www.gempa.de" target="_blank">gempa GmbH</a>
	</footer>
</div>
