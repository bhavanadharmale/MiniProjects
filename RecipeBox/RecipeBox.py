import tkinter as tk
from tkinter import *
import json




def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class RecipeBox:
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

        self.data = self.loadJsonData()

        main_menu = list(self.data.keys())

        self.clicked_main = StringVar()
        self.clicked_main.set(main_menu[0])

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.217, rely=0.067, height=21, width=84)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Main Menu''')

        self.Listbox1 = tk.OptionMenu(top, self.clicked_main , *main_menu)
        self.Listbox1.place(relx=0.383, rely=0.067, relheight=0.049, relwidth=0.24)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")

        self.Get_Recipe_Button = tk.Button(top)
        self.Get_Recipe_Button["command"] = lambda: self.get_recipe_list()
        self.Get_Recipe_Button.place(relx=0.47, rely=0.150, height=34, width=77)
        self.Get_Recipe_Button.configure(activebackground="#ececec")
        self.Get_Recipe_Button.configure(activeforeground="#000000")
        self.Get_Recipe_Button.configure(background="#d9d9d9")
        self.Get_Recipe_Button.configure(disabledforeground="#a3a3a3")
        self.Get_Recipe_Button.configure(foreground="#000000")
        self.Get_Recipe_Button.configure(highlightbackground="#d9d9d9")
        self.Get_Recipe_Button.configure(highlightcolor="black")
        self.Get_Recipe_Button.configure(pady="0")
        self.Get_Recipe_Button.configure(text='''Get_Recipe''')

        self.recipe_display_label = tk.Text(top)
        self.recipe_display_label.place(relx=0.19, rely=0.356, height=300, width=1000)
        self.recipe_display_label.configure(background="#d9d9d9")
        self.recipe_display_label.configure(foreground="blue")
        self.recipe_display_label.configure(wrap="word")

    def loadJsonData(self):
        with open("Recipe.json", "r") as fp:
            data = json.load(fp)
            return data


    def get_recipe_list(self):

        self.recipe_display_label.delete('1.0', END)

        ingredientString = "Ingredients:\n\n"
        item = self.clicked_main.get()
        for ingredient in self.data[item]["ingredients"]:
            ingredientString += ingredient + "\n"

        self.recipe_display_label.insert(tk.END, ingredientString)

        directionString = "\n\nDirections:\n\n"
        for direction in self.data[item]["Directions"]:
            directionString += direction + "\n"

        self.recipe_display_label.insert(tk.END, directionString)




    def list_to_string(self, arr):
        retStr = ""
        for i in range(0, len(arr)):
            retStr += str(i+1) + "." + arr[i] + "\n"

        return retStr




if __name__ == '__main__':
    root = tk.Tk()
    top = RecipeBox(root)
    root.mainloop()