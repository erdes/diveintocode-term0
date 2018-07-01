import requests
page=requests.get("https://diveintocode.jp/")


def get_link(htmlsource):
    href_number=htmlsource.find("href=")     #hrefがある場所を探す。   〜.find('href"')  とかにしてもいいけど、結局文字列の先頭のインデックスを返していだけなので結果は同じ
    if href_number==-1:
        return None,0

    else:
        start_number=htmlsource.find('"',href_number)      #ダブルクオーテーション自体はいたるところにあるけど、特に「href=」のあとの"を位置を特定している。
        end_number=htmlsource.find('"',start_number+1)     #start_numberからにしてしまうと、初めの"の場所が返されてしまう。

        url=htmlsource[start_number+1:end_number]    #start_numberは"の位置のインデックスだったので、その次から数え始める。

        return url,end_number



page_damy=page.text         #一度変数に代入しておかないとエラーが出る。

while True:
    url,end_position=get_link(page_damy)

    if url is None:
        break
    else:
        print(url)
        page_damy=page_damy[end_position:]
