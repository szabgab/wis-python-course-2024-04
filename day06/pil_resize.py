# pip install pillow

import argparse
from PIL import Image

# Resize, tried on jpg => jpg

parser = argparse.ArgumentParser()
parser.add_argument('--inf', help='Input filename', required=True)
parser.add_argument('--out', help='Output filename', required=True)
parser.add_argument('--size', help='Size in percentage (100 = keep it the same)', required=False, type=float)
parser.add_argument('--width', help='Width in pixels', required=False, type=float)
args = parser.parse_args()
#print(args.inf)

if ((not args.size and not args.width) or (args.size and args.width)):
    exit("Need either --size or --width but not both")

im = Image.open(args.inf)
print(im.format, im.size, im.mode)
if args.width:
    size = 100 * args.width / im.size[0]
else:
    size = args.size

#print(size)
#exit()
width = int(size * im.size[0] / 100)
height = int(size * im.size[1] / 100)

out = im.resize((width, height))
out.save(args.out)

