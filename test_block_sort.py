from blocksorter import BlockSorter
import random
import os

input_image = '/home/stephen.salmon/Pictures/drr.jpg'
output_path = '/home/stephen.salmon/Pictures/blocksort/output'
input_filename = input_image.split('/')[-1].split('.')[0]
script_name = __file__.split('/')[-1].split('.')[0]
output_filename = input_filename + "_" + script_name + "_" + str(random.randint(0,100000)) + ".png"
output_filepath  = os.path.join(output_path, output_filename)

bs = BlockSorter(input_image, block_size=20, step_sort_repetitions=40, color_size=2048)
x = bs.sort_image_step()
x.rotate(180)
x.save(output_filepath)
x.show()





