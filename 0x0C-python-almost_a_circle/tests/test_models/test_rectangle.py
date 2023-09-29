#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    '''Tests the Rectangle class.'''

    def setUp(self):
        '''Set up before each test method.'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Clean up after each test method.'''
        pass

    # ----------------- Tests for #2 ------------------------

    def test_A_class(self):
        '''Tests Rectangle class type.'''
        self.assertEqual(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        '''Tests if Rectangle inherits Base.'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_C_constructor_no_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        s = "__init__() takes from 3 to 6 positional arguments but 7 were given"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_one_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Tests instantiation.'''
        r = Rectangle(10, 20)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10, '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Rectangle("1", 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, "3")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, "4")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -2)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -3)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -4)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        '''Tests positional instantiation.'''
        r = Rectangle(5, 10, 15, 20)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5, '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Rectangle(5, 10, 15, 20, 98)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5, '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Tests positional instantiation.'''
        r = Rectangle(100, 200, id=421, y=99, x=101)
        d = {'_Rectangle__height': 200, '_Rectangle__width': 100, '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Tests if id is inherited from Base.'''
        Base._Base__nb_objects = 98
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''Tests property getters/setters.'''
        r = Rectangle(5, 9)
        r.width = 100
        r.height = 101
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 101, '_Rectangle__width': 100, '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 101)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    # ----------------- Tests for #3 ------------------------

    def invalid_types(self):
        '''Returns tuple of types for validation.'''
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,), [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_type(self):
        '''Tests property validation.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''Tests property validation.'''
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''Tests property validation.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        '''Tests property validation.'''
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        '''Tests property setting/getting.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        '''Tests property setting/getting.'''
        r = Rectangle(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    # ----------------- Tests for #4 ------------------------
    def test_I_area_no_args(self):
        '''Tests area() method signature.'''
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        '''Tests area() method computation.'''
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r.width = w
        r.height = h
        self.assertEqual(r.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r = Rectangle(w, h, 7, 8, 9)
        self.assertEqual(r.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r = Rectangle(w, h, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * h)

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    # ----------------- Tests for #5 & #7 ------------------------
    def test_J_display_no_args(self):
        '''Tests display() method signature.'''
        r = Rectangle(9, 8)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_J_display_simple(self):
        '''Tests display() method output.'''
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.width = 3
        r.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "###\n###\n###\n###\n###\n"
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(5, 6, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\n\n\n\n\n\n       #####\n       #####\n       #####\n       #####\n       #####\n       #####\n"
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#########\n#########\n#########\n#########\n#########\n#########\n#########\n#########\n"
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(1, 1, 10, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\n\n\n\n\n\n\n\n\n\n          #\n"
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 3, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "     #####\n     #####\n     #####\n"
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 3, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\n\n\n\n\n#####\n#####\n#####\n"
        self.assertEqual(f.getvalue(), s)

    # ----------------- Tests for #6 ------------------------

    def test_K_str_no_args(self):
        '''Tests __str__() method signature.'''
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_K_str(self):
        '''Tests __str__() method return.'''
        r = Rectangle(5, 2)
        s = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(r), s)
        r = Rectangle(1, 1, 1)
        s = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(r), s)
        r = Rectangle(3, 4, 5, 6)
        s = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(r), s)

        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

        r3 = Rectangle(10, 10)
        self.assertEqual(str(r3), "[Rectangle] (2) 0/0 - 10/10")

    # ----------------- Tests for #8 ------------------------

    def test_L_update_no_args(self):
        '''Tests update() method signature.'''
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_L_update_args(self):
        '''Tests update() method with *args.'''
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        s = '[Rectangle] (89) 10/10 - 10/10'
        self.assertEqual(str(r), s)
        r.update(89, 2)
        s = '[Rectangle] (89) 10/10 - 2/10'
        self.assertEqual(str(r), s)
        r.update(89, 2, 3)
        s = '[Rectangle] (89) 10/10 - 2/3'
        self.assertEqual(str(r), s)
        r.update(89, 2, 3, 4)
        s = '[Rectangle] (89) 4/10 - 2/3'
        self.assertEqual(str(r), s)
        r.update(89, 2, 3, 4, 5)
        s = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(str(r), s)

        r.update(98, 10, 10, 10, 10, 1)
        s = '[Rectangle] (98) 10/10 - 10/10'
        self.assertEqual(str(r), s)

        r.update(100)
        s = '[Rectangle] (100) 10/10 - 10/10'
        self.assertEqual(str(r), s)

        r.update(100, 2)
        s = '[Rectangle] (100) 10/10 - 2/10'
        self.assertEqual(str(r), s)

        r.update(100, 2, 3)
        s = '[Rectangle] (100) 10/10 - 2/3'
        self.assertEqual(str(r), s)

        r.update(100, 2, 3, 4)
        s = '[Rectangle] (100) 4/10 - 2/3'
        self.assertEqual(str(r), s)

        r.update(100, 2, 3, 4, 5)
        s = '[Rectangle] (100) 4/5 - 2/3'
        self.assertEqual(str(r), s)

    def test_M_update_kwargs(self):
        '''Tests update() method with **kwargs.'''
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89)
        s = '[Rectangle] (89) 10/10 - 10/10'
        self.assertEqual(str(r), s)
        r.update(id=89, width=2)
        s = '[Rectangle] (89) 10/10 - 2/10'
        self.assertEqual(str(r), s)
        r.update(id=89, width=2, height=3)
        s = '[Rectangle] (89) 10/10 - 2/3'
        self.assertEqual(str(r), s)
        r.update(id=89, width=2, height=3, x=4)
        s = '[Rectangle] (89) 4/10 - 2/3'
        self.assertEqual(str(r), s)
        r.update(id=89, width=2, height=3, x=4, y=5)
        s = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(str(r), s)

        r.update(y=1, width=2, x=3, id=89, height=4)
        s = '[Rectangle] (89) 3/1 - 2/4'
        self.assertEqual(str(r), s)

    def test_N_update_edge_cases(self):
        '''Tests update() with invalid types/values.'''
        r = Rectangle(10, 10, 10, 10)
        r.update(98, 10, 10, 10, 10, "Hello")
        s = '[Rectangle] (98) 10/10 - 10/10'
        self.assertEqual(str(r), s)

        r.update(y=1, width=2, x=3, id=89, height=-4)
        s = '[Rectangle] (89) 3/1 - 2/-4'
        self.assertEqual(str(r), s)

        r.update(y=1, width="2", x=3, id=89, height=4)
        s = '[Rectangle] (89) 3/1 - 2/4'
        self.assertEqual(str(r), s)

        r.update(width=5, height=5, x=5, y=5, id=55)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 55)

    # ----------------- Tests for #10 ------------------------
    def test_O_to_dictionary_no_args(self):
        '''Tests to_dictionary() method signature.'''
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_O_to_dictionary(self):
        '''Tests to_dictionary() method output.'''
        r = Rectangle(10, 2, 1, 9)
        d = {'x': 1, 'y': 9, 'width': 10, 'height': 2, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

        r = Rectangle(1, 1)
        d = {'x': 0, 'y': 0, 'width': 1, 'height': 1, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

        r = Rectangle(1, 1, 1)
        d = {'x': 1, 'y': 0, 'width': 1, 'height': 1, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

        r = Rectangle(1, 1, 1, 1)
        d = {'x': 1, 'y': 1, 'width': 1, 'height': 1, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

        r = Rectangle(1, 1, 1, 1, 89)
        d = {'x': 1, 'y': 1, 'width': 1, 'height': 1, 'id': 89}
        self.assertDictEqual(r.to_dictionary(), d)

        r = Rectangle(2, 4, 0, 0, 12)
        self.assertEqual(r.to_dictionary(), {'x': 0, 'y': 0, 'width': 2, 'height': 4, 'id': 12})

        r = Rectangle(1, 2)
        d = {'x': 0, 'y': 0, 'width': 1, 'height': 2, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

    def test_O_to_dictionary_update(self):
        '''Tests if to_dictionary() receives updates correctly.'''
        r = Rectangle(10, 2, 1, 9)
        d = {'x': 1, 'y': 9, 'width': 10, 'height': 2, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)
        r.update(89)
        d = {'x': 1, 'y': 9, 'width': 10, 'height': 2, 'id': 89}
        self.assertDictEqual(r.to_dictionary(), d)
        r.update(89, 2)
        d = {'x': 1, 'y': 9, 'width': 2, 'height': 2, 'id': 89}
        self.assertDictEqual(r.to_dictionary(), d)
        r.update(89, 2, 3)
        d = {'x': 1, 'y': 9, 'width': 2, 'height': 3, 'id': 89}
        self.assertDictEqual(r.to_dictionary(), d)
        r.update(89, 2, 3, 4)
        d = {'x': 4, 'y': 9, 'width': 2, 'height': 3, 'id': 89}
        self.assertDictEqual(r.to_dictionary(), d)
        r.update(y=1, width=2, x=3, id=89, height=4)
        d = {'x': 3, 'y': 1, 'width': 2, 'height': 4, 'id': 89}
        self.assertDictEqual(r.to_dictionary(), d)

    # ----------------- Additional Tests ------------------------

    def test_P_more_area_tests(self):
        '''Tests area() method with additional cases.'''
        r = Rectangle(0, 10)
        self.assertEqual(r.area(), 0)

        r.width = 5
        r.height = 0
        self.assertEqual(r.area(), 0)

        r.width = 0
        r.height = 0
        self.assertEqual(r.area(), 0)

    def test_Q_more_str_tests(self):
        '''Tests __str__() method with additional cases.'''
        r = Rectangle(1, 1, 1, 1, 1)
        s = '[Rectangle] (1) 1/1 - 1/1'
        self.assertEqual(str(r), s)

        r = Rectangle(1, 1, 1)
        s = '[Rectangle] (1) 1/0 - 1/1'
        self.assertEqual(str(r), s)

        r = Rectangle(1, 1)
        s = '[Rectangle] (1) 0/0 - 1/1'
        self.assertEqual(str(r), s)

    def test_R_more_to_dictionary_tests(self):
        '''Tests to_dictionary() method with additional cases.'''
        r = Rectangle(1, 1, 1, 1, 1)
        d = {'x': 1, 'y': 1, 'width': 1, 'height': 1, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

        r = Rectangle(1, 1, 1)
        d = {'x': 1, 'y': 0, 'width': 1, 'height': 1, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

        r = Rectangle(1, 1)
        d = {'x': 0, 'y': 0, 'width': 1, 'height': 1, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

    def test_S_json_string(self):
        '''Tests from_json_string and to_json_string methods.'''
        r = Rectangle(1, 1)
        json_string = r.to_json_string([{'id': 89}])
        self.assertEqual(json_string, '[{"id": 89}]')
        self.assertEqual(type(json_string), str)

        from_json = Rectangle.from_json_string(json_string)
        self.assertEqual(from_json, [{'id': 89}])
        self.assertEqual(type(from_json), list)

        json_string = Rectangle.to_json_string(None)
        self.assertEqual(json_string, '[]')
        self.assertEqual(type(json_string), str)

        from_json = Rectangle.from_json_string(None)
        self.assertEqual(from_json, [])
        self.assertEqual(type(from_json), list)

        json_string = Rectangle.to_json_string([])
        self.assertEqual(json_string, '[]')
        self.assertEqual(type(json_string), str)

        from_json = Rectangle.from_json_string('[]')
        self.assertEqual(from_json, [])
        self.assertEqual(type(from_json), list)

    def test_T_create(self):
        '''Tests create method.'''
        r = Rectangle(3, 5, 1, 1, 99)
        r_dictionary = r.to_dictionary()
        r2 = Rectangle.create(**r_dictionary)
        self.assertNotEqual(r, r2)
        self.assertIsInstance(r2, Rectangle)
        self.assertDictEqual(r.to_dictionary(), r2.to_dictionary())
        self.assertIsNot(r, r2)

        r = Rectangle(3, 5, 1, 1)
        r_dictionary = r.to_dictionary()
        r2 = Rectangle.create(**r_dictionary)
        self.assertNotEqual(r, r2)
        self.assertIsInstance(r2, Rectangle)
        self.assertDictEqual(r.to_dictionary(), r2.to_dictionary())
        self.assertIsNot(r, r2)

    def test_U_load_from_file(self):
        '''Tests load_from_file method.'''
        r = Rectangle(3, 5, 1, 1, 98)
        r2 = Rectangle(3, 5, 1, 1, 99)
        r3 = Rectangle(4, 6, 2, 2, 100)

        Rectangle.save_to_file([r, r2, r3])
        list_rectangles_output = Rectangle.load_from_file()

        self.assertIsInstance(list_rectangles_output, list)
        self.assertGreater(len(list_rectangles_output), 0)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertEqual(list_rectangles_output[0].__str__(), r.__str__())
        self.assertEqual(list_rectangles_output[1].__str__(), r2.__str__())
        self.assertEqual(list_rectangles_output[2].__str__(), r3.__str__())

        list_rectangles_output = Rectangle.load_from_file()
        self.assertIsInstance(list_rectangles_output, list)
        self.assertEqual(len(list_rectangles_output), 0)

    def test_V_more_update_tests(self):
        '''Tests update() method with more cases.'''
        r = Rectangle(10, 10, 10, 10)
        r.update(x=99)
        s = '[Rectangle] (The code appears to be written to test a Python class representing a Rectangle. The tests cover various aspects of the Rectangle class, including initialization, methods, properties, and JSON serialization.

Here is the code again, this time with proper indentation and comments for clarity:

```python
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    # ----------------- Tests for #1 ------------------------

    def test_A_init_no_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_B_init_height_arg(self):
        '''Tests constructor with height argument only.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'width'"
        self.assertEqual(str(e.exception), s)

    def test_C_init(self):
        '''Tests constructor with valid arguments.'''
        r = Rectangle(10, 20)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_D_init_extra_args(self):
        '''Tests constructor with extra arguments.'''
        r = Rectangle(10, 20, 30, 40, 99, "hello")
        self.assertEqual(r.id, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)

    def test_E_init_with_zero(self):
        '''Tests constructor with zero arguments.'''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 0)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

    def test_F_init_with_negative(self):
        '''Tests constructor with negative arguments.'''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, -20)
        s = "height must be > 0"
        self.assertEqual(str(e.exception), s)

    def test_G_init_with_non_integer(self):
        '''Tests constructor with non-integer arguments.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10.5, 20)
        s = "width must be an integer"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 20.5)
        s = "height must be an integer"
        self.assertEqual(str(e.exception), s)

    def test_H_init_with_zero(self):
        '''Tests constructor with zero arguments.'''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 10)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

    # ----------------- Tests for #2 ------------------------

    def test_I_width_property(self):
        '''Tests width property getter and setter.'''
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        r.width = 30
        self.assertEqual(r.width, 30)
        with self.assertRaises(ValueError) as e:
            r.width = 0
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.width = -10
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

    # ----------------- Tests for #3 ------------------------

    def test_J_height_property(self):
        '''Tests height property getter and setter.'''
        r = Rectangle(10, 20)
        self.assertEqual(r.height, 20)
        r.height = 30
        self.assertEqual(r.height, 30)
        with self.assertRaises(ValueError) as e:
            r.height = 0
        s = "height must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.height = -10
        s = "height must be > 0"
        self.assertEqual(str(e.exception), s)

    # ----------------- Tests for #4 ------------------------

    def test_K_x_property(self):
        '''Tests x property getter and setter.'''
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.x, 30)
        r.x = 50
        self.assertEqual(r.x, 50)
        with self.assertRaises(ValueError) as e:
            r.x = -10
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

    # ----------------- Tests for #5 ------------------------

    def test_L_y_property(self):
        '''Tests y property getter and setter.'''
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.y, 40)
        r.y = 50
        self.assertEqual(r.y, 50)
        with self.assertRaises(ValueError) as e:
            r.y = -10
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

    # ----------------- Tests for #6 ------------------------

    def test_M_area(self):
        '''Tests area() method.'''
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)
        r.width = 5
        r.height = 10
        self.assertEqual(r.area(), 50)

    # ----------------- Tests for #7 ------------------------

    def test_N_display_no_offset(self):
        '''Tests display() method with no offset.'''
        r = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_O_display_with_offset(self):
        '''Tests display() method with offset.'''
        r = Rectangle(2, 2, 2, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n\n\n  ##\n  ##\n")

    # ----------------- Tests for #8 ------------------------

    def test_P_str(self):
        '''Tests __str__() method.'''
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")

        r = Rectangle(1, 1)
        self.assertEqual(str(r), "[Rectangle] (2) 0/0 - 1/1")

    # ----------------- Tests for #9 ------------------------

    def test_Q_display_no_offset(self):
        '''Tests display() method with no offset.'''
        r = Rectangle(2, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n##\n")

    def test_R_display_with_offset(self):
        '''Tests display() method with offset.'''
        r = Rectangle(2, 3, 2, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n  ##\n  ##\n  ##\n")

    # ----------------- Tests for #10 ------------------------

    def test_S_update_args(self):
        '''Tests update() method with *args.'''
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(x=1, height=2, y=3, width=4, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    # ----------------- Tests for #11 ------------------------

    def test_T_update_kwargs(self):
        '''Tests update() method with **kwargs.'''
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")
        r.update(id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(id=89, width=2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(height=3, id=89, width=2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(y=1, width=2, x=3, id=89, height=4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/4")

    # ----------------- Tests for #12 ------------------------

    def test_U_to_dictionary(self):
        '''Tests to_dictionary() method.'''
        r = Rectangle(10, 10, 10, 10)
        d = {'x': 10, 'y': 10, 'width': 10, 'height': 10, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

        r = Rectangle(1, 2, 3, 4, 12)
        d = {'x': 3, 'y': 4, 'width': 1, 'height': 2, 'id': 12}
        self.assertDictEqual(r.to_dictionary(), d)

    def test_V_to_dictionary_from_update(self):
        '''Tests to_dictionary() method from an update().'''
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.to_dictionary(), {'x': 10, 'y': 10, 'width': 10, 'height': 10, 'id': 1})

        r.update(89)
        self.assertEqual(r.to_dictionary(), {'x': 10, 'y': 10, 'width': 10, 'height': 10, 'id': 89})

        r.update(89, 2)
        self.assertEqual(r.to_dictionary(), {'x': 10, 'y': 10, 'width': 2, 'height': 10, 'id': 89})

        r.update(89, 2, 3)
        self.assertEqual(r.to_dictionary(), {'x': 10, 'y': 10, 'width': 2, 'height': 3, 'id': 89})

        r.update(89, 2, 3, 4)
        self.assertEqual(r.to_dictionary(), {'x': 4, 'y': 10, 'width': 2, 'height': 3, 'id': 89})

        r.update(y=1, width=2, x=3, id=89, height=4)
        self.assertEqual(r.to_dictionary(), {'x': 3, 'y': 1, 'width': 2, 'height': 4, 'id': 89})

    # ----------------- Additional Tests ------------------------

    def test_W_more_area_tests(self):
        '''Tests area() method with additional cases.'''
        r = Rectangle(0, 10)
        self.assertEqual(r.area(), 0)

        r.width = 5
        r.height = 0
        self.assertEqual(r.area(), 0)

        r.width = 0
        r.height = 0
        self.assertEqual(r.area(), 0)

    def test_X_more_str_tests(self):
        '''Tests __str__() method with additional cases.'''
        r = Rectangle(1, 1, 1, 1, 1)
        s = '[Rectangle] (1) 1/1 - 1/1'
        self.assertEqual(str(r), s)

        r = Rectangle(1, 1, 1)
        s = '[Rectangle] (1) 1/0 - 1/1'
        self.assertEqual(str(r), s)

        r = Rectangle(1, 1)
        s = '[Rectangle] (1) 0/0 - 1/1'
        self.assertEqual(str(r), s)

    def test_Y_more_to_dictionary_tests(self):
        '''Tests to_dictionary() method with additional cases.'''
        r = Rectangle(1, 1, 1, 1, 1)
        d = {'x': 1, 'y': 1, 'width': 1, 'height': 1, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

        r = Rectangle(1, 1, 1)
        d = {'x': 1, 'y': 0, 'width': 1, 'height': 1, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

        r = Rectangle(1, 1)
        d = {'x': 0, 'y': 0, 'width': 1, 'height': 1, 'id': 1}
        self.assertDictEqual(r.to_dictionary(), d)

    def test_Z_json_string(self):
        '''Tests from_json_string and to_json_string methods.'''
        r = Rectangle(1, 1)
        json_string = r.to_json_string([{'id': 89}])
        self.assertEqual(json_string, '[{"id": 89}]')
        self.assertEqual(type(json_string), str)

        from_json = Rectangle.from_json_string(json_string)
        self.assertEqual(from_json, [{'id': 89}])
        self.assertEqual(type(from_json), list)

        json_string = Rectangle.to_json_string(None)
        self.assertEqual(json_string, '[]')
        self.assertEqual(type(json_string), str)

        from_json = Rectangle.from_json_string("[]")
        self.assertEqual(from_json, [])
        self.assertEqual(type(from_json), list)

    def test_AA_save_to_file_and_from_file(self):
        '''Tests save_to_file and create and load methods.'''
        try:
            os.remove("Rectangle.json")
        except:
            pass

        r = Rectangle(1, 1)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{'id': 1, 'x': 0, 'y': 0, 'width': 1, 'height': 1}])

        loaded = Rectangle.load_from_file()
        self.assertEqual(loaded, [{'id': 1, 'x': 0, 'y': 0, 'width': 1, 'height': 1}])

        r2 = Rectangle(2, 2, 2, 2, 2)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{'id': 1, 'x': 0, 'y': 0, 'width': 1, 'height': 1},
                                                      {'id': 2, 'x': 2, 'y': 2, 'width': 2, 'height': 2}])

        loaded = Rectangle.load_from_file()
        self.assertEqual(loaded, [{'id': 1, 'x': 0, 'y': 0, 'width': 1, 'height': 1},
                                  {'id': 2, 'x': 2, 'y': 2, 'width': 2, 'height': 2}])
