import os
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import html

path = "data/"
dir_list = os.listdir(path)

p=0
for dir in dir_list:
    with open('data/'+dir) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for company in csv_reader:
            url= company[0]
            x = requests.get(url)
            soup=BeautifulSoup(x.text,features="lxml")
           
            
           
            try:
                j_data=html.unescape(str(soup.find('div',class_="component-company-profile")).split('data-react-props="')[1].split('"></div>')[0].split('</div>')[0])
            except:
                j_data=html.unescape(str(soup.find('div',class_="component-company-profile")).split("data-react-props='")[1].split("'></div>")[0].split('</div>')[0])
            
            try:
                j_l_data=json.loads(j_data)
            except:
                print(url)

            j_l_data=j_l_data['railsProps']['refactoredCompanyProfile']['owner']
            
            row=company
        
            try:
                row.append("https://www.biggerpockets.com/users/"+j_l_data['username'])
            except:
                row.append("")

            try:
                row.append(j_l_data['id'])
            except:
                row.append("")

            try:
                row.append(j_l_data['username'])
            except:
                row.append("")
        
            try:
                row.append(j_l_data['name'])
            except:
                row.append("")

            try:
                row.append(j_l_data['premium'])
            except:
                row.append("")

            with open('data_s/'+dir, mode='a') as open_file:
                open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                open_writer.writerow(row)

            line_count+=1
            print('state='+dir+' p='+str(line_count)+' time='+datetime.now().strftime("%H:%M:%S"))


            
    

print(p)