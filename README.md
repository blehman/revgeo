#revgeo
======

##simple application of pygeocoder: returns geo location info. 
<pre>
usage: rev_geo.py [-h] [-d INPUT_DELIM] [-D OUTPUT_DELIM] [-k KEY]

takes 'lat,long' pairs and returns location information 

optional arguments:
  -h, --help            show this help message and exit
  -d INPUT_DELIM, --input_delim INPUT_DELIM
                        Delimiter between lattitude and longitude
  -D OUTPUT_DELIM, --output_delim OUTPUT_DELIM
                        Delimiter between lattitude and longitude
  -k KEY, --simple_api_key KEY
                        simple api key from google (https://developers.google.
                        com/maps/documentation/geocoding/#api_key)
</pre>
##Example
<pre>
$ cat data.geo
</pre>
38.44999261, 27.21017361
38.42217564, 27.12925136
51.34414215, -0.47409109
<pre>
$ cat data.geo | ./rev\_geo.py -k 'your simple google api key' -D"|"
</pre>
"Turkey"|"TR"|"Izmir"|"35030"|"Forum Bornova Avm, Kazımdirik Mh., Forum Bornova, 35100 Izmir/Izmir Province, Turkey"

"Turkey"|"TR"|"Izmir"|"35260"|"Konak Mh., Mustafa Kemal Sahil Bulvarı, 35480 Konak/Izmir Province, Turkey"

"United Kingdom"|"GB"|null|"KT13"|"Sopwith Drive, Weybridge, Surrey KT13, UK"

##Results header

"Country"|"Country Abbreviation"|"Province"|"Postal Code"|"Formatted Address"

