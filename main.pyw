import os

from init import *


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


def OpenThemeSettings(event=None):
    bgSetTimeFrame.grid_forget()
    setFrame.grid_forget()
    bgSetTimeCanvas.pack_forget()
    themeFrame.grid(row=3, column=0)
    canvas.itemconfigure(oval_obj1, outline=colorbg, fill=colorbg)
    canvas.itemconfigure(oval_obj2, outline=colorbg, fill=colorbg)
    canvas.itemconfigure(oval_obj3, outline=colorbg)
    canvas.itemconfigure(label_obj, fill=colorbg)


def timerSetSettings():
    global timerSeconds, timerTime, isRelaxBeen
    timerSeconds = timerTime - 1
    timerTick()


def timerSetTime(h, m, s):
    global timerTime
    timerTime = (((h * 60) + m) * 60) + s
    canvas.itemconfigure(label_obj, text=f"{(timerTime // 60):02}:{(timerTime % 60):02}")


def timerStartPause(event=None):
    global isTimerRuning
    isTimerRuning = not isTimerRuning
    if label["text"] == "START":
        label["text"] = "PAUSE"
    else:
        label["text"] = "START"
    if isTimerRuning:
        timerTick()


def timerTick():
    global timerSeconds, isTimerRuning, isRelaxBeen, colorfg_pomodoros, timerTime
    if isTimerRuning and timerSeconds:
        timerSeconds += 1
        canvas.after(ticksPerSecond, timerTick)
        timerShow()
    if timerSeconds == timerTime:
        print(isRelaxBeen)
        if isRelaxBeen % 2 == 0:
            if isRelaxBeen != 0 and isRelaxBeen % ((int(smallperbig.get()) - 1) * 2) == 0:
                timerSetTime(int(bbreakH.get()), int(bbreakM.get()), int(bbreakS.get()))
                isTimerRuning = False
                timerSeconds = 1
                timerShow()
                canvas.itemconfigure(oval_obj1, outline=colorfgbd_break, fill=colorfgbd_break)
                canvas.itemconfigure(oval_obj2, outline=colorfg_break, fill=colorfg_break)
                canvas.itemconfigure(oval_obj3, outline=colorfgbd_break)
                isRelaxBeen += 1
                mixer.music.play()
                canvas.itemconfigure(label_obj, text=f"{int(bbreakM.get()):02}:{int(bbreakS.get()):02}")
                if autoStartBreaks:
                    isTimerRuning = True
            else:
                timerSetTime(int(sbreakH.get()), int(sbreakM.get()), int(sbreakS.get()))
                isTimerRuning = False
                timerSeconds = 1
                timerShow()
                canvas.itemconfigure(oval_obj1, outline=colorfgbd_break, fill=colorfgbd_break)
                canvas.itemconfigure(oval_obj2, outline=colorfg_break, fill=colorfg_break)
                canvas.itemconfigure(oval_obj3, outline=colorfgbd_break)
                isRelaxBeen += 1
                mixer.music.play()
                canvas.itemconfigure(label_obj, text=f"{int(sbreakM.get()):02}:{int(sbreakS.get()):02}")
                if autoStartBreaks:
                    isTimerRuning = True
        else:
            timerSetTime(int(workH.get()), int(workM.get()), int(workS.get()))
            isTimerRuning = False
            timerSeconds = 1
            timerShow()
            canvas.itemconfigure(oval_obj1, outline=colorfgbd_pomodoros, fill=colorfgbd_pomodoros)
            canvas.itemconfigure(oval_obj2, outline=colorfg_pomodoros, fill=colorfg_pomodoros)
            canvas.itemconfigure(oval_obj3, outline=colorfgbd_pomodoros)
            isRelaxBeen += 1
            mixer.music.play()
            canvas.itemconfigure(label_obj, text=f"{int(workM.get()):02}:{int(workS.get()):02}")
            if autoStartPomodoros:
                isTimerRuning = True


def timerShow():
    global isRelaxBeen
    if isRelaxBeen % 2 == 0:
        if timerSeconds != 1:
            canvas.itemconfigure(oval_obj2, extent=(timerSeconds * (360 / timerTime)) * -1)
        else:
            canvas.itemconfigure(oval_obj2)
        tex = timerTime - timerSeconds + 1
        if timerSeconds != 1: canvas.itemconfigure(label_obj, text=f"{(tex // 60):02}:{(tex % 60):02}")
        if timerSeconds == 1:
            canvas.itemconfigure(label_obj, text="00:00")
    else:
        if timerSeconds != 1:
            canvas.itemconfigure(oval_obj2, extent=(360 - (timerSeconds * (360 / timerTime))) * -1)
        else:
            canvas.itemconfigure(oval_obj2)
        tex = timerTime - timerSeconds + 1
        if timerSeconds != 1: canvas.itemconfigure(label_obj, text=f"{(tex // 60):02}:{(tex % 60):02}")
        if timerSeconds == 1:
            canvas.itemconfigure(label_obj, text="00:00")


fgFrame = tk.Frame()
setFrame = tk.Frame(bg=colorbg)

workH = tk.StringVar()
workH.set(0)
workM = tk.StringVar()
workM.set(25)
workS = tk.StringVar()
workS.set(0)
sbreakH = tk.StringVar()
sbreakH.set(0)
sbreakM = tk.StringVar()
sbreakM.set(5)
sbreakS = tk.StringVar()
sbreakS.set(0)
bbreakH = tk.StringVar()
bbreakH.set(0)
bbreakM = tk.StringVar()
bbreakM.set(15)
bbreakS = tk.StringVar()
bbreakS.set(0)

smallperbig = tk.StringVar()
smallperbig.set(4)

list = [[workH, "h"], [workM, "m"], [workS, "s"]], [[sbreakH, "h"], [sbreakM, "m"], [sbreakS, "s"]], [[bbreakH, "h"],
                                                                                                      [bbreakM, "m"],
                                                                                                      [bbreakS, "s"]]
# l["raised", "sunken", "flat", "ridge", "solid", "groove"]
for i in range(len(list)):
    for j in range(len(list[i])):
        tk.Entry(setFrame, textvariable=list[i][j][0], width=5, bg=colorbg, fg=fontcolor, relief=tk.FLAT,
                 insertbackground=fontcolor, justify="right", highlightthickness=0.5, highlightbackground=colorclsb,
                 highlightcolor=colorclsb).grid(row=i * 4 + 1, column=2 * j)
        tk.Label(setFrame, text=list[i][j][1], bg=colorbg, fg=fontcolor).grid(row=i * 4 + 1, column=2 * j + 1)

tk.Label(setFrame, text="Work", bg=colorbg, fg=fontcolor, anchor="e", justify=tk.LEFT).grid(row=0, column=0,
                                                                                            columnspan=6)
# tk.Label(setFrame, text="---", bg=colorbg,fg=fontcolor).grid(row=3, column=0, columnspan=5)
tk.Label(setFrame, text="Small Rest", bg=colorbg, fg=fontcolor, anchor="e", justify="left").grid(row=4, column=0,
                                                                                                 columnspan=6)
tk.Label(setFrame, text="Big Rest", bg=colorbg, fg=fontcolor, anchor="e", justify=tk.LEFT).grid(row=6, column=0,
                                                                                                columnspan=6)
tk.Label(setFrame, text="Small per Big", bg=colorbg, fg=fontcolor, anchor="e", justify=tk.LEFT).grid(row=10, column=0,
                                                                                                     columnspan=3)
tk.Entry(setFrame, textvariable=smallperbig, width=5, bg=colorbg, fg=fontcolor, relief=tk.FLAT, highlightthickness=0.5,
         highlightbackground=colorclsb, highlightcolor=colorclsb,
         insertbackground=fontcolor, justify="left").grid(row=10, column=4)

buttonSetTime = tk.Label(setFrame, text="UPDATE", bg=colorbg, fg=fontcolor, font=10)
buttonSetTime.grid(row=11, column=0, columnspan=6)
buttonSetTime.bind("<Button-1>", lambda x: timerSetSettings())

themeFrame = tk.Frame(root, bg=colorbg, width=100, height=100)


def applyTheme(theme):
    print(theme)
    with open('config.json', 'r') as f:
        json_data = json.load(f)
        json_data['theme'] = theme
        print(theme)
    with open('config.json', 'w') as f:
        f.write(json.dumps(json_data))
    root.destroy()
    os.startfile("main.pyw")

themesButton1 = tk.Label(themeFrame, text="light", bg=colorbg, fg=fontcolor, font=12)
themesButton1.grid(row=1, column=0)
themesButton1.bind("<Button-1>", lambda x: applyTheme("light"))
themesButton2 = tk.Label(themeFrame, text="dark-bright", bg=colorbg, fg=fontcolor, font=12)
themesButton2.grid(row=2, column=0)
themesButton2.bind("<Button-1>", lambda x: applyTheme("dark-bright"))
themesButton3 = tk.Label(themeFrame, text="dark", bg=colorbg, fg=fontcolor, font=12)
themesButton3.grid(row=3, column=0)
themesButton3.bind("<Button-1>", lambda x: applyTheme("dark"))


buttonSetTheme = tk.Label(setFrame, text="CHANGE THEME", bg=colorbg, fg=fontcolor, font=10)
buttonSetTheme.grid(row=12, column=0, columnspan=6)
buttonSetTheme.bind("<Button-1>", lambda x: OpenThemeSettings())

label = tk.Label(fgFrame, text="START", background=colorbg, fg=fontcolor)
label.bind("<Button-1>", timerStartPause)

label.pack()

fgFrame.grid(row=5, column=0)


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x, y))


canvas.tag_bind(dragableArea, '<Button-1>', SaveLastClickPos)
canvas.tag_bind(dragableArea, '<B1-Motion>', Dragging)
canvas.tag_bind(set_obj, '<Button-1>', OpenSettings)
canvas.tag_bind(close_obj, '<Button-1>', exit)

if __name__ == '__main__':
    root.mainloop()

# TODO настройка времени больших и маленьких перерывов
# TODO настройки кол-ва маленьких до большого
