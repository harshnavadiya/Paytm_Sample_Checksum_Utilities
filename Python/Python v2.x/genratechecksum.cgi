#!/usr/bin/python

import Checksum
import requests
import base64
import json
import requests

print "Content-type: text/html\n"
MERCHANT_KEY = 'XXXXXXXXX';
import cgi

form = cgi.FieldStorage()
respons_dict = {}

respons_dict['MID'] = 'XXXXXXXXX';
respons_dict['ORDER_ID'] = 'XXXXXXXXX';
respons_dict['CUST_ID'] = 'XXXXXXXXX';
respons_dict['INDUSTRY_TYPE_ID'] = 'XXXXXXXXX';
respons_dict['CHANNEL_ID'] = 'XXXXXXXXX';
respons_dict['TXN_AMOUNT'] = 'XXXXXXXXX';
respons_dict['WEBSITE'] = 'XXXXXXXXX';
respons_dict['EMAIL'] = 'XXXXXXXXX';
respons_dict['MOBILE_NO'] = 'XXXXXXXXX';
respons_dict['CALLBACK_URL'] = 'XXXXXXXXX';

checksum = Checksum.generate_checksum(respons_dict, MERCHANT_KEY)

paramarr = {};

paramarr = respons_dict;

paramarr['CHECKSUMHASH'] = checksum;

print paramarr;
