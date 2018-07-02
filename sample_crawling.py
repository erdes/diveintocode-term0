import requests

def join_list(receive_list,send_list):
    for send_list_element in send_list:
        if send_list_element not in receive_list:
            receive_list.append(send_list_element)
    return receive_list



def get_link(htmlsource):
    href_number=htmlsource.find("href=")     #hrefがある場所を探す。   〜.find('href="')  とかにしてもいいけど、結局文字列の先頭のインデックスを返していだけなので結果は同じ
    if href_number==-1:
        return None,0

    else:
        start_number=htmlsource.find('"',href_number)      #ダブルクオーテーション自体はいたるところにあるけど、特に「href=」のあとの"を位置を特定している。
        end_number=htmlsource.find('"',start_number+1)     #start_numberからにしてしまうと、初めの"の場所が返されてしまう。

        url=htmlsource[start_number+1:end_number]    #start_numberは"の位置のインデックスだったので、その次から数え始める。

        return url,end_number



def get_all_links(something_URL):
    page = requests.get(something_URL)
    text = page.text
    urls=[]

    while True:
        url,end_position=get_link(text)

        if url:
            urls.append(url)
            text=text[end_position:]

        else:
            return urls



crawl_urls = ["https://diveintocode-crawling-sample.herokuapp.com/"]
already_crawled_urls=[]
while crawl_urls:
    scheduled_to_crawl =crawl_urls.pop()

    if (scheduled_to_crawl not in already_crawled_urls) is True:
        already_crawled_urls.append(scheduled_to_crawl)
        obtained_urls=get_all_links(scheduled_to_crawl)

        crawl_urls=join_list(crawl_urls,obtained_urls)
        print(already_crawled_urls)

# urls=get_all_links(initial_url)
# print(urls)
