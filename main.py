import tkinter as tk
from tkinter import messagebox
from tkinter.constants import BOTTOM, CENTER, END, LEFT, RIGHT, TOP, TRUE, Y
from time import sleep

from utils import random_matrix
from compute import compare_all_slice


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
my_pattern_w = 3
my_pattern_h = 2
canvas_w = 10
canvas_h = 10


# define the setting frame
def frame():
    newWindow = tk.Toplevel(window)
    newWindow.grab_set()  # no release?
    newWindow.title("Settings")
    # dimension and position
    newWindow.geometry('%dx%d+%d+%d' % (w/2, h/2, x+x/2, y+y/2))
    # layout

    frameLeftCanvasW = tk.Frame(newWindow)
    frameLeftCanvasH = tk.Frame(newWindow)
    frameLeftPatternW = tk.Frame(newWindow)
    frameLeftPatternH = tk.Frame(newWindow)
    frameLeftBottomError = tk.Frame(newWindow)
    frameLeftBottomButton = tk.Frame(newWindow)
    # layout left side
    frameLeftCanvasW.place(in_=newWindow, anchor="c", relx=.5, rely=.2)
    frameLeftCanvasH.place(in_=newWindow, anchor="c", relx=.5, rely=.3)
    frameLeftPatternW.place(in_=newWindow, anchor="c", relx=.5, rely=.5)
    frameLeftPatternH.place(in_=newWindow, anchor="c", relx=.5, rely=.6)
    frameLeftBottomError.place(in_=newWindow, anchor="c", relx=.5, rely=.8)
    frameLeftBottomButton.place(in_=newWindow, anchor="c", relx=.5, rely=.9)
    # 2 labels left
    tk.Label(frameLeftCanvasW, text="My canvas w").pack(side=LEFT)
    tk.Label(frameLeftCanvasH, text="My canvas h").pack(side=LEFT)
    tk.Label(frameLeftPatternW, text="My pattern w").pack(side=LEFT)
    tk.Label(frameLeftPatternH, text="My pattern h").pack(side=LEFT)
    # error
    lbl_err = tk.Label(frameLeftBottomError,
                       text="Warning: only numerical value will be saved")
    # live changing textbox for error warning

    def callback(sv):
        if (not str(sv.get()).isdigit()):
            lbl_err.pack(expand=TRUE)
        else:
            lbl_err.pack_forget()
    # 4 entry
    sv1 = tk.StringVar()
    sv1.trace("w", lambda name, index, mode, sv=sv1: callback(sv))
    e1 = tk.Entry(frameLeftCanvasW, textvariable=sv1)
    e1.insert(tk.END, canvas_w)
    sv2 = tk.StringVar()
    sv2.trace("w", lambda name, index, mode, sv=sv2: callback(sv))
    e2 = tk.Entry(frameLeftCanvasH, textvariable=sv2)
    e2.insert(tk.END, canvas_h)
    sv3 = tk.StringVar()
    sv3.trace("w", lambda name, index, mode, sv=sv3: callback(sv))
    e3 = tk.Entry(frameLeftPatternW, textvariable=sv3)
    e3.insert(tk.END, my_pattern_w)
    sv4 = tk.StringVar()
    sv4.trace("w", lambda name, index, mode, sv=sv4: callback(sv))
    e4 = tk.Entry(frameLeftPatternH, textvariable=sv4)
    e4.insert(tk.END, my_pattern_h)

    e1.pack(side=RIGHT)
    e2.pack(side=RIGHT)
    e3.pack(side=RIGHT)
    e4.pack(side=RIGHT)
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
        global canvas_w
        global canvas_h
        ch_canvas_w = (str(canvas_w) != str(e1.get()))
        ch_canvas_h = (str(canvas_h) != str(e2.get()))
        pattern_w = (str(my_pattern_w) != str(e3.get()))
        pattern_h = (str(my_pattern_h) != str(e4.get()))
        return ch_canvas_w or ch_canvas_h or pattern_w or pattern_h

    def save_changes():
        if has_changes():
            global my_pattern_w
            global my_pattern_h
            global canvas_w
            global canvas_h
            # canvas save the value if positive, else =1
            if e1.get().isdigit():
                if int(e1.get()) < 1:
                    canvas_w = 1
                else:
                    canvas_w = int(e1.get())
            if e2.get().isdigit():
                if int(e2.get()) < 1:
                    canvas_h = 1
                else:
                    canvas_h = int(e2.get())
            # pattern save the value if positive, else =1
            if e3.get().isdigit():
                if int(e3.get()) < 1:
                    my_pattern_w = 1
                else:
                    my_pattern_w = int(e3.get())
            if e4.get().isdigit():
                if int(e4.get()) < 1:
                    my_pattern_h = 1
                else:
                    my_pattern_h = int(e4.get())
            reset_changes()
            reload_button_pattern()
            randomize_canvas()

    def reset_changes():
        if has_changes():
            # canvas
            global canvas_w
            global canvas_h
            e1.delete(0, END)
            e1.insert(0, canvas_w)
            e2.delete(0, END)
            e2.insert(0, canvas_h)
            # pattern
            global my_pattern_w
            global my_pattern_h
            e3.delete(0, END)
            e3.insert(0, my_pattern_w)
            e4.delete(0, END)
            e4.insert(0, my_pattern_h)

    def on_closing():
        if has_changes():
            if messagebox.askokcancel("Quit", "Do you want to keep changes?"):
                save_changes()
                newWindow.destroy()
        newWindow.destroy()
    newWindow.protocol("WM_DELETE_WINDOW", on_closing)


# layout
windowLeft, windowRight = tk.Frame(window), tk.Frame(window)
windowLeft.pack(side=LEFT, expand=True, fill="both")
windowRight.pack(side=LEFT)

windowLeftMid = tk.Frame(windowLeft)
windowLeftMid.place(in_=windowLeft, anchor="c", relx=.5, rely=0.5)
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
    btn = [[None for z in range(my_pattern_w)] for z in range(my_pattern_h)]
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
                frame_btn[heigth], height=1, width=2, bg="white", relief="groove", command=lambda x1=width, y1=heigth: color_change(x1, y1))
            btn[heigth][width].pack(side=LEFT)


def reload_button_pattern():
    global btn_value, btn, frame_btn, my_pattern_lbl
    actual_w = (len(btn[0]))
    actual_y = (len(btn))
    for heigth in range(actual_y):
        frame_btn[heigth].destroy()
        for width in range(actual_w):
            btn[heigth][width].destroy()
    my_pattern_lbl.set("My pattern {}x{}".format(my_pattern_w, my_pattern_h))
    make_button_pattern()  # redraw


make_button_pattern()  # draw first time

computebutton = tk.Button(windowLeftBottom, text="COMPUTE", padx=10,
                          command=lambda: compute_score())
computebutton.pack(side=LEFT, padx=10)

randomize = tk.Button(windowLeftBottom, text="RANDOMIZE", padx=10,
                      command=lambda: randomize_canvas())
randomize.pack(side=LEFT, padx=10)
framebutton = tk.Button(windowLeftBottom, text="SETTINGS",
                        command=lambda: frame(), padx=10)
framebutton.pack(side=LEFT, padx=10)

svN = tk.StringVar()
tk.Button(windowLeft, textvariable=svN, fg="red", command=lambda: show_score("N")).place(
    in_=windowLeft, anchor="c", relx=.35, rely=0.96)
svS = tk.StringVar()
tk.Button(windowLeft, textvariable=svS, fg="green", command=lambda: show_score("S")).place(
    in_=windowLeft, anchor="c", relx=.45, rely=0.96)
svW = tk.StringVar()
tk.Button(windowLeft, textvariable=svW, fg="purple", command=lambda: show_score("W")).place(
    in_=windowLeft, anchor="c", relx=.55, rely=0.96)
svE = tk.StringVar()
tk.Button(windowLeft, textvariable=svE, fg="blue",command=lambda: show_score("E")).place(
    in_=windowLeft, anchor="c", relx=.65, rely=0.96)


# frameRight


canvas = tk.Canvas(windowRight, width=w/2, height=h, bg="red")

canvas_rect, width_rect, height_rect = None, None, None


def randomize_canvas():
    global canvas_rect
    canvas_rect = random_matrix(canvas_w, canvas_h)
    render_canvas()


last_score = None


def render_canvas():
    global canvas, canvas_h, canvas_w, last_score, width_rect, height_rect
    last_score = None
    all_width = w/2
    all_height = h
    width_rect = all_width/canvas_w
    height_rect = all_height/canvas_h
    for h_c in range(0, canvas_h):
        for w_c in range(0, canvas_w):
            if(canvas_rect[h_c][w_c] == 0):
                canvas.create_rectangle(
                    w_c*width_rect, h_c*height_rect, (1+w_c)*width_rect, (1+h_c)*height_rect, fill="white")
            else:
                canvas.create_rectangle(
                    w_c*width_rect, h_c*height_rect, (1+w_c)*width_rect, (1+h_c)*height_rect, fill="black")
    canvas.pack()


randomize_canvas()


def compute_score():
    global svN, svE, svS, svW
    global last_score

    last_score = compare_all_slice(btn_value, canvas_rect)
    svN.set("N: {}".format(len(last_score["N"])))
    svS.set("S: {}".format(len(last_score["S"])))
    svW.set("W: {}".format(len(last_score["W"])))
    svE.set("E: {}".format(len(last_score["E"])))


def show_score(cd):
    colors_directions = {"N": "red", "S": "green", "W": "purple", "E": "blue"}
    if last_score != None:
        for elem in last_score[cd]:
            startX, startY = elem["x"], elem["y"]
            endX = (elem["x"] + my_pattern_w) if cd == "N" or cd == "S" else (elem["x"] + my_pattern_h)
            endY = (elem["y"] + my_pattern_h) if cd == "N" or cd == "S" else (elem["y"] + my_pattern_w)
            for cubeY in range(startY, endY):
                for cubeX in range(startX, endX):
                    col = "yellow" if  canvas_rect[cubeY][cubeX] == 0 else colors_directions[cd]
                    spot = canvas.create_rectangle(
                        cubeX*width_rect, cubeY*height_rect, (1+cubeX)*width_rect, (1+cubeY)*height_rect, fill=col)
                    window.after(2000, canvas.delete, (spot))

                
    
    pass


if __name__ == "__main__":
    window.mainloop()
