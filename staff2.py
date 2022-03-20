from tkinter import *
from tkinter import ttk
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

root = Tk()
root.geometry("550x250")
root.title("Vaccine Patient 02")


def insert():
    mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
    mycursor=mydb.cursor()
     
    ID=E_Patient_ID.get()
    
    mycursor.execute("Select Vaccine_selected from patient where P_ID='"+ID+"'")

    for name in mycursor:
        Vakcn=name
    #print(Vakcn)
    Vakcn = list(Vakcn)
    vaccine=Vakcn[0] #value of vaccine

    mycursor.execute("Select Dose_to_be_given from vaccine where name='"+vaccine+"'")

    for dose in mycursor:
        t_dose=dose
    

    t_dose = list(t_dose)
    Total_dose=int(t_dose[0]) #value of total dose in int
    
    #R_dose = Total_dose - 1

    mycursor.execute("Select Dose_given from patient where P_ID='"+ID+"'")

    for dose in mycursor:
        g_dose= dose

    if(g_dose[0]==None):
        #print("In None")
        G_dose=1
    else:
        g_dose = list (g_dose) 
        G_dose = int(g_dose[0]) + 1
    #print(G_dose)

    R_dose = Total_dose - G_dose


    if(R_dose>-1):
        
        effect=E_Side_effect.get()
        date=E_Next_Vist_date.get()
    
    
        if (ID=="" or date=="" or effect=="" ):
            Messagebox.showinfo("Insert Status", "All fields are required")
        else:
            mycursor.execute("update patient set Side_effect='"+effect+"',Next_vist_date='"+date+"', Dose_given='"+str(G_dose) +"', Remaining_dose='"+str(R_dose)+"' where P_ID='"+ID+"'")
            mydb.commit()
            mycursor.execute("update vaccine set available=available-1 where name='"+vaccine+"'")
            mydb.commit()

            Messagebox.showinfo("Insert Status", "Inserted successfully")
            if(R_dose==0):
                Messagebox.showinfo("Vaccination Status", "Vaccination completed")

   
            E_Side_effect.delete(0,'end')
            E_Next_Vist_date.delete(0,'end')
            E_Patient_ID.delete(0 , 'end')
            
            mydb.close()
    else:
        Messagebox.showinfo("Alert" , "Vaccination is already completed")
    
def search():
    root2=Tk()
    root2.geometry("800x100")


    headings = ttk.Treeview(root2 , columns = (1,2,3,4,5,6,7,8) , show = "headings" , height="1")
    
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

    done=Button(root2, text="Done" , font=("italic", 10) , bg="white" , command=root2.destroy)
    done.place(x=400,y=70)

    ID=E_Patient_ID.get()

    mydb=mysql.connect(host="localhost",user="root",passwd="root",database="project")
    mycursor=mydb.cursor()  
    mycursor.execute("Select * from patient where P_ID='"+ID+"'")

    Patients= mycursor.fetchall()
    #mydb.commit()

    for patient in Patients:
        headings.insert('' , 'end' , values = patient)
    
    E_Patient_ID.delete(0 , 'end')
    #Messagebox.showinfo("Show Status" , "Data Fetched Succesfully")
    mydb.close()  

def show():
    
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
    mycursor.execute("Select * from patient where Side_effect is not null")

    Patients= mycursor.fetchall()
    #mydb.commit()

    for patient in Patients:
        headings.insert('' , 'end' , values = patient)
    
    
    #Messagebox.showinfo("Show Status" , "Data Fetched Succesfully")
    mydb.close()  


###########################
Patient_ID=Label(root,text="Enter Patient ID" , font="Bold")
Patient_ID.place(x=20 , y=30)

E_Patient_ID=Entry(root)
E_Patient_ID.place(x=350 , y=30)

Side_effect=Label(root,text="Enter Detail Of Side Effect" , font="Bold")
Side_effect.place(x=20 , y=70)

E_Side_effect=Entry(root)
E_Side_effect.place(x=350 , y=70)

Next_Vist_date=Label(root,text="Enter Next Vist Date (YY-MM-DD)" , font="Bold")
Next_Vist_date.place(x=20 , y=110)

E_Next_Vist_date=Entry(root)
E_Next_Vist_date.place(x=350 , y=110)
###########################
insert=Button(root, text="Insert" , font=("italic", 10) , bg="white" , command=insert)
insert.place(x=20 , y = 170)

search=Button(root, text="Search" , font=("italic", 10) , bg="white" , command=search)
search.place(x=120 , y = 170)

show=Button(root, text="Show" , font=("italic", 10) , bg="white" , command=show)
show.place(x=220 , y = 170)

root.mainloop()
