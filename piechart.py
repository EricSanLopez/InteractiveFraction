import tkinter as Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class App:
    def __init__(self, master):
        # Create a container
        frame = Tkinter.Frame(master)
        # Create 2 buttons
        self.button = Tkinter.Button(frame,text="Ok",
                                        command=self.draw,
                                        height = 2, 
                                        width = 5)
        self.numer = Tkinter.Entry(frame, text='Numerador')
        self.denom = Tkinter.Entry(frame, text='Denominador')
        self.numer.pack()
        self.denom.pack()
        self.button.pack(side="bottom")
        
        self.is_on = True
        self.exp_button = Tkinter.Button(text="EXPLOSIVE", width=10, 
                                         command=self.Switch)
        self.exp_button.config(fg='green')
        self.exp_button.pack(pady=10, side='bottom')

        fig = Figure()
        self.ax = fig.add_subplot(111)
        
        self.valors = [1,1]
        col = ['yellow','blue']
        if self.is_on:
            explode = (0.2,0.2)
        else:
            explode = (0.0,0.0)
        self.pie = self.ax.pie(self.valors, explode = explode, radius=1, 
                               shadow=True, colors=col, startangle=90)
        
        self.chart1 = FigureCanvasTkAgg(fig,frame)
        self.chart1.get_tk_widget().pack()
        self.chart1.draw()
        frame.pack()
    
    def draw(self):
        try:
            num = int(self.numer.get())
            denom = int(self.denom.get())
        except:
            num = 1
            denom = 2
        self.valors = [1]*denom
        col = ['yellow']*num + ['blue']*(denom-num)
        if self.is_on:
            explode = [0.2]*denom 
        else:
            explode = [0.0]*denom
        self.ax.clear()
        self.pie = self.ax.pie(self.valors, explode=explode, radius=1, 
                               shadow=True, colors=col, startangle=90)
        self.chart1.draw()

    def Switch(self):
        if self.is_on:
            self.exp_button.config(fg = 'grey')
            self.is_on = False
        else:
            self.exp_button.config(fg = 'green')
            self.is_on = True
        self.draw()
    
        
root = Tkinter.Tk()
Tkinter.Button(root, text="Quit", command=root.destroy).pack(side="bottom")
app = App(root)
root.mainloop()