import matplotlib.pyplot as plt
import pylab

def int_plot(df, param, legend = ''):
    df.plot(y=param)
    plt.xticks(rotation=90)
    plt.ylabel(param+legend)
    plt.show()

def show_plot(df, param):
    if param == 'Wind' or param == 'Condition':
        x = list(df.index.values)
        y = list(df[param])
        pylab.figure(1)
        x1 = range(len(x))
        pylab.xticks(x1, x, rotation='vertical')
        plt.xticks(x1[::80])
        pylab.plot(x1, y, "o", label=param)
        plt.xlabel('day/month')
        plt.ylabel('Type of ' + param)
        plt.legend()
        pylab.show()
    elif param == 'Humidity':
        int_plot(df, param, ' (in %)')
    elif param == 'Wind Speed' or param == 'Wind Gust':
        int_plot(df, param, ' (in mph)')
    else:
        int_plot(df, param)

def make_graphics(df, list_of_params):
    if type(list_of_params) is list:
        for param in list_of_params:
            show_plot(df, param)
    else:
        show_plot(df, list_of_params)
