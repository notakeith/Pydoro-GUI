from pygame import mixer
import tkinter as tk
import json

width = 250
height = 250

radius = 32
diameter = 200
borderradius = 50
borderwidth = 4
diameter2 = diameter - borderradius
diameter3 = diameter - 4

with open('config.json', 'r') as f:
    json_data = json.load(f)
    theme = json_data['theme']

if theme == "light":
    fontcolor = "black"
    colorbg = "gray95"
    colorfg_pomodoros = "#ff4c30"
    colorfgbd_pomodoros = "#ffcec7"
    colorbgbd_pomodoros = "#ffcec7"
    colorfg_break = "#00BD68"
    colorfgbd_break = "#BDD2C9"
    colorbgbd_break = "#BDD2C9"
    colorsetb = "#fad859"
    colorclsb = "#fe7968"

if theme == "dark-bright":
    fontcolor = "white"
    colorbg = "#2e2e2e"  # A dark gray background
    colorfg_pomodoros = "#ff6b5a"  # A lighter red for visibility on dark background
    colorfgbd_pomodoros = "#7a302b"  # A darker red for borders
    colorbgbd_pomodoros = "#7a302b"  # Matching border color for pomodoros
    colorfg_break = "#00e58a"  # A brighter green for visibility on dark background
    colorfgbd_break = "#006b43"  # A darker green for borders
    colorbgbd_break = "#006b43"  # Matching border color for breaks
    colorsetb = "#fad859"
    colorclsb = "#fe7968"


if theme == "dark":
    fontcolor = "white"
    colorbg = "#2e2e2e"  # A dark gray background
    colorfg_pomodoros = "#d1584a"  # A lighter red for visibility on dark background
    colorfgbd_pomodoros = "#7a302b"  # A darker red for borders
    colorbgbd_pomodoros = "#7a302b"  # Matching border color for pomodoros
    colorfg_break = "#0ab571"  # A brighter green for visibility on dark background
    colorfgbd_break = "#006b43"  # A darker green for borders
    colorbgbd_break = "#006b43"  # Matching border color for breaks
    colorsetb = "#bca54c"
    colorclsb = "#bf6256"

ticksPerSecond = 1000
timerSeconds = 1

isRelaxBeen = False
autoStartBreaks = True
autoStartPomodoros = True
labelText = ""

mixer.init()
mixer.music.load(f"bell.mp3")

root = tk.Tk()
root.geometry(f'{width}x{height}+{root.winfo_screenwidth()-width-24}+{root.winfo_screenheight()-height-24}')
root.overrideredirect(True)
root.attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "gray94")
root["bg"] = "gray94"