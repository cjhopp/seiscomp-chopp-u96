* Generated at $date - Do not edit!
* template: $template

[$seedlink.source.id]

* Settings for Vaisala weather station

* Station ID (network/station code is set in seedlink.ini)
station=$seedlink.station.id

* Use the command 'serial_plugin -m' to find out which protocols are
* supported.
protocol=vaisala

* Serial port
port=$sources.vaisala.comport

* Baud rate
bps=$sources.vaisala.baudrate

* Time interval in minutes when weather information is logged, 0 (default)
* means "disabled". Weather channels can be used independently of this
* option.
statusinterval=60

* Maximum number of consecutive zeros in datastream before data gap will be
* declared (-1 = disabled).
zero_sample_limit = -1

* Default timing quality in percents. This value will be used when no
* timing quality information is available. Can be -1 to omit the blockette
* 1001 altogether.
default_tq = -1

* Keyword 'channel' is used to map input channels to symbolic channel
* names. Channel names are arbitrary 1..10-letter identifiers which should
* match the input names of the stream processing scheme in streams.xml,
* which is referenced from seedlink.ini

* Outdoor Temperature (C * 100)
channel KO source_id=Ta scale=100

* Outdoor Humidity (%RH)
channel IO source_id=Ua scale=1

* Air Pressure (hPa * 10)
channel DO source_id=Pa scale=10

* Wind Direction (deg)
channel WD source_id=Dm scale=1

* Wind Speed (m/s * 10)
channel WS source_id=Sm scale=10

* Rain accumulation (mm * 100)
channel RA source_id=Rc scale=100

* Hail accumulation (hits/cm^2 * 10)
channel HA source_id=Hc scale=10

