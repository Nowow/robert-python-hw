

import urllib3
import time
import json
import warnings
import requests
warnings.filterwarnings("ignore")


method_url = 'https://api.vk.com/method/users.search'
pars = {
    'access_token':'433099a8d1d786bc46929aa8d8b334bdc38e07f44412556db62bf36afadfc11d456e9af1acf9bd16834a9',
    'count':200,
    'city': 3831, 
    'country': 1,
    'fields':'bdate,sex,occupation,relation,personal'
    }
#req_cash = ''
#for i in pars:
#    req_cash += i + '=' + str(pars[i]) + '&'

#http = urllib3.PoolManager()

#respons = http.request('GET', method_url + '?' + req_cash[:-1] )
respons = requests.get(method_url, pars)
user_data = respons.json()
#try:

#    user_data = json.loads(respons.data.decode().replace("'","\""))
#except:
#    print(respons.data.decode().replace("'","\""))
#    raise Exception('ewwwwww')

sorted_list = ['first_name', 'last_name','bdate','sex','occupation','relation','personal']



w_pars = {
    'access_token':'433099a8d1d786bc46929aa8d8b334bdc38e07f44412556db62bf36afadfc11d456e9af1acf9bd16834a9',
    'filter' : 'owner',
    'count' : 100
    }

wall_method = 'https://api.vk.com/method/wall.get'


string_cash = ''
for person in user_data['response'][1:]:
    for field in sorted_list:
        try:
            string_cash += str(person[field]).replace('\t',' ') + '\t'
        except:
            print('No ' + field + ' here')
            string_cash += 'SPACE_FOR_SALE \t'
    string_cash += '\n'
    w_pars['owner_id'] = person['uid']
    wall = requests.get(wall_method, w_pars)
    time.sleep(0.4)
    wall_cash = wall.json()
#    for i in w_pars:
#        req_cash += i + '=' + str(w_pars[i]) + '&'
#    print('getting wall')
#    try:
#        wall = http.request('GET', wall_method + '?' + req_cash[:-1] )
#        time.sleep(0.4)
#        print('sleeping')
#        wall_cash = json.loads(wall.data.decode().replace("'","\""))
#    except:
#        print('strange responce??')
#        wall_cash = wall.data.decode().replace("'","\"")
        
    
    with open('/run/media/robert/1TB-1/linuxfolder/gitlair/robert-python-hw/vk_walls/'+ str(person['uid']) + '.txt', 'w' ) as wall_dump:
        try:
            for post in wall_cash['response'][1:]:
                wall_dump.write(post['text'].replace('<br>','\n'))
        except:
            wall_dump.write(str(wall_cash))
            print('probably too many requests at a time')
        wall_dump.close()

people_table =  open('vk_table_of_people.txt', 'w')
people_table.write(string_cash)
people_table.close()
            


