
import cv2

for i in range(1,13):
	img = cv2.imread(str(i)+'.jpg')
	img_re = cv2.resize(img,(201,131))
	cv2.imwrite(str(i)+'.jpg',img_re)
      
