from http import cookies
import os
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import html
import sys

path = "data_company/"
dir_list = os.listdir(path)

p=0
for dir in dir_list:
    with open('data_company/'+dir) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for company in csv_reader:
            
            url= company[3]
            if(url.find('https://') > -1 ):
                pass
            else: 
                continue
            # url='https://www.biggerpockets.com/users/mpandreotta#0'
            cookies={'_biggerpo_rsk':'75776327dacb85c5e1e5928f816ec202'}
            try:
                x = requests.get(url,cookies=cookies)
            except:
                print(url)
                x = requests.get(url,cookies=cookies)
                # sys.exit(url)

            soup=BeautifulSoup(x.text,features="lxml")
            f = open("demofile2.html", "w")
            f.write(x.text)
            # print(url)
            f.close()
            

            try:
                j_data=html.unescape(str(soup.find('div',{"data-react-class" : "ProfileApp"})).split('data-react-props="')[1].split('"></div>')[0])
            except:
                continue

            

            try:
                j_l_data=json.loads(j_data)
            except:
                print(url)

            

            

            j_l_data=j_l_data['initialState']['data']['relationships']['profile']['data']['social-profiles']
            s=''
            for x in j_l_data:
                s+=x['network-name']+'['+x['value']+']='+str(x['url'])+','
           
            
            row=company


            row.append(s)

            

            with open('data_lender/'+dir, mode='a') as open_file:
                open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                open_writer.writerow(row)

            line_count+=1
            print('state='+dir+' p='+str(line_count)+' time='+datetime.now().strftime("%H:%M:%S"))


            
    

# print(p)