import csv
import os


path = "data/"
dir_list = os.listdir(path)

p=0
for dir in dir_list:
    with open('data/'+dir) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for company in csv_reader:
            ok=True
            name=company[1]

            with open('unique.csv') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    for n in csv_reader:
                        if(name==n[1]):
                            ok=False

            if ok:
                company[0]=company[0].split('?')[0]
                with open('unique.csv', mode='a') as open_file:
                    open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    open_writer.writerow(company)