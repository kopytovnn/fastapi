import asyncio
import requests


async def getdata(ip, token, username):
    await requests.get('https://github.com/', proxies={'https': ip})
    
    
print(requests.get('https://github.com/', proxies={'https': 'https://51.222.10.230:39336'}))
