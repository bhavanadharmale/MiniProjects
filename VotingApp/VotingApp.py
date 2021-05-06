from tkinter import *
import tkinter as tk
import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class VotingApp:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.voteCount = [0, 0, 0]

        options = [
            "BJP",
            "CONGRESS",
            "SHIV-SENA"
        ]

        self.clicked = StringVar()

        self.clicked.set("BJP")

        self.mb = tk.OptionMenu(top, self.clicked , *options)
        self.mb.place(relx=0.217, rely=0.044, relheight=0.079, relwidth=0.59)
        self.mb.configure(background="white")
        self.mb.configure(disabledforeground="#a3a3a3")
        self.mb.configure(font="TkFixedFont")
        self.mb.configure(foreground="#000000")


        self.Button1 = tk.Button(top)
        self.Button1["command"] = lambda: self.voteButtonClicked()
        self.Button1.place(relx=0.467, rely=0.156, height=34, width=57)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Vote''')

        self.Graph = tk.Button(top)
        self.Graph["command"] = lambda: self.graphButtonClicked()
        self.Graph.place(relx=0.467, rely=0.267, height=34, width=57)
        self.Graph.configure(activebackground="#ececec")
        self.Graph.configure(activeforeground="#000000")
        self.Graph.configure(background="#d9d9d9")
        self.Graph.configure(disabledforeground="#a3a3a3")
        self.Graph.configure(foreground="#000000")
        self.Graph.configure(highlightbackground="#d9d9d9")
        self.Graph.configure(highlightcolor="black")
        self.Graph.configure(pady="0")
        self.Graph.configure(text='''Graph''')

    def voteButtonClicked(self):

        if self.clicked.get() == "BJP":
            self.voteCount[0] += 1
        elif self.clicked.get() == "CONGRESS":
            self.voteCount[1] += 1
        elif self.clicked.get() == "SHIV-SENA":
            self.voteCount[2] += 1

    def graphButtonClicked(self):

        labels = 'BJP', 'Congress', 'Shiv-Sena'
        colors = ['red', 'green', 'orange']
        explode = (0.1, 0, 0)  # explode 1st slice

        print("BJP : ",self.voteCount[0])
        print("CONGRESS : ", self.voteCount[1])
        print("SHIV-SENA : ", self.voteCount[2])

        fig = matplotlib.figure.Figure(figsize=(4, 4))
        ax = fig.add_subplot(111)
        ax.pie(self.voteCount, explode=explode, labels=labels, colors=colors,
                autopct='%1.0f%%', shadow=True, startangle=140)


        circle = matplotlib.patches.Circle((0, 0), 0.7, color='white')
        ax.add_artist(circle)

        window = tk.Tk()
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().pack()
        canvas.draw()

if __name__ == '__main__':
    root = tk.Tk()
    top = VotingApp(root)
    root.mainloop()
