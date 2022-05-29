# Plant-Leaf-Segmentation
A program for the automated segmentation of plant leaves.
The program’s input is a plant leaf image, and the output should consist of a binary image with only the plant leaf object.

##Step 1:
The program starts by importing required libraries such as cv2, numpy, sklearn and imutils.
### Original Image:
![Original Image](https://gcdnb.pbrd.co/images/o4tZyt5HIIIX.png?o=1)

##Step 2:
Remove the salt and pepper noise and apply filters to sharp the image.
### Remove Noise:
![Clean Image](https://gcdnb.pbrd.co/images/5xkV20yVERKT.png?o=1)

##Step 3:
Make normalization to the contrast of the image if it’s either too dark or too bright.
### Normalized image:
![Normalized Image](https://gcdnb.pbrd.co/images/MGXlluBseRDW.png?o=1)

##Step 4:
Create a mask for the colour boundaries for the desired object to be extracted (‘Green’ in our case) and apply it on the desired image.
### Masked image:
![Masked Image](https://gcdnb.pbrd.co/images/VCWFrvj1ooVa.png?o=1)

##Step 5:
After applying the colour mask, I change the image into a binary image, using a certain threshold (1 if intensity is higher than 100 and black otherwise).
### Binary image:
![Binary Image](https://gcdnb.pbrd.co/images/aC5RmacGS1Dq.png?o=1)

##Step 6:
Then, I used Morphological operation to apply a structuring element to an input image.
### Output image:
![Output Image](https://gcdnb.pbrd.co/images/uc4dkqgKoMqU.jpg?o=1)
