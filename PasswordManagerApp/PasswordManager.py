import tkinter as tk
root = tk.Tk()
root.title("Password Manager App")
# root.geometry("600x400")
root.maxsize(height=500,width=600)

UserNameLabel = tk.Label(root,text="Enter UserName Here",font=25,bg="black",fg="white")
UserNameLabel.grid(row=0,column=1)
userNameEntry = tk.Entry(root,bd=20,width=200)
userNameEntry.grid(row=0 ,column=12)
ConfirmUserButton = tk.Button(root,text="confirm",bg="red",bd=12)
ConfirmUserButton.grid(row=30,column=4)
root.mainloop()
