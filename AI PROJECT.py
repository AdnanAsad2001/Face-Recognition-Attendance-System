import tkinter as tk
from pathlib import Path
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time

# ####Window is our Main frame of system
window = tk.Tk()
window.title("FACE RECOGNITION ATTENDANCE SYSTEM")

img = Image.open('E:\\adnan asad\\FACE RECOGNIATION SYSTEM\\synthetic-data-1024x640_1280x720.jpg')
bg = ImageTk.PhotoImage(img)

window.geometry('1280x720')
window.configure(background='BLACK')

label = Label(window, image=bg)
label.place(x=0, y=0)
# ###GUI for manually fill attendance


def manually_fill():
    global sb
    sb = tk.Toplevel()
    sb.title("ENTER SUBJECT NAME...")
    sb.geometry('580x320')
    sb.wm_iconbitmap('E:\\adnan asad\\FACE RECOGNIATION SYSTEM\\images_48x48 .ico')
    sb.configure(background='BLACK')
    img_3 = Image.open('E:\\adnan asad\\FACE RECOGNIATION SYSTEM\\synthetic-data-1024x640_2_580x320.jpg')
    bg_3 = ImageTk.PhotoImage(img_3)

    label_2 = Label(sb, image=bg_3)
    label_2.place(x=0, y=0)

    def err_screen_for_subject():

        def ec_delete():
            ec.destroy()
        global ec
        ec = tk.Toplevel()
        ec.geometry('420x150')
        ec.iconbitmap('E:/adnan asad/FACE RECOGNIATION SYSTEM/images_48x48 .ico')
        ec.title('WARNING!!')
        ec.configure(background='BLACK')
        Label(ec, text='PLEASE ENTER YOUR SUBJECT NAME!!!', fg='black', bg='cadetblue', font=('times', 16, ' bold ')).pack()
        Button(ec, text='OK', command=ec_delete, fg="black", bg="deepskyblue4", width=9, height=1, activeforeground="white", activebackground="turquoise3", font=('times', 15, 'bold')).place(x=150, y=80)

    def fill_attendance():
        ts = time.time()
        Date = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        date_for_DB = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
        global subb
        subb = SUB_ENTRY.get()
        DB_table_name = str(subb + "_" + Date + "-" + Hour + "_" + Minute + "_" + Second)

        if subb == '':
            err_screen_for_subject()
        else:
            sb.destroy()
            MFW = tk.Toplevel()
            MFW.iconbitmap('E:/adnan asad/FACE RECOGNIATION SYSTEM/images_48x48 .ico')
            MFW.title("MANUAL ATTENDANCE OF " + str(subb))
            MFW.geometry('880x470')
            MFW.configure(background='BLACK')
            img_ = Image.open(
                'E:\\adnan asad\\FACE RECOGNIATION SYSTEM\\synthetic-data-1024x640_880x470.jpg')
            bg_ = ImageTk.PhotoImage(img_)

            label_ = Label(MFW, image=bg_)
            label_.place(x=0, y=0)

            def del_errsc2():
                errsc2.destroy()

            def err_screen1():
                global errsc2
                errsc2 = tk.Toplevel()
                errsc2.geometry('430x150')
                errsc2.iconbitmap('E:/adnan asad/FACE RECOGNIATION SYSTEM/images_48x48 .ico')
                errsc2.title('WARNING!!')
                errsc2.configure(background='BLACK')
                Label(errsc2, text='PLEASE ENTER NAME & ENROLLMENT!!!', fg='black', bg='cadetblue', font=('times', 16, ' bold ')).pack()
                Button(errsc2, text='OK', command=del_errsc2, fg="black", bg="deepskyblue4", width=9, height=1, activeforeground="white", activebackground="turquoise3", font=('times', 15, ' bold ')).place(x=150, y=80)

            def ForIntegerInput(inStr, acttyp):
                if acttyp == '1':  # insert
                    if not inStr.isdigit():
                        return False
                return True

            ENR = tk.Label(MFW, text="ENTER ENROLLMENT", width=20, height=2, fg="black", bg="darkslategray2", font=('times', 15, ' bold '))
            ENR.place(x=30, y=100)

            STU_NAME = tk.Label(MFW, text="ENTER STUDENT NAME", width=20, height=2, fg="black", bg="darkslategray2", font=('times', 15, ' bold '))
            STU_NAME.place(x=30, y=200)

            global ENR_ENTRY
            ENR_ENTRY = tk.Entry(MFW, width=20, validate='key', bg="gray79", fg="black", font=('times', 23, ' bold '))
            ENR_ENTRY['validatecommand'] = (ENR_ENTRY.register(ForIntegerInput), '%P', '%d')
            ENR_ENTRY.place(x=330, y=105)

            def remove_enr():
                ENR_ENTRY.delete(first=0, last=22)

            STUDENT_ENTRY = tk.Entry(MFW, width=20, bg="gray79", fg="black", font=('times', 23, ' bold '))
            STUDENT_ENTRY.place(x=330, y=205)

            def remove_student():
                STUDENT_ENTRY.delete(first=0, last=22)

            def enter_data_DB():
                global ENROLLMENT
                global STUDENT
                global aa1
                ENROLLMENT = ENR_ENTRY.get()
                STUDENT = STUDENT_ENTRY.get()
                if ENROLLMENT == '':
                    err_screen1()
                elif STUDENT == '':
                    err_screen1()
                else:
                    df1 = pd.read_csv("StudentDetails\StudentDetails.csv")
                    aa1 = df1.loc[df1['Enrollment'] == ENROLLMENT]['Name'].values
                    ENR_ENTRY.delete(first=0, last=22)
                    STUDENT_ENTRY.delete(first=0, last=22)

            def create_csv():
                import csv
                csv_name = 'E:/adnan asad/FACE RECOGNIATION SYSTEM/Attendance/Manually Attendance/'+DB_table_name+'.csv'
                col_names1 = ['Enrollment', 'Name', 'Date', 'Time']
                attendance1 = pd.DataFrame(columns=col_names1)
                attendance1.loc[len(attendance1)] = [ENROLLMENT, STUDENT, Date, timeStamp]
                attendance1 = attendance1.drop_duplicates(['Enrollment'], keep='first')
                print(attendance1)
                attendance1.to_csv(csv_name, index=False)
                CSV_Success = "CSV created Successfully"
                Notifi.configure(text=CSV_Success, fg="white", bg="gray11", highlightthickness=2, highlightbackground="white", highlightcolor="white", width=33, font=('times', 19, 'bold'))
                Notifi.place(x=180, y=380)
                import csv
                import tkinter
                root = tkinter.Toplevel()
                root.title("Attendance of " + subb)
                root.configure(background='black')
                with open(csv_name, newline="") as file:
                    reader = csv.reader(file)
                    r = 0
                    for col in reader:
                        c = 0
                        for row in col:
                            label = tkinter.Label(root, width=13, height=1, fg="black", font=('times', 13, ' bold '), bg="light blue", text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()

            Notifi = tk.Label(MFW, text="CSV CREATED SUCCESSFULLY", fg="white", bg="gray11", highlightthickness=2, highlightbackground="white", highlightcolor="white", height=2, width=33, font=('times', 19, 'bold'))

            c1ear_enroll = tk.Button(MFW, text="CLEAR", command=remove_enr, fg="black", bg="cadetblue", width=10, height=1, activebackground="cadetblue4", font=('times', 15, ' bold '))
            c1ear_enroll.place(x=690, y=105)

            c1ear_student = tk.Button(MFW, text="CLEAR", command=remove_student, fg="black", bg="cadetblue", width=10, height=1, activebackground="cadetblue4", font=('times', 15, ' bold '))
            c1ear_student.place(x=690, y=205)

            DATA_SUB = tk.Button(MFW, text="ENTER DATA", command=enter_data_DB, fg="black", bg="deepskyblue4", width=20, height=2, activeforeground="white", activebackground="turquoise3", font=('times', 15, ' bold '))
            DATA_SUB.place(x=150, y=300)

            MAKE_CSV = tk.Button(MFW, text="CONVERT TO CSV", command=create_csv, fg="black", bg="cadetblue", width=20, height=2, activebackground="cadetblue4", font=('times', 15, ' bold '))
            MAKE_CSV.place(x=550, y=300)

            MFW.mainloop()

    SUB = tk.Label(sb, text="ENTER SUBJECT", width=15, height=2, fg="black", bg="darkslategray2", font=('times', 15, ' bold '))
    SUB.place(x=30, y=100)
    global SUB_ENTRY
    SUB_ENTRY = tk.Entry(sb, width=20, bg="gray79", fg="black", font=('times', 23, ' bold '))
    SUB_ENTRY.place(x=250, y=105)

    fill_manual_attendance = tk.Button(sb, text="FILL ATTENDANCE", command=fill_attendance, fg="black", bg="deepskyblue4", width=20, height=2, activeforeground="white", activebackground="turquoise3", font=('times', 15, ' bold '))
    fill_manual_attendance.place(x=250, y=180)
    sb.mainloop()


def clear():
    txt.delete(first=0, last=22)


def clear1():
    txt2.delete(first=0, last=22)


def del_sc1():
    sc1.destroy()


def err_screen():
    global sc1
    sc1 = tk.Toplevel()
    sc1.geometry('420x150')
    sc1.iconbitmap('E:/adnan asad/FACE RECOGNIATION SYSTEM/images_48x48 .ico')
    sc1.title('WARNING!!')
    sc1.configure(background='black')
    Label(sc1, text='ENROLLMENT & NAME REQUIRED!!!', fg='black', bg='cadetblue', font=('times', 16, 'bold')).pack()
    Button(sc1, text='OK', command=del_sc1, fg="black", bg="deepskyblue4", width=9, height=1, activeforeground="white", activebackground="turquoise3", font=('times', 15, ' bold ')).place(x=150, y=80)


def del_sc2():
    sc2.destroy()


def del_scc():
    scc.destroy()


def err_screen_time():
    global scc
    scc = tk.Toplevel()
    scc.geometry('420x150')
    scc.iconbitmap('E:/adnan asad/FACE RECOGNIATION SYSTEM/images_48x48 .ico')
    scc.title('WARNING!!')
    scc.configure(background='black')

    xc = tk.Label(scc, text='PLEASE ENTER CLASS DURATION!!!', fg='black', bg='cadetblue', font=('times', 18, ' bold'))
    xc.place(x=0, y=0)
    Button(scc, text='OK', command=del_scc, fg="black", bg="deepskyblue4", width=9, height=1, activeforeground="white", activebackground="turquoise3", font=('times', 15, ' bold ')).place(x=150, y=80)


def err_screen1():
    global sc2
    sc2 = tk.Toplevel()
    sc2.geometry('420x150')
    sc2.iconbitmap('E:/adnan asad/FACE RECOGNIATION SYSTEM/images_48x48 .ico')
    sc2.title('WARNING!!')
    sc2.configure(background='black')

    x = tk.Label(sc2, text='PLEASE ENTER YOUR SUBJECT NAME!!!', fg='black', bg='cadetblue', font=('times', 16, ' bold'))
    x.place(x=0, y=0)
    Button(sc2, text='OK', command=del_sc2, fg="black", bg="deepskyblue4", width=9, height=1, activeforeground="white", activebackground="turquoise3", font=('times', 15, ' bold ')).place(x=150, y=80)


# ##For take images for datasets
def take_img():
    l1 = txt.get()
    l2 = txt2.get()
    if l1 == '':
        err_screen()
    elif l2 == '':
        err_screen()
    else:
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            Enrollment = txt.get()
            Name = txt2.get()
            sampleNum = 0
            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder
                    cv2.imwrite("TrainingImage/ " + Name + "." + Enrollment + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    cv2.imshow('Frame', img)
                # wait for 100 milliseconds
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                # break if the sample number is more than 70
                elif sampleNum > 70:
                    break
            cam.release()
            cv2.destroyAllWindows()
            ts = time.time()
            Date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            row = [Enrollment, Name, Date, Time]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile, delimiter=',')
                writer.writerow(row)
                csvFile.close()
            res = "IMAGES SAVED FOR ENROLLMENT : " + Enrollment + " Name : " + Name
            Notification.configure(text=res, bg="gray11", fg="white", highlightthickness=2, highlightbackground="white", highlightcolor="white", width=55, font=('times', 18, 'bold'))
            Notification.place(x=250, y=390)
        except FileExistsError as F:
            f = 'STUDENT DATA ALREADY EXISTS'
            Notification.configure(text=f, bg="gray11", fg="white", highlightthickness=2, highlightbackground="white", highlightcolor="white", width=21)
            Notification.place(x=250, y=390)


# ##for choose subject and fill attendance
def subjectchoose():
    def Check_attendance():
        A = int(tim.get())
        B = (int(A / 30))
        Fillattendances()
        for i in range(B):
            cv2.waitKey(10000)
            print("FILLING ATTENDANCE")
            Fillattendances()
            print("ATTENDANCE FILLED", B)
            B = B - 1
            """
            10 sec = 10000
            30 sec = 30000
            1 min = 60000
            15 min = 900000
            30 min = 1800000
            """
        Probability()

    def Fillattendances():
        sub = tx.get()
        now = time.time()  # ##For calculate seconds of video
        future = now + 20
        if time.time() < future:
            if sub == '':
                err_screen1()
            else:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                try:
                    recognizer.read("E:/adnan asad/FACE RECOGNIATION SYSTEM/TrainingImageLabel/Train model.yml")
                except:
                    e = 'MODEL NOT FOUND, PLEASE TRAIN MODEL'
                    Notifica.configure(text=e, bg="gray11", fg="white", highlightthickness=2, highlightbackground="white", highlightcolor="white", width=33, font=('times', 15, 'bold'))
                    Notifica.place(x=250, y=390)

                harcascadePath = "E:/adnan asad/FACE RECOGNIATION SYSTEM/haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(harcascadePath)
                df = pd.read_csv("E:/adnan asad/FACE RECOGNIATION SYSTEM/StudentDetails/StudentDetails.csv")
                cam = cv2.VideoCapture(0)
                col_names = ['Enrollment', 'Name', 'Date', 'Time']
                attendance = pd.DataFrame(columns=col_names)
                while True:
                    ret, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    # reading and scaling face from gray image using scale factor 1.2 and neighbor number = 5
                    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if conf < 70:
                            print(conf)
                            global Subject
                            global aa
                            global date
                            global timeStamp
                            Subject = tx.get()
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                            aa = df.loc[df['Enrollment'] == Id]['Name'].values
                            attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                        else:
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)

                    attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
                    cv2.imshow('Filling attendance..', im)
                    if cv2.waitKey(1) == ord('q'):
                        break

                Subject = tx.get()
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                Hour, Minute, Second = timeStamp.split(":")
                path = "E:/adnan asad/FACE RECOGNIATION SYSTEM/Attendance/"
                os.chdir(path)
                NF = Subject + "-" + date
                isExist = os.path.exists(NF)
                if not isExist:
                    # Create a new directory because it does not exist
                    os.makedirs(NF)
                fileName = Subject + "-" + date + "/" + Subject + "_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
                attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
                print(attendance)
                attendance.to_csv(fileName, index=False)

                M = 'ATTENDANCE FILLED SUCCESSFULLY'
                Notifica.configure(text=M, highlightthickness=2, highlightbackground="white", highlightcolor="white", bg="gray11", fg="white", width=33, font=('times', 15, 'bold'))
                Notifica.place(x=100, y=300)

                cam.release()
                cv2.destroyAllWindows()

                import csv
                import tkinter
                root = tkinter.Tk()
                root.title("ATTENDANCE OF " + Subject)
                root.configure(background='BLACK')
                cs = 'E:/adnan asad/FACE RECOGNIATION SYSTEM/Attendance/' + fileName
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:
                            label = tkinter.Label(root, width=12, height=1, fg="black", font=('times', 15, ' bold '), bg="light blue", text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.after(5000, root.destroy())
                # root.after(5000, root.destroy())
                print(attendance)
    from IPython.display import display

    def Probability():
        subject = tx.get()
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        path = Path("E:/adnan asad/FACE RECOGNIATION SYSTEM/Attendance/" + subject + "-" + date + "/")
        csvlist = path.glob("*.csv")
        col_names = ['Enrollment', 'Name', 'Date', 'Time']
        finalcsvsheet = pd.DataFrame(columns=col_names)
        csvs = [pd.concat(pd.read_csv(g, header=None, skiprows=1) for g in csvlist)]
        """csvs = pd.DataFrame(csvs, columns=col_names)"""
        print(finalcsvsheet, csvs)

        """# to iterate csv file one by one
        # inside the folder
        for file in csvlist:
            # combining multiple excel worksheets
            # into single data frames
            df = pd.concat(pd.read_csv(file))

            # appending csv files one by one
            finalcsvsheet = finalcsvsheet.append(df, ignore_index=True)
"""
        # to print the combined data
        """print('Final Sheet:')
        display(finalcsvsheet)"""
        """for f in csvlist:
            # read the csv file
            df = pd.read_csv(f)

            # print the location and filename
            # print('Location:', f)
            # print('File Name:', f.split("\\")[-1])

            # print the content
            print('Content:')
            display(df)"""

    def ForIntegerInput_Time(inStr, acttyp):
        if acttyp == '1':  # insert
            if not inStr.isdigit():
                return False
        return True

    # ##windo is frame for subject chooser
    windo = tk.Toplevel()
    windo.title("ENTER SUBJECT NAME...")
    windo.geometry('630x360')
    windo.iconbitmap('E:/adnan asad/FACE RECOGNIATION SYSTEM/images_48x48 .ico')
    windo.configure(background='BLACK')
    img_2 = Image.open(
        'E:\\adnan asad\\FACE RECOGNIATION SYSTEM\\synthetic-data-1024x640_630x360.jpg')
    bg_2 = ImageTk.PhotoImage(img_2)

    label_2 = Label(windo, image=bg_2)
    label_2.place(x=0, y=0)
    Notifica = tk.Label(windo, text="ATTENDANCE FILLED SUCCESSFULLY",  highlightthickness=2, highlightbackground="white", highlightcolor="white", bg="gray11", fg="white", width=33, height=2, font=('times', 15, 'bold'))

    sub = tk.Label(windo, text="ENTER SUBJECT", width=20, height=2, fg="black", bg="darkslategray2", font=('times', 15, ' bold '))
    sub.place(x=30, y=80)

    tx = tk.Entry(windo, width=20, bg="gray79", fg="black", font=('times', 23, ' bold '))
    tx.place(x=290, y=85)

    TIM = tk.Label(windo, text="ENTER TIME (IN MIN)", width=20, height=2, fg="black", bg="darkslategray2", font=('times', 15, ' bold '))
    TIM.place(x=30, y=150)

    tim = tk.Entry(windo, width=20, bg="gray79", fg="black", font=('times', 23, ' bold '))
    tim['validatecommand'] = (tim.register(ForIntegerInput_Time), '%P', '%d')
    tim.place(x=290, y=155)

    fill_a = tk.Button(windo, text="FILL ATTENDANCE", fg="black", command=Check_attendance, bg="deepskyblue4", width=20, height=2, activeforeground="white", activebackground="turquoise3", font=('times', 15, ' bold '))
    fill_a.place(x=290, y=220)
    windo.mainloop()


def admin_panel():
    win = tk.Toplevel()
    img_1 = Image.open('E:\\adnan asad\\FACE RECOGNIATION SYSTEM\\synthetic-data-1024x640_1_880x420.jpg')
    bg_1 = ImageTk.PhotoImage(img_1)

    label_1 = Label(win, image=bg_1)
    label_1.place(x=0, y=0)
    win.title("LOGIN")
    win.geometry('880x420')
    win.configure(background='#00538C')
    win.iconbitmap('E:/adnan asad/FACE RECOGNIATION SYSTEM/images_48x48 .ico')

    def log_in():
        username = un_entr.get()
        password = pw_entr.get()

        if username == 'ADNAN':
            if password == '249':
                win.destroy()
                import csv
                import tkinter
                root = tkinter.Toplevel()
                root.title("STUDENT DETAILS")
                root.configure(background='black')
                root.wm_iconbitmap('E:/adnan asad/FACE RECOGNIATION SYSTEM/images_48x48 .ico')

                cs = 'E:/adnan asad/FACE RECOGNIATION SYSTEM/StudentDetails/StudentDetails.csv'
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0
                    # show student list register
                    for col in reader:
                        c = 0
                        for row in col:
                            label_list = tkinter.Label(root, width=12, height=1, fg="black", font=('times', 15, ' bold '), bg="darkslategray2", text=row, relief=tkinter.RIDGE)
                            label_list.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()
            else:
                valid = 'INCORRECT ID OR PASSWORD'
                Nt.configure(text=valid, highlightthickness=2, highlightbackground="white", highlightcolor="white", bg="gray11", fg="white", width=38, font=('times', 19, 'bold'))
                Nt.place(x=120, y=350)

        else:
            valid = 'INCORRECT ID OR PASSWORD'
            Nt.configure(text=valid, highlightthickness=2, highlightbackground="white", highlightcolor="white", bg="gray11", fg="white", width=38, font=('times', 19, 'bold'))
            Nt.place(x=120, y=350)

    Nt = tk.Label(win, text="PLEASE ENTER USERNAME & PASSWORD", highlightthickness=2, highlightbackground="white", highlightcolor="white", bg="gray11", fg="white", width=40, height=2, font=('times', 19, 'bold'))
    Nt.place(x=120, y=350)

    un = tk.Label(win, text="ENTER USERNAME", width=15, height=2, fg="black", bg="darkslategray2", font=('times', 15, ' bold '))
    un.place(x=30, y=50)

    pw = tk.Label(win, text="ENTER PASSWORD", width=15, height=2, fg="black", bg="darkslategray2", font=('times', 15, ' bold '))
    pw.place(x=30, y=150)

    def c00():
        un_entr.delete(first=0, last=22)

    un_entr = tk.Entry(win, width=20, bg="gray79", fg="black", font=('times', 23, ' bold '))
    un_entr.place(x=290, y=55)

    def c11():
        pw_entr.delete(first=0, last=22)

    pw_entr = tk.Entry(win, width=20, show="*", bg="gray79", fg="black", font=('times', 23, ' bold '))
    pw_entr.place(x=290, y=155)

    c0 = tk.Button(win, text="CLEAR", command=c00, fg="black", bg="cadetblue", width=10, height=1, activebackground="cadetblue4", font=('times', 15, ' bold '))
    c0.place(x=690, y=55)

    c1 = tk.Button(win, text="CLEAR", command=c11, fg="black", bg="cadetblue", width=10, height=1, activebackground="cadetblue4", font=('times', 15, ' bold '))
    c1.place(x=690, y=155)

    Login = tk.Button(win, text="LOGIN", fg="black", bg="deepskyblue4", width=20, height=2, activeforeground="white", activebackground="turquoise3", command=log_in, font=('times', 15, ' bold '))
    Login.place(x=290, y=250)
    win.mainloop()


# ##For train the model
def trainimg():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    global detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    try:
        global faces, Id
        faces, Id = getImagesAndLabels("TrainingImage")
    except Exception as e:
        l = 'PLEASE MAKE "TrainingImage" FOLDER TO PUT IMAGES'
        Notification.configure(text=l, fg="white", bg="gray11", highlightthickness=2, highlightbackground="white", highlightcolor="white", width=50, height=2, font=('times', 18, 'bold'))
        Notification.place(x=250, y=390)

    recognizer.train(faces, np.array(Id))
    try:
        recognizer.save("TrainingImageLabel\Train model.yml")
    except Exception as e:
        q = 'PLEASE MAKE "TrainingImageLabel" FOLDER'
        Notification.configure(text=q, fg="white", bg="gray11", highlightthickness=2, highlightbackground="white", highlightcolor="white", width=55, height=2, font=('times', 18, 'bold'))
        Notification.place(x=250, y=390)

    res = "MODEL TRAINED"
    Notification.configure(text=res, fg="white", bg="gray11", highlightthickness=2, highlightbackground="white", highlightcolor="white", width=50, height=2, font=('times', 18, 'bold'))
    Notification.place(x=250, y=390)


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empty face list
    faceSamples = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image

        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces = detector.detectMultiScale(imageNp)
        # If a face is there then append that in the list as well as Id of it
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids


window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
img_icon = PhotoImage(file='images_48x48.png')
window.tk.call('wm', 'iconphoto', window._w, img_icon)


def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("QUIT", "DO YOU WANT TO QUIT?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

IMG_UNI_LOGO = ImageTk.PhotoImage(Image.open("UNIVERSITY_LOGO_140x140.png"))
LABEL = tk.Label(window, image=IMG_UNI_LOGO, bg="deepskyblue3")
LABEL.place(x=50, y=20)

IMG_DEPART_LOGO = ImageTk.PhotoImage(Image.open("DEPARTMENT_LOGO_140x140.png"))
LABEL1 = tk.Label(window, image=IMG_DEPART_LOGO, bg="deepskyblue3")
LABEL1.place(x=1090, y=20)

message = tk.Label(window, text="FACE RECOGNITION ATTENDANCE SYSTEM", bg="deepskyblue3", fg="black", width=39, height=3, font=('times', 30, 'italic bold '))
message.place(x=190, y=20)

Notification = tk.Label(window, text="ALL THINGS GOOD", fg="white", bg="gray11", highlightthickness=2, highlightbackground="white", highlightcolor="white", width=50, height=2, font=('times', 18, 'bold'))
Notification.place(x=250, y=390)

lbl = tk.Label(window, text="ENTER ENROLLMENT", width=20, height=2, fg="black", bg="darkslategray2", font=('times', 15, ' bold '))
lbl.place(x=200, y=200)


def ForIntegerInput(inStr, acttyp):
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True


txt = tk.Entry(window, validate="key", width=20, bg="gray79", fg="black", font=('times', 25, ' bold '))
txt['validatecommand'] = (txt.register(ForIntegerInput), '%P', '%d')
txt.place(x=550, y=210)

lbl2 = tk.Label(window, text="ENTER NAME", width=20, fg="black", bg="darkslategray2", height=2, font=('times', 15, ' bold '))
lbl2.place(x=200, y=300)

txt2 = tk.Entry(window, width=20, bg="gray79", fg="black", font=('times', 25, ' bold '))
txt2.place(x=550, y=310)

clearButton = tk.Button(window, text="CLEAR", command=clear, fg="black", bg="cadetblue", width=10, height=1, activebackground="cadetblue4", font=('times', 15, ' bold '))
clearButton.place(x=950, y=210)

clearButton1 = tk.Button(window, text="CLEAR", command=clear1, fg="black", bg="cadetblue", width=10, height=1, activebackground="cadetblue4", font=('times', 15, ' bold '))
clearButton1.place(x=950, y=310)

AP = tk.Button(window, text="CHECK STUDENT LIST", command=admin_panel, fg="black", bg="darkturquoise", width=23, height=1, activebackground="cadetblue4", font=('times', 15, ' bold '))
AP.place(x=945, y=630)

takeImg = tk.Button(window, text="TAKE IMAGES", command=take_img, fg="black", bg="deepskyblue4", width=20, height=3, activeforeground="white", activebackground="turquoise3", font=('times', 15, ' bold '))
takeImg.place(x=90, y=500)

trainImg = tk.Button(window, text="TRAIN IMAGES", fg="black", command=trainimg, bg="cadetblue", width=20, height=3, activebackground="cadetblue4", font=('times', 15, ' bold '))
trainImg.place(x=360, y=500)

FA = tk.Button(window, text="AUTOMATIC ATTENDANCE", fg="black", command=subjectchoose, bg="deepskyblue4", width=22, height=3, activeforeground="white", activebackground="turquoise3", font=('times', 15, ' bold '))
FA.place(x=630, y=500)

quitWindow = tk.Button(window, text="MANUAL ATTENDANCE", command=manually_fill, fg="black", bg="cadetblue", width=25, height=3, activebackground="cadetblue4", font=('times', 15, ' bold '))
quitWindow.place(x=930, y=500)

window.mainloop()
