#!/usr/bin/python3
"""
Unittest for the Rectangle class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_square.py
"""
import unittest
import pep8
import sys
import io
from models import base
from models import rectangle
from models import square
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Sets the private class attribute __nb_objects back to 0
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        print("setUp")
        Base._Base__nb_objects = 0

    def tearDown(self):
        """
        Sets the private class attribute __nb_objects back to 0
        Method called immediately after the test method has been called and
        the result recorded
        """
        print("tearDown")
        del Base._Base__nb_objects

    def test_pep8_conformance(self):
        """Test that Square conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the Square methods are all present"""
        l1 = dir(Square)
        self.assertIn('__init__', l1)
        self.assertIn('width', l1)
        self.assertIn('height', l1)
        self.assertIn('size', l1)
        self.assertIn('x', l1)
        self.assertIn('y', l1)
        self.assertIn('area', l1)
        self.assertIn('display', l1)
        self.assertIn('__str__', l1)
        self.assertIn('update', l1)
        self.assertIn('to_dictionary', l1)
        self.assertIn('from_json_string', l1)
        self.assertIn('load_from_file', l1)
        self.assertIn('load_from_file_csv', l1)
        self.assertIn('save_to_file', l1)
        self.assertIn('save_to_file_csv', l1)
        self.assertIn('to_json_string', l1)

    def test_class_attribute_presence(self):
        """Test that the Square attributes are all present"""
        l1 = dir(Square(1))
        self.assertIn('_Rectangle__width', l1)
        self.assertIn('_Rectangle__height', l1)
        self.assertIn('_Rectangle__x', l1)
        self.assertIn('_Rectangle__y', l1)
#        self.assertIn('id', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(square.__doc__, None)
        self.assertIsNot(Square.__doc__, None)
        self.assertIsNot(Square.__init__.__doc__, None)
        self.assertIsNot(Square.width.__doc__, None)
        self.assertIsNot(Square.height.__doc__, None)
        self.assertIsNot(Square.x.__doc__, None)
        self.assertIsNot(Square.y.__doc__, None)
        self.assertIsNot(Square.area.__doc__, None)
        self.assertIsNot(Square.display.__doc__, None)
        self.assertIsNot(Square.__str__.__doc__, None)
        self.assertIsNot(Square.update.__doc__, None)
        self.assertIsNot(Square.to_dictionary.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation with various parameter values"""

        with self.assertRaises(TypeError):
            s1 = Square()
            self.assertIsInstance(s1, Square)
            self.assertEqual(s1.id, 1)
            self.assertEqual(Base._Base__nb_objects, 1)

        s2 = Square(3)
        self.assertIsInstance(s2, Square)
        self.assertEqual(s2.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

        s3 = Square(3, 2, 4, 1)
        self.assertIsInstance(s3, Square)
        self.assertEqual(s3.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

        s4 = Square(3, 2, 4)
        self.assertIsInstance(s4, Square)
        self.assertEqual(s4.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

        with self.assertRaises(ValueError):
            s5 = Square(-3, 2, 4, 1)
        with self.assertRaises(ValueError):
            s6 = Square(3, -2, 4, 1)
        with self.assertRaises(ValueError):
            s7 = Square(3, 2, -4, 1)

        with self.assertRaises(TypeError):
            s8 = Square(3.5, 2, 4, 1)
        with self.assertRaises(TypeError):
            s9 = Square(3, 2.5, 4, 1)
        with self.assertRaises(TypeError):
            s10 = Square(3, 2, 4.5, 1)

        with self.assertRaises(TypeError):
            s11 = Square(float('inf'), 2, 4, 1)
        with self.assertRaises(TypeError):
            s12 = Square(3, float('inf'), 4, 1)
        with self.assertRaises(TypeError):
            s13 = Square(3, 2, float('inf'), 1)

        with self.assertRaises(TypeError):
            s14 = Square(float('nan'), 2, 4, 1)
        with self.assertRaises(TypeError):
            s15 = Square(3, float('nan'), 4, 1)
        with self.assertRaises(TypeError):
            s16 = Square(3, 2, float('nan'), 1)

        with self.assertRaises(TypeError):
            s17 = Square(True, 2, 4, 1)
        with self.assertRaises(TypeError):
            s18 = Square(3, True, 4, 1)
        with self.assertRaises(TypeError):
            s19 = Square(3, 2, True, 1)

        with self.assertRaises(TypeError):
            s20 = Square("String", 2, 4, 1)
        with self.assertRaises(TypeError):
            s21 = Square(3, "String", 4, 1)
        with self.assertRaises(TypeError):
            s22 = Square(3, 2, "String", 1)

        with self.assertRaises(TypeError):
            s23 = Square(['a', 2], 2, 4, 1)
        with self.assertRaises(TypeError):
            s24 = Square(3, ['a', 2], 4, 1)
        with self.assertRaises(TypeError):
            s25 = Square(3, 2, ['a', 2], 1)

        with self.assertRaises(TypeError):
            s26 = Square(('a', 2), 2, 4, 1)
        with self.assertRaises(TypeError):
            s27 = Square(3, ('a', 2), 4, 1)
        with self.assertRaises(TypeError):
            s28 = Square(3, 2, ('a', 2), 1)

        with self.assertRaises(TypeError):
            s29 = Square({'a', 2}, 2, 4, 1)
        with self.assertRaises(TypeError):
            s30 = Square(3, {'a', 2}, 4, 1)
        with self.assertRaises(TypeError):
            s31 = Square(3, 2, {'a', 2}, 1)

        with self.assertRaises(TypeError):
            b38 = Square({1: 'a', 2: 'b'}, 2, 4, 1)
        with self.assertRaises(TypeError):
            b40 = Square(3, {1: 'a', 2: 'b'}, 4, 1)
        with self.assertRaises(TypeError):
            b41 = Square(3, 2, {1: 'a', 2: 'b'}, 1)

        with self.assertRaises(TypeError):
            s42 = Square(None, 2, 4, 1)
        with self.assertRaises(TypeError):
            s43 = Square(3, None, 4, 1)
        with self.assertRaises(TypeError):
            s44 = Square(3, 2, None, 1)

        with self.assertRaises(ValueError):
            s45 = Square(0, 2, 4, 1)

        s46 = Square(3, 0, 4, 1)
        self.assertIsInstance(s46, Square)
        self.assertEqual(s46.id, 1)
        self.assertEqual(Base._Base__nb_objects, 2)

        s47 = Square(3, 2, 0, 1)
        self.assertIsInstance(s47, Square)
        self.assertEqual(s47.id, 1)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_area(self):
        """Test the area method"""

        s1 = Square(3, 2, 4, 1)
        self.assertEqual(s1.area(), 9)
        s2 = Square(3, 2, 4)
        self.assertEqual(s2.area(), 9)
        s3 = Square(3)
        self.assertEqual(s3.area(), 9)

    def test_display(self):
        """Test the display method"""

        s1 = Square(3)
        sys.stdout = io.StringIO()
        s1.display()
        self.assertEqual('###\n###\n###\n', sys.stdout.getvalue())

        s2 = Square(3, 1, 0)
        sys.stdout = io.StringIO()
        s2.display()
        self.assertEqual(' ###\n ###\n ###\n', sys.stdout.getvalue())

        s3 = Square(3, 0, 1)
        sys.stdout = io.StringIO()
        s3.display()
        self.assertEqual('\n###\n###\n###\n', sys.stdout.getvalue())

        s4 = Square(3, 1, 1)
        sys.stdout = io.StringIO()
        s4.display()
        self.assertEqual('\n ###\n ###\n ###\n', sys.stdout.getvalue())

    def test___str__(self):
        """Test the __str__ method"""

        s1 = Square(3)
        sys.stdout = io.StringIO()
        print(s1)
        self.assertEqual('[Square] (1) 0/0 - 3\n', sys.stdout.getvalue())

        s2 = Square(3, 1, 0)
        sys.stdout = io.StringIO()
        print(s2)
        self.assertEqual('[Square] (2) 1/0 - 3\n', sys.stdout.getvalue())

        s3 = Square(3, 0, 1)
        sys.stdout = io.StringIO()
        print(s3)
        self.assertEqual('[Square] (3) 0/1 - 3\n', sys.stdout.getvalue())

        s4 = Square(3, 1, 1)
        sys.stdout = io.StringIO()
        print(s4)
        self.assertEqual('[Square] (4) 1/1 - 3\n', sys.stdout.getvalue())

        s5 = Square(3, 1, 1, 1)
        sys.stdout = io.StringIO()
        print(s5)
        self.assertEqual('[Square] (1) 1/1 - 3\n', sys.stdout.getvalue())

        s6 = Square(3, 1, 1, "String")
        sys.stdout = io.StringIO()
        print(s6)
        self.assertEqual('[Square] (String) 1/1 - 3\n',
                         sys.stdout.getvalue())

    def test_update(self):
        """Test the update method"""

        s1 = Square(3)
        s1.update()
        sys.stdout = io.StringIO()
        print(s1)
        self.assertEqual('[Square] (1) 0/0 - 3\n', sys.stdout.getvalue())
        s1.update(10)
        sys.stdout = io.StringIO()
        print(s1)
        self.assertEqual('[Square] (10) 0/0 - 3\n', sys.stdout.getvalue())
        s1.update(10, 10)
        sys.stdout = io.StringIO()
        print(s1)
        self.assertEqual('[Square] (10) 0/0 - 10\n', sys.stdout.getvalue())
        s1.update(10, 10, 10)
        sys.stdout = io.StringIO()
        print(s1)
        self.assertEqual('[Square] (10) 10/0 - 10\n', sys.stdout.getvalue())
        s1.update(10, 10, 10, 10)
        sys.stdout = io.StringIO()
        print(s1)
        self.assertEqual('[Square] (10) 10/10 - 10\n', sys.stdout.getvalue())

        s2 = Square(3)
        s2.update()
        sys.stdout = io.StringIO()
        print(s2)
        self.assertEqual('[Square] (2) 0/0 - 3\n', sys.stdout.getvalue())
        s2.update(id=10)
        sys.stdout = io.StringIO()
        print(s2)
        self.assertEqual('[Square] (10) 0/0 - 3\n', sys.stdout.getvalue())
        s2.update(id=10, size=10)
        sys.stdout = io.StringIO()
        print(s2)
        self.assertEqual('[Square] (10) 0/0 - 10\n', sys.stdout.getvalue())
        s2.update(id=10, size=10, x=10)
        sys.stdout = io.StringIO()
        print(s2)
        self.assertEqual('[Square] (10) 10/0 - 10\n', sys.stdout.getvalue())
        s2.update(id=10, size=10, x=10, y=10)
        sys.stdout = io.StringIO()
        print(s2)
        self.assertEqual('[Square] (10) 10/10 - 10\n', sys.stdout.getvalue())

        s3 = Square(3, 1, 1, 1)
        s3.update(10, 10, 10, 10)
        sys.stdout = io.StringIO()
        print(s3)
        self.assertEqual('[Square] (10) 10/10 - 10\n', sys.stdout.getvalue())
        s3.update(id=20, size=20, x=20, y=20)
        sys.stdout = io.StringIO()
        print(s3)
        self.assertEqual('[Square] (20) 20/20 - 20\n', sys.stdout.getvalue())

        s3 = Square(3, 1, 1, 1)
        s3.update(-10, 10, 10, 10)
        sys.stdout = io.StringIO()
        print(s3)
        self.assertEqual('[Square] (-10) 10/10 - 10\n', sys.stdout.getvalue())
        s3.update(id=-20, size=20, x=20, y=20)
        sys.stdout = io.StringIO()
        print(s3)
        self.assertEqual('[Square] (-20) 20/20 - 20\n', sys.stdout.getvalue())
        s3.update(id=0, size=20, x=20, y=20)
        sys.stdout = io.StringIO()
        print(s3)
        self.assertEqual('[Square] (0) 20/20 - 20\n', sys.stdout.getvalue())
        s3.update(id="String", size=20, x=20, y=20)
        sys.stdout = io.StringIO()
        print(s3)
        self.assertEqual('[Square] (String) 20/20 - 20\n',
                         sys.stdout.getvalue())
        s3.update(id=1.5, size=20, x=20, y=20)
        sys.stdout = io.StringIO()
        print(s3)
        self.assertEqual('[Square] (1.5) 20/20 - 20\n', sys.stdout.getvalue())

        s4 = Square(3, 1, 1, 1)
        with self.assertRaises(ValueError):
            s4.update(10, -10, 10, 10)
        with self.assertRaises(ValueError):
            s4.update(id=20, size=-20, x=20, y=20)
        with self.assertRaises(ValueError):
            s4.update(id=20, size=0, x=20, y=20)
        with self.assertRaises(TypeError):
            s4.update(id=20, size="String", x=20, y=20)
        with self.assertRaises(TypeError):
            s4.update(id=20, size=1.5, x=20, y=20)
        with self.assertRaises(TypeError):
            s4.update(id=20, size=None, x=20, y=20)

        s5 = Square(3, 1, 1, 1)
        with self.assertRaises(ValueError):
            s5.update(10, 10, -10, 10)
        with self.assertRaises(ValueError):
            s5.update(id=20, size=20, x=-20, y=20)
        s5.update(id=20, size=20, x=0, y=20)
        sys.stdout = io.StringIO()
        print(s5)
        self.assertEqual('[Square] (20) 0/20 - 20\n', sys.stdout.getvalue())
        with self.assertRaises(TypeError):
            s5.update(id=20, size=20, x="String", y=20)
        with self.assertRaises(TypeError):
            s5.update(id=20, size=20, x=1.5, y=20)
        with self.assertRaises(TypeError):
            s5.update(id=20, size=20, x=None, y=20)

    def test_to_dictionary(self):
        """Test the to_dictionary method"""

        s1 = Square(3, 2, 4, 1)
        d1 = {"size": 3, "x": 2, "y": 4, "id": 1}
        self.assertEqual(s1.to_dictionary(), d1)

        s2 = Square(3, 2, 4)
        d2 = {"size": 3, "x": 2, "y": 4, "id": 1}
        self.assertEqual(s2.to_dictionary(), d2)

        s3 = Square(3)
        d3 = {"size": 3, "x": 0, "y": 0, "id": 2}
        self.assertEqual(s3.to_dictionary(), d3)
