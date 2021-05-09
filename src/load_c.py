
# from bs4 import BeautifulSoup
# import urllib.request as req

# def getCourseinfo (semester=input):
#     baseURL='https://cs.nyu.edu/dynamic/courses/schedule/?semester='
#     res=req.urlopen(baseURL+semester)
#     soup = BeautifulSoup(res,'html.parser')
#     courses=soup.find_all(class_='row')
#     dic = {}
#     for course in courses:
#         # print(repr(course.dt.text), end="")
#         # st = course.ul.text 
#         # st = st.replace ('\r\n', ' ')
#         # st = st.replace ('\n', '')
#         # print(st,end="")
        
#         #course.dt.text 
#         dic.update({course.dt.text: course.ul.text})
#         #st= course.ul.text
#     return dic 


# input_semester = input("Enter a term (fall_2020 or spring_2020):")
# info=getCourseinfo(input_semester)
# print(info)



from bs4 import BeautifulSoup
import urllib.request as req

#def getCourseInfo (sem=input):
sem="fall_2020"
baseURL='https://cs.nyu.edu/dynamic/courses/schedule/?semester='
res=req.urlopen(baseURL+sem)
soup = BeautifulSoup(res,'html.parser')
#print(soup.find("li"))
courses=soup.find_all(class_="schedule-listing")

print(courses.)
    # print(courses.find)
    #table = courses.('table.')
    #print(courses.find_all(id="csci-ua0480-572-desc"))
    # for course in courses:
    #     print(course.getText(), end="")


#user_semester = input("Enter a semester(fall_2020 or spring_2020):")
#info=getCourseInfo(user_semester)
#print(info)
