from __future__ import print_function
import cv2
import numpy as np
import argparse
import random as rng
rng.seed(12345)


#main
def main():
    conveks = input("Masukkan metode:\n 1. Sifat Bundar\n 2. Convex Hull\n 3. Momen Jarak ke Pusat")
    if conveks == 1:
        bundar()
    elif conveks == 2:
        convexHull()
    elif conveks == 3:
        momen()
    else:
        print("Error")
        main()

#Sifat Bundar
def bundar():
    [px, py] = centroid(BW);
    
    [m, n] = size(BW);
    Kontur = inbound_tracing(BW);
    
    jum =length(Kontur);
    
    total = 0;
    for i in jum:
        i = 1
        total =  total + sqrt( (Kontur(i,1)-py)^2 + (Kontur(i,2)-px)^2);

    mu = total / jum;

    total = 0;
    
    for i in jum:
        i = 1
        total =  total + (sqrt( (Kontur(i,1)-py)^2 + (Kontur(i,2)-px)^2) - mu) ^ 2;
    
    sigma = total / jum;
    
    #hasil
    c = mu / sigma;

#Convex hull
def convexHull():
    def thresh_callback(val):
        threshold = val

        canny_output = cv2.Canny(src_gray, threshold, threshold * 2)

        contours, _ = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        hull_list = []
        for i in range(len(contours)):
            hull = cv2.convexHull(contours[i])
            hull_list.append(hull)

        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        for i in range(len(contours)):
            color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
            cv2.drawContours(drawing, contours, i, color)
            cv2.drawContours(drawing, hull_list, i, color)

        cv2.imshow('Contours', drawing)

    parser = argparse.ArgumentParser(description='Code for Convex Hull tutorial.')
    parser.add_argument('--input', help='Path to input image.', default='bung-A.jpg')
    args = parser.parse_args()
    src = cv2.imread(cv2.samples.findFile(args.input))
    if src is None:
        print('Could not open or find the image:', args.input)
        exit(0)

    src_gray = cv2.cv2tColor(src, cv2.COLOR_BGR2GRAY)
    src_gray = cv2.blur(src_gray, (3,3))

    source_window = 'Source'
    cv2.namedWindow(source_window)
    cv2.imshow(source_window, src)
    max_thresh = 255
    thresh = 100 # treshold awal
    cv2.createTrackbar('Canny thresh:', source_window, thresh, max_thresh, thresh_callback)
    thresh_callback(thresh)
    cv2.waitKey()

#Momen jarak ke pusat
def momen():
    Fitur.F1 = sqrt(momen_pusat_ke_p(F, 2)) / momen_ke_p(F, 1);
    Fitur.F2 = momen_pusat_ke_p(F, 3) / (momen_ke_p(F, 2)^1.5);
    Fitur.F3 = momen_pusat_ke_p(F, 4) / (momen_ke_p(F, 2)^2);
    
    Fitur.F2a = momen_pusat_ke_p(F, 3)^(1/3) / momen_ke_p(F, 1);
    Fitur.F3a = momen_pusat_ke_p(F, 4)^(1/4) / momen_ke_p(F, 1);
    
    Fitur.mf = Fitur.F3a - Fitur.F1;
    
    function [momen] = momen_pusat_ke_p(F, p)
    
    momen_p = momen_ke_p(F, p);
    momen_1 = momen_ke_p(F, 1);
    
    Kontur = inbound_tracing(F);
    
    [m, n] = size(F);
    [xp, yp] = centroid(F);
    jum = length(Kontur);
    
    momen = 0;
    for i in jum:
        i=1
        jarak = sqrt((Kontur(i,2)-xp)^2 + (Kontur(i,1)-yp)^2);
        
        momen = momen + abs(jarak - momen_1) ^ p;
    
    momen = momen / jum;

    function [momen] = momen_ke_p(F, p)
    
    Kontur = inbound_tracing(F);
    [m, n] = size(F);
    [xp, yp] = centroid(F);
    jum = length(Kontur);

    momen = 0;
    for i in jum:
        jarak = sqrt((Kontur(i,2)-xp)^2 + (Kontur(i,1)-yp)^2);

        momen = momen + jarak ^ p;
    
    momen = momen / jum;

main()
#referensi
#https://www.researchgate.net/publication/358220979_Pengolahan_Citra_Digital_Menggunakan_Python
#https://www.researchgate.net/profile/Abdul-Kadir-14/publication/236673073_Teori_dan_Aplikasi_Pengolahan_Citra/links/00b49518db5b7608fd000000/Teori-dan-Aplikasi-Pengolahan-Citra.pdf
#https://www.youtube.com/watch?v=W7YKrMynXpE