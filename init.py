from config import *
import tkinter as tk

isTimerRuning = False
timerTime = 25 * 60

bgFrame = tk.Frame()
bgFrame.grid(row=0, column=0, rowspan=8)

canvas = tk.Canvas(bgFrame, bd=0, highlightthickness=0, relief='ridge', width=width, height=height)

canvas["background"] = "gray94"

params = ([0,0,radius,radius],
          [width,0,width-radius,radius],
          [width,height,width-radius,height-radius],
          [0,height,radius,height-radius])

for i in params:
    canvas.create_oval(*i, outline="gray94",fill=colorbg, width=2)

points = [0, radius / 2, radius / 2, 0, width - (radius / 2), 0, width, radius / 2, width, height - (radius / 2),
          width - (radius / 2), height, radius / 2, height, 0, height - (radius / 2)]

dragableArea = canvas.create_polygon(points, outline=colorbg, fill=colorbg, width=2)

oval_obj1 = canvas.create_oval((width - diameter) / 2, (height - diameter) / 2, ((width - diameter) / 2) + diameter,
                               ((height - diameter) / 2) + diameter, outline=colorfgbd_pomodoros, fill=colorbgbd_pomodoros,
                               width=borderwidth)
oval_obj2 = canvas.create_arc((width - diameter3) / 2, (height - diameter3) / 2, ((width - diameter3) / 2) + diameter3,
                              ((height - diameter3) / 2) + diameter3, outline=colorfg_pomodoros, fill=colorfg_pomodoros,
                              width=0, start=90, extent=0)
oval_obj3 = canvas.create_oval((width - diameter2) / 2, (height - diameter2) / 2, ((width - diameter2) / 2) + diameter2,
                               ((height - diameter2) / 2) + diameter2, outline=colorfgbd_pomodoros, fill=colorbg,
                               width=borderwidth)

label_obj = canvas.create_text(height / 2, width / 2, text="25:00", font=("Calibri Light", 32),fill=fontcolor)

close_obj = canvas.create_oval(
    width - 13, 10, width - radius, radius - 5, outline=colorclsb,
    fill=colorclsb, width=2
)

set_obj = canvas.create_oval(
    width - 38, 10, width - radius - 25, radius - 5, outline=colorsetb,
    fill=colorsetb, width=2
)
canvas.pack()

bgSetTimeFrame = tk.Frame()
bgSetTimeCanvas = tk.Canvas(bgSetTimeFrame, bd=0, highlightthickness=0, relief='ridge', width=width, height=height)

bgSetTimeCanvas["background"] = "gray94"

for i in params:
    bgSetTimeCanvas.create_oval(*i, outline="gray94",fill=colorbg, width=2)

bgSetTimeArea = bgSetTimeCanvas.create_polygon(points, outline=colorbg, fill=colorbg, width=2)

set_objOpen = bgSetTimeCanvas.create_oval(
    width - 38, 10, width - radius - 25, radius - 5, outline=colorsetb,
    fill=colorsetb, width=2
)

bgSetTimeCanvas.pack()