import tkinter as tk
import yfinance as yf
import plotly.graph_objs as go
from tkinter import messagebox

class StockMarket:
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

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.280, rely=0.080, height=38, width=241)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter Stock Symbol :''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.450, rely=0.089, height=20, relwidth=0.126)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button1 = tk.Button(top)
        self.Button1["command"] = lambda: self.getStock()
        self.Button1.place(relx=0.488, rely=0.15, height=24, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Get Stock''')


    def getStock(self):
        # Interval set to 5 minute
        stock_symbol = self.Entry1.get()
        data = yf.download(tickers=stock_symbol, period='1d', interval='5m')
        # print(data)

        if not data.empty:
            # declare figure
            fig = go.Figure()

            # Plot data and add to figure for display
            fig.add_trace(go.Scatter(x=data.index, y=data['High'], name='market data'))

            # Add titles
            fig.update_layout(
                title=stock_symbol.upper() + ' live share price evolution',
                yaxis_title='Stock Price (USD per Shares)')

            # X-Axes
            fig.update_xaxes(
                rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=15, label="15m", step="minute", stepmode="backward"),
                        dict(count=45, label="45m", step="minute", stepmode="backward"),
                        dict(count=1, label="HTD", step="hour", stepmode="todate"),
                        dict(count=3, label="3h", step="hour", stepmode="backward"),
                        dict(step="all")
                    ])
                )
            )

            # show the plot
            fig.show()
        else:
            messagebox.showerror(title="Not Found", message='"{}" stock symbol is invalid'.format(stock_symbol.upper()))

if __name__=='__main__':
    root = tk.Tk()
    top = StockMarket(root)
    root.mainloop()