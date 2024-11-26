from PIL import Image,ImageOps
import sys
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
else:
    ext1=sys.argv[1].strip()
    ext2=sys.argv[2].strip()
    ext1=ext1.split('.')
    ext2=ext2.split('.')
    if ext2[1] not in ["jpg","jpeg","png"] :
        sys.exit("Invalid output")
    if ext1[1]!=ext2[1]:
        sys.exit("Input and output have different extensions")
    img=Image.open("shirt.png")
    try:
        image=Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    size=img.size
    temp=ImageOps.fit(image,size)
    temp.paste(img,img)
    temp.save(sys.argv[2])