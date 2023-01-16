#!/usr/bin/python3
"""
Unittest for the Rectangle class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_rectangle.py
"""
import unittest
import pep8
import sys
import io
from models import base
from models import rectangle
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
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
        """Test that Rectangle conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the Rectangle methods are all present"""
        l1 = dir(Rectangle)
        self.assertIn('__init__', l1)
        self.assertIn('width', l1)
        self.assertIn('height', l1)
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
        """Test that the Rectangle attributes are all present"""
        l1 = dir(Rectangle(1, 1))
        self.assertIn('_Rectangle__width', l1)
        self.assertIn('_Rectangle__height', l1)
        self.assertIn('_Rectangle__x', l1)
        self.assertIn('_Rectangle__y', l1)
        self.assertIn('id', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(rectangle.__doc__, None)
        self.assertIsNot(Rectangle.__doc__, None)
        self.assertIsNot(Rectangle.__init__.__doc__, None)
        self.assertIsNot(Rectangle.width.__doc__, None)
        self.assertIsNot(Rectangle.height.__doc__, None)
        self.assertIsNot(Rectangle.x.__doc__, None)
        self.assertIsNot(Rectangle.y.__doc__, None)
        self.assertIsNot(Rectangle.area.__doc__, None)
        self.assertIsNot(Rectangle.display.__doc__, None)
        self.assertIsNot(Rectangle.__str__.__doc__, None)
        self.assertIsNot(Rectangle.update.__doc__, None)
        self.assertIsNot(Rectangle.to_dictionary.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation with various parameter values"""

        with self.assertRaises(TypeError):
            b1 = Rectangle()
            self.assertIsInstance(b1, Rectangle)
            self.assertEqual(b1.id, 1)
            self.assertEqual(Base._Base__nb_objects, 1)

        with self.assertRaises(TypeError):
            b2 = Rectangle(3)
            self.assertIsInstance(b2, Rectangle)
            self.assertEqual(b2.id, 2)
            self.assertEqual(Base._Base__nb_objects, 2)

        b3 = Rectangle(3, 5, 2, 4, 1)
        self.assertIsInstance(b3, Rectangle)
        self.assertEqual(b3.id, 1)
        self.assertEqual(Base._Base__nb_objects, 0)

        b4 = Rectangle(3, 5, 2, 4)
        self.assertIsInstance(b4, Rectangle)
        self.assertEqual(b4.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

        b5 = Rectangle(3, 5)
        self.assertIsInstance(b5, Rectangle)
        self.assertEqual(b5.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

        with self.assertRaises(ValueError):
            b6 = Rectangle(-3, 5, 2, 4, 1)
        with self.assertRaises(ValueError):
            b7 = Rectangle(3, -5, 2, 4, 1)
        with self.assertRaises(ValueError):
            b8 = Rectangle(3, 5, -2, 4, 1)
        with self.assertRaises(ValueError):
            b9 = Rectangle(3, 5, 2, -4, 1)

        with self.assertRaises(TypeError):
            b10 = Rectangle(3.5, 5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b11 = Rectangle(3, 5.5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b12 = Rectangle(3, 5, 2.5, 4, 1)
        with self.assertRaises(TypeError):
            b13 = Rectangle(3, 5, 2, 4.5, 1)

        with self.assertRaises(TypeError):
            b14 = Rectangle(float('inf'), 5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b15 = Rectangle(3, float('inf'), 2, 4, 1)
        with self.assertRaises(TypeError):
            b16 = Rectangle(3, 5, float('inf'), 4, 1)
        with self.assertRaises(TypeError):
            b17 = Rectangle(3, 5, 2, float('inf'), 1)

        with self.assertRaises(TypeError):
            b14 = Rectangle(float('nan'), 5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b15 = Rectangle(3, float('nan'), 2, 4, 1)
        with self.assertRaises(TypeError):
            b16 = Rectangle(3, 5, float('nan'), 4, 1)
        with self.assertRaises(TypeError):
            b17 = Rectangle(3, 5, 2, float('nan'), 1)

        with self.assertRaises(TypeError):
            b18 = Rectangle(True, 5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b19 = Rectangle(3, True, 2, 4, 1)
        with self.assertRaises(TypeError):
            b20 = Rectangle(3, 5, True, 4, 1)
        with self.assertRaises(TypeError):
            b21 = Rectangle(3, 5, 2, True, 1)

        with self.assertRaises(TypeError):
            b22 = Rectangle("String", 5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b23 = Rectangle(3, "String", 2, 4, 1)
        with self.assertRaises(TypeError):
            b24 = Rectangle(3, 5, "String", 4, 1)
        with self.assertRaises(TypeError):
            b25 = Rectangle(3, 5, 2, "String", 1)

        with self.assertRaises(TypeError):
            b26 = Rectangle(['a', 2], 5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b27 = Rectangle(3, ['a', 2], 2, 4, 1)
        with self.assertRaises(TypeError):
            b28 = Rectangle(3, 5, ['a', 2], 4, 1)
        with self.assertRaises(TypeError):
            b29 = Rectangle(3, 5, 2, ['a', 2], 1)

        with self.assertRaises(TypeError):
            b30 = Rectangle(('a', 2), 5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b31 = Rectangle(3, ('a', 2), 2, 4, 1)
        with self.assertRaises(TypeError):
            b32 = Rectangle(3, 5, ('a', 2), 4, 1)
        with self.assertRaises(TypeError):
            b33 = Rectangle(3, 5, 2, ('a', 2), 1)

        with self.assertRaises(TypeError):
            b34 = Rectangle({'a', 2}, 5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b35 = Rectangle(3, {'a', 2}, 2, 4, 1)
        with self.assertRaises(TypeError):
            b36 = Rectangle(3, 5, {'a', 2}, 4, 1)
        with self.assertRaises(TypeError):
            b37 = Rectangle(3, 5, 2, {'a', 2}, 1)

        with self.assertRaises(TypeError):
            b38 = Rectangle({1: 'a', 2: 'b'}, 5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b39 = Rectangle(3, {1: 'a', 2: 'b'}, 2, 4, 1)
        with self.assertRaises(TypeError):
            b40 = Rectangle(3, 5, {1: 'a', 2: 'b'}, 4, 1)
        with self.assertRaises(TypeError):
            b41 = Rectangle(3, 5, 2, {1: 'a', 2: 'b'}, 1)

        with self.assertRaises(TypeError):
            b38 = Rectangle(None, 5, 2, 4, 1)
        with self.assertRaises(TypeError):
            b39 = Rectangle(3, None, 2, 4, 1)
        with self.assertRaises(TypeError):
            b40 = Rectangle(3, 5, None, 4, 1)
        with self.assertRaises(TypeError):
            b41 = Rectangle(3, 5, 2, None, 1)

        with self.assertRaises(ValueError):
            b42 = Rectangle(0, 5, 2, 4, 1)
        with self.assertRaises(ValueError):
            b43 = Rectangle(3, 0, 2, 4, 1)

        b44 = Rectangle(3, 5, 0, 4, 1)
        self.assertIsInstance(b44, Rectangle)
        self.assertEqual(b44.id, 1)
        self.assertEqual(Base._Base__nb_objects, 2)

        b45 = Rectangle(3, 5, 2, 0, 1)
        self.assertIsInstance(b45, Rectangle)
        self.assertEqual(b45.id, 1)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_area(self):
        """Test the area method"""

        r1 = Rectangle(3, 5, 2, 4, 1)
        self.assertEqual(r1.area(), 15)
        r2 = Rectangle(3, 5, 2, 4)
        self.assertEqual(r1.area(), 15)
        r3 = Rectangle(3, 5)
        self.assertEqual(r1.area(), 15)

    def test_display(self):
        """Test the display method"""

        r1 = Rectangle(3, 3)
        sys.stdout = io.StringIO()
        r1.display()
        self.assertEqual('###\n###\n###\n', sys.stdout.getvalue())

        r2 = Rectangle(1, 3)
        sys.stdout = io.StringIO()
        r2.display()
        self.assertEqual('#\n#\n#\n', sys.stdout.getvalue())

        r3 = Rectangle(3, 1)
        sys.stdout = io.StringIO()
        r3.display()
        self.assertEqual('###\n', sys.stdout.getvalue())

        r4 = Rectangle(3, 3, 1, 0)
        sys.stdout = io.StringIO()
        r4.display()
        self.assertEqual(' ###\n ###\n ###\n', sys.stdout.getvalue())

        r5 = Rectangle(3, 3, 0, 1)
        sys.stdout = io.StringIO()
        r5.display()
        self.assertEqual('\n###\n###\n###\n', sys.stdout.getvalue())

        r6 = Rectangle(3, 3, 1, 1)
        sys.stdout = io.StringIO()
        r6.display()
        self.assertEqual('\n ###\n ###\n ###\n', sys.stdout.getvalue())

    def test___str__(self):
        """Test the __str__ method"""

        r1 = Rectangle(3, 3)
        sys.stdout = io.StringIO()
        print(r1)
        self.assertEqual('[Rectangle] (1) 0/0 - 3/3\n', sys.stdout.getvalue())

        r2 = Rectangle(1, 3)
        sys.stdout = io.StringIO()
        print(r2)
        self.assertEqual('[Rectangle] (2) 0/0 - 1/3\n', sys.stdout.getvalue())

        r3 = Rectangle(3, 1)
        sys.stdout = io.StringIO()
        print(r3)
        self.assertEqual('[Rectangle] (3) 0/0 - 3/1\n', sys.stdout.getvalue())

        r4 = Rectangle(3, 3, 1, 0)
        sys.stdout = io.StringIO()
        print(r4)
        self.assertEqual('[Rectangle] (4) 1/0 - 3/3\n', sys.stdout.getvalue())

        r5 = Rectangle(3, 3, 0, 1)
        sys.stdout = io.StringIO()
        print(r5)
        self.assertEqual('[Rectangle] (5) 0/1 - 3/3\n', sys.stdout.getvalue())

        r6 = Rectangle(3, 3, 1, 1)
        sys.stdout = io.StringIO()
        print(r6)
        self.assertEqual('[Rectangle] (6) 1/1 - 3/3\n', sys.stdout.getvalue())

        r7 = Rectangle(3, 3, 1, 1, 1)
        sys.stdout = io.StringIO()
        print(r7)
        self.assertEqual('[Rectangle] (1) 1/1 - 3/3\n', sys.stdout.getvalue())

        r8 = Rectangle(3, 3, 1, 1, "String")
        sys.stdout = io.StringIO()
        print(r8)
        self.assertEqual('[Rectangle] (String) 1/1 - 3/3\n',
                         sys.stdout.getvalue())

    def test_update(self):
        """Test the update method"""

        r1 = Rectangle(3, 3)
        r1.update()
        sys.stdout = io.StringIO()
        print(r1)
        self.assertEqual('[Rectangle] (1) 0/0 - 3/3\n', sys.stdout.getvalue())
        r1.update(10)
        sys.stdout = io.StringIO()
        print(r1)
        self.assertEqual('[Rectangle] (10) 0/0 - 3/3\n', sys.stdout.getvalue())
        r1.update(10, 10)
        sys.stdout = io.StringIO()
        print(r1)
        self.assertEqual('[Rectangle] (10) 0/0 - 10/3\n',
                         sys.stdout.getvalue())
        r1.update(10, 10, 10)
        sys.stdout = io.StringIO()
        print(r1)
        self.assertEqual('[Rectangle] (10) 0/0 - 10/10\n',
                         sys.stdout.getvalue())
        r1.update(10, 10, 10, 10)
        sys.stdout = io.StringIO()
        print(r1)
        self.assertEqual('[Rectangle] (10) 10/0 - 10/10\n',
                         sys.stdout.getvalue())
        r1.update(10, 10, 10, 10, 10)
        sys.stdout = io.StringIO()
        print(r1)
        self.assertEqual('[Rectangle] (10) 10/10 - 10/10\n',
                         sys.stdout.getvalue())

        r2 = Rectangle(3, 3)
        r2.update()
        sys.stdout = io.StringIO()
        print(r2)
        self.assertEqual('[Rectangle] (2) 0/0 - 3/3\n', sys.stdout.getvalue())
        r2.update(id=10)
        sys.stdout = io.StringIO()
        print(r2)
        self.assertEqual('[Rectangle] (10) 0/0 - 3/3\n', sys.stdout.getvalue())
        r2.update(id=10, width=10)
        sys.stdout = io.StringIO()
        print(r2)
        self.assertEqual('[Rectangle] (10) 0/0 - 10/3\n',
                         sys.stdout.getvalue())
        r2.update(id=10, width=10, height=10)
        sys.stdout = io.StringIO()
        print(r2)
        self.assertEqual('[Rectangle] (10) 0/0 - 10/10\n',
                         sys.stdout.getvalue())
        r2.update(id=10, width=10, height=10, x=10)
        sys.stdout = io.StringIO()
        print(r2)
        self.assertEqual('[Rectangle] (10) 10/0 - 10/10\n',
                         sys.stdout.getvalue())
        r2.update(id=10, width=10, height=10, x=10, y=10)
        sys.stdout = io.StringIO()
        print(r2)
        self.assertEqual('[Rectangle] (10) 10/10 - 10/10\n',
                         sys.stdout.getvalue())

        r3 = Rectangle(3, 3, 1, 1, 1)
        r3.update(10, 10, 10, 10, 10)
        sys.stdout = io.StringIO()
        print(r3)
        self.assertEqual('[Rectangle] (10) 10/10 - 10/10\n',
                         sys.stdout.getvalue())
        r3.update(id=20, width=20, height=20, x=20, y=20)
        sys.stdout = io.StringIO()
        print(r3)
        self.assertEqual('[Rectangle] (20) 20/20 - 20/20\n',
                         sys.stdout.getvalue())

        r3 = Rectangle(3, 3, 1, 1, 1)
        r3.update(-10, 10, 10, 10, 10)
        sys.stdout = io.StringIO()
        print(r3)
        self.assertEqual('[Rectangle] (-10) 10/10 - 10/10\n',
                         sys.stdout.getvalue())
        r3.update(id=-20, width=20, height=20, x=20, y=20)
        sys.stdout = io.StringIO()
        print(r3)
        self.assertEqual('[Rectangle] (-20) 20/20 - 20/20\n',
                         sys.stdout.getvalue())
        r3.update(id=0, width=20, height=20, x=20, y=20)
        sys.stdout = io.StringIO()
        print(r3)
        self.assertEqual('[Rectangle] (0) 20/20 - 20/20\n',
                         sys.stdout.getvalue())
        r3.update(id="String", width=20, height=20, x=20, y=20)
        sys.stdout = io.StringIO()
        print(r3)
        self.assertEqual('[Rectangle] (String) 20/20 - 20/20\n',
                         sys.stdout.getvalue())
        r3.update(id=1.5, width=20, height=20, x=20, y=20)
        sys.stdout = io.StringIO()
        print(r3)
        self.assertEqual('[Rectangle] (1.5) 20/20 - 20/20\n',
                         sys.stdout.getvalue())

        r4 = Rectangle(3, 3, 1, 1, 1)
        with self.assertRaises(ValueError):
            r4.update(10, -10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r4.update(id=20, width=-20, height=20, x=20, y=20)
        with self.assertRaises(ValueError):
            r4.update(id=20, width=0, height=20, x=20, y=20)
        with self.assertRaises(TypeError):
            r4.update(id=20, width="String", height=20, x=20, y=20)
        with self.assertRaises(TypeError):
            r4.update(id=20, width=1.5, height=20, x=20, y=20)
        with self.assertRaises(TypeError):
            r4.update(id=20, width=None, height=20, x=20, y=20)

        r5 = Rectangle(3, 3, 1, 1, 1)
        with self.assertRaises(ValueError):
            r5.update(10, 10, 10, -10, 10)
        with self.assertRaises(ValueError):
            r5.update(id=20, width=20, height=20, x=-20, y=20)
        r5.update(id=20, width=20, height=20, x=0, y=20)
        sys.stdout = io.StringIO()
        print(r5)
        self.assertEqual('[Rectangle] (20) 0/20 - 20/20\n',
                         sys.stdout.getvalue())
        with self.assertRaises(TypeError):
            r5.update(id=20, width=20, height=20, x="String", y=20)
        with self.assertRaises(TypeError):
            r5.update(id=20, width=20, height=20, x=1.5, y=20)
        with self.assertRaises(TypeError):
            r5.update(id=20, width=20, height=20, x=None, y=20)

    def test_to_dictionary(self):
        """Test the to_dictionary method"""

        r1 = Rectangle(3, 5, 2, 4, 1)
        d1 = {"width": 3, "height": 5, "x": 2, "y": 4, "id": 1}
        self.assertEqual(r1.to_dictionary(), d1)

        r2 = Rectangle(3, 5, 2, 4)
        d2 = {"width": 3, "height": 5, "x": 2, "y": 4, "id": 1}
        self.assertEqual(r2.to_dictionary(), d2)

        r3 = Rectangle(3, 5)
        d3 = {"width": 3, "height": 5, "x": 0, "y": 0, "id": 2}
        self.assertEqual(r3.to_dictionary(), d3)
