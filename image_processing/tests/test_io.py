import unittest
from image_processing.utils.io import load_image, save_image

class TestIO(unittest.TestCase):
    def test_load_image(self):
        image = load_image('tests/test_image.jpg')
        self.assertIsNotNone(image)

    def test_save_image(self):
        image = load_image('tests/test_image.jpg')
        result = save_image(image, 'tests/test_image_saved.jpg')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()