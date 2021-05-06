import requests
import tkinter as tk
from tkinter import messagebox


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class LocalWeatherApp:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1536x801+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.450, rely=0.089, height=20, relwidth=0.126)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.280, rely=0.080, height=38, width=241)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter City Name :''')

        self.Button1 = tk.Button(top)
        self.Button1["command"] = lambda: self.displayCityData()
        self.Button1.place(relx=0.488, rely=0.15, height=24, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.273, rely=0.275, relheight=0.512, relwidth=0.315)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

    def displayCityData(self):
        city = self.Entry1.get()
        print('City:',city)
        try:
            query = 'q=' + city;
            result = self.weather_data(query);

            temperature = "{}'s temperature: \t{}°C\n".format(city, result['main']['temp'])
            windSpeed = "Wind speed: \t{} m/s\n".format(result['wind']['speed'])
            description = "Description: \t{}\n".format(result['weather'][0]['description'])
            weather = "Weather: \t{}\n".format(result['weather'][0]['main'])

            self.Text1.delete('1.0', tk.END)
            self.Text1.insert(tk.END, temperature)
            self.Text1.insert(tk.END, windSpeed)
            self.Text1.insert(tk.END, description)
            self.Text1.insert(tk.END, weather)
        except:
            self.Text1.delete('1.0', tk.END)
            messagebox.showerror("Data not Found", message="No Data found for City:{}".format(city))

    def weather_data(self, query):
        res = requests.get('http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
        return res.json();

if __name__ == '__main__':
    root = tk.Tk()
    top = LocalWeatherApp(root)
    root.mainloop()





