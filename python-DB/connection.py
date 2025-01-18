import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    password="root",
    database="cvr"
)

mycursor = mydb.cursor()
print(mydb)
mycursor.execute("create table student(sid int,sname varchar(20),marks int)")
mycursor.execute("insert into student (sid, sname, marks) values (6653, 'Teja', 99)")
mycursor.execute("show tables")
tables=mycursor.fetchall()
print(tables)
while True:
    print("1.delete Data 2.Exit")
    if int(input("Enter Op:"))==2: break

    id=int(input("Enter your id: "))
    mycursor.execute("delete from  student where sid=%s",(id,))
    mydb.commit()

mycursor.execute("create table student(id int, name varchar(20), score int, city varchar(20))")

for i in range(1,5):
    try:
        values = int(input("id: ")),input("name: "),int(input("score: ")),input("city: ")
        mycursor.execute("insert into student values(%s,%s,%s,%s)",values)
        print(i," records inserted successfully\n")
    except:
        print("Insertion failed\n")
mydb.commit()

id = input("Enter id to delete: ")
mycursor.execute("delete from student where id = %s", (id,))
print("Deleted successfully\n")
mydb.commit()

print("Update details")
id = input("Enter id to update: ")
name = input("Enter name to update: ")
score = int(input("Enter score to update: "))
city = input("Enter city to update: ")
mycursor.execute("update student set name = %s, score = %s, city = %s where id=%s",(name,score,city,id))
mydb.commit()


print("Displaying all the student details")
mycursor.execute("select * from student")
std = mycursor.fetchall()
print(std)

print("Displaying all the student asc order based on name")
mycursor.execute("select * from student order by name")
std = mycursor.fetchall()
print(std)

print("students score btw 70-90")
mycursor.execute("select * from student where score between 70 and 90")
marks=mycursor.fetchall()
print(marks)

print("Hyderabad students")
city=input("city: ")
mycursor.execute("select * from student where city=%s",(city,))
res = mycursor.fetchall()
print(res)



