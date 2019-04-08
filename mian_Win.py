import gi
import cv2
import gtk
import numpy as np 
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from PIL import Image
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):


    def __init__(self):

        Gtk.Window.__init__(self, title="Image Forgery Tool")
        #self.set_default_size(150, 100)
        #self.set_border_width(20)
        self.box = Gtk.Box(spacing=5)
        self.add(self.box)

        #image_favicon = Gtk.Image()
        #image_favicon.set_from_file("forensics-icon.png")
        #self.add(image_favicon)
        
    # for button 1
        self.button1 = Gtk.Button(label="Image1")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, False, False, 10)
    # for button 2
        self.button2 = Gtk.Button(label="Image2")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, False, False, 10)
    # for button 3
        self.button3 = Gtk.Button(label="Result")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.button3, False, False, 10)
    # for button 4
        self.button4 = Gtk.Button("Help")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.box.pack_start(self.button4, False, False, 10)


    def on_button1_clicked(self, widget):
        print("Upload Image1")
        #self.set_default_size(10, 50)
        img1 = cv2.imread("/home/luke/Desktop/MohitSir/modified_03.png")
        cv2.imshow('image',img1)
    def on_button2_clicked(self, widget):
        print("Upload Image2")
        img2 = cv2.imread("/home/luke/Desktop/MohitSir/original_03.png")
        cv2.imshow('image',img2)
    def on_button3_clicked(self,widget):
        img1 = cv2.imread("/home/luke/Desktop/MohitSir/modified_03.png")
        img2 = cv2.imread("/home/luke/Desktop/MohitSir/original_03.png")
        diff= cv2.subtract(img1,img2)
        # if difference is all zeros it will return false
        result = not np.any(diff) 
        if result is True:
            print("The image are the same")
        else:
            img3 = cv2.imwrite("/home/luke/Desktop/MohitSir/result.png",diff)
            img4 = cv2.imread("/home/luke/Desktop/MohitSir/result.png")
            print("the image are different")
            cv2.imshow('image',img4)
        
    def on_button4_clicked(self, widget):
        print("Gtk Application which checks the image is forged or not and gitve autput as a forged part in the image!!!!")
        
        

        
cv2.waitKey(3000)
cv2.destroyAllWindows()
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
