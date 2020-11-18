from cv2 import *
import numpy as np
#Read Image
path = str(os.getcwd()) #Obtiene la ruta relativa en la computadora de trabajo actual
img = cv2.imread('img/test_sky.jpeg')
#Display Image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Applying Grayscale filter to image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Saving filtered image to new file
cv2.imwrite('graytest.jpeg',gray)