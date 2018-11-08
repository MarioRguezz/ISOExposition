import unittest
from unnecessary_math import multiply

class TestUM(unittest.TestCase):

	def setUp(self):
		pass
	
	#Compara la multiplicación
	def test_numbers_3_4(self):
		self.assertEqual( multiply(3,4), 12)

	#Compara triplicar la cadena
	def test_string_a_3(self):
		self.assertEqual( multiply('a',3), 'aaa')

if __name__ == '__main__':
	unittest.main()
