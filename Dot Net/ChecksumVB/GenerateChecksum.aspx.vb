Imports System
Imports paytm
Imports PaytmContant
Partial Public Class GenerateChecksum
    Inherits System.Web.UI.Page
    Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs)
        If Request.Form.AllKeys.Length > 0 Then
            Try
                
                Dim parameters As New Dictionary(Of String, String)()
                Dim paytmChecksum As String = ""
                parameters.Add("MID", "xxxxxxxxxxxxx")
                parameters.Add("ORDER_ID", "xxxxxxxxxxxxx")
                parameters.Add("CUST_ID", "xxxxxxxxxxxxx")
                parameters.Add("CHANNEL_ID", "xxxxxxxxxxxxx")
                parameters.Add("INDUSTRY_TYPE_ID", "xxxxxxxxxxxxx")
                parameters.Add("WEBSITE", "xxxxxxxxxxxxx")
                parameters.Add("TXN_AMOUNT", "xxxxxxxxxxxxx")
                
                paytmChecksum = CheckSum.generateCheckSum(PaytmConstants.MERCHANT_KEY, parameters)
				
				Response.Write(paytmChecksum)

            Catch generatedExceptionName As Exception

            End Try
        End If
    End Sub
End Class

