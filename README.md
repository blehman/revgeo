#revgeo
======

##simplifies the use of pygeocoder (and google geocoding api) to return location information about geo coordinates. 

usage: rev\_geo.py [-h] [-d INPUT\_DELIM] [-D OUTPUT\_DELIM] [-k KEY]

takes 'lat,long' pairs and returns location information about a given geo
coordinate

optional arguments:
  -h, --help            show this help message and exit
  -d INPUT\_DELIM, --input\_delim INPUT\_DELIM
                        Delimiter between lattitude and longitude
  -D OUTPUT\_DELIM, --output\_delim OUTPUT\_DELIM
                        Delimiter between lattitude and longitude
  -k KEY, --simple\_api\_key KEY
                        simple api key from google (https://developers.google.
                        com/maps/documentation/geocoding/#api\_key)

##Example
$ cat data.geo
38.44999261, 27.21017361
38.42217564, 27.12925136
51.34414215, -0.47409109

$ cat data.geo | ./rev\_geo.py -k '<simple google api key>' -D"|"
"Turkey"+"TR"+"Izmir"+"35030"+"Forum Bornova Avm, Kazımdirik Mh., Forum Bornova, 35100 Izmir/Izmir Province, Turkey"
"Turkey"+"TR"+"Izmir"+"35260"+"Konak Mh., Mustafa Kemal Sahil Bulvarı, 35480 Konak/Izmir Province, Turkey"
"United Kingdom"+"GB"+null+"KT13"+"Sopwith Drive, Weybridge, Surrey KT13, UK"
