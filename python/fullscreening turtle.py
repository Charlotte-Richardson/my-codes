#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Charlotte
#
# Created:     30/03/2019
# Copyright:   (c) Charlotte 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tkinter
import turtle

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()

print(width,height)

turtle.setup(width,height)
