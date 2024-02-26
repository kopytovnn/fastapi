from config import *
from constants import *
from models import *
from webpart import *
import sys


# Reading file
users = open('users', 'rt').split('') 
work = {} # group: user


# Grouping
if(len(AVAiLABLE_IPS) != len(AVAiLABLE_TOKENS)):
    print('Count of available ips is not equal to count of available tokens')
    sys.exit()
for group in range(len(AVAiLABLE_IPS)):
    my_token, my_ip = AVAiLABLE_TOKENS[group], AVAiLABLE_IPS[group]
    my_group = Group(my_token, my_ip)
    work[my_group] = []
    for local_number in range(grsize):
        username = users[local_number + group * grsize]
        work[my_group].append(username)


async def main():
    # Infinite cycle
    while True:
        # Cycle through all groups
        for group in work:
            # Cycle through all users in this group
            for username in work[group]:
                await getdata(group.my_ip, group.my_token, username)
                
                
asyncio.run(main())