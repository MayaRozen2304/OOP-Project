from unittest import TestCase
from Collection import Collection


class TestCollection(TestCase):
    def test_add(self):
        a = Collection([1, 2])
        self.assertRaises(NotImplementedError, a.add, 3, 2)


    def test_get_collection(self):
        array = [1, 'a', 8.05]
        collection = Collection(array)
        self.assertEqual(array, collection.get_collection())


    def test_get_item(self):
        array = [1, 'a', 8.05]
        collection = Collection(array)
        self.assertEqual(1, collection.__getitem__(0))
        self.assertEqual(None, collection.__getitem__(4))

    def test_eq(self):
        array = [1, 'a', 8.05]
        array2 = [1, 'a', 8.05]
        array3 = [1, 'a', 8]
        collection1 = Collection(array)
        collection2 = Collection(array2)
        collection3 = Collection(array3)
        self.assertEqual(False, collection1 == 'maya')
        self.assertEqual(True, collection1 == collection2)
        self.assertEqual(False, collection1 == collection3)


    def test_ne(self):
        array = [1, 'a', 8.05]
        array2 = [1, 'a', 8.05]
        array3 = [1, 'a', 8]
        collection1 = Collection(array)
        collection2 = Collection(array2)
        collection3 = Collection(array3)
        self.assertEqual(True, collection1 != 'maya')
        self.assertEqual(False, collection1 != collection2)
        self.assertEqual(True, collection1 != collection3)

    def test_len(self):
        array1 = [1, 'a', 8]
        array2 = []
        collection1 = Collection(array1)
        collection2 = Collection(array2)
        self.assertEqual(3, len(collection1))
        self.assertEqual(0, len(collection2))

    def test_contains(self):
        array1 = [1, 'a', 8]
        collection1 = Collection(array1)
        self.assertEqual(True, collection1.__contains__(1))
        self.assertEqual(False, collection1.__contains__('m'))

    def test_str(self):
        array1 = [1, 'a', 8]
        array2 = []
        collection1 = Collection(array1)
        collection2 = Collection(array2)
        self.assertEqual('1a8', collection1.__str__())
        self.assertEqual('[]', collection2.__str__())

    def test_repr(self):
        array1 = [1, 'a', 8]
        array2 = []
        collection1 = Collection(array1)
        collection2 = Collection(array2)
        self.assertEqual('1a8', collection1.__repr__())
        self.assertEqual('[]', collection2.__repr__())


