#!/usr/bin/python3
'''Module for Base unit tests.'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def setUp(self):
        """Set up before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up after each test."""

    def test_A_nb_objects_private(self):
        """Test if nb_objects is a private class attribute."""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        """Test if nb_objects initializes to zero."""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        """Test Base() instantiation."""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        """Test constructor signature."""
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        """Test constructor signature with 2 non-self args."""
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        """Test consecutive ids."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        """Test sync between class and instance id."""
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_F_id_synced_more(self):
        """Test sync between class and instance id with more instances."""
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        """Test custom int id."""
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_str(self):
        """Test custom str id."""
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_id_keyword(self):
        """Test id passed as a keyword argument."""
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

    # ----------------- Tests for #15 ------------------------
    def test_H_to_json_string(self):
        """Test to_json_string() method."""
        # Add your tests for to_json_string() here
        pass

    # ----------------- Tests for #17 ------------------------
    def test_H_test_from_json_string(self):
        """Test from_json_string() method."""
        # Add your tests for from_json_string() here
        pass

    # ----------------- Tests for #16 ------------------------
    def test_I_save_to_file(self):
        """Test save_to_file() method."""
        # Add your tests for save_to_file() here
        pass

    # ----------------- Tests for #18 ------------------------
    def test_J_create_rectangle(self):
        """Test create() method for Rectangle."""
        # Add your tests for create() method for Rectangle here
        pass

    def test_J_create_square(self):
        """Test create() method for Square."""
        # Add your tests for create() method for Square here
        pass

    # ----------------- Tests for #19 ------------------------
    def test_K_load_from_file(self):
        """Test load_from_file() method for Rectangle and Square."""
        # Add your tests for load_from_file() method for Rectangle and Square here
        pass


if __name__ == "__main__":
    unittest.main()
