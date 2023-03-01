import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime



page=1
with open('states.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for rw in csv_reader:
        state=rw[0]
        for r in range(page,20):
            url="https://www.biggerpockets.com/real-estate-companies/hard-money-lenders/"+state+"?page="+str(page)

            x = requests.get(url)
            f = open("demo.html", "w")
            f.write(x.text)
            f.close()
            soup=BeautifulSoup(x.text,features="lxml")

            for i in soup.find_all('div', class_="search-result-company"):
                try:
                    link="https://www.biggerpockets.com"+i.find('a',class_="company-directory-company-card-link-container")['href']
                except:
                    link=''

                try:
                    name=i.find('div',class_="company-directory-company-card-company-name").text
                except:
                    name=''

                try:
                    description=i.find('div',class_="company-directory-company-card-company-description").text
                except:
                    description=''

                try:
                    rating=i.find('span',class_="j-star-rating__average-rating").text
                except:
                    rating='N/A'

                row=[link,name,description,rating]
                with open('data/'+state+'.csv', mode='a') as open_file:
                    open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    open_writer.writerow(row)
                
            print(url)
            break
            print('state='+state+' page='+str(r)+' time='+datetime.now().strftime("%H:%M:%S"))

    



