import colour
from colour.plotting import *
from colour.models.rgb.datasets import *
from colour.algebra import LinearInterpolator
from colour.plotting.diagrams import plot_spectral_locus
import numpy as np

colour_style()

defaultSarnoffTripleGamutSpaces = (BT2020_COLOURSPACE,
                                   DCI_P3_COLOURSPACE,
                                   BT709_COLOURSPACE)


def draw_sarnoff_triple_gamut_diagram(
        colourspaces=defaultSarnoffTripleGamutSpaces,
        num_edge_points=7,
        **kwargs):
    fig, axes = plot_spectral_locus(standalone=False,
                                    spectral_locus_colors='RGB')
    settings = {'colour_cycle_count': len(colourspaces)}
    settings.update(kwargs)
    cycle = colour_cycle(**settings)
    for colourspace in colourspaces:
        R, G, B, _A = next(cycle)
        # return primaries as np.array([rx, ry, gx, gy, bx, by])
        primaries = colourspace.primaries.reshape((3, 2))
        for edge in range(3):
            start_vertex = primaries[edge, ]
            end_vertex = primaries[(edge + 1) % 3, ]
            interpolator_x = LinearInterpolator(range(2),
                                                np.array((start_vertex[0],
                                                          end_vertex[0])))
            interpolator_y = LinearInterpolator(range(2),
                                                np.array((start_vertex[1],
                                                          end_vertex[1])))
            print('should have drawn line from ( ',
                  start_vertex[0], ',', start_vertex[1], ') to ( ',
                  end_vertex[0], ',', end_vertex[1], ')')
            # bycols = np.array([start_vertex, end_vertex])
            # axes.plot(bycols)
            axes.plot((start_vertex[0], end_vertex[0]),
                      (start_vertex[1], end_vertex[1]),
                      color=(R, G, B))
            for edge_point in range(num_edge_points):
                x = interpolator_x(edge_point / num_edge_points)
                y = interpolator_y(edge_point / num_edge_points)
                axes.plot(x, y, "bo")
    render()


def draw_photopic_relative_luminosity_curve():
    plot_multi_sds(
        [colour.PHOTOPIC_LEFS['CIE 1924 Photopic Standard Observer']],
        y_label='Luminous Efficiency')

if __name__ == '__main__':
    # draw_sarnoff_triple_gamut_diagram()
    draw_photopic_relative_luminosity_curve()
