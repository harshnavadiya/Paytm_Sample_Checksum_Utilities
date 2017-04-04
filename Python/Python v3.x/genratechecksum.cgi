#!/usr/bin/python

import Checksum
#import requests
import base64
#import json
#import requests

print "Content-type: text/html\n"
MERCHANT_KEY = 'XXXXXXXXXX';
#import cgi

#form = cgi.FieldStorage()
respons_dict = {}

respons_dict['MID'] = 'XXXXXXXXXX';
respons_dict['ORDER_ID'] = 'XXXXXXXXXX';
respons_dict['CUST_ID'] = 'XXXXXXXXXX';
respons_dict['INDUSTRY_TYPE_ID'] = 'XXXXXXXXXX';
respons_dict['CHANNEL_ID'] = 'XXXXXXXXXX';
respons_dict['TXN_AMOUNT'] = 'XXXXXXXXXX';
respons_dict['WEBSITE'] = 'XXXXXXXXXX';
respons_dict['EMAIL'] = 'XXXXXXXXXX';
respons_dict['MOBILE_NO'] = 'XXXXXXXXXX';
respons_dict['CALLBACK_URL'] = 'XXXXXXXXXX';


checksum = Checksum.generate_checksum(respons_dict, MERCHANT_KEY)

#paramarr = {};

#paramarr = respons_dict;

respons_dict['CHECKSUMHASH'] = checksum;

print respons_dict;