#!/usr/bin/python3
"""
Unittest for the Base class
"""
import unittest
import pep8
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import path, remove


class TestBase(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Sets the private class attribute __nb_objects back to 0
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
#        print("setUp")
        Base._Base__nb_objects = 0
#        Base.__nb_objects = 0
#        self.__nb_objects = 0

    def tearDown(self):
        """
        Sets the private class attribute __nb_objects back to 0
        Method called immediately after the test method has been called and
        the result recorded
        """
#        print("tearDown")
        del Base._Base__nb_objects
#        del Base.__nb_objects
#        del self.__nb_objects
        if path.exists("Rectangle.json"):
            remove("Rectangle.json")
        if path.exists("Square.json"):
            remove("Square.json")
        if path.exists("Base.json"):
            remove("Base.json")
        if path.exists("Rectangle.csv"):
            remove("Rectangle.csv")
        if path.exists("Square.csv"):
            remove("Square.csv")
        if path.exists("Base.csv"):
            remove("Base.csv")
        """This try and except structure also works:"""
        # try:
        #     remove("Rectangle.json")
        # except IOError:
        #     pass
        # try:
        #     remove("Square.json")
        # except IOError:
        #     pass
        # try:
        #     remove("Base.json")
        # except IOError:
        #     pass
        # try:
        #     remove("Rectangle.csv")
        # except IOError:
        #     pass
        # try:
        #     remove("Square.csv")
        # except IOError:
        #     pass
        # try:
        #     remove("Base.csv")
        # except IOError:
        #     pass

    def test_pep8_conformance(self):
        """Test that Base conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_attribute_presence(self):
        """Test that __nb_objects is present"""
        l1 = dir(Base)
        self.assertIn('_Base__nb_objects', l1)

    def test_class_attribute(self):
        """Test that the private class attribute __nb_objects is set to 0"""
#        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_class_method_presence(self):
        """Test that the Base methods are all present"""
        l1 = dir(Base)
        self.assertIn('__init__', l1)
        self.assertIn('create', l1)
        self.assertIn('from_json_string', l1)
        self.assertIn('load_from_file', l1)
        self.assertIn('load_from_file_csv', l1)
        self.assertIn('save_to_file', l1)
        self.assertIn('save_to_file_csv', l1)
        self.assertIn('to_json_string', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(base.__doc__, None)
        self.assertIsNot(Base.__init__.__doc__, None)
        self.assertIsNot(Base.create.__doc__, None)
        self.assertIsNot(Base.from_json_string.__doc__, None)
        self.assertIsNot(Base.load_from_file.__doc__, None)
        self.assertIsNot(Base.load_from_file_csv.__doc__, None)
        self.assertIsNot(Base.save_to_file.__doc__, None)
        self.assertIsNot(Base.save_to_file_csv.__doc__, None)
        self.assertIsNot(Base.to_json_string.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation with various parameter values"""

        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertEqual(b1.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

        b2 = Base(1)
        self.assertIsInstance(b2, Base)
        self.assertEqual(b2.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

        b3 = Base(-1)
        self.assertIsInstance(b3, Base)
        self.assertEqual(b3.id, -1)
        self.assertEqual(Base._Base__nb_objects, 1)

        b4 = Base(1.5)
        self.assertIsInstance(b4, Base)
        self.assertEqual(b4.id, 1.5)
        self.assertEqual(Base._Base__nb_objects, 1)

        b5 = Base(float('inf'))
        self.assertIsInstance(b5, Base)
        self.assertEqual(b5.id, float('inf'))
        self.assertEqual(Base._Base__nb_objects, 1)

        b6 = Base(float('nan'))
        self.assertIsInstance(b6, Base)
        self.assertNotEqual(b6.id, float('nan'))
        self.assertEqual(Base._Base__nb_objects, 1)

        b7 = Base("String")
        self.assertIsInstance(b7, Base)
        self.assertEqual(b7.id, "String")
        self.assertEqual(Base._Base__nb_objects, 1)

        b8 = Base(['a', 2])
        self.assertIsInstance(b8, Base)
        self.assertEqual(b8.id, ['a', 2])
        self.assertEqual(Base._Base__nb_objects, 1)

        b9 = Base(('a', 2))
        self.assertIsInstance(b9, Base)
        self.assertEqual(b9.id, ('a', 2))
        self.assertEqual(Base._Base__nb_objects, 1)

        b10 = Base({'a', 2})
        self.assertIsInstance(b10, Base)
        self.assertEqual(b10.id, {'a', 2})
        self.assertEqual(Base._Base__nb_objects, 1)

        b11 = Base({1: 'a', 2: 'b'})
        self.assertIsInstance(b11, Base)
        self.assertEqual(b11.id, {1: 'a', 2: 'b'})
        self.assertEqual(Base._Base__nb_objects, 1)

        b12 = Base(None)
        self.assertIsInstance(b12, Base)
        self.assertEqual(b12.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

        b13 = Base(None)
        self.assertIsInstance(b13, Base)
        self.assertEqual(b13.id, 3)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_to_json_string(self):
        """Test to_json_string method"""

        l1 = None
        l2 = []
        l3 = [1, 2]
        l4 = [(1, 2)]
        l5 = [[1, 2]]
        l6 = [{1, 2}]
        l7 = [{}]
        # l8 = [{'a': 1, 'b': 2}]
        l8 = [{'a': 1}]
        # l9 = [{'a': 'c', 'b': 'd'}]
        l9 = [{'a': 'c'}]
        # l10 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
        l11 = "string"
        l12 = 1234
        self.assertEqual(Base.to_json_string(l1), '[]')
        self.assertEqual(Base.to_json_string(l2), '[]')
        self.assertEqual(Base.to_json_string(l3), '[1, 2]')
        self.assertEqual(Base.to_json_string(l4), '[[1, 2]]')
        self.assertEqual(Base.to_json_string(l5), '[[1, 2]]')
        with self.assertRaises(TypeError):
            Base.to_json_string(l6)
        # self.assertEqual(Base.to_json_string(l6), '[{1, 2}]')
        self.assertEqual(Base.to_json_string(l7), '[{}]')
        # self.assertEqual(Base.to_json_string(l8), '[{"a": 1, "b": 2}]')
        self.assertEqual(Base.to_json_string(l8), '[{"a": 1}]')
        # self.assertEqual(Base.to_json_string(l9), '[{"a": "c", "b": "d"}]')
        self.assertEqual(Base.to_json_string(l9), '[{"a": "c"}]')
        # self.assertEqual(Base.to_json_string(l10),
        # '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]')
        self.assertEqual(Base.to_json_string(l11), '"string"')
        with self.assertRaises(TypeError):
            Base.to_json_string(l12)

    def test_save_to_file(self):
        """Test save_to_file method"""

        with self.assertRaises(AttributeError):
            b1 = Base(1)
            Base.save_to_file([b1])
            self.assertTrue(path.isfile('Base.json'))

        r1 = Rectangle(3, 5, 2, 4, 1)
        Rectangle.save_to_file([r1])
        self.assertTrue(path.isfile('Rectangle.json'))

        r2 = Rectangle(3, 5, 2, 4)
        Rectangle.save_to_file([r2])
        self.assertTrue(path.isfile('Rectangle.json'))

        r3 = Rectangle(3, 5)
        Rectangle.save_to_file([r3])
        self.assertTrue(path.isfile('Rectangle.json'))

        Rectangle.save_to_file(None)
        self.assertTrue(path.isfile('Rectangle.json'))
        with open('Rectangle.json') as f:
            self.assertEqual(f.read(), '[]')

        Rectangle.save_to_file([])
        self.assertTrue(path.isfile('Rectangle.json'))
        with open('Rectangle.json') as f:
            self.assertEqual(f.read(), '[]')

        s1 = Square(3, 2, 4, 1)
        Square.save_to_file([s1])
        self.assertTrue(path.isfile('Square.json'))

        s2 = Square(3, 2, 4)
        Square.save_to_file([s2])
        self.assertTrue(path.isfile('Square.json'))

        s3 = Square(3)
        Square.save_to_file([s3])
        self.assertTrue(path.isfile('Square.json'))

        Square.save_to_file(None)
        self.assertTrue(path.isfile('Square.json'))
        with open('Square.json') as f:
            self.assertEqual(f.read(), '[]')

        Square.save_to_file([])
        self.assertTrue(path.isfile('Square.json'))
        with open('Square.json') as f:
            self.assertEqual(f.read(), '[]')

    def test_from_json_string(self):
        """Test from_json_string method"""

        l1 = None
        l2 = []
        l3 = [[1, 2]]
        l4 = [{'a': 1}]
        l5 = [{'a': 'c'}]
        l6 = "string"
        s1 = Base.to_json_string(l1)
        s2 = Base.to_json_string(l2)
        s3 = Base.to_json_string(l3)
        s4 = Base.to_json_string(l4)
        s5 = Base.to_json_string(l5)
        s6 = Base.to_json_string(l6)
        self.assertEqual(Base.from_json_string(s1), [])
        self.assertEqual(Base.from_json_string(s2), l2)
        self.assertEqual(Base.from_json_string(s3), l3)
        self.assertEqual(Base.from_json_string(s4), l4)
        self.assertEqual(Base.from_json_string(s5), l5)
        self.assertEqual(Base.from_json_string(s6), l6)

    def test_create(self):
        """Test instantiation via Create method"""

        dr1 = {'id': 1, 'width': 3, 'height': 5, 'x': 2, 'y': 4}
        r1 = Rectangle.create(**dr1)
        self.assertEqual(r1.to_dictionary(), dr1)
        self.assertEqual(Base._Base__nb_objects, 1)

        ds1 = {'id': 1, 'size': 3, 'x': 2, 'y': 4}
        s1 = Square.create(**ds1)
        self.assertEqual(s1.to_dictionary(), ds1)
        self.assertEqual(Base._Base__nb_objects, 2)

        r2 = Rectangle(3, 5, 2, 4, 1)
        dr2 = r2.to_dictionary()
        r3 = Rectangle.create(**dr2)
        self.assertEqual(r3.to_dictionary(), dr2)
        self.assertEqual(Base._Base__nb_objects, 3)

        r4 = Rectangle(3, 5, 2, 4)
        dr4 = r4.to_dictionary()
        r5 = Rectangle.create(**dr4)
        self.assertEqual(r5.to_dictionary(), dr4)
        self.assertEqual(Base._Base__nb_objects, 5)

        r6 = Rectangle(3, 5)
        dr6 = r6.to_dictionary()
        r7 = Rectangle.create(**dr6)
        self.assertEqual(r7.to_dictionary(), dr6)
        self.assertEqual(Base._Base__nb_objects, 7)

        s2 = Square(3, 2, 4, 1)
        ds2 = s2.to_dictionary()
        s3 = Square.create(**ds2)
        self.assertEqual(s3.to_dictionary(), ds2)
        self.assertEqual(Base._Base__nb_objects, 8)

        s4 = Square(3, 2, 4)
        ds4 = s4.to_dictionary()
        s5 = Square.create(**ds4)
        self.assertEqual(s5.to_dictionary(), ds4)
        self.assertEqual(Base._Base__nb_objects, 10)

        s6 = Square(3, 2)
        ds6 = s6.to_dictionary()
        s7 = Square.create(**ds6)
        self.assertEqual(s7.to_dictionary(), ds6)
        self.assertEqual(Base._Base__nb_objects, 12)

    def test_load_from_file(self):
        """Test load_from_file method"""

        r1 = Rectangle(3, 5, 2, 4, 1)
        dr1 = r1.to_dictionary()
        r2 = Rectangle(3, 5, 2, 4)
        dr2 = r2.to_dictionary()
        r3 = Rectangle(3, 10)
        dr3 = r3.to_dictionary()
        s1 = Square(3, 2, 4, 1)
        ds1 = s1.to_dictionary()
        s2 = Square(3, 2, 4)
        ds2 = s2.to_dictionary()
        s3 = Square(3)
        ds3 = s3.to_dictionary()

        Rectangle.save_to_file([r1, r2, r3])
        list_objs_r = Rectangle.load_from_file()
        Square.save_to_file([s1, s2, s3])
        list_objs_s = Square.load_from_file()

        self.assertIsInstance(list_objs_r[0], Rectangle)
        self.assertDictEqual(list_objs_r[0].to_dictionary(), dr1)

        self.assertIsInstance(list_objs_r[1], Rectangle)
        self.assertDictEqual(list_objs_r[1].to_dictionary(), dr2)

        self.assertIsInstance(list_objs_r[2], Rectangle)
        self.assertDictEqual(list_objs_r[2].to_dictionary(), dr3)

        self.assertIsInstance(list_objs_s[0], Square)
        self.assertDictEqual(list_objs_s[0].to_dictionary(), ds1)

        self.assertIsInstance(list_objs_s[1], Square)
        self.assertDictEqual(list_objs_s[1].to_dictionary(), ds2)

        self.assertIsInstance(list_objs_s[2], Square)
        self.assertDictEqual(list_objs_s[2].to_dictionary(), ds3)

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""

        with self.assertRaises(AttributeError):
            b1 = Base(1)
            Base.save_to_file_csv([b1])
            self.assertTrue(path.isfile('Base.csv'))

        r1 = Rectangle(3, 5, 2, 4, 1)
        Rectangle.save_to_file_csv([r1])
        self.assertTrue(path.isfile('Rectangle.csv'))

        r2 = Rectangle(3, 5, 2, 4)
        Rectangle.save_to_file_csv([r2])
        self.assertTrue(path.isfile('Rectangle.csv'))

        r3 = Rectangle(3, 5)
        Rectangle.save_to_file_csv([r3])
        self.assertTrue(path.isfile('Rectangle.csv'))

        s1 = Square(3, 2, 4, 1)
        Square.save_to_file_csv([s1])
        self.assertTrue(path.isfile('Square.csv'))

        s2 = Square(3, 2, 4)
        Square.save_to_file_csv([s2])
        self.assertTrue(path.isfile('Square.csv'))

        s3 = Square(3)
        Square.save_to_file_csv([s3])
        self.assertTrue(path.isfile('Square.csv'))

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method"""

        r1 = Rectangle(3, 5, 2, 4, 1)
        dr1 = r1.to_dictionary()
        r2 = Rectangle(3, 5, 2, 4)
        dr2 = r2.to_dictionary()
        r3 = Rectangle(3, 10)
        dr3 = r3.to_dictionary()
        s1 = Square(3, 2, 4, 1)
        ds1 = s1.to_dictionary()
        s2 = Square(3, 2, 4)
        ds2 = s2.to_dictionary()
        s3 = Square(3)
        ds3 = s3.to_dictionary()

        Rectangle.save_to_file_csv([r1, r2, r3])
        list_objs_r = Rectangle.load_from_file_csv()
        Square.save_to_file_csv([s1, s2, s3])
        list_objs_s = Square.load_from_file_csv()

        self.assertIsInstance(list_objs_r[0], Rectangle)
        self.assertDictEqual(list_objs_r[0].to_dictionary(), dr1)

        self.assertIsInstance(list_objs_r[1], Rectangle)
        self.assertDictEqual(list_objs_r[1].to_dictionary(), dr2)

        self.assertIsInstance(list_objs_r[2], Rectangle)
        self.assertDictEqual(list_objs_r[2].to_dictionary(), dr3)

        self.assertIsInstance(list_objs_s[0], Square)
        self.assertDictEqual(list_objs_s[0].to_dictionary(), ds1)

        self.assertIsInstance(list_objs_s[1], Square)
        self.assertDictEqual(list_objs_s[1].to_dictionary(), ds2)

        self.assertIsInstance(list_objs_s[2], Square)
        self.assertDictEqual(list_objs_s[2].to_dictionary(), ds3)

# if __name__ == '__main__':
#     unittest.main()
