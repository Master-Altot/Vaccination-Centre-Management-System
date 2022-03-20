from tkinter import *
from tkinter import ttk
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

root = Tk()
root.geometry("550x300")
root.title("Vaccine Center Management")
#################STAFFF################
def Staff():

    root2 = Tk()
    root2.geometry("500x300")
    root2.title("Staff Management")


    def updatedelete():

        root3 = Tk()
        root3.geometry("500x250")
        root3.title("Staff Management")
    
        def update():
            
            mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
            mycursor=mydb.cursor()
            
            ID = E_Staff_ID.get()
            name = E_Name.get()
            post = E_Post.get()
            
      
            if (name=="" or ID =="" or Post==""):
                 Messagebox.showinfo("Update Status", "All fields are required")
            else:
                mycursor.execute("update staff set name='"+ name +"',post='" +post +"' where ID ='"+ID+"'")
                mydb.commit()
                Messagebox.showinfo("Update Status", "Updated successfully")
  
                E_Staff_ID.delete(0,'end')
                E_Name.delete(0,'end')
                E_Post.delete(0,'end')
            
            mydb.close()  
        def delete():

            if(E_Staff_ID.get()==""):
                Messagebox.showinfo("Delete Status" , "Patient ID is Missing")
            else:
                mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
                mycursor=mydb.cursor()
        
                mycursor.execute("delete from staff where ID ='"+ E_Staff_ID.get() +"'")
                mydb.commit()
                Messagebox.showinfo("Delete Status" , "Deleted Succesfully")
                mydb.close()

                E_Staff_ID.delete(0,'end')
                E_Name.delete(0,'end')
                E_Post.delete(0,'end')
                
                
        
        Staff_ID=Label(root3,text="Enter ID of Staff" , font="Bold")
        Staff_ID.place(x=20 , y=30)
        
        E_Staff_ID=Entry(root3)
        E_Staff_ID.place(x=350 , y=30)

        Name=Label(root3,text="Enter Name of Staff" , font="Bold")
        Name.place(x=20 , y=70)
        
        E_Name=Entry(root3)
        E_Name.place(x=350 , y=70)
        
        Post=Label(root3,text="Enter Post of staff" , font="Bold")
        Post.place(x=20 , y=110)
        
        E_Post=Entry(root3)
        E_Post.place(x=350 , y=110)   
    
        
    #####################
    
    
        update=Button(root3, text="Update" , font=("italic", 10) , bg="white" , command=update)
        update.place(x=120 , y = 175)
    
        delete=Button(root3, text="Delete" , font=("italic", 10) , bg="white" , command=delete)
        delete.place(x=220 , y = 175)
    
        Close=Button(root3, text="Close" , font=("italic", 10) , bg="white" , command=root3.destroy)
        Close.place(x=320 , y = 175)
    
    
    def insert():
        mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
        mycursor=mydb.cursor()
    
        mycursor.execute("select max(ID) from staff")
        
        for value in mycursor:
            ID = int(''.join(map(str,value))) + 1  #tupple to string then int
        
        str(ID)
        name = E_Name.get()
        post =  E_Post.get()
        S_ID= "%s" % ID  #into string
        
        #data=(",".join([P_ID , name , date , vaccine]))
       
        
        if (name=="" or post==""):
            Messagebox.showinfo("Insert Status", "All fields are required")
        else:
            mycursor.execute("insert into staff values('"+ S_ID +"','"+ name +"','" +post+"')")
            mydb.commit()
            Messagebox.showinfo("Insert Status", "Inserted successfully")
    
            E_Name.delete(0,'end')
            E_Post.delete(0,'end')
            mydb.close()
    
    def showstaff():
         
        root_staff=Tk()
        root_staff.geometry("500x300")
    
        headings = ttk.Treeview(root_staff , columns = (1,2,3) , show = "headings" , height="15")
    
        headings.column("1" , width=50 , anchor= CENTER )
        headings.column("2", width=130 , anchor= CENTER )
        headings.column("3", width=110 , anchor= CENTER )
    
        headings.heading("1", text="ID")
        headings.heading("2", text="Name")
        headings.heading("3", text="Post")
        
        headings.pack(padx=5 , pady=10)
    
        done=Button(root_staff, text="Done" , font=("italic", 10) , bg="white" , command=root_staff.destroy)
        done.place(x=225,y=250)
    
    
        mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
        mycursor=mydb.cursor()  
        mycursor.execute("Select * from staff")
    
        Staffs= mycursor.fetchall()
        #mydb.commit()
    
        for staff in Staffs:
            headings.insert('' , 'end' , values = staff)
        
        
        #Messagebox.showinfo("Show Status" , "Data Fetched Succesfully")
        mydb.close()  

        
    def search():
        
        ID = E_Staff_ID.get()
        Data_list_staff1.delete(0)
        mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
        mycursor=mydb.cursor()  
        mycursor.execute("Select * from staff where ID='"+ID+"'")
    
        Staffs= mycursor.fetchall()
        #mydb.commit()
    
        for staff in Staffs:
            Detailes = str(staff[0])+'  '+staff[1]+'  '+staff[2]
            Data_list_staff1.insert(1, Detailes)
        
        
        #Messagebox.showinfo("Show Status" , "Data Fetched Succesfully")
        mydb.close()

        E_Staff_ID.delete(0,'end')  
        

    
    Name=Label(root2,text="Enter Name of Staff" , font="Bold")
    Name.place(x=20 , y=30)
    
    E_Name=Entry(root2)
    E_Name.place(x=350 , y=30)
    
    Post=Label(root2,text="Enter Post of staff" , font="Bold")
    Post.place(x=20 , y=70)
    
    E_Post=Entry(root2)
    E_Post.place(x=350 , y=70)

    Staff_ID=Label(root2,text="Enter ID of Staff to search" , font="Bold")
    Staff_ID.place(x=20 , y=170)

    E_Staff_ID=Entry(root2)
    E_Staff_ID.place(x=260 , y=175)

    Data_list_staff1=Listbox(root2,width = 55, height = 1, bg = "#262626", fg = "cyan", selectbackground = 'blue', selectforeground = 'black')
    Data_list_staff1.place(x=20 , y=220)
    
    ###########################
    insert=Button(root2, text="Insert" , font=("italic", 10) , bg="white" , command=insert)
    insert.place(x=20 , y = 120)
    
    updateDelete=Button(root2, text="Update/Delete" , font=("italic", 10) , bg="white" , command=updatedelete)
    updateDelete.place(x=120 , y = 120)
    
    show=Button(root2, text="Show" , font=("italic", 10) , bg="white" , command=showstaff)
    show.place(x=270 , y = 120)

    search=Button(root2, text="Search" , font=("italic", 10) , bg="white" , command=search)
    search.place(x=380 , y = 174)
######################STAFFFF############

##################VACCINE################   
def Vaccine():
    
    rootv = Tk()
    rootv.geometry("500x300")
    rootv.title("Vaccine Management")
    
    def insert():
        
        mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
        mycursor=mydb.cursor()
    
        
        name = E_Name.get()
        Adate = E_Arival_date.get()
        Edate = E_Expiry_date.get()
        dose = E_Dose.get()
        avilable = E_Avilable.get()
       
        
        if (name=="" or Adate=="" or Edate =="" or dose == "" or avilable ==""):
            Messagebox.showinfo("Insert Status", "All fields are required")
        else:
            mycursor.execute("insert into vaccine values('"+ name +"','"+ Adate +"','" +Edate+"','" +dose+"','" +avilable+"')")
            mydb.commit()
            Messagebox.showinfo("Insert Status", "Inserted successfully")
    
            E_Name.delete(0,'end')
            E_Arival_date.delete(0,'end')
            E_Expiry_date.delete(0,'end')
            E_Dose.delete(0,'end')
            E_Avilable.delete(0,'end')
            
            mydb.close()
    
        

    def update():

        
        mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
        mycursor=mydb.cursor()
    
        
        name = E_Name.get()
        Adate = E_Arival_date.get()
        Edate = E_Expiry_date.get()
        dose = E_Dose.get()
        avilable = E_Avilable.get()
       
        
        if (name=="" or Adate=="" or Edate =="" or dose == "" or avilable ==""):
            Messagebox.showinfo("Insert Status", "All fields are required")
        else:
            mycursor.execute("update vaccine set Arrival_date='"+ Adate +"',Expiry_date='" +Edate+"',Dose_to_be_given='" +dose+"', Available='" +avilable+"' where name='"+ name +"'")
            mydb.commit()
            Messagebox.showinfo("Update Status", "Updated successfully")
    
            E_Name.delete(0,'end')
            E_Arival_date.delete(0,'end')
            E_Expiry_date.delete(0,'end')
            E_Dose.delete(0,'end')
            E_Avilable.delete(0,'end')
            
            mydb.close()
    

        

    def delete():
        
        
        if(E_Name.get()==""):
            Messagebox.showinfo("Delete Status" , "Patient ID is Missing")
        else:
            mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
            mycursor=mydb.cursor()
   
            mycursor.execute("delete from vaccine where name ='"+ E_Name.get() +"'")
            mydb.commit()
            Messagebox.showinfo("Delete Status" , "Deleted Successfully")
            mydb.close()   
            E_Name.delete(0,'end')
            E_Arival_date.delete(0,'end')
            E_Expiry_date.delete(0,'end')
            E_Dose.delete(0,'end')
            E_Avilable.delete(0,'end')

        

    def showvaccine():
        
        root_vaccine=Tk()
        root_vaccine.geometry("700x400")
    
        headings = ttk.Treeview(root_vaccine , columns = (1,2,3,4,5) , show = "headings" , height="15")
    
        headings.column("1" , width=110 , anchor= CENTER )
        headings.column("2", width=110 , anchor= CENTER )
        headings.column("3", width=110 , anchor= CENTER )
        headings.column("4", width=110 , anchor= CENTER )
        headings.column("5", width=110 , anchor= CENTER )
    
        headings.heading("1", text="Name")
        headings.heading("2", text="Arr Date")
        headings.heading("3", text="Exp Date")
        headings.heading("4", text="Dose")
        headings.heading("5", text="Avl Dose")
        
        headings.pack(padx=5 , pady=10)

        done=Button(root_vaccine, text="Done" , font=("italic", 10) , bg="white" , command=root_vaccine.destroy)
        done.place(x=300,y=250)
    
    
        mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
        mycursor=mydb.cursor()  
        mycursor.execute("Select * from vaccine")
    
        vaccines= mycursor.fetchall()
        #mydb.commit()
    
        for vaccine in vaccines:
            headings.insert('' , 'end' , values = vaccine)
        
        
        #Messagebox.showinfo("Show Status" , "Data Fetched Succesfully")
        mydb.close()  

        
    

   ################################
    Name=Label(rootv,text="Enter Name of Vaccine " , font="Bold")
    Name.place(x=20 , y=30)
    
    E_Name=Entry(rootv)
    E_Name.place(x=350 , y=30)
    
    Arival_date=Label(rootv,text="Enter Arrival date of Vaccine" , font="Bold")
    Arival_date.place(x=20 , y=70)
    
    E_Arival_date=Entry(rootv)
    E_Arival_date.place(x=350 , y=70)

    Expiry_date=Label(rootv,text="Enter Expiry date of Vaccine" , font="Bold")
    Expiry_date.place(x=20 , y=110)

    E_Expiry_date=Entry(rootv)
    E_Expiry_date.place(x=350 , y=110)

    Dose=Label(rootv,text="Enter dose to be given" , font="Bold")
    Dose.place(x=20 , y=150)

    E_Dose=Entry(rootv)
    E_Dose.place(x=350 , y=150)

    Avilable=Label(rootv,text="Enter Available dose of vaccine" , font="Bold")
    Avilable.place(x=20 , y=190)

    E_Avilable=Entry(rootv)
    E_Avilable.place(x=350 , y=190)
    
    
    ###########################
    insert=Button(rootv, text="Insert" , font=("italic", 10) , bg="white" , command=insert)
    insert.place(x=20 , y = 240)
    
    update=Button(rootv, text="Update" , font=("italic", 10) , bg="white" , command=update)
    update.place(x=120 , y = 240)

    delete=Button(rootv, text="Delete" , font=("italic", 10) , bg="white" , command=delete)
    delete.place(x=220 , y = 240)
    
    show=Button(rootv, text="Show" , font=("italic", 10) , bg="white" , command=showvaccine)
    show.place(x=320 , y = 240)

    
###############VAccine##############

###########get##########################
def get():

    root1=Tk()
    root1.geometry("800x400")

    headings = ttk.Treeview(root1 , columns = (1,2,3,4,5,6,7,8) , show = "headings" , height="15")
    
    headings.column("1" , width=50 , anchor= CENTER )
    headings.column("2", width=130 , anchor= CENTER )
    headings.column("3", width=110 , anchor= CENTER )
    headings.column("4", width=110 , anchor= CENTER )
    headings.column("5", width=110 , anchor= CENTER )
    headings.column("6", width=110 , anchor= CENTER )
    headings.column("7", width=60 , anchor= CENTER )
    headings.column("8", width=60 , anchor= CENTER )

    headings.heading("1", text="P ID")
    headings.heading("2", text="Name")
    headings.heading("3", text="Vaccine")
    headings.heading("4", text="Vaccine Date")
    headings.heading("5", text="Side Effect")
    headings.heading("6", text="Next Date")
    headings.heading("7", text="GvnDose")
    headings.heading("8", text="RmgDose")
    
    headings.pack(padx=5 , pady=10)


    done=Button(root1, text="Done" , font=("italic", 10) , bg="white" , command=root1.destroy)
    done.place(x=400,y=310)


    mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
    mycursor=mydb.cursor()  
    mycursor.execute("Select * from patient")

    Patients= mycursor.fetchall()
    #mydb.commit()

    for patient in Patients:
        headings.insert('' , 'end' , values = patient)
    
    
    #Messagebox.showinfo("Show Status" , "Data Fetched Succesfully")
    mydb.close()  
########################get############


#################################

Staff_label=Label(root,text="For Options Related For Staff Management" , font="Bold")
Staff_label.place(x=30 , y=30)

Vaccine_lable=Label(root,text="For Options Related For Vaccine Management" , font="Bold")
Vaccine_lable.place(x=30 , y=110)


Patinet_lable=Label(root,text="To Check Patient Record" , font="Bold")
Patinet_lable.place(x=30 , y=190)


############################
Staff=Button(root, text="Staff" , font=("italic", 10) , bg="red" , command=Staff )
Staff.place(x=230 , y = 70)

Vaccine=Button(root, text="Vaccine" , font=("italic", 10) , bg="red" , command=Vaccine)
Vaccine.place(x=230 , y = 150)

show=Button(root, text="Show" , font=("italic", 10) , bg="red" , command=get)
show.place(x=230 , y = 230)



root.mainloop()
