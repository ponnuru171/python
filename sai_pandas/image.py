import numpy as np                            #image programs cannot run im pycharm it run in jupyter notes
from skimage import io
import matplotlib.pyplot as plt
p=io.imread('taj.jpg')
print(plt.imshow(p))                        #this command prints the image
print(p.shape)                              #this command  print the dimensitions of the image
print(plt.imshow(p[::-1]))                  #this command reverse the image
print(plt.imshow(p[0:138,200:350]))         #this command zoom the image
print(plt.imshow(p[:,::,1]))                #this command changes the color to green color
print(plt.imshow(p[::20,::20]))             #this command blur the image
print(plt.imshow(p[::2]))                   #this command compress image in horizontal
print(plt.imshow(p[:,400,::]))              #this command zoom in horizontal only
print(p.size)                               #this comment print the size of the diagram
