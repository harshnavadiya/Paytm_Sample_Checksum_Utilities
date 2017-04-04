#!C:\Ruby21-x64\bin\ruby.exe
require './paytm/encryption_new_pg.rb'
require './paytm/checksum_tool.rb'
#require 'json'
#require 'cgi'
require 'uri'
#cgi = CGI.new
#params = cgi.params


puts "Content-type: text/html"
puts ""

paytmHASH = Hash.new

paytmHASH["MID"] = 'XXXXXXXXXX';
paytmHASH["ORDER_ID"] = 'XXXXXXXXXX';
paytmHASH["CUST_ID"] = 'XXXXXXXXXX';
paytmHASH["INDUSTRY_TYPE_ID"] = 'XXXXXXXXXX';
paytmHASH["CHANNEL_ID"] = 'XXXXXXXXXX';
paytmHASH["TXN_AMOUNT"] = 'XXXXXXXXXX';
paytmHASH["WEBSITE"] = 'XXXXXXXXXX';
paytmHASH["EMAIL"] = 'XXXXXXXXXX';
paytmHASH["MOBILE_NO"] = 'XXXXXXXXXX';
paytmHASH["CALLBACK_URL"] = 'XXXXXXXXXX';

#paytmparamsnew = paytmHASH

checksum_hash = ChecksumTool.new.get_checksum_hash(paytmHASH).gsub("\n",'')

paytmHASH["CHECKSUMHASH"] =  checksum_hash

puts "#{paytmHASH}"