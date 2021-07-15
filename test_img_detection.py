import face_detect_alex
import unittest
import os

# Testing
image_path = os.getcwd()
test_img_1 = "/18_faces.png"
test_img_2 = "/11_bulgarian_team.png"
test_img_3 = "/4_abba.png"
eleven = 11
eighteen = 18
four = 4
class ImageFaceRecognitionTests(unittest.TestCase):

    def test_01_image_recognition(self):
        self.assertEqual((eleven, eighteen, four), (face_detect_alex.face_detect(image_path + test_img_2, eleven),
                                        face_detect_alex.face_detect(image_path + test_img_1, eighteen),
                                        face_detect_alex.face_detect(image_path + test_img_3, four)))