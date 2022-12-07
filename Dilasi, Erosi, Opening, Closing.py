
import cv2
img = cv2.imread('red.png')

def main():
    erosi = cv2.erode(img,kernel,iterations = 1)
    dilasi = cv2.dilate(erosi,kernel,iterations = 1)
    opening = cv2.morphologyEx(dilasi, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    options()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def options():
    show_morf = input("Masukkan metode Morfologi:\n 1. Erosi\n 2. Dilasi\n 3. Opening\n 4. Closing\n 5. Original \n 6. Semua")
    if show_morf == 1:
        cv2.imshow('erosi', erosi)
    elif show_morf == 2:
        cv2.imshow('dilasi', dilasi)
    elif show_morf == 3:
        cv2.imshow('opening', opening)
    elif show_morf == 4:
        cv2.imshow('closing', closing)
    elif show_morf == 5:
        cv2.imshow('original', img)
    elif show_morf == 6:
        cv2.imshow('original', img)
        cv2.imshow('erosi', erosi)
        cv2.imshow('dilasi', dilasi)
        cv2.imshow('opening', opening)
        cv2.imshow('closing', closing)
    else:
        print("Error")
        options()

main()

#referensi
#https://www.ivanjul.com/dilation-pelebaran-dengan-opencv-python/   
#https://www.youtube.com/watch?v=DUq7IPLi8TA&t=511s
#https://github.com/jjone36/vision_4_beginners