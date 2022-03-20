from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("500x350")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="white", command = register_user).pack()
 
# Master login design

def master_login():
    global master_login_screen
    master_login_screen = Toplevel(main_screen)
    master_login_screen.title("Master Login")
    master_login_screen.geometry("500x350")
    Label(master_login_screen, text="Please enter details below to master login").pack()
    Label(master_login_screen, text="").pack()
 
    global master_username_verify
    global master_password_verify

    master_username_verify = StringVar()
    master_password_verify = StringVar()
 
    global master_username_login_entry
    global master_password_login_entry
 
    Label(master_login_screen, text="Master Username * ").pack()
    master_username_login_entry = Entry(master_login_screen, textvariable=master_username_verify)
    master_username_login_entry.pack()
    Label(master_login_screen, text="").pack()
    Label(master_login_screen, text="Master Password * ").pack()
    master_password_login_entry = Entry(master_login_screen, textvariable=master_password_verify, show= '*')
    master_password_login_entry.pack()
    Label(master_login_screen, text="").pack()
    Button(master_login_screen, text="Master Login", width=10, height=1, command = master_login_verify).pack()
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x350")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Master login verify event
def master_login_verify():
    username1 = master_username_verify.get()
    password1 = master_password_verify.get()
    if username1 == "admin":
        if password1 == "admin12345":
            master_login_sucess()
            
 
        else:
            master_password_not_recognised()
 
    else:
        master_user_not_found() 
# Implementing event on login button 
 
def login_verify():
    username2 = username_verify.get()
    password2 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username2 in list_of_files:
        file2 = open(username2, "r")
        verify = file2.read().splitlines()
        if password2 in verify:
            login_sucess()
            
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()

#Master login pupup success
def master_login_sucess():
    global master_login_success_screen
    master_login_success_screen = Toplevel(master_login_screen)
    master_login_success_screen.title("Success")
    master_login_success_screen.geometry("150x100")
    Label(master_login_success_screen, text="Master Login Success").pack()
    Button(master_login_success_screen, text="OK", command=delete_master_login_success).pack()
    import head
  
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    import staff1
    import staff2
# ivalid master password

def master_password_not_recognised():
    global master_password_not_recog_screen
    master_password_not_recog_screen = Toplevel(master_login_screen)
    master_password_not_recog_screen.title("Success")
    master_password_not_recog_screen.geometry("150x100")
    Label(master_password_not_recog_screen, text="Invalid Password ").pack()
    Button(master_password_not_recog_screen, text="OK", command=delete_master_password_not_recognised).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# MAter user not found
def master_user_not_found():
    global master_user_not_found_screen
    master_user_not_found_screen = Toplevel(master_login_screen)
    master_user_not_found_screen.title("Success")
    master_user_not_found_screen.geometry("150x100")
    Label(master_user_not_found_screen, text="Master User Not Found").pack()
    Button(master_user_not_found_screen, text="OK", command=delete_master_user_not_found_screen).pack() 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
def delete_master_login_success():
    master_login_success_screen.destroy() 

def delete_login_success():
    login_success_screen.destroy()
 
def delete_master_password_not_recognised():
    master_password_not_recog_screen.destroy() 

def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
def delete_master_user_not_found_screen():
    master_user_not_found_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x350")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Master login",height="2",width="30",command=master_login).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
 