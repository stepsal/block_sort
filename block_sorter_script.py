from blocksorter import BlockSorter
import os
import argparse
import binascii
from PIL import Image

OUTPUT_FORMAT = ".png"
image_formats = ['.jpg', '.jpeg', '.png', '.tif', '.bmp', 'gif', 'tiff']
SAVE_IMAGE = True


def get_all_images_from_the_input_dir(input_dir):
    images = []
    for file in os.listdir(input_dir):
        filepath = os.path.join(input_dir, file)
        if os.path.isfile(filepath):
            if os.path.splitext(filepath)[1].lower() in image_formats:
                img = Image.open(filepath)
                images.append(img)
    return images


def save_image(image):
    random_hash = str(binascii.b2a_hex(os.urandom(15)))[2:-1]
    output_image_name = "block_sort" + random_hash + "_" + OUTPUT_FORMAT
    output_dir = "output"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir_path = os.path.join(script_dir, output_dir)
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    image_path = os.path.join(output_dir_path, output_image_name)
    print("Image saved to {0}".format(image_path))
    image.save(image_path)


def main():
    images = get_all_images_from_the_input_dir(INPUT_DIR)
    for image in images:
        bs = BlockSorter(image, block_size=BLOCK_SIZE, step_sort_repetitions=STEP_SORT_REPETITIONS, color_size=2048)
        sorted_image = getattr(bs, "sort_image_"+SORT_TYPE)()
        sorted_image.show()
        save_image(sorted_image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Block Sorter Script')
    parser.add_argument("-b", "--blocksize", dest="BLOCK_SIZE", default=10, type=int, help="Block Size")
    parser.add_argument("-t", "--sort_type", dest="SORT_TYPE", default='step',
                        choices=['rgb', 'hsv', 'lum', 'step'],
                        help="Sort Type")
    parser.add_argument("-s", "--step_repetitions", dest="STEP_SORT_REPETITIONS", default=64, type=int,
                        help="Number of Step repetitions for avg_step sort")
    parser.add_argument("-i", "--input", dest="INPUT_DIR",
                        default="/home/stephen.salmon/Pictures/sunsets/", help="input directory")
    try:
        args = parser.parse_args()
    except:
        print("Args Error")
        parser.print_help()
        exit(2)

    if args.BLOCK_SIZE:
        BLOCK_SIZE = args.BLOCK_SIZE
    if args.SORT_TYPE:
        SORT_TYPE = args.SORT_TYPE
    if args.STEP_SORT_REPETITIONS:
        STEP_SORT_REPETITIONS = args.STEP_SORT_REPETITIONS
    if args.INPUT_DIR:
        if os.path.isdir(args.INPUT_DIR):
            INPUT_DIR = args.INPUT_DIR
        else:
            print("Not a valid input directory")
            parser.print_help()
            exit(2)
    main()