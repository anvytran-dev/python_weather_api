import matplotlib.pyplot as plt
import numpy as np

import main

from main import get_current_weather, get_forcast, continue_or_quit_program, get_menu

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
