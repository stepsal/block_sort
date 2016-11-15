# block_sort
Block sorting script written in Python.
Image is divived up into blocks which are then color sorted in either of 4 ways (rgb, hsv, lum, step)
The block_sort_script.py will sort all images in the input directory and spit the results into a output
directory under the script folder.

## Usage

```
Block Sorter Script

optional arguments:
  -h, --help            show this help message and exit
  -b BLOCK_SIZE, --blocksize BLOCK_SIZE
                        Block Size
  -t {rgb,hsv,lum,step}, --sort_type {rgb,hsv,lum,step}
                        Sort Type
  -s STEP_SORT_REPETITIONS, --step_repetitions STEP_SORT_REPETITIONS
                        Number of Step repetitions for avg_step sort
  -i INPUT_DIR, --input INPUT_DIR
                        input directory
```
