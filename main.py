import _sqlite3
conn =  _sqlite3.connect("univercity.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               major TEXT 
               )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS courses(
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT,
               instrector TEXT 
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS student_courses(
               student_id INTEGER,
               course_id INTEGER,
               FOREIGN KEY(student_id) REFERENCES students(id),
               FOREIGN KEY(course_id) REFERENCES courses(course_id),
               PRIMARY KEY(student_id, course_id)

               )''')

while(True):
    print("\n1.Додати нового студента")
    print("2.Додати новий курс")
    print("3.Показати список студентів")
    print("4.Показати список курсів")
    print("5.Зареєструвати студента на курс")
    print("6.Показати студентів на конкретному курсі")
    print("7.Вийти")
    choise=input("Оберіть опцію 1-7")
    if choise =="1":
        name=input("Введіть ім'я студента")
        age=int(input("Введіть вік"))
        major=input("Введіть спеціальність студента")
        cursor.execute("INSERT INTO students(name,age,major) VALUES (?,?,?)",())
        conn.commit()
    elif choise=="2":
        course=input("Введіть назву курсу")
        instructor=input("Введіть викладача курсу")
        cursor.execute("INSERT INTO students(name,age,major) VALUES (?,?)",())
        conn.commit()
    elif choise=="3":
        cursor.execute("SELECT * FROM students")
        students=cursor.fetchall()
        if not students:
            print("База порожня")
        else:
            print("\nСписок студентів")
            for i in students:
                print(f"ID: {i[0]},Імя: {i[1]},Вік: {i[2]}, Спеціальність: {i[3]}")
    elif choise=="4":
        cursor.execute("SELECT * FROM course")
        students=cursor.fetchall()
        if not students:
            print("База порожня")
        else:
            print("\nСписок студентів")
            for i in students:
                print(f"ID: {i[0]},Імя: {i[1]},Вік: {i[2]}")

    elif choise=="5":
        student_id=int(input("Введіть ID студента"))
        course_id=int("Введіть ID курсу")
        cursor.execute("INSERT INTO students(name,age,major) VALUES (?,?)",())
        conn.commit()


    elif choise=="6":
        course_id=int("Введіть ID курсу")
        cursor.execute('''SELECT student.id, student.name, student.name, student.major
                       FROM students, student_courses
                       WHERE student.id=student_courses.student_id
                       AND student_courses.course_id=?''',(course_id))
        students_on_course=cursor.fetchall()
        if not students_on_course:
            print("На цьому курсі нема студентів")
        else:
            print("Список студентів на курсі")
            for i in students_on_course:
                print(f"ID: {i[0]},Імя: {i[1]},Вік: {i[2]}, Спеціальність: {i[3]}")

    elif choise=="7":
        break
    else:
        print("Введіть число від 1 до 7")

conn.close