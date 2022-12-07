import numpy as np 
import cv2 
from matplotlib import pyplot as plt 

def main():
    gambar = input("Masukkan Nama File dan Ekstensinya: ")
    noiseRemover(gambar)

def noiseRemover(x):
    image = cv2.imread(x,1) 

    image_greyscale = cv2.imread(x,0)

    noiseless_image_greyscale = cv2.fastNlMeansDenoising(image_greyscale, None, 20, 7, 21) 

    noiseless_image = cv2.fastNlMeansDenoisingColored(image,None,20,20,7,21) 

    titles = ['Gambar Asli','Gambar setelah Noise Dihilangkan', 'Gambar Asli (grayscale)','Gambar setelah Noise Dihilangkan (grayscale)']
    images = [image,noiseless_image, image_greyscale, noiseless_image_greyscale]
    plt.figure(figsize=(13,5))
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.tight_layout()
    plt.show()

main()

#referensi
#https://www.youtube.com/watch?v=Czdo4VWJNAM