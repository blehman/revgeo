#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys 

reload(sys)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stdin = codecs.getreader('utf-8')(sys.stdin)

######
import pygeocoder as geoc
import json
import argparse
#####

def rev_geo(latitude,longitude,simple_api_key):
    my_geocoder=geoc.Geocoder(api_key=simple_api_key)
    result=my_geocoder.reverse_geocode(latitude,longitude)
    return [result.country,result.country__short_name,result.province,result.postal_code,result.formatted_address]

if __name__=='__main__':
    geo_parser = argparse.ArgumentParser(
            description="takes 'lat,long' pairs and returns location information about a given geo coordinate")
    geo_parser.add_argument("-d", "--input_delim", dest="input_delim", default=",",
            help="Delimiter between lattitude and longitude")
    geo_parser.add_argument("-D", "--output_delim", dest="output_delim", default="|", 
            help="Delimiter between lattitude and longitude")
    geo_parser.add_argument("-k", "--simple_api_key", dest="key", 
            help="simple api key from google (https://developers.google.com/maps/documentation/geocoding/#api_key)")
    options = geo_parser.parse_args() 
    
    for cords in sys.stdin:
        latitude=float(cords.strip().split(options.input_delim)[0])
        longitude=float(cords.strip().split(options.input_delim)[1])
        result=rev_geo(latitude,longitude,options.key)
        print options.output_delim.join([json.dumps(item,ensure_ascii=False) for item in result])
       
    
    
