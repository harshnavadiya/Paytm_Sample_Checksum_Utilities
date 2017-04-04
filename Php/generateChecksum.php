<?php
header("Pragma: no-cache");
header("Cache-Control: no-cache");
header("Expires: 0");
// following files need to be included
require_once("./lib/config_paytm.php");
require_once("./lib/encdec_paytm.php");
$checkSum = "";

// below code snippet is mandatory, so that no one can use your checksumgeneration url for other purpose .

$paramList = array();

$paramList["MID"] = 'xxxxxxxxxxxxx';
$paramList["ORDER_ID"] = 'xxxxxxxx';
$paramList["CUST_ID"] = 'xxxxx';
$paramList["INDUSTRY_TYPE_ID"] = 'xxxxxxxxxxx';
$paramList["CHANNEL_ID"] = 'xxxx';
$paramList["TXN_AMOUNT"] = 'xxxxxxx';
$paramList["WEBSITE"] = 'xxxxxxxx';


$checkSum = getChecksumFromArray($paramList,PAYTM_MERCHANT_KEY);

 echo $checkSum;

 
?>
