import face_detect_alex
import unittest
import pytest

# Testing
test_img_1 = "/Users/bozhiale/PycharmProjects/pythonProject/18_faces.png"
test_img_2 = "/Users/bozhiale/PycharmProjects/pythonProject/11_bulgarian_team.png"
test_img_3 = "/Users/bozhiale/PycharmProjects/pythonProject/4_abba.png"

class ImageFaceRecognitionTests(unittest.TestCase):

    def test_01_image_recognition(self):
        self.assertEqual((11, 18, 4), (face_detect_alex.face_detect(test_img_2),
                                        face_detect_alex.face_detect(test_img_1),
                                        face_detect_alex.face_detect(test_img_3)))

    # def test_02_image(self):
    #     self.assertIsNone(face_detect_alex.face_detect(test_img_4))

    # @pytest.mark.parametrize("param, pics", [(11, test_img_2), (18, test_img_1), (4, test_img_3)])
    # @pytest.mark.parametrize("param", [11, 18, 4], "pics", [test_img_2, test_img_1, test_img_3])
    # def test_is_negative(self, param, pics):
    #     self.assertEqual((param), (face_detect_alex.face_detect(pics)))