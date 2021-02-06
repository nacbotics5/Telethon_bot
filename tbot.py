import sys
import csv
import time
import random
import traceback
from config import*
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest


client = TelegramClient(phone, api_id, api_hash)
 
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))


input_file = "tbot.csv"
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 5000
groups=[]

channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}

for i,channel_name in enumerate(channels.keys()):
        try:print(f"{i} ::: {channel_name}")
        except:pass

channel_id = int(input("Please select a number :: "))

channel_name = list(channels.keys())[channel_id]
target_group = channels[channel_name]
print(f"\n\nYou have selected:: {channel_name}")


target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
 
mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
 
n = 0


for user in users:
    n += 1
    if n % 50 == 0:
    	sleep(900)
    try:
        print ("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")
        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
        print("Waiting for 5-10 Seconds...")
        time.sleep(random.randrange(10,60))
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except:
        traceback.print_exc()
        print("Unexpected Error")
    continue
import sys
import csv
import time
import random
import traceback
from config import*
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest


client = TelegramClient(phone, api_id, api_hash)
 
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))


input_file = "tbot.csv"
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 5000
groups=[]

channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}

for i,channel_name in enumerate(channels.keys()):
        try:print(f"{i} ::: {channel_name}")
        except:pass

channel_id = int(input("Please select a number :: "))

channel_name = list(channels.keys())[channel_id]
target_group = channels[channel_name]
print(f"\n\nYou have selected:: {channel_name}")


target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
 
mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
 
n = 0


for user in users:
    n += 1
    if n % 50 == 0:
    	time.sleep(900)
    try:
        print ("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")
        #client(InviteToChannelRequest(target_group_entity,[user_to_add]))
        client(InviteToChannelRequest(channel_name,[user['username']]))
        print("Waiting for 5-10 Seconds...")
        time.sleep(random.randrange(20,60))
    except ValueError:
    	print("Sorry couldn't add user")
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except:
        #traceback.print_exc()
        print("Unexpected Error")
    continue
