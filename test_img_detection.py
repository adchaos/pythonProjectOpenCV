import face_detect_alex
import unittest

# Testing
test_img_1 = "/Users/bozhiale/PycharmProjects/pythonProject/18_faces.png"
test_img_2 = "/Users/bozhiale/PycharmProjects/pythonProject/11_bulgarian_team.png"
test_img_3 = "/Users/bozhiale/PycharmProjects/pythonProject/4_abba.png"
eleven = 11
eighteen = 18
four = 4
class ImageFaceRecognitionTests(unittest.TestCase):

    def test_01_image_recognition(self):
        self.assertEqual((eleven, eighteen, four), (face_detect_alex.face_detect(test_img_2, eleven),
                                        face_detect_alex.face_detect(test_img_1, eighteen),
                                        face_detect_alex.face_detect(test_img_3, four)))