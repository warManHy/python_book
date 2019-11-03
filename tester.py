# coding: utf-8
import unittest

def get_formatted_name(first_name, last_name):
    full_name = first_name + last_name
    return full_name.title()

def test():
    print "Enter 'q' any time to quit"
    while True:
        first_name = raw_input("Enter input u first_name\n")
        if first_name == 'q':
            break
        last_name = raw_input("Enter input u last_name\n")
        if last_name == 'q':
            break
        formatted_name = get_formatted_name(first_name, last_name)
        print "formatted_name is " + formatted_name
        # break

class NameTestCase(unittest.TestCase):
    """ 测试name """
    def test_name(self):
        formatted_name = get_formatted_name("jack", "frost")
        self.assertEqual(formatted_name, "Jackfrost")

unittest.main()
