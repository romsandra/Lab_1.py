import csv

with open('books.csv') as csvfile:
      k = 0
      table = csv.reader(csvfile, delimiter = ';')
      for row in list(table):
         k += 1

print(k-1)



m = 0
with open('books.csv') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    for row in list(table):
       length_name = len(row[1])
       if (length_name>30):
           m +=1

print(m)





flag = 0
data = input(' Search for: ')
with open('books.csv') as csvfile:
      table = csv.reader(csvfile, delimiter = ';')
      for row in list(table):
         lower_case = row[4].lower()
         index = lower_case.find(data.lower())
         if (index != -1):
            print(row)
            flag = 1

if (flag == 0):
     print('Nothing found.')







m = 1
with open('books.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    f = open('spisok.txt', 'w')
    for row in list(table)[1:21]:
            f.write(str(m) + '. ' + row[3] + '. ' + row[1] + ' - ' + row[6][6:10] + ' \n')
            m += 1

f.close()


d = []
with open('books.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        tags = row[12]
        tags_list = tags.split('# ')
        for tag in tags_list:
            if tag not in d:
                d.append(tag)

print(d)


def criteria(row):
    return row[8]

with open('books.csv') as csvfile:
     table = list(csv.reader(csvfile, delimiter=';'))
     table.sort(reverse=True, key=criteria)
     table.pop(0)
     for i in range(20):
         print(table[i])

