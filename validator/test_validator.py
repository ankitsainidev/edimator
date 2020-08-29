import unittest
from . import validate

class ValidatTest(unittest.TestCase):
	def test_content_validity(self):
		content = [{
			"timestamp": 1.0,
			"cursor_position": (3, 7),
			"buffer": "Hello Everyone",
			"visual_selection": [(3, 2)]
		}]
		self.assertTrue(validate.is_valid_content(content))
	
class InvalidTest(unittest.TestCase):
	def test_invalid_keyword(self):
		content = [{
			"timestamp": 1.0,
			"cursor_position": (3, 7),
			"not_valid": "Hello Everyone",
			"visual_selection": [(3, 2)]
		}]
		self.assertFalse(validate.is_valid_content(content))

	def test_invalid_type(self):
		content = [{
			"timestamp": 1.0,
			"cursor_position": (3, 7),
			"buffer": "Hello Everyone",
			"visual_selection": [(3, 2.7)]
		}]
		self.assertFalse(validate.is_valid_content(content))

if __name__ == "__main__":
	unittest.main()