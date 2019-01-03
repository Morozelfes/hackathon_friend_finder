import csv
from operator import itemgetter
filename = 'pearl_tower_status.csv'
csv_file = csv.reader(open(filename, 'r',encoding='UTF-8'))
dict = {}
for row in csv_file:
    #print(row)
    emoji = ''
    flag = False
    for ch in row[2]:
        if ch == ']':
            flag = False
            if emoji in dict.keys():
                dict[emoji] += 1
            else:
                dict[emoji] = 1
            emoji=""
        else:
            if not flag:
                if ch == '[':
                    flag = True
            else:
                emoji += ch

dict= sorted(dict.items(), key=lambda d:d[1], reverse = True)
print(dict)
