import csv,operator

#読み込みとソートまでしたコードになります。

f=open("task.csv")
reader=csv.reader(f)

sortlize_reader=sorted(reader,key=operator.itemgetter(1))

for row in sortlize_reader:
    print(row)

f.close()
