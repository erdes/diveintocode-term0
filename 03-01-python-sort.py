import csv,operator

#読み込みとソートまでしたコードになります。

f=open("task.csv")
reader=csv.reader(f)
print(" ".join(next(reader)))   # next関数で一行目だけ先に処理。
                                # join関数は文字列に対する処理。""内の文字を間に
                                # 挟みながらリストに含まれるそれぞれの要素を連結。

sortlize_reader=sorted(reader,key=operator.itemgetter(1))
                                # 残りの行に対してソート
for row in sortlize_reader:
    print(" ".join(row))

f.close()
