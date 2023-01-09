import unittest
from validationClass import TestClass

class InitializationText(unittest.TestCase):
    """Validate the class initialization input and type"""
    def testValidInput(self):
            try:
                TestClass('bob', 15)
                TestClass('bob', 15, False)
            except Exception as err:
                self.fail(f'Initialization of TestClass failed - {repr(err)}')

            return

class AttributesTest(unittest.TestCase):
        def testReadOnlyAttributes(self):
            """Validate the readOnly data as unchanged"""
            defaultInstance = TestClass('bob', 15, True)
            self.assertEqual(defaultInstance.name, 'bob')
            self.assertEqual(defaultInstance.age, 15)
            self.assertEqual(defaultInstance.male, True)

            return

class AddAgeToListTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.defaultInstance = TestClass('bob', 15)

        return super().setUpClass()

    def testValidInput(self):
        try:
            self.defaultInstance.addAgeToList([0,1000,2000])
        except Exception as err:
            self.fail(f'Unable to call addAgeToList - {repr(err)}')

        return