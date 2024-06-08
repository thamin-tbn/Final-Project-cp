
from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 


from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    return butter(order, [lowcut, highcut], fs=fs, btype='band')

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
def plot(): 
    global x,y1,y2
    
    xx1=x[500:800]
    yy1=y1[500:800]
    yy2=y2[500:800]
    # the figure that will contain the plot 
    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
  
    # list of squares 
    
  
    # adding the subplot 
    plot1 = fig.add_subplot(311) 
  
    # plotting the graph 
    plot1.plot(xx1) 
    
    plot1 = fig.add_subplot(312) 
  
    # plotting the graph 
    plot1.plot(yy1) 
    
    plot1 = fig.add_subplot(313) 
  
    # plotting the graph 
    plot1.plot(yy2) 
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt



    fs = 2000.0
    lowcut1 = 10.0
    highcut1 = 120.0
    lowcut2 = 450.0
    highcut2 = 550.0
    T = 2
    nsamples = T * fs
    t = np.arange(0, nsamples) / fs
    a = 0.02
    f1 = 100.0
    f2 = 500.0
    x =10 * np.sin(2 * np.pi  *f1* np.sqrt(t))
    x += 20 * np.cos(2 * np.pi * f2 * t )
    y1 = butter_bandpass_filter(x, lowcut1, highcut1, fs, order=6)
    y2 = butter_bandpass_filter(x, lowcut2, highcut2, fs, order=6)
    
    window = Tk() 
      

    window.title('Plotting in Tkinter') 
      

    window.geometry("500x500") 
      

    plot_button = Button(master = window,  
                         command = plot, 
                         height = 2,  
                         width = 10, 
                         text = "Plot") 
      

    plot_button.pack() 

    window.mainloop() 




  

