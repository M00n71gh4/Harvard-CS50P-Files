import sys
from PIL import Image
from PIL import ImageOps

def main():

    if error_handling(sys.argv):
        image_handling(sys.argv)


def image_handling(argv_input):

    image_out = argv_input[2]
    image1 = Image.open(argv_input[1])
    image2 = Image.open("shirt.png")

    image1_crop = ImageOps.fit(image1, image2.size)

    new_image = Image.new("RGB", image2.size, (0,0,0))
    new_image.paste(image1_crop)
    new_image.paste(image2, box=None, mask=image2)

    new_image.save(image_out, "JPEG")
    new_image.show()




def error_handling(argv_input):
     # checks for correct number of argument
    arg_lenght = len(argv_input)

    if arg_lenght > 3:
        sys.exit("Too many command-line arguments")
    elif arg_lenght < 3:
        sys.exit("Too few command-line arguments ")

    #Checks for period
    if not "." in argv_input[1] or not "." in argv_input[2]:
        sys.exit("Not .")

    #Gets the pictures, makes it a lowercase string
    image1, image2 = argv_input[1], argv_input[2]
    image1 = str(image1).lower()
    image2 = str(image2).lower()

    #Splits on . and takes the image extension
    end_img1 = image1.split(".")[1]
    end_img2 = image2.split(".")[1]

    #Checks that the image HAS CORECT EXTENTIONS
    if not end_img1 == "jpg" and not end_img1 == "jpeg" and not end_img1 == "png":
        sys.exit("Invalid input 1")

    if not end_img2 == "jpg" and not end_img2 == "jpeg" and not end_img2 == "png":
        sys.exit("Invalid input 2")

    if not end_img1 == end_img2:
        sys.exit("Input and output have different extensions")

    return(True)





if __name__ == "__main__":
    main()