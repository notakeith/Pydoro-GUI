import tkinter as tk
from pygame import mixer

width = 250
height = 250
round = 32
x0, y0, x1, y1 = 0, 0, 50, 50
diametr = 200
borderradius = 50
borderwidth = 4
diametr2 = diametr - borderradius
diametr3 = diametr - 4

colorbg = "gray95"
colorfg_pomodoros = "#ff4c30"
colorfgbd_pomodoros = "#ffcec7"
colorbgbd_pomodoros = "#ffcec7"
colorfg_break = "#00BD68"
colorfgbd_break = "#BDD2C9"
colorbgbd_break = "#BDD2C9"

ticksPerSecond = 2
isTimerRuning = False
timerTime = 25 * 60
defaultSeconds = 1
timerSeconds = defaultSeconds
isRelaxBeen = False
autoStartBreaks = True
autoStartPomodoros = True
labelText = ""

mixer.init()
mixer.music.load(f"bell.mp3")

root = tk.Tk()
root.geometry(f'{width}x{height}+2313+1124')
root.overrideredirect(True)
root.attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "gray94")
root["bg"] = "gray94"

bgFrame = tk.Frame()
bgFrame.grid(row=0, column=0, rowspan=8)

canvas = tk.Canvas(bgFrame, bd=0, highlightthickness=0, relief='ridge', width=width, height=height)

canvas["background"] = "gray94"

canvas.create_oval(
    0, 0, round, round, outline="gray94",
    fill=colorbg, width=2
)
canvas.create_oval(
    width, 0, width - round, round, outline="gray94",
    fill=colorbg, width=2
)
canvas.create_oval(
    width, height, width - round, height - round, outline="gray94",
    fill=colorbg, width=2
)
canvas.create_oval(
    0, height, round, height - round, outline="gray94", fill=colorbg, width=2
)

points = [0, round / 2, round / 2, 0, width - (round / 2), 0, width, round / 2, width, height - (round / 2),
          width - (round / 2), height, round / 2, height, 0, height - (round / 2)]

dragableArea = canvas.create_polygon(points, outline=colorbg, fill=colorbg, width=2)
oval_id1 = canvas.create_oval((width - diametr) / 2, (height - diametr) / 2, ((width - diametr) / 2) + diametr,
                              ((height - diametr) / 2) + diametr, outline=colorfgbd_pomodoros, fill=colorbgbd_pomodoros,
                              width=borderwidth)
oval_id2 = canvas.create_arc((width - diametr3) / 2, (height - diametr3) / 2, ((width - diametr3) / 2) + diametr3,
                             ((height - diametr3) / 2) + diametr3, outline=colorfg_pomodoros, fill=colorfg_pomodoros,
                             width=0, start=90,
                             extent=0)
oval_id3 = canvas.create_oval((width - diametr2) / 2, (height - diametr2) / 2, ((width - diametr2) / 2) + diametr2,
                              ((height - diametr2) / 2) + diametr2, outline=colorfgbd_pomodoros, fill=colorbg,
                              width=borderwidth)

label_id = canvas.create_text(height / 2, width / 2, text="25:00", font=("Calibri Light", 32))

close_obj = canvas.create_oval(
    width - 13, 10, width - round, round - 5, outline="#fe7968",
    fill="#fe7968", width=2
)

set_obj = canvas.create_oval(
    width - 38, 10, width - round - 25, round - 5, outline="#fad859",
    fill="#fad859", width=2
)
canvas.pack()

bgSetTimeFrame = tk.Frame()
bgSetTimeCanvas = tk.Canvas(bgSetTimeFrame, bd=0, highlightthickness=0, relief='ridge', width=width, height=height)

bgSetTimeCanvas["background"] = "gray94"

bgSetTimeCanvas.create_oval(
    0, 0, round, round, outline="gray94",
    fill=colorbg, width=2
)
bgSetTimeCanvas.create_oval(
    width, 0, width - round, round, outline="gray94",
    fill=colorbg, width=2
)
bgSetTimeCanvas.create_oval(
    width, height, width - round, height - round, outline="gray94",
    fill=colorbg, width=2
)
bgSetTimeCanvas.create_oval(
    0, height, round, height - round, outline="gray94", fill=colorbg, width=2
)

bgSetTimeArea = bgSetTimeCanvas.create_polygon(points, outline=colorbg, fill=colorbg, width=2)

set_objOpen = bgSetTimeCanvas.create_oval(
    width - 38, 10, width - round - 25, round - 5, outline="#fad859",
    fill="#fad859", width=2
)

bgSetTimeCanvas.pack()


def OpenSettings(event=None):
    global labelText
    canvas.tag_bind(set_obj, '<Button-1>', CloseSettings)
    bgSetTimeCanvas.tag_bind(set_objOpen, '<Button-1>', CloseSettings)
    bgSetTimeFrame.grid(row=0, column=0, rowspan=8)
    bgSetTimeCanvas.pack()
    labelText = label["text"]
    label["text"] = ""
    setFrame.grid(row=3, column=0)


def CloseSettings(event=None):
    canvas.tag_bind(set_obj, '<Button-1>', OpenSettings)
    bgSetTimeCanvas.tag_bind(set_objOpen, '<Button-1>', OpenSettings)
    bgSetTimeFrame.grid_forget()
    setFrame.grid_forget()
    bgSetTimeCanvas.pack_forget()
    label["text"] = labelText


def timerSetTime(h, m, s):
    global timerTime
    timerTime = (((h * 60) + m) * 60) + s
    canvas.itemconfigure(label_id, text=f"{(timerTime // 60):02}:{(timerTime % 60):02}")


def timerStartPause(event=None):
    global isTimerRuning
    isTimerRuning = not isTimerRuning
    if label["text"] == "START":
        label["text"] = "PAUSE"
    else:
        label["text"] = "START"
    if isTimerRuning:
        timerTick()


def timerReset(event=None):
    global isTimerRuning, timerSeconds
    isTimerRuning = False
    timerSeconds = defaultSeconds
    timerShow()


def timerTick():
    global timerSeconds, isTimerRuning, isRelaxBeen, colorfg_pomodoros, timerTime
    if isTimerRuning and timerSeconds:
        timerSeconds += 1
        canvas.after(ticksPerSecond, timerTick)
        timerShow()
    if timerSeconds == timerTime:
        if not isRelaxBeen:
            timerTime = 5 * 60
            isTimerRuning = False
            timerSeconds = 1
            timerShow()
            canvas.itemconfigure(oval_id1, outline=colorfgbd_break, fill=colorfgbd_break)
            canvas.itemconfigure(oval_id2, outline=colorfg_break, fill=colorfg_break)
            canvas.itemconfigure(oval_id3, outline=colorfgbd_break)
            isRelaxBeen = True
            mixer.music.play()
            canvas.itemconfigure(label_id, text=f"{5:02}:{00:02}")
            if autoStartBreaks:
                isTimerRuning = True
        else:
            timerSetTime(int(entryH.get()), int(entryM.get()), int(entryS.get()))
            isTimerRuning = False
            timerSeconds = 1
            timerShow()
            canvas.itemconfigure(oval_id1, outline=colorfgbd_pomodoros, fill=colorfgbd_pomodoros)
            canvas.itemconfigure(oval_id2, outline=colorfg_pomodoros, fill=colorfg_pomodoros)
            canvas.itemconfigure(oval_id3, outline=colorfgbd_pomodoros)
            isRelaxBeen = False
            mixer.music.play()
            canvas.itemconfigure(label_id, text=f"{int(entryM.get()):02}:{int(entryS.get()):02}")
            if autoStartPomodoros:
                isTimerRuning = True


def timerShow():
    global isRelaxBeen
    s = timerSeconds % 60
    m = timerSeconds // 60 - (timerSeconds // (60 * 60) * 60)
    h = timerSeconds // (60 * 60)
    if not isRelaxBeen:
        if timerSeconds != 1:
            canvas.itemconfigure(oval_id2, extent=(timerSeconds * (360 / timerTime)) * -1)
        else:
            canvas.itemconfigure(oval_id2)
        tex = timerTime - timerSeconds + 1
        if timerSeconds != 1: canvas.itemconfigure(label_id, text=f"{(tex // 60):02}:{(tex % 60):02}")
        if timerSeconds == 1:
            canvas.itemconfigure(label_id, text="00:00")
    else:
        if timerSeconds != 1:
            canvas.itemconfigure(oval_id2, extent=(360 - (timerSeconds * (360 / timerTime))) * -1)
        else:
            canvas.itemconfigure(oval_id2)
        tex = timerTime - timerSeconds + 1
        if timerSeconds != 1: canvas.itemconfigure(label_id, text=f"{(tex // 60):02}:{(tex % 60):02}")
        if timerSeconds == 1:
            canvas.itemconfigure(label_id, text="00:00")


fgFrame = tk.Frame()
setFrame = tk.Frame(bg="gray95")
entryH = tk.Entry(setFrame, width=5, bg="gray95")
entryH.grid(row=0, column=0)
labelH = tk.Label(setFrame, text="h", bg="gray95")
labelH.grid(row=0, column=1)
entryM = tk.Entry(setFrame, width=5, bg="gray95")
entryM.grid(row=0, column=2)
labelM = tk.Label(setFrame, text="m", bg="gray95")
labelM.grid(row=0, column=3)
entryS = tk.Entry(setFrame, width=5, bg="gray95")
entryS.grid(row=0, column=4)
labelS = tk.Label(setFrame, text="s", bg="gray95")
labelS.grid(row=0, column=5)
entryH.insert(tk.END, '0')
entryM.insert(tk.END, '25')
entryS.insert(tk.END, '0')
buttonSetTime = tk.Label(setFrame, text="set timer", bg="gray95")
buttonSetTime.grid(row=1, column=0, columnspan=5)


label = tk.Label(fgFrame, text="START", background="gray95")
label.bind("<Button-1>", timerStartPause)
buttonSetTime.bind("<Button-1>", lambda x: timerSetTime(int(entryH.get()), int(entryM.get()), int(entryS.get())))
label.pack()

fgFrame.grid(row=5, column=0)


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x, y))
    print(x, y)


canvas.tag_bind(dragableArea, '<Button-1>', SaveLastClickPos)
canvas.tag_bind(dragableArea, '<B1-Motion>', Dragging)
canvas.tag_bind(set_obj, '<Button-1>', OpenSettings)
canvas.tag_bind(close_obj, '<Button-1>', exit)
if __name__ == '__main__':
    root.mainloop()


#TODO настройка времени больших и маленьких перерывов
#TODO настройки кол-ва маленьких до большого
#TODO настройки звука
#TODO настройки цвета
#TODO тёмная тема