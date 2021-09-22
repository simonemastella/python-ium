import tkinter as tk
from tkinter import messagebox
from tkinter.constants import BOTTOM, CENTER, END, LEFT, RIGHT, TOP, TRUE, Y

window = tk.Tk()
window.configure()
window.title("Progetto 915927")

# size and position of mainframe
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
w = ws/2
h = hs/2
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

# environment var
my_pattern_w = 5
my_pattern_h = 3

# define the setting frame
def frame():
    newWindow = tk.Toplevel(window)
    newWindow.grab_set()  # no release?
    newWindow.title("Settings")
    # dimension and position
    newWindow.geometry('%dx%d+%d+%d' % (w/2, h/2, x+x/2, y+y/2))
    # layout
    frameLeftPatternW = tk.Frame(newWindow)
    frameLeftPatternH = tk.Frame(newWindow)
    frameLeftBottomError = tk.Frame(newWindow)
    frameLeftBottomButton = tk.Frame(newWindow)
    # layout left side
    frameLeftPatternW.place(in_=newWindow, anchor="c", relx=.5, rely=.4)
    frameLeftPatternH.place(in_=newWindow, anchor="c", relx=.5, rely=.5)
    frameLeftBottomError.place(in_=newWindow, anchor="c", relx=.5, rely=.6)
    frameLeftBottomButton.place(in_=newWindow, anchor="c", relx=.5, rely=.7)
    # 2 labels left
    tk.Label(frameLeftPatternW, text="My pattern w").pack(side=LEFT)
    tk.Label(frameLeftPatternH, text="My pattern h").pack(side=LEFT)
    # error left
    lbl_err = tk.Label(frameLeftBottomError,
                       text="Warning: only numerical value will be saved")
    # live changing textbox for error warning

    def callback(sv):
        if (not str(sv.get()).isdigit()):
            lbl_err.pack(expand=TRUE)
        else:
            lbl_err.pack_forget()
    # 2 entry in left
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
    save_button = tk.Button(
        frameLeftBottomButton, text="SAVE", command=lambda: save_changes(), padx=20)
    reset_button = tk.Button(
        frameLeftBottomButton, text="RESET", command=lambda: reset_changes(), padx=20)
    save_button.pack(side=LEFT, padx=20)
    reset_button.pack(side=RIGHT, padx=20)
    
    # check and function for saving or quitting
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
                if int(e1.get()) < 1:
                    my_pattern_w = 1
                else:
                    my_pattern_w = int(e1.get())
            if e2.get().isdigit():
                if int(e2.get()) < 1:
                    my_pattern_h = 1
                else:
                    my_pattern_h = int(e2.get())
            reset_changes()
            reload_button_pattern()

    def reset_changes():
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


# layout
windowLeft = tk.Frame(window)
windowRight = tk.Frame(window, bg="red")

vscrollbar = tk.Scrollbar(window, orient=tk.VERTICAL)
vscrollbar.pack(fill=Y, side=RIGHT)

windowLeft.pack(side=LEFT, expand=True, fill="both")
windowRight.pack(side=LEFT, expand=True, fill="both")


windowLeftMid = tk.Frame(windowLeft)
windowLeftMid.place(in_=windowLeft, anchor="c", relx=.5, rely=.5)
windowLeftBottom = tk.Frame(windowLeft)
windowLeftBottom.place(in_=windowLeft, anchor="c", relx=.5, rely=0.9)
my_pattern_lbl = tk.StringVar()
my_pattern_lbl.set("My pattern {}x{}".format(my_pattern_w, my_pattern_h))
tk.Label(windowLeftMid, textvariable=my_pattern_lbl).pack(side=TOP)

# button of my pattern configuration
btn_value = []
btn = []
frame_btn = []


def make_button_pattern():
    global btn_value
    global btn
    global frame_btn
    btn_value = [[0 for z in range(my_pattern_w)] for z in range(my_pattern_h)]
    btn = [[0 for z in range(my_pattern_w)] for z in range(my_pattern_h)]
    frame_btn = [0 for z in range(my_pattern_h)]

    def color_change(b, a):
        if btn_value[a][b] == 0:
            btn[a][b].config(bg="black")
            btn_value[a][b] = 1
        elif btn_value[a][b] == 1:
            btn[a][b].config(bg="white")
            btn_value[a][b] = 0
    for heigth in range(my_pattern_h):
        frame_btn[heigth] = tk.Frame(windowLeftMid)
        frame_btn[heigth].pack(side=TOP)
        for width in range(my_pattern_w):
            btn[heigth][width] = tk.Button(
                frame_btn[heigth], height=1, width=1, bg="white", relief="groove", command=lambda x1=width, y1=heigth: color_change(x1, y1))
            btn[heigth][width].pack(side=LEFT)


def reload_button_pattern():
    global btn_value
    global btn
    global frame_btn
    global my_pattern_lbl
    actual_w = (len(btn[0]))
    actual_y = (len(btn))
    print(actual_w)
    print(actual_y)
    for heigth in range(actual_y):
        frame_btn[heigth].destroy()
        for width in range(actual_w):
            btn[heigth][width].destroy()
    my_pattern_lbl.set("My pattern {}x{}".format(my_pattern_w, my_pattern_h))
    make_button_pattern()  # redraw


make_button_pattern()  # draw first time

computebutton = tk.Button(windowLeftBottom, text="COMPUTE", padx=10)
computebutton.pack(side=LEFT, padx=10)
randomize = tk.Button(windowLeftBottom, text="RANDOMIZE", padx=10)
randomize.pack(side=LEFT, padx=10)
framebutton = tk.Button(windowLeftBottom, text="SETTINGS", command=lambda: frame(), padx=10)
framebutton.pack(side=LEFT, padx=10)

if __name__ == "__main__":
    window.mainloop()
