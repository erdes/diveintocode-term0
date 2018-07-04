WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']

def output_schedule(study_time_list, holiday):
    '''今週の勉強予定を出力します'''

    hours_of_days=dict(zip(WEEK_LIST,study_time_list))


    k=1  #最後に終わったインデックスの場所を記憶するための変数。
    for week_days in WEEK_LIST:
        if week_days is not  holiday:
            print("{0}曜日は{1}時間勉強する予定です。".format(week_days,hours_of_days[week_days]))

            for i in list(range(hours_of_days[week_days])):
                    print("{0}限目 {1}".format(i+1,\
                    SUBJECT_LIST[(k+i)%len(SUBJECT_LIST)]))   # %をとって、リストのインデックスをぐるぐる回す。
                                                              #でもなんか周りくどい書き方な気がする。もうちょっと簡潔にかけますかね？
                    m=(k+i+1)%len(SUBJECT_LIST)    #インデックスの値を保存しておきたいので、一旦仮の変数mに保存。

            k=m  #ループの外でkの値を更新。
        else:
            print("{0}曜日はおやすみです。".format(week_days,hours_of_days[week_days]))


def main():
#    '''勉強情報をoutput_scheduleに渡します'''
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list,WEEK_LIST[3])


if __name__ == '__main__':
    main()



# list=[1,2,3,4,5]
# print(list[5%len(list)])
