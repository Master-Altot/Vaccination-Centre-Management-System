from tkinter import *
from tkinter import ttk
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

root = Tk()
root.geometry("500x250")
root.title("Vaccine Patient")

#############
def Selected(event):
    pass
    

def insert():
    mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
    mycursor=mydb.cursor()
    
    mycursor.execute("select max(P_ID) from patient")
    
    for value in mycursor:
        ID = int(''.join(map(str,value))) + 1  #tupple to string then int
    
    str(ID)
    Vakcn = clicked.get() #tupple
    Vakcn = list(Vakcn)
    Vakcn = Vakcn[2:(len(Vakcn)-3)]
    vaccine=str
    vaccine = ''.join(Vakcn)
    name = E_Patient_name.get()
    date =  E_Vaccination_date.get()
    P_ID= "%s" % ID  #into string
    
    #data=(",".join([P_ID , name , date , vaccine]))
   
    
    if (name=="" or date==""):
        Messagebox.showinfo("Insert Status", "All fields are required")
    else:
        mycursor.execute("insert into patient (P_ID,name,vaccination_date,vaccine_selected) values('"+ P_ID +"','"+ name +"','" +date +"','"+vaccine+"')")
        mydb.commit()
        Messagebox.showinfo("Insert Status", "Inserted successfully")

        E_Patient_name.delete(0,'end')
        E_Vaccination_date.delete(0,'end')
        clicked.set(Vaccine_list[0])
    mydb.close()


    

def updatedelete():

    def Selected2(event):
        print(clicked2.get())

    def update():
            mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
            mycursor=mydb.cursor()
    
            Vakcn = clicked2.get() #tupple
            Vakcn = list(Vakcn)
            Vakcn = Vakcn[2:(len(Vakcn)-3)]
            vaccine=str
            vaccine = ''.join(Vakcn)
            name = E_Patient_name.get()
            date = E_Vaccination_date.get()
            P_ID = E_Patient_ID.get()
            #data=(",".join([P_ID , name , date , vaccine]))
            #print(data)
    
     
            if (name=="" or date=="" or P_ID=="" or vaccine==""):
                 Messagebox.showinfo("Update Status", "All fields are required")
            else:
                mycursor.execute("update patient set name='"+ name +"',vaccination_date='" +date +"',vaccine_selected='"+vaccine+"' where P_ID ='"+P_ID+"'")
                mydb.commit()
                Messagebox.showinfo("Update Status", "Updated successfully")
 
                E_Patient_name.delete(0,'end')
                E_Vaccination_date.delete(0,'end')
                clicked2.set(Vaccine_list[0])
            mydb.close()




    def delete():
        if(E_Patient_ID.get()==""):
            Messagebox.showinfo("Delete Status" , "Patient ID is Missing")
        else:
            mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
            mycursor=mydb.cursor()
    
            mycursor.execute("delete from patient where P_ID ='"+ E_Patient_ID.get() +"'")
            mydb.commit()
            Messagebox.showinfo("Delete Status" , "Deleted Successfully")
            mydb.close()

            E_Patient_ID.delete(0,'end')
            E_Patient_name.delete(0,'end')
            E_Vaccination_date.delete(0,'end')
            clicked2.set(Vaccine_list[0])
        

    root2 = Tk()
    root2.geometry("500x350")
    root2.title("Patient Data Modify")

    Patient_ID=Label(root2,text="Enter Patient ID" , font="Bold")
    Patient_ID.place(x=20 , y=30)

    E_Patient_ID=Entry(root2)
    E_Patient_ID.place(x=300 , y=30)

    Patient_name=Label(root2,text="Enter Patient Name" , font="Bold")
    Patient_name.place(x=20 , y=70)

    E_Patient_name=Entry(root2)
    E_Patient_name.place(x=300 , y=70)
#########################
    Vaccination_date=Label(root2,text="Enter Date (YY-MM-DD)" , font="Bold")
    Vaccination_date.place(x=20 , y=110)

    E_Vaccination_date=Entry(root2)
    E_Vaccination_date.place(x=300 , y=110)
##################
    Select_vaccine=Label(root2,text="Select Vaccine" , font="Bold")
    Select_vaccine.place(x=20 , y=150)
##getting vaccine names
    mydb=mysql.connect(host="localhost", user="root", passwd="root",database="project")
    mycursor = mydb.cursor()

    Vaccine_list2=[]
    mycursor.execute("Select name from vaccine order by name")

    for name in mycursor:
        Vaccine_list2.append(name)
    mydb.close()
    clicked2= StringVar()
    clicked2.set(Vaccine_list2[0])

    drop= OptionMenu(root2, clicked2 , *Vaccine_list2 , command=Selected2)
    drop.pack(padx=175 , pady=155)
    
#####################


    update=Button(root2, text="Update" , font=("italic", 10) , bg="white" , command=update)
    update.place(x=120 , y = 250)

    delete=Button(root2, text="Delete" , font=("italic", 10) , bg="white" , command=delete)
    delete.place(x=220 , y = 250)

    Close=Button(root2, text="Close" , font=("italic", 10) , bg="white" , command=root2.destroy)
    Close.place(x=320 , y = 250)

    
def new():
    import staff2

def show():
    
    root1=Tk()
    root1.geometry("450x400")
    
    headings = ttk.Treeview(root1 , columns = (1,2,3,4) , show = "headings" , height="15")
    
    headings.column("1" , width=50 , anchor= CENTER )
    headings.column("2", width=130 , anchor= CENTER )
    headings.column("3", width=110 , anchor= CENTER )
    headings.column("4", width=110 , anchor= CENTER )

    headings.heading("1", text="P ID")
    headings.heading("2", text="Name")
    headings.heading("3", text="Vaccine")
    headings.heading("4", text="Vaccine Date")
    
    headings.pack(padx=5 , pady=10)

    done=Button(root1, text="Done" , font=("italic", 10) , bg="white" , command=root1.destroy)
    done.place(x=225,y=350)


    mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
    mycursor=mydb.cursor()  
    mycursor.execute("Select * from patient")

    Patients= mycursor.fetchall()
    #mydb.commit()

    for patient in Patients:
        #Detailes = str(patient[0])+'  '+patient[1]+'  '+patient[2]+'  '+str(patient[3])
        #Data_list.insert(END, Detailes)
        headings.insert('' , 'end' , values = patient)
    
    
    #Messagebox.showinfo("Show Status" , "Data Fetched Succesfully")
    mydb.close()  

##############
Patient_name=Label(root,text="Enter Patient Name" , font="Bold")
Patient_name.place(x=20 , y=30)

E_Patient_name=Entry()
E_Patient_name.place(x=300 , y=30)
#########################
Vaccination_date=Label(root,text="Enter Date (YY-MM-DD)" , font="Bold")
Vaccination_date.place(x=20 , y=70)

E_Vaccination_date=Entry()
E_Vaccination_date.place(x=300 , y=70)
##################
Select_vaccine=Label(root,text="Select Vaccine" , font="Bold")
Select_vaccine.place(x=20 , y=110)
##getting vaccine names
mydb=mysql.connect(host="localhost", user="root", passwd="root",database="project")
mycursor = mydb.cursor()

Vaccine_list=[]
mycursor.execute("Select name from vaccine order by name")

for name in mycursor:
    Vaccine_list.append(name)
mydb.close()
clicked= StringVar()
clicked.set(Vaccine_list[0])

drop= OptionMenu(root, clicked , *Vaccine_list , command=Selected)
drop.pack(padx=210 , pady=110)
#####################

insert=Button(root, text="Insert" , font=("italic", 10) , bg="white" , command=insert)
insert.place(x=40 , y = 170)

updateDelete=Button(root, text="Update/Delete" , font=("italic", 10) , bg="white" , command=updatedelete)
updateDelete.place(x=120 , y = 170)

#delete=Button(root, text="DELETE" , font=("italic", 10) , bg="white" , command=delete)
#delete.place(x=220 , y = 170)

show=Button(root, text="Show" , font=("italic", 10) , bg="white" , command=show)
show.place(x=240 , y = 170)

new=Button(root, text="Add Info" , font=("italic", 10) , bg="white" , command=new)
new.place(x=320 , y = 170)


root.mainloop()

