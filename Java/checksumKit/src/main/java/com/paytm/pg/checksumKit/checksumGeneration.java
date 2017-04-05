package com.paytm.pg.checksumKit;

import com.paytm.merchant.*;
import java.util.TreeMap;

public class checksumGeneration {
	
	//Below parameters provided by Paytm
	
	private static String MID = "XXXXXXXXXXXXXXXXXXXXXXXX"; 
	private static String MercahntKey = "XXXXXXXXXXX";
	private static String INDUSTRY_TYPE_ID = "XXXXXXXXXXXX";
	private static String CHANNLE_ID = "WAP";
	private static String WEBSITE = "XXXXXXXXXX";
	private static String CALLBACK_URL = "https://pguat.paytm.com/paytmchecksum/paytmCallback.jsp";
	
	public static void main(String[] a){
		
		TreeMap<String,String> paramMap = new TreeMap<String,String>();
		paramMap.put("MID" , MID); //Provided by Paytm
		paramMap.put("ORDER_ID" , "ORDER00011"); //unique OrderId for every request
		paramMap.put("CUST_ID" , "CUST00011"); // unique customer identifier 
		paramMap.put("INDUSTRY_TYPE_ID" , INDUSTRY_TYPE_ID); //Provided by Paytm
		paramMap.put("CHANNEL_ID" , CHANNLE_ID); //Provided by Paytm
		paramMap.put("TXN_AMOUNT" , "1.00"); // transaction amount
		paramMap.put("WEBSITE" , WEBSITE); //Provided by Paytm
		paramMap.put("EMAIL" , "test@gmail.com"); // customer email id
		paramMap.put("MOBILE_NO" , "9999999999"); // customer 10 digit mobile no
		paramMap.put("CALLBACK_URL" , CALLBACK_URL); //Provided by Paytm
		
		try{
		String checkSum =  CheckSumServiceHelper.getCheckSumServiceHelper().genrateCheckSum(MercahntKey, paramMap);
		paramMap.put("CHECKSUMHASH" , checkSum);
		
		System.out.println("Paytm Payload: "+ paramMap);
		
		}catch(Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
