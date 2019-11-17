import unittest

class Sample_class(unittest.TestCase):

    def test1(self):
        self.assertEqual(3+5,8)

    def test2(self):
        self.assertNotEqual('a'*4,'aaa')

    def test3(self):
        self.assertTrue('FOO'.isupper())

    def test4(self):
        self.assertFalse('foo'.isupper())

    def test5(self):
        self.assertIn(3,[4,5,6,3])

    def test6(self):
        self.assertNotIn(3,[2,4])

    def test7(self):
        self.assertIs(5,5)

    def test8(self):
        self.assertIsNot(8+9,18)

    def test9(self):
        self.assertIsNone(None)

    def test10(self):
        self.assertIsNotNone(13)

if __name__=='__main__':
    unittest.main()