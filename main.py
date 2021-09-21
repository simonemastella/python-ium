import tkinter as tk
from tkinter import messagebox
from tkinter.constants import BOTTOM, CENTER, END, LEFT, RIGHT, TOP, TRUE

window = tk.Tk()
window.configure()
window.title("Progetto 915927")


#size and position of mainframe
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
w = ws/2 
h = hs/2 
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#environment var

my_pattern_w =3
my_pattern_h =3
#define the setting frame
def frame():
    newWindow = tk.Toplevel(window)
    newWindow.grab_set() #no release?
    newWindow.title("Settings")
    newWindow.geometry('%dx%d+%d+%d' % (w/2, h/2, x+x/2, y+y/2)) #dimension and position
    
    #layout
    frameLeft=tk.Frame(newWindow)
    frameLeftPatternW=tk.Frame(frameLeft)
    frameLeftPatternH=tk.Frame(frameLeft)
    frameLeftBottomError=tk.Frame(frameLeft)
    frameLeftBottomButton=tk.Frame(frameLeft)
    frameRight=tk.Frame(newWindow)

    #layout left side
    frameLeft.pack(side=LEFT, expand=True, fill="both")
    frameLeftPatternW.place(in_=frameLeft, anchor="c", relx=.5, rely=.4)
    frameLeftPatternH.place(in_=frameLeft, anchor="c", relx=.5, rely=.5)
    frameLeftBottomError.place(in_=frameLeft, anchor="c", relx=.5, rely=.6)
    frameLeftBottomButton.place(in_=frameLeft, anchor="c", relx=.5, rely=.7)
    #2 labels left
    tk.Label(frameLeftPatternW, text="My pattern w").pack(side=LEFT)
    tk.Label(frameLeftPatternH, text="My pattern h").pack(side=LEFT)
    #error left
    lbl_err = tk.Label(frameLeftBottomError, text="Warning: only numerical value will be saved")
    
    def callback(sv):
        if (not str(sv.get()).isdigit()):
            lbl_err.pack(expand=TRUE)
        else:
            lbl_err.pack_forget()    
    #2 entry in left
    sv1 = tk.StringVar()
    sv1.trace("w", lambda name, index, mode, sv=sv1: callback(sv))
    e1 = tk.Entry(frameLeftPatternW, textvariable=sv1)
    e1.insert(tk.END, my_pattern_w)
    sv2 = tk.StringVar()
    sv2.trace("w", lambda name, index, mode, sv=sv2: callback(sv))
    e2 = tk.Entry(frameLeftPatternH, textvariable=sv2)
    e2.insert(tk.END, my_pattern_h)
    
    e1.pack(side=RIGHT)
    e2.pack(side=RIGHT)
    save_button = tk.Button(frameLeftBottomButton, text="SAVE", command=lambda: save_changes(), padx=20)
    reset_button = tk.Button(frameLeftBottomButton, text="RESET", command=lambda: reset_changes(), padx=20)
    save_button.pack(side=LEFT, padx=20) 
    reset_button.pack(side=RIGHT, padx=20) 

    frameRight.pack(side=LEFT, expand=True, fill="both")
    def has_changes():
        global my_pattern_w 
        global my_pattern_h 
        pattern_w = (str(my_pattern_w) != str(e1.get())) 
        pattern_h = (str(my_pattern_h) != str(e2.get())) 
        return pattern_w or pattern_h
    def save_changes():
        if has_changes():
            global my_pattern_w 
            global my_pattern_h 
            if e1.get().isdigit():
                my_pattern_w= int(e1.get())
            
            if e2.get().isdigit():
                my_pattern_h= int(e2.get())
            reset_changes()
    def  reset_changes():
        if has_changes():
            global my_pattern_w 
            global my_pattern_h 
            e1.delete(0, END)
            e1.insert(0, my_pattern_w)
            e2.delete(0, END)
            e2.insert(0, my_pattern_h)
    def on_closing():
        if has_changes():
            print(has_changes())
            if messagebox.askokcancel("Quit", "Do you want to keep changes?"):
                save_changes()
                newWindow.destroy()
        newWindow.destroy()
    newWindow.protocol("WM_DELETE_WINDOW", on_closing)
    
    
           


framebutton = tk.Button(window, text="Frame", command=lambda: frame())
framebutton.pack()    

if __name__=="__main__":
    window.mainloop()
