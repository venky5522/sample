import unittest
from employee import Employee
class TestEmloyee(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.emp_1 = Employee('corey', 'schafer', 50000)
        self.emp_2 = Employee('sue', 'smith', 60000)
    def tearDown(self):
        print('tearDown\n')
    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email,'corey.schafer@email.com')
        self.assertEqual(self.emp_2.email,'sue.smith@email.com')
        self.emp_1.first = 'john'
        self.emp_2.first = 'jane'
        self.assertEqual(self.emp_1.email,'john.schafer@email.com')
        self.assertEqual(self.emp_2.email,'jane.smith@email.com')
    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname,'corey schafer')
        self.assertEqual(self.emp_2.fullname,'sue smith')
        self.emp_1.first = 'john'
        self.emp_2.first = 'jane'
        self.assertEqual(self.emp_1.fullname,'john schafer')
        self.assertEqual(self.emp_2.fullname,'jane smith')
    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
if __name__=='__main__':
    unittest.main()



