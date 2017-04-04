using System;
using System.Collections.Generic;
using paytm;
using PaytmContant;
public partial class GenerateChecksum : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        try
        {
            Dictionary<string, string> parameters = new Dictionary<string, string>();
			parameters.Add("MID", "xxxxxxx");
			parameters.Add("ORDER_ID", "xxxxxxx");
			parameters.Add("CUST_ID", "xxxxxxx");
			parameters.Add("CHANNEL_ID", "xxxxxxx");
			parameters.Add("INDUSTRY_TYPE_ID", "xxxxxxx");
			parameters.Add("WEBSITE", "xxxxxxx");
			parameters.Add("TXN_AMOUNT", "xxxxxxx");
		
			string paytmChecksum = "";
			 
			paytmChecksum = CheckSum.generateCheckSum(PaytmConstants.MERCHANT_KEY, parameters);
			Response.Write(paytmChecksum);

		}
		catch (Exception)
		{
		}
    }
}
