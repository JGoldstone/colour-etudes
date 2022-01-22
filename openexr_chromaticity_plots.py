import os
import colour
import colour.models.rgb.transfer_functions.st_2084
import colour.plotting

colour.plotting.colour_style()


def pathify(directory, prefix, base_filename, frame, suffix):
    filename = base_filename
    if prefix != '':
        filename = prefix + '_' + filename
    if suffix == '':
        raise ValueError
    if frame >= 0:
        filename = filename + '.' + str(frame)
    filename = filename + '.' + suffix
    return os.path.join(directory, filename)


def plot_scene_and_display_chromaticities():
    img_base_filename = 'A007C001_120713_R0SW'
    img_dir = '/var/tmp'

    scene_path = pathify(img_dir, 'aces', img_base_filename, 0, 'exr')
    scene_img = colour.read_image(scene_path)
    colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(
        scene_img[::5, ::5, ...], "ACES",
        scatter_parameters={'c': 'black', 'marker': '+', 'alpha': 0.5},
        filename="/var/tmp/aces.png")

    r709_path = pathify(img_dir, '709', img_base_filename, 0, 'tif')
    r709_img = colour.read_image(r709_path) ** 2.4
    colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(
        r709_img[::5, ::5, ...], "ITU-R BT.709",
        scatter_parameters={'c': 'black', 'marker': '+', 'alpha': 0.5},
        filename="/var/tmp/rec709.png")

    p3d65_path = pathify(img_dir, 'p3_d65', img_base_filename, 0, 'tif')
    p3d65_img = colour.read_image(p3d65_path) ** 2.6
    colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(
        p3d65_img[::5, ::5, ...], "DCI-P3",
        scatter_parameters={'c': 'black', 'marker': '+', 'alpha': 0.5},
        filename="/var/tmp/p3d65.png")

    r2100pq_path = pathify(img_dir, '2100_PQ', img_base_filename, 0, 'tif')
    r2100pq_img = colour.models.rgb.transfer_functions.st_2084.eotf_ST2084(
        colour.read_image(r2100pq_path)) / 10000
    colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(
        r2100pq_img[::5, ::5, ...], "ITU-R BT.2020",
        scatter_parameters={'c': 'black', 'marker': '+', 'alpha': 0.5},
        filename="/var/tmp/rec2020.png")


if __name__ == '__main__':
    plot_scene_and_display_chromaticities()
