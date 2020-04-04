import imageio
from numpy import array

CONFIG = {}

def config():
    try:
        cfg = open("config.cfg")
    except:
        print("Cannot find config.cfg!")
        return False
    
    print("config.cfg loaded:")
    
    try:
        print("---------------------")
        print(" R   G   B   ->  CHR")  
        print("---------------------")
        for line in cfg:
            line = line.split()
            print(line[0].zfill(3) + " " + line[1].zfill(3) + " " + line[2].zfill(3) + "       " + line[3])
            CONFIG[(int(line[0]), int(line[1]), int(line[2]))] = line[3]
    except:
        print("An error occured while processing config.cfg!")
        return False
        
    print("")
    return True

def levedit():
    in_path = input("Enter filename: imgs/")
    out_path = "levs/" + in_path.split(".")[0] + ".lev"
    in_path = "imgs/" + in_path
    
    try:
        img = imageio.imread(in_path)
    except:
        print("An error occured while opening input file!")
        return

    output = open(out_path, "w")

    h, w, _ = img.shape

    lev = []
    print("+" * (w+2))
    for y in range(h):
        p = ""
        for x in range(w):
            try:
                p += CONFIG[(img[y, x][0], img[y, x][1], img[y, x][2])]
            except:
                p += " "
        print("+" + p + "+")
        lev.append(p)
        output.write(p + "\n")
    print("+" * (w+2))
    print("Size: " + str(w) + "x" + str(h))
        

def main():
    cfg = config()
    if not cfg:
        return

    while True:
        levedit()
        choice = input("\nOnce again? [Y/N]: ")
        if choice == "Y" or choice == "y":
            continue
        break

main()