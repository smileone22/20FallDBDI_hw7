from bs4 import BeautifulSoup
import urllib.request as req
from  configparser import ConfigParser
import pymysql

def get_config(fn):
    parser = ConfigParser()
    parser.read(fn)
    db = parser.items('db')
    return {name: value for name, value in db}


def get_conn(conf):
    conn=pymysql.connect(**conf, cursorclass=pymysql.cursors.DictCursor)
    return conn

# inserting directly to the database
def insert_courses(conn, semester,course_number, course_title,instructor,meeting_times,class_type,location,cancellation_status):
    cursor =conn.cursor()
    q= 'INSERT INTO Courses_20 VALUES (%s, %s, %s, %s,  %s, %s, %s, %s)'
    cursor.execute(q,(semester,course_number, course_title,instructor,meeting_times,class_type,location,cancellation_status))
    conn.commit()

def getCourseInfo (sem):
    baseURL='https://cs.nyu.edu/dynamic/courses/schedule/?semester='
    semester=sem
    res=req.urlopen(baseURL+semester)
    soup = BeautifulSoup(res,'html.parser')
    courses=soup.find_all("li",class_="row")
    #course_count=0
    for course in courses:
        temp=[]
        course_number =course.attrs['id']
        title=course.find("span",attrs={"class":"col-xs-12 col-sm-3"}).find("a",attrs={"class":"expand"}).text.strip()
        c_info =course.find_all("span",attrs={"class":"col-xs-12 col-sm-2"})
        
        instructor_tmp = c_info[0].text.lstrip()
        instructor_tmp_a= instructor_tmp.replace("Office Hours","").lstrip()
        instructor = instructor_tmp_a.replace("\n","").lstrip()
        meeting_times_tmp= c_info[1].text.lstrip()
        meeting_times= meeting_times_tmp.replace("\n","")
        class_type= c_info[2].text.lstrip()
        if "CANCELLED" in instructor:
            instructor= ""
            meeting_times = ""
            class_type =""
            cancellation = "CANCELLED"
        else: 
            cancellation = "NOT CANCELLED"
        
        if class_type!="ONLINE":
            location=class_type
            class_type="OFFLINE"
        else:
            location=""
        #course_count=course_count+1;
        
        #PART-3 EXTRACTING DATA , SEEN TRHOUGH PRINT(CONTENTS)
        #instead of printing we should insert 
        # insert_course(conn,course_num,',',join(profs))
        print("------------------------")
        print("semester:    ",semester)
        print("course_number:   ",course_number)
        print("course_title:    ",title)
        print("instructor:  ",instructor)
        print("meeting_times:   ",meeting_times)
        print("class_type:  ",class_type)
        print("cancellation_status: ",cancellation)
        print("location:    ",location)
        
        #Part 1-6 
        insert_courses(conn,semester,course_number,title,instructor,meeting_times,class_type,location,cancellation)
    #print(course_count)

conf = get_config('/home/hk2874/csci60-hw07/config.ini')
conn = get_conn(conf)
print(conf)    

getCourseInfo("spring_2020") #142 inputs through course_count
getCourseInfo("fall_2020") #164 inputs through course_count 
#checked that 306 total rows added correctly to the Courses_20 table  



