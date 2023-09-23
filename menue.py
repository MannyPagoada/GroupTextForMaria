import tkinter as tk
#importing the module

#font for everything
customFont=("Comic stans", 20)

#creating the main window
root=tk.Tk()

#creating the window title
root.title("Catholic Club Text System")


#set up the resolution
root.geometry("400x300")

#customization here
welcome_label=tk.Label(root, text="Welcome Back Maria!", font=customFont)
welcome_label.pack()

#start the tkinter main loop
root.mainloop()

