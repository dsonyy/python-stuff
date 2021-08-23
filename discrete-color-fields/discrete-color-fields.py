import random
import sys

W = 1000
H = 1000

SVG_BEGIN = '<?xml version="1.0"?>\n \
<svg xmlns="http://www.w3.org/2000/svg" \
xmlns:xlink="http://www.w3.org/1999/xlink"  \
width="' + str(W) + '" height="' + str(H) + '">\n'

SVG_BACKGROUND = '<rect width="' + str(W) + '" height="' + \
    str(H) + '" style="fill:rgb(0,0,255)" />\n'

SVG_END = '</svg>\n'


def get_random_color():
    return "rgb(" + str(random.randrange(0, 256)) + \
        "," + str(random.randrange(0, 256)) + \
        "," + str(random.randrange(0, 256)) + ")"


def get_gray_color():
    c = str(random.randrange(0, 256))
    return "rgb(" + c + "," + c + "," + c + ")"


"""
lev rects   total       range
0   1       1           (1-1):1     0:1
1   2       3           (3-2):3     1:3
2   4       7           (7-4):7     3:7
3   8       15          (15-8):15   7:15
4   16      31          (31-16):31  15:31
i   2**i    2**(i+1)-1  (2**i-1):(2**(i+1)-1)
"""


def split_rects(rects):
    splitted_rects = []
    for parent in rects:
        a = random.choice(("vertical", "horizontal"))
        try:
            if a == "vertical":
                b = random.randrange(parent[0], parent[1])
                rect0 = (parent[0], b, parent[2], parent[3])
                rect1 = (b, parent[1], parent[2], parent[3])
            else:
                b = random.randrange(parent[2], parent[3])
                rect0 = (parent[0], parent[1], parent[2], b)
                rect1 = (parent[0], parent[1], b, parent[3])
            splitted_rects.extend((rect0, rect1))
        except ValueError:
            continue
    return splitted_rects


def gen_rects(lev):
    rects = [(0, W, 0, H)]
    for i in range(lev):
        rects = split_rects(rects)
    return rects


def gen_svg(rects):
    svg = SVG_BEGIN
    svg += SVG_BACKGROUND

    for rect in rects:
        svg += '<rect ' + \
            'x="' + str(rect[0]) + '" ' + \
            'y="' + str(rect[2]) + '" ' + \
            'width="' + str(rect[1] - rect[0]) + '" ' + \
            'height="' + str(rect[3] - rect[2]) + '" ' + \
            'style="fill:' + get_gray_color() + '" />\n'

    svg += SVG_END
    return svg


def save(svg, name):
    with open(name, "w") as f:
        f.write(svg)


def main():
    lev = 10
    if len(sys.argv) > 1:
        lev = int(sys.argv[1])

    rects = gen_rects(lev)
    print("X0", "X1", "Y0", "Y1", sep="\t")
    for rect in rects:
        print(*rect, sep="\t")
    svg = gen_svg(rects)
    save(svg, "output.svg")


if __name__ == "__main__":
    main()
