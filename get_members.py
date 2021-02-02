import csv
from config import*
from telethon import TelegramClient, sync


client = TelegramClient(phone, api_id, api_hash)
 
# get all the channels that I can access
channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}


def save_members(username,id, access_hash,name):
    with open('tbot.csv', mode='a+') as csv_file:
        fieldnames = ['username','id','access_hash','name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({'username': username,'id':id,'access_hash': access_hash,'name': name})


for i,channel_name in enumerate(channels.keys()):
    try:print(f"{i} ::: {channel_name}")
    except:pass

channel_id = int(input("Please select a number :: "))

channel_name = list(channels.keys())[channel_id]
channel = channels[channel_name]
print(f"\n\nYou have selected:: {channel_name}")

print("\n\nGetting the members of this channel\n")

try:
    # get all the users and print them
    for user in client.get_participants(channel):
        name = f"{user.first_name} {user.last_name}"
        save_members(user.username,user.id,user.access_hash,name)import csv
from config import*
from telethon import TelegramClient, sync


client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))




def get_channels():
    # get all the channels that I can access
    channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}
    for i,channel_name in enumerate(channels.keys()):
        try:print(f"{i} ::: {channel_name}")
        except:pass

    channel_id = int(input("Please select a number :: "))

    channel_name = list(channels.keys())[channel_id]
    channel = channels[channel_name]
    print(f"\n\nYou have selected:: {channel_name}")

    print("\n\nGetting the members of this channel\n")

    try:
        with open('tbot.csv', mode='w+') as csv_file:
            fieldnames = ['username','id','access_hash','name']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            
            # get all the users and print them
            for user in client.get_participants(channel):
                name = f"{user.first_name} {user.last_name}"
                writer.writerow({'username': user.username,'id':user.id,'access_hash':user.access_hash,'name':name})
                print(user.username,user.id,user.access_hash,name)
    except Exception as e:
		    print(e)
		    get_channels()
		    
try:
    get_channels()
except Exception as e:
    print(e)
		     



        print(user.username,user.id,user.access_hash,name)
except Exception as e:
		print(e)


