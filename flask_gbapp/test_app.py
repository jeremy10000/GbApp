import unittest

from scripts.parser import Parser

class TestParser(unittest.TestCase):

	def test_parser(self):
		parser = Parser()
		question = "Ou est le musée du louvre ?"
		result = parser.extract(question)

		self.assertEqual(result, "musée louvre ")


if __name__ == '__main__':
    unittest.main()
