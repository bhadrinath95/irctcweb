from tkinter import *
root=Tk()
root.title("ENTER OTP:")
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)
    root.destroy()

textBox=Text(root, height=5, width=50)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Submit", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

mainloop()