import matplotlib.pyplot as plt
import numpy as np
from math import floor


def draw_magnetic_rolling_shutter_chart():
    fig_w_inch = 18
    fig_h_inch = 12
    fig_dpi = 300
    fig = plt.figure(figsize=[fig_w_inch, fig_h_inch], dpi=fig_dpi)
    axes = fig.add_axes([0, 0, 1, 1])
    axes.set_axis_off()
    axes.grid(b=None)
    axes.margins(0)
    fig_w = fig_w_inch * fig_dpi
    fig_h = fig_h_inch * fig_dpi
    # pattern is dot, then 3 dots worth of space, then dot...
    # first and last are half-dot
    vis_dots_per_w = 16
    vis_dots_per_h = floor(vis_dots_per_w * fig_h_inch / fig_w_inch)
    invis_dots_between = 3
    dots_per_w = (vis_dots_per_w - 1) * (invis_dots_between + 1)
    dot_d = fig_w / dots_per_w
    vis_dot_spacing = dot_d * (invis_dots_between + 1)
    vis_dot_origin = [0, 0]
    vis_dot_max_x = vis_dot_origin[0] + vis_dot_spacing * (vis_dots_per_w - 1)
    vis_dot_max_y = vis_dot_origin[1] + vis_dot_spacing \
                    * ((vis_dots_per_w * fig_h_inch / fig_w_inch) - 1)
    dot_x_range = np.linspace(vis_dot_origin[0], vis_dot_max_x, vis_dots_per_w)
    dot_y_range = np.linspace(vis_dot_origin[1], vis_dot_max_y, vis_dots_per_h)
    dot_colors = ['r', 'g', 'w']
    dot_x = []
    dot_y = []
    dot_color = []
    for iy, y in enumerate(dot_y_range):
        color_cycle_offset = iy % len(dot_colors)
        for ix, x in enumerate(dot_x_range):
            if (ix == 0 and iy == 2) or (ix == 1 and iy == 1) or (ix == 2 and iy == 0):
                continue
            dot_x.append(x)
            dot_y.append(y)
            dot_color.append(
                dot_colors[(color_cycle_offset + ix) % len(dot_colors)])
    axes.scatter(dot_x, dot_y, dot_d * 3, dot_color)
    dir = '/Users/jgoldstone/tfe/experiments/3de_metadata/magnetic_targets'
    filename = f'rendered_{fig_w}x{fig_h}_rs.png'
    pathname = f'{dir}/{filename}'
    plt.savefig(pathname, bbox_inches='tight', facecolor='#000000', dpi=fig_dpi,
                pad_inches=0)


if __name__ == '__main__':
    draw_magnetic_rolling_shutter_chart()

