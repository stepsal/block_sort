# Block sorter class
# Take an image as in input
# should return an image.. not save it?

from color_sort_functions import get_average_color, lum, step, tester
import colorsys
from PIL import Image


class BlockSorter:
    def __init__(self, image_path, block_size=10, sort_type='avg_color', step_sort_repetitions=64,
                 color_size=2048):

        self.image = Image.open(image_path)
        self.block_size = block_size
        self.sort_type = sort_type
        self.step_sort_repetitions = step_sort_repetitions
        self.color_size = color_size
        self.sort_dict = self._populate_sort_dict()
        self.sorting_types = ['avg_color', 'avg_hls',
                              'avg_hsv', 'avg_hls',
                              'avg_lum', 'avg_step',
                              'avg_tester', 'avg_yiq']

    def _populate_sort_dict(self):
        keys_list = ['section_coordinates', 'sequence', 'avg_color',
                     'avg_hsv', 'avg_hls', 'avg_lum',
                     'avg_step', 'avg_tester', 'avg_yiq']
        sort_dict = {}
        for key in keys_list:
            sort_dict[key] = []
        x = 0
        w, h = self.image.size
        for section in self._sections(w, h, self.block_size):
            x += 1
            rsb = get_average_color(self.image.crop(section), color_size=self.color_size)
            sort_dict['section_coordinates'].append(section)
            sort_dict['sequence'].append(x)
            sort_dict['avg_color'].append(rsb)
            sort_dict['avg_hsv'].append(colorsys.rgb_to_hsv(*rsb))
            #sort_dict['avg_hls'].append(colorsys.rgb_to_hls(*rsb))
            sort_dict['avg_lum'].append(lum(*rsb))
            sort_dict['avg_step'].append(step(*rsb, self.step_sort_repetitions))
            # sort_dict['avg_tester'].append(tester(*rsb))
            # sort_dict['avg_yiq'].append(colorsys.rgb_to_yiq(*rsb))
        return sort_dict

    def _sections(self, width, height, n):
        for x in range(0, width, n):
            for y in range(0, height, n):
                if (x + n > width) or (y + n > height):
                    continue
                yield (x, y, x + n, y + n)

    def _sort_sequence(self, sorting_type):
        if sorting_type not in self.sorting_types:
            raise ValueError("{0} Is not a valid sorting type".format(sorting_type))
        sorted_seq = []
        myzip = zip(self.sort_dict[sorting_type], self.sort_dict['sequence'])
        myzip = sorted(myzip, key=lambda x: x[0])
        for x in myzip:
            sorted_seq.append(x[1] - 1)
        return sorted_seq

    def sort_image(self, sorting_type):
        sort_seq = self._sort_sequence(sorting_type=sorting_type)
        sorted_image = Image.new('RGB', self.image.size)
        sequence_iter = iter(self.sort_dict['sequence'])

        for num in sort_seq:
            section = self.image.crop(self.sort_dict['section_coordinates'][num])
            # section = section.rotate(270)
            new_image_coords = self.sort_dict['section_coordinates'][(sequence_iter.__next__()) - 1]
            sorted_image.paste(section, new_image_coords)
        return sorted_image
        # return sorted_image.rotate(90)

    def sort_image_rgb(self):
        return self.sort_image('avg_color')

    def sort_image_hls(self):
        return self.sort_image('avg_hls')

    def sort_image_hsv(self):
        return self.sort_image('avg_hsv')

    def sort_image_lum(self):
        return self.sort_image('avg_lum')

    def sort_image_step(self):
        return self.sort_image('avg_step')

    def sort_image_tester(self):
        return self.sort_image('avg_tester')

    def sort_image_yiq(self):
        return self.sort_image('avg_yiq')



























