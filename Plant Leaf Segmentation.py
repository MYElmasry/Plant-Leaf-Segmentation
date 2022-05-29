import cv2
import numpy as np
from imutils import paths
from sklearn.metrics import jaccard_score
imagePaths = list(paths.list_images("D:\Digital Image Processing\_Output\_Output"))
outputPaths = list(paths.list_images("D:\Digital Image Processing\_Ground_Truth\_GroundTruth"))
sum = 0
for i in range(len(imagePaths)):
    BGR_image = cv2.imread(imagePaths[i], 1)

    median = cv2.medianBlur(BGR_image,11)
    gaussian_blur = cv2.GaussianBlur(src=median, ksize=(5,5), sigmaX=5, sigmaY=5)
    sharpen_filter = np.array([[-1,-1,-1], 
                           [-1, 9,-1],
                           [-1,-1,-1]])
    sharped_img = cv2.filter2D(gaussian_blur, -1, sharpen_filter)


    norm_img2 = cv2.normalize(sharped_img, None, alpha=0, beta=1.2, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)


    norm_img2 = np.clip(norm_img2, 0, 1)
    norm_img2 = (255*norm_img2).astype(np.uint8)

    lower = [0, 135, 0]
    upper = [255, 255, 255]
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(norm_img2, lower, upper)
    output = cv2.bitwise_and(norm_img2, norm_img2, mask = mask)

    img_gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    thresh = 100
    maxValue = 255 
    th, dst = cv2.threshold(img_gray, thresh, maxValue, cv2.THRESH_BINARY)
    dilated= cv2.dilate(dst.copy(),None, iterations=2)
    # cv2.imshow('dilated', dilated)
    (T, threshInv) = cv2.threshold(dilated, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    closing = cv2.morphologyEx(threshInv, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    # cv2.imshow('opening', opening)
    
    # cv2.imshow('original',BGR_image)
    # cv2.imshow('normalized2',norm_img2)
    # cv2.imshow('masked',output)
    imgture = np.array(cv2.imread(outputPaths[i],0)).ravel()
    imgpred = np.array(opening).ravel()
    sum += jaccard_score(imgture,imgpred,average='weighted')
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
print("The overall segmentation accuracy=", (sum/len(imagePaths))*100,'%')