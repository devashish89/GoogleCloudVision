# +
import json
import cv2


def bounding_box_object(x,y,w,h, filepath):

    image = cv2.imread(filepath)
    


        # Using cv2.rectangle() method
        # Draw a rectangle with blue line borders of thickness of 2 px
        # image = cv2.rectangle(image, start_point, end_point, color, thickness)

    img1=cv2.rectangle(image, (int(x), int(y)), (int(x+w), int(y+h)), (255, 0, 0), 2)
    cv2.imwrite("BoundingBoxImage.jpg",img1)


if __name__=='__main__':
    bounding_box_object(285,154,255,296, 'MyFace.jpeg')



    
