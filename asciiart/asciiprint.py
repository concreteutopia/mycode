#!/usr/bin/env python3

import PIL.Image, time
from crayon import *
from subprocess import call
from os import name as osname


#ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

ASCII_CHARS = ["@","%","#","*","+","=","-",":",";","."]

def clear():
    # check and make call for specific operating system
    call('clear' if osname =='posix' else 'cls')

def resize(image, new_width = 80):
    width, height = image.size
    #print(f"{width} x {height}")
    #width_percent = new_width/float(width)
    #new_height = int(float(height)*float(width_percent))
    new_height = new_width * height / width
    #print(f"{new_width} x {new_height}")
    return image.resize((int(new_width), int(new_height)))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    ascii_str_ch=""
    for pixel in pixels:
        #ascii_str_ch += ASCII_CHARS[pixel//25];
        ascii_str += str(pixel//23)
    return ascii_str

def main():
    path = input("Enter the path to the image: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")
    #resize image
    image = resize(image);
    #convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    
    ascii_str_len = len(ascii_str)
    ascii_img=""
    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    #color_config = {'fg':5, 'bg':0}
    #printout(ascii_img, color=color_config)
    clear() 
    for x in range(0,len(ascii_img)):
        if ascii_img[x] != '\n':
            my_grayscale_color = gray(int(ascii_img[x]))
            color_config = {'fg':my_grayscale_color, 'bg':0}

            #printout(ascii_img[x], color=color_config, end='')
            printout("\u2589", color=color_config, end='')
            
        else:
            print(ascii_img[x],end='')
            #time.sleep(0.075)

    #with open("ascii_image.txt", "w") as f:
    #    f.write(ascii_img);
main()
