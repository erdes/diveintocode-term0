import webbrowser

class School():
    def __init__(self,name,address,number_of_students,founding_years,\
            introduction_video_url,introduction_statement):


        self.name=name
        self.address=address
        self.number_of_students=number_of_students
        self.founding_years=founding_years
        self.introduction_video_url=introduction_video_url
        self.introduction_statement=introduction_statement


    def introduction_statement_of(self):
        print( "{0}。そして、{1}は{2}にあり、創立から{3}年の学校で、生徒数は{4}人です。".format(self.introduction_statement,self.name,self.address,\
            self.founding_years,self.number_of_students))



    def introduction_video_url_of(self):
        webbrowser.open(self.introduction_video_url,new=2,autoraise=True)


a_school=School("A学校","東京都新宿区...",300,100,"https://www.youtube.com/watch?v=srX-xUe1L18&index=3&list=PLqMSTn3bGwgy0UxwZ6CSz4Ap-oprBGopn","A学校は自然豊かな...")
b_school=School("B学校","東京都新宿区...",500,30,"https://www.youtube.com/watch?v=zkUYZbeV44s&list=PLqMSTn3bGwgy0UxwZ6CSz4Ap-oprBGopn&index=5","B学校は文武両立で...")


a_school.introduction_statement_of()
b_school.introduction_statement_of()

a_school.introduction_video_url_of()
b_school.introduction_video_url_of()
