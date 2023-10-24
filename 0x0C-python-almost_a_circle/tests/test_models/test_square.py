#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io

class TestSquare(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    # ----------------- Tests for #2 ------------------------
    def test_A_class(self):
        '''Tests Square class type.'''
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        '''Tests if Square inherits Base.'''
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 were given"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Tests instantiation.'''
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Square("1")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        '''Tests positional instantiation.'''
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Tests positional instantiation.'''
        r = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 100, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Tests if id is inherited from Base.'''
        Base._Base__nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''Tests property getters/setters.'''
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 98, '_Rectangle__width': 98,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.size, 98)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    # ----------------- Tests for #3 ------------------------
    def invalid_types(self):
        '''Returns tuple of types for validation.'''
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_type(self):
        '''Tests property validation.'''
        r = Square(1)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)
        s = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as e:
                setattr(r, "width", invalid_type)
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''Tests property validation.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''Tests property validation.'''
        r = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        '''Tests property validation.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        '''Tests property setting/getting.'''
        r = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        '''Tests property setting/getting.'''
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    # ----------------- Tests for #4 ------------------------
    def test_I_area_no_args(self):
        '''Tests area() method signature.'''
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        '''Tests area() method computation.'''
        r = Square(6)
        self.assertEqual(r.area(), 36)
        w = randrange(10) + 1
        r.size = w
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, 7, 8, 9)
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * w)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as e:
            s1.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    # ----------------- Tests for #5 & #7 ------------------------
    def test_J_display_no_args(self):
        '''Tests display() method signature.'''
        r = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_J_display_simple(self):
        '''Tests display() method output.'''
        r = Square(1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.size = 3
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        r = Square(5, 6, 7)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(1, 1, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\










 #
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 3)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        f = io.StringIO()
        with redirect_stdout(f):
            s2.display()
        s = """\
  ##
  ##
"""
        self.assertEqual(f.getvalue(), s)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        f = io.StringIO()
        with redirect_stdout(f):
            s3.display()
        s = """\



 ###
 ###
 ###
"""
        self.assertEqual(f.getvalue(), s)

    # ----------------- Tests for #6 ------------------------
    def test_K_str_no_args(self):
        '''Tests __str__() method signature.'''
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_K_str(self):
        '''Tests __str__() method return.'''
        r = Square(5)
        s = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(r), s)
        r = Square(1, 1)
        s = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(r), s)
        r = Square(3, 4, 5)
        s = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(r), s)
        r = Square(10, 20, 30, 40)
        s = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(r), s)
        r = Square(1, 1, 1, 1)
        s = '[Square] (1) 1/1 - 1'
        self.assertEqual(str(r), s)

    # ----------------- Tests for #9 ------------------------
    def test_L_update_no_args(self):
        '''Tests update() method signature.'''
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_L_update_args(self):
        '''Tests update() method signature.'''
        r = Square(5, 2)
        r.update(10)
        self.assertEqual(str(r), "[Square] (10) 2/0 - 5")
        r.update(10, 10)
        self.assertEqual(str(r), "[Square] (10) 2/0 - 10")
        r.update(10, 10, 10)
        self.assertEqual(str(r), "[Square] (10) 10/0 - 10")
        r.update(10, 10, 10, 10)
        self.assertEqual(str(r), "[Square] (10) 10/10 - 10")
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), "[Square] (10) 10/10 - 10")

    def test_L_update_args_setter(self):
        '''Tests update() method with setters.'''
        r = Square(5, 2)
        r.update(id=10)
        self.assertEqual(str(r), "[Square] (10) 2/0 - 5")
        r.update(width=10, x=10)
        self.assertEqual(str(r), "[Square] (10) 10/0 - 5")
        r.update(y=10, width=10, x=10, id=10)
        self.assertEqual(str(r), "[Square] (10) 10/10 - 10")

    def test_L_update_args_validators(self):
        '''Tests update() method validators.'''
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            r.update(10, "9")
        s = "width must be an integer"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 0)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 10, -1)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(TypeError) as e:
            r.update(10, 10, 10, -1)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

    # ----------------- Tests for #10 ------------------------
    def test_M_kwargs(self):
        '''Tests for kwargs in Square.'''
        r = Square(5, 2)
        r.update(10, 10, 10, 10)
        r.update(size=1)
        self.assertEqual(str(r), "[Square] (10) 10/10 - 1")
        r.update(size=1, id=11)
        self.assertEqual(str(r), "[Square] (11) 10/10 - 1")
        r.update(x=9, size=1, id=11)
        self.assertEqual(str(r), "[Square] (11) 9/10 - 1")
        r.update(y=8, x=9, size=1, id=11)
        self.assertEqual(str(r), "[Square] (11) 9/8 - 1")
        r.update(x=1, y=2, size=3, id=12, random=14)
        self.assertEqual(str(r), "[Square] (12) 1/2 - 3")

    # ----------------- Tests for #11 ------------------------
    def test_N_dict(self):
        '''Tests to_dict() method.'''
        r = Square(10, 2)
        d = {'id': 1, 'x': 2, 'size': 10, 'y': 0}
        self.assertEqual(r.to_dictionary(), d)

    def test_N_dict_more(self):
        '''Tests to_dictionary() method.'''
        Base._Base__nb_objects = 0
        r = Square(1)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'x': 0, 'size': 1, 'y': 0})
        r.update(3, 4, 5, 6)
        self.assertEqual(r.to_dictionary(), {'id': 3, 'x': 5, 'size': 4, 'y': 6})
        r.update(x=12, size=7, y=21)
        self.assertEqual(r.to_dictionary(), {'id': 3, 'x': 12, 'size': 7, 'y': 21})
        r.update(size=7, id=8, y=21, x=12)
        self.assertEqual(r.to_dictionary(), {'id': 8, 'x': 12, 'size': 7, 'y': 21})
        r.update(10)
        self.assertEqual(r.to_dictionary(), {'id': 8, 'x': 12, 'size': 10, 'y': 21})

    def test_O_dict_to_json_string(self):
        '''Tests to_json_string() method.'''
        r = Square(5)
        self.assertEqual(r.to_json_string(None), '[]')
        self.assertEqual(r.to_json_string([]), '[]')
        d = r.to_dictionary()
        s = Base.to_json_string([d])
        self.assertEqual(type(s), str)
        dd = eval(s)
        self.assertEqual(dd, [d])

    # ----------------- Tests for #16 ------------------------
    def test_P_save_to_file_empty(self):
        '''Tests save_to_file() method with no args.'''
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertFalse(os.path.isfile("Square.json"))
        Square.save_to_file([])
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_P_save_to_file_square(self):
        '''Tests save_to_file() method with square instances.'''
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertFalse(os.path.isfile("Square.json"))
        Square.save_to_file(None)
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        r1 = Square(1)
        Square.save_to_file([r1])
        with open("Square.json", "r") as f:
            self.assertNotEqual(f.read(), "[]")

    # ----------------- Tests for #17 ------------------------
    def test_Q_load_from_file_no_file(self):
        '''Tests load_from_file() method with no file.'''
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertFalse(os.path.isfile("Square.json"))
        l = Square.load_from_file()
        self.assertEqual(l, [])

    def test_Q_load_from_file_square(self):
        '''Tests load_from_file() method with square instances.'''
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertFalse(os.path.isfile("Square.json"))
        l = Square.load_from_file()
        self.assertEqual(l, [])
        r1 = Square(1)
        r2 = Square(2)
        Square.save_to_file([r1, r2])
        l = Square.load_from_file()
        self.assertEqual(len(l), 2)
        for r in l:
            self.assertTrue(type(r), Square)

    # ----------------- Tests for #18 ------------------------
    def test_R_save_to_file_None(self):
        '''Tests save_to_file() method with None.'''
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertFalse(os.path.isfile("Square.json"))
        Square.save_to_file(None)
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_R_save_to_file_more(self):
        '''Tests save_to_file() method with more instances.'''
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertFalse(os.path.isfile("Square.json"))
        Square.save_to_file(None)
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        r1 = Square(1, 1)
        Square.save_to_file([r1])
        self.assertTrue(os.path.isfile("Square.json"))
        r1 = Square(1, 1)
        Square.save_to_file([r1])
        self.assertTrue(os.path.isfile("Square.json"))


if __name__ == '__main__':
    unittest.main()
