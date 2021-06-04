import tkinter as tk
import webbrowser
root=tk.Tk()
root.title("WEB BROWSER")
root.geometry("400x150")


x=tk.StringVar()

def fb():
    webbrowser.open_new("https://www.facebook.com/")
def yt():
    webbrowser.open_new("https://www.youtube.com/")
def ig():
    webbrowser.open_new("https://www.instagram.com/")
def tw():
    webbrowser.open_new("https://www.twitter.com/")

def search():
    word=x.get()
    search='https://www.google.com/search?q='+word
    webbrowser.open_new(search)


b1=tk.Button(root,text="Facebook",fg="white",bg="#3b5998",command=fb)
b2=tk.Button(root,text="YouTube",fg="white",bg="#FF0000",command=yt)
b3=tk.Button(root,text="Instagram",fg="white",bg="#C13584",command=ig)
b4=tk.Button(root,text="Twitter",fg="white",bg="#00acee",command=tw)
b1.place(x=10,y=70,width=80,height=30)
b2.place(x=100,y=70,width=80,height=30)
b3.place(x=190,y=70,width=80,height=30)
b4.place(x=10,y=105,width=135,height=30)
b5=tk.Button(root,text="Search",fg="white",bg="#202020",command=search)
b5.place(x=320,y=10,width=70,height=50)
e1=tk.Entry(root,textvariable=x)
e1.place(x=10,y=10,width=300,height=50)
root.mainloop()
