#!/usr/bin/python3.7
import cv2
import os


def face_detect(image, index=None):
    #FIXME put image_path for the input of the method and delete assigment
    image_path = image
    casc_path = os.getcwd() + "/haarcascade_frontalface_default.xml"

    # Create the haar cascade
    face_cascade = cv2.CascadeClassifier(casc_path)

    # Read the image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(5, 5),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print("Found {0} faces!".format(len(faces)))
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Possible fixes:
    # save the picture for further visual verifications
    new_image_path = f"./Output_image_{index}.png"
    cv2.imwrite(filename=new_image_path, img=image)

    # show the picture and wait for user interaction
    cv2.imshow("window_name", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return len(faces)