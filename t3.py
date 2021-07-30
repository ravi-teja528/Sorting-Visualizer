from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()
root.title("Sorting Visualizer")
root.maxsize(900, 750)
root.config(bg="black")

# varibles

selected_alg = StringVar()
data = []
q_sor = []


def drawData(data, color):
    canvas.delete("all")
    c_height = 530
    c_width = 800
    x_width = c_width / (len(data) + 1)
    offset = 50
    spacing = 10
    normalizeddata = [i / max(data) for i in data]
    for i, height in enumerate(normalizeddata):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 500
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def startalgorithm():
    global data
    if (selected_alg.get() == "Bubble Sort") :
        bubble_sort(data, 2.20-speedScale.get())
    elif selected_alg.get() == "Insertion Sort" :
        insertionSort(data,2.20-speedScale.get())
    elif selected_alg.get() == "Selection Sort":
        selectionSort(data, 2.20 - speedScale.get())
    elif selected_alg.get() == "Quick Sort" :
        q_sor.clear()
        for i in range(len(data))  :
            q_sor.append(0)
        quick_Sort(data, 0, len(data)-1, 2.20-speedScale.get())
    else :
        mSort(data, 2.20-speedScale.get())


def generate():
    global data
    print("Algorithm " + selected_alg.get())
    try:
        maxval = int(maxEntry.get())
    except:
        maxval = 120

    try:
        minval = int(minEntry.get())
    except:
        minval = 5

    try:
        size = int(sizeEntry.get())
    except:
        size = 10

    if minval < 0:
        minval = 5
    if maxval > 150 :
        maxval = 125
    if size > 100 or size <= 0 :
        size = 20
    if minval > maxval :
        minval, maxval = maxval, minval

    data = []
    for _ in range(size):
        data.append(random.randrange(minval, maxval + 1))

    drawData(data, ["red" for x in range(len(data))])

def selectionSort (data,timeTick):
    for i in range(0,len(data)):
        m=data[i]
        t=i
        for j in range(i,len(data)):
            drawData(data, ["green"  if x < i else "white" if x == i else "blue" if x == t or x== j else "red" for x in range(len(data))])
            time.sleep(timeTick)
            if m>data[j] :
                m=data[j]
                t=j
        data[t], data[i] = data[i], data[t]
        drawData(data, ["green" if x <= i else "red" for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ["green" if x <= i else "red" for x in range(len(data))])
    time.sleep(timeTick)

def bubble_sort(data, timeTick):
    for _ in range(len(data) - 1):
        k = 0
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                k = 1
                drawData(data, ["green" if x == j or x == j + 1 else "blue" if x > len(data) - (_ + 1) else "red" for x in range(len(data))])
                time.sleep(timeTick)
        if k == 0 :
            break
    drawData(data, ["green" for x in range(len(data))])

def partition(data, head, tail, timeTick):
    border = head
    pivot = data[tail]
    drawData(data, color_array(len(data), head, tail, border, border))
    time.sleep(timeTick)
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, color_array(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, color_array(len(data), head, tail, j, border))
        time.sleep(timeTick)

    drawData(data, color_array(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    return border


def insertionSort(data, timeTick):
    for i in range(0, len(data)):
        p = data[i]
        j = i - 1
        while j >= 0:
            if p < data[j]:
                data[j + 1], data[j] = data[j], p
                drawData(data,["blue" if x == j else "green" if x < i else "red" for x in range(len(data))])
                time.sleep(timeTick)
            else:
                data[j + 1] = p
                drawData(data, ["green" if x <= i else "red" for x in range(len(data))])
                time.sleep(timeTick)
                break
            j -= 1
        data[j + 1] = p
        drawData(data, ["green" if x <= i else "red" for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ["green" for x in range(len(data))])


def quick_Sort(data, head, tail, timeTick):

    if head < tail:
        part = partition(data, head, tail, timeTick)
        q_sor[part] = 1
        quick_Sort(data, head, (part - 1), timeTick)
        quick_Sort(data, (part + 1), tail, timeTick)
    else :
        if head >= 0 and head <= len(data)-1 :
            q_sor[head] = 1
        if tail >= 0 and tail <= len(data)-1 :
            q_sor[tail] = 1
    drawData(data, ["green" for i in range(len(data))])


def color_array(data, head, tail, border, cur, isSwaping = False) :
    color = []
    for i in range(data) :
        if i >= head or i <= tail :
            color.append("grey")
        else :
            color.append("white")

        if i == tail :
            color[i] = "blue"
        elif i == border :
            color[i] = "red"
        elif i == cur :
            color[i] = "yellow"

        if isSwaping :
            if i == border or i == cur :
                color[i] = "orange"

        if q_sor[i] == 1 :
            color[i] = "green"


    return color


def mSort(data, timeTick):
    merge_sort(data, 0, len(data) - 1, timeTick)


def merge_sort(data, left, right, timeTick):
    if left < right:
        middle = (left + right) // 2
        drawData(data, colorarr(len(data), left, middle, right))
        time.sleep(timeTick)
        merge_sort(data, left, middle, timeTick)
        merge_sort(data, middle + 1, right, timeTick)
        merge(data, left, middle, right, timeTick)


def merge(data, left, middle, right, timeTick):
    drawData(data, colorarr(len(data), left, middle, right))
    time.sleep(timeTick)
    leftl = data[left:middle + 1]
    rightl = data[middle + 1:right + 1]
    leftind = rightind = 0
    for ind in range(left, right + 1):
        if leftind < len(leftl) and rightind < len(rightl):
            if leftl[leftind] <= rightl[rightind]:
                data[ind] = leftl[leftind]
                leftind += 1
            else:
                data[ind] = rightl[rightind]
                rightind += 1
        elif rightind < len(rightl):
            data[ind] = rightl[rightind]
            rightind += 1
        else:
            data[ind] = leftl[leftind]
            leftind += 1

    drawData(data, ["green" if i >= left and i <= right else "grey" for i in range(len(data))])
    time.sleep(timeTick)


def colorarr(len, left, middle, right):
    color = []
    for i in range(len):
        if i >= left and i <= right:
            if i <= middle:
                color.append("yellow")
            else:
                color.append("pink")
        else:
            color.append("grey")

    return color
# UI_frame

UI_frame = Frame(root, width=900, height=200, bg="grey")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, height=530, width=900, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# UI_AREA
# row0

Label(UI_frame, text="Algorithm", bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algmenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=["Bubble Sort","Quick Sort", "Merge Sort","Selection Sort","Insertion Sort"])
algmenu.grid(row=0, column=1, padx=5, pady=5)
algmenu.current(0)

speedScale = Scale(UI_frame, from_=0.05, to=2.15, length=200, digits=3, resolution=0.2, orient=HORIZONTAL,label="Speed[x]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=startalgorithm, bg="pink").grid(row=0, column=3, padx=5, pady=5)
# row{1}


Label(UI_frame, text="Size(0-50)", bg="grey").grid(row=1, column=0, padx=5, pady=5, sticky=E)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5)

Label(UI_frame, text="Min(5)", bg="grey").grid(row=1, column=2, padx=5, pady=5, sticky=E)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5)

Label(UI_frame, text="Max(150)", bg="grey").grid(row=1, column=4, padx=5, pady=5, sticky=E)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5)

Button(UI_frame, text="Generate", command=generate, bg="white").grid(row=1, column=6, padx=5, pady=5)

root.mainloop()
