
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class Student:
    def __init__(self, root):
        self.root= root
        self.root.title("Student Management System")
        self.root.geometry('1350x750+0+0')
        title=Label(self.root, text="Student Management System", bd=8, relief= GROOVE, font=("times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        manage_frame.place(x=10,y=90, height=600, width=500)

        m_title = Label(manage_frame, text="Manage Students", font=("times new roman", 27, "bold"), bg="crimson",fg="white")
        m_title.grid(row=0, columnspan=2,pady=10, padx=20)

        lbl_roll = Label(manage_frame, text="Roll No.",font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_roll.grid(row=1, column=0,padx=20,pady=10, sticky="w")

        text_roll = Entry(manage_frame, textvariable=self.Roll_No_var, font=("times new roman", 20, "bold"), bd=4, relief=GROOVE)
        text_roll.grid(row=1, column=1,padx=20,pady=10, sticky="w")

        lbl_name = Label(manage_frame, text="Name", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        text_name = Entry(manage_frame,textvariable=self.name_var, font=("times new roman", 20, "bold"), bd=4, relief=GROOVE)
        text_name.grid(row=2, column=1,padx=20, pady=10, sticky="w")

        lbl_email = Label(manage_frame, text="Email", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_email.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        text_email = Entry(manage_frame, textvariable=self.email_var, font=("times new roman", 20, "bold"), bd=4, relief=GROOVE)
        text_email.grid(row=3, column=1,padx=20, pady=10, sticky="w")

        lbl_gender = Label(manage_frame, text="Gender", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_gender.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var, font=("times new roman", 19, "bold"), state="readonly")
        combo_gender['values']=('male','female','other')
        combo_gender.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        lbl_contact = Label(manage_frame, text="Contact", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_contact.grid(row=5, column=0, padx=20, pady=10, sticky="w")

        text_contact = Entry(manage_frame, textvariable=self.contact_var, font=("times new roman", 20, "bold"), bd=4, relief=GROOVE)
        text_contact.grid(row=5, column=1,padx=20, pady=10, sticky="w")

        lbl_dob = Label(manage_frame, text="D.O.B", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_dob.grid(row=6, column=0, padx=20, pady=10, sticky="w")

        text_dob = Entry(manage_frame, textvariable=self.dob_var, font=("times new roman", 20, "bold"), bd=4, relief=GROOVE)
        text_dob.grid(row=6, column=1,padx=20, pady=10, sticky="w")

        lbl_address = Label(manage_frame, text="Address", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_address.grid(row=7, column=0, padx=20, pady=10, sticky="w")

        self.text_address=Text(manage_frame, width=41,height=4,font=("",10))
        self.text_address.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        btn_frame= Frame(manage_frame, bg="crimson")
        btn_frame.place(x=20,y=520,width=435, height=60)
        addbtn=Button(btn_frame, text="Add", width=10, command=self.add_student).grid(row=8, column=0, padx=20, pady=10)
        updatebtn=Button(btn_frame, text="Update", width=10, command=self.update_data).grid(row=8, column=1, padx=10, pady=10)
        deletebtn=Button(btn_frame, text="Delete", width=10, command=self.delete_data).grid(row=8, column=2, padx=10, pady=10)
        clearbtn=Button(btn_frame, text="Clear", width=10, command=self.clear).grid(row=8, column=3, padx=10,pady=10)


        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_frame.place(x=550,y=90, height=600, width=790)

        lbl_search = Label(detail_frame, text="Search By", font=("times new roman", 20, "bold"), bg="crimson",fg="white")
        lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        combo_search=ttk.Combobox(detail_frame, textvariable=self.search_by, font=("times new roman", 19, "bold"), state="readonly", width=10)
        combo_search['values']=('Roll_no','Name','Contact')
        combo_search.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        txt_search = Entry(detail_frame, textvariable=self.search_txt, font=("times new roman", 20, "bold"), bd=4, relief=GROOVE, width=15)
        txt_search.grid(row=0, column=2,padx=20, pady=10, sticky="w")

        searchbtn=Button(detail_frame, text="Search", width=8,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showbtn=Button(detail_frame, text="Show All", width=8,command=self.fetch_data).grid(row=0, column=4, padx=10,pady=10)

        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
        table_frame.place(x=10,y=68, height=500, width=750)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(table_frame, columns=("roll","name","email","gender","contact","dob","address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_student(self):
        myconn = mysql.connector.connect(host = "localhost", user = "root",passwd="$$$$$$", database = "stm")
        cur = myconn.cursor()
        if self.Roll_No_var.get()=='' and self.name_var.get()=='':
            messagebox.showerror('Error','All fields are required')
        cur.execute("insert into Student values(%s,%s,%s,%s,%s,%s,%s)",(
        self.Roll_No_var.get(),
        self.name_var.get(),
        self.email_var.get(),
        self.gender_var.get(),
        self.contact_var.get(),
        self.dob_var.get(),
        self.text_address.get('1.0',END)
        ))
        myconn.commit()
        messagebox.showinfo('Success', 'Record has been inserted')
        self.fetch_data()
        self.clear()
        myconn.close()

    def fetch_data(self):
        myconn = mysql.connector.connect(host = "localhost", user = "root",passwd="$$$$$$", database = "stm")
        cur = myconn.cursor()
        cur.execute("select * from Student")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            myconn.commit()
        myconn.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.text_address.delete('1.0', END)

    def get_cursor(self, event):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.text_address.delete('1.0', END)
        self.text_address.insert(END, row[6])
    def update_data(self):
        myconn = mysql.connector.connect(host = "localhost", user = "root",passwd="$$$$$$", database = "stm")
        cur = myconn.cursor()
        cur.execute("update Student set name= %s, email= %s, gender= %s, contact= %s, dob= %s,address= %s where roll_no=%s",(
        self.name_var.get(),
        self.email_var.get(),
        self.gender_var.get(),
        self.contact_var.get(),
        self.dob_var.get(),
        self.text_address.get('1.0', END),
        self.Roll_No_var.get()
        ))
        myconn.commit()
        self.fetch_data()
        self.clear()
        myconn.close()

    def delete_data(self):
        myconn = mysql.connector.connect(host = "localhost", user = "root",passwd="$$$$$$", database = "stm")
        cur = myconn.cursor()
        cur.execute("delete from Student where roll_no=%s",(self.Roll_No_var.get(),))
        myconn.commit()
        myconn.close()
        self.fetch_data()
        self.clear()
    def search_data(self):
        myconn = mysql.connector.connect(host = "localhost", user = "root",passwd="$$$$$$", database = "stm")
        cur = myconn.cursor()
        cur.execute("select * from Student where "+str(self.search_by.get())+ " LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            myconn.commit()
        myconn.close()

root = Tk()
ob = Student(root)
root.mainloop( )
