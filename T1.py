from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    return butter(order, [lowcut, highcut], fs=fs, btype='band')

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt


    # Sample rate and desired cutoff frequencies (in Hz).
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

    plt.figure()
    

    plt.plot(t[500:600], x[500:600], label='signal')
    plt.xlabel('time (seconds)')       
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')




    plt.figure()

    y1 = butter_bandpass_filter(x, lowcut1, highcut1, fs, order=6)
    plt.plot(t[500:600], y1[500:600], label='Filtered signal (%g Hz)' % f1)
    plt.xlabel('time (seconds)')
    # plt.hlines([-a, a], 0, T, linestyles='--')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')

    plt.show()
    
    plt.figure()

    y2 = butter_bandpass_filter(x, lowcut2, highcut2, fs, order=6)
    plt.plot(t[500:600], y2[500:600], label='Filtered signal (%g Hz)' % f2)
    plt.xlabel('time (seconds)')
    # plt.hlines([-a, a], 0, T, linestyles='--')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')

    plt.show()