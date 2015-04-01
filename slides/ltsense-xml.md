## LtSense
```
2015-03-16 03:28:56,256 DEBUG    Generated XML
<?xml version="1.0" ?>
<AgraData>
	<package id="VagrantRelay01" timestamp="1426476536256">
		<sensors>
			<sensor id="VRTEMP01" type="Temperature" units="C">
				<data>10</data>
			</sensor>
			<sensor id="VRTEMP02" type="Temperature" units="C">
				<data>5</data>
			</sensor>
		</sensors>
	</package>
</AgraData>

2015-03-16 03:29:05,877 DEBUG    Preparing payload for transport to http://10.11.34.20:8080/Sensor.agra.xml
2015-03-16 03:29:05,887 ERROR    HTTP Error 403
2015-03-16 03:29:05,888 WARNING  Error delivering payload. Requeueing (Queue Size:18176). Retry in 10.0
```