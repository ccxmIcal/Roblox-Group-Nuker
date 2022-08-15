import json
import roblox
from roblox import Client
import colorama
from colorama import Fore
import asyncio
import os

colorama.init()

try:
    with open('configuration/config.json', 'r') as f:
        data = json.loads(f.read())
        COOKIE = data['Cookie']
except FileNotFoundError:
    print(f'{Fore.RED} Could not find configuration/config.json. We automatically made them for you. Please restart the exe and write the cookie in the "config.json" file located inside the "configuration" folder.')
    input('Press ENTER to exit!')
    os.mkdir('configuration')
    f = open('configuration/config.json', 'w')
    f.write('{\n    "Cookie": "CookieHere"\n}')
    f.close()
    exit()

def makeError(errorMsg):
    print(f'{Fore.RED}{errorMsg}')

client = Client(COOKIE)




async def main():

    try:
        user = await client.get_authenticated_user()
        print(f'{Fore.GREEN}Logged in as: {user.name} with the UserID: {user.id}')
        os.system(f'title Made by sufi#1337(ccx) (https://github.com/ccxmIcal). Logged in as {user.name}')
    except:
        makeError('Authentication fail. Please check the cookie.')
        input('Press ENTER to exit!')
        exit()

    loggedUser = await client.get_authenticated_user()
    groupId = input("Enter the Group ID: ")
    isInGroup = False
        
    try:
        group = await client.get_group(int(groupId))
    except:
        makeError('Invalid Group!')
        input('Press ENTER to exit!')
        exit()

    for role in await loggedUser.get_group_roles():
        if role.group.id == group.id:
            isInGroup = True
            break

    if not isInGroup:
        makeError('User is not in group!')
        input('Press ENTER to exit!')
        exit()

    input(f'{Fore.WHITE}Press enter to begin nuking!')

    async for member in group.get_members():
        try:
            if member.id != loggedUser.id:
                await group.kick_user(member.id)
                print(f'{Fore.GREEN} Kicked {member.name}')  
        except:
            print(f'{Fore.RED}Could not kick user {member.name}')
            pass


if __name__ == "__main__":
    asyncio.run(main())