import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import numpy as np

np.random.seed(19680801)


def get_data(date_temp_dictionary):
    print(date_temp_dictionary)

    def gradient_image(ax, extent, direction=0.3, cmap_range=(0, 1), **kwargs):
        """
        Draw a gradient image based on a colormap.

        Parameters
        ----------
        ax : Axes
            The axes to draw on.
        extent
            The extent of the image as (xmin, xmax, ymin, ymax).
            By default, this is in Axes coordinates but may be
            changed using the *transform* keyword argument.
        direction : float
            The direction of the gradient. This is a number in
            range 0 (=vertical) to 1 (=horizontal).
        cmap_range : float, float
            The fraction (cmin, cmax) of the colormap that should be
            used for the gradient, where the complete colormap is (0, 1).
        **kwargs
            Other parameters are passed on to `.Axes.imshow()`.
            In particular useful is *cmap*.
        """
        phi = direction * np.pi / 2
        v = np.array([np.cos(phi), np.sin(phi)])
        X = np.array([[v @ [1, 0], v @ [1, 1]],
                      [v @ [0, 0], v @ [0, 1]]])
        a, b = cmap_range
        X = a + (b - a) / X.max() * X
        im = ax.imshow(X, extent=extent, interpolation='bicubic',
                       vmin=0, vmax=1, **kwargs)
        return im

    # getting the first 10 data points for dates and storing it in an array named 'new date'

    new_date = []

    for date in date_temp_dictionary.get('date')[0:10]:
        date = date[5:10]
        date = date.replace('-', '.')
        date = float(date)
        print(date)
        new_date.append(date)

    print(new_date)

    def gradient_bar(ax, x, y, width=0.5, bottom=0):
        for left, top in zip(x, y):
            right = left + width
            gradient_image(ax, extent=(left, right, bottom, top),
                           cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))

    date_min = new_date[0]
    date_max = new_date[9]

    temp_min = min(date_temp_dictionary.get('temp'))
    temp_max = max(date_temp_dictionary.get('temp'))

    # creating the x and y axis range

    xmin, xmax = xlim = 1.0, 1.2
    ymin, ymax = ylim = 0, 100

    fig, ax = plt.subplots()
    ax.set(xlim=xlim, ylim=ylim, autoscale_on=False)

    # background image
    gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
                   cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

    N = 10

    examplex = np.arange(N) + 0.15
    print(examplex)

    # x-axis range
    x = new_date
    print(x)

    #y-axis range
    y = date_temp_dictionary.get('temp')[0:10]
    print(y)

    exampley = np.random.rand(N)
    print(exampley)

    gradient_bar(ax, x, y, width=0.7)
    ax.set_aspect('auto')
    plt.show()

    
def basic_plot(data: dict):
    fig, ax = plt.subplots()
    ax.plot(data["date"], data['temp'])
    plt.xlabel('Date')
    plt.xticks(data["date"])
    ax.xaxis.set_major_locator(LinearLocator(numticks=7))
    plt.ylabel('Temperature')
    plt.title('5 Day Forecast')
    plt.show()

if __name__ == "__main__":
    dt = {'date': ['2022-01-13 18:00:00', '2022-01-13 21:00:00', '2022-01-14 00:00:00', '2022-01-14 03:00:00', 
                   '2022-01-14 06:00:00', '2022-01-14 09:00:00', '2022-01-14 12:00:00', '2022-01-14 15:00:00', 
                   '2022-01-14 18:00:00', '2022-01-14 21:00:00', '2022-01-15 00:00:00', '2022-01-15 03:00:00', 
                   '2022-01-15 06:00:00', '2022-01-15 09:00:00', '2022-01-15 12:00:00', '2022-01-15 15:00:00', 
                   '2022-01-15 18:00:00', '2022-01-15 21:00:00', '2022-01-16 00:00:00', '2022-01-16 03:00:00', 
                   '2022-01-16 06:00:00', '2022-01-16 09:00:00', '2022-01-16 12:00:00', '2022-01-16 15:00:00', 
                   '2022-01-16 18:00:00', '2022-01-16 21:00:00', '2022-01-17 00:00:00', '2022-01-17 03:00:00', 
                   '2022-01-17 06:00:00', '2022-01-17 09:00:00', '2022-01-17 12:00:00', '2022-01-17 15:00:00', 
                   '2022-01-17 18:00:00', '2022-01-17 21:00:00', '2022-01-18 00:00:00', '2022-01-18 03:00:00', 
                   '2022-01-18 06:00:00', '2022-01-18 09:00:00', '2022-01-18 12:00:00', '2022-01-18 15:00:00'], 
          'temp': [41.9, 41.54, 37.02, 36.5, 36.82, 35.67, 34.65, 34.79, 38.37, 34.84, 30.79, 26.19, 22.75, 21.94, 
                   21.47, 22.21, 25.38, 26.51, 23.95, 22.15, 20.91, 21.02, 20.95, 26.13, 31.06, 24.78, 23.63, 24.3, 
                   24.69, 26.4, 26.06, 28.26, 28.96, 26.35, 21.25, 19.69, 23.36, 22.82, 21.87, 22.3]}
    basic_plot(dt)
