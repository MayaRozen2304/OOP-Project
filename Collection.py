
class Collection:
    def __init__(self, array):
        """
        :param array: a list that includes objects
        """
        self.array = array

    def get_collection(self):
        """
the function will returns the attribute self.array
        :return: attribute self.array
        """
        return self.array

    def add(self, item, option):
        """
this method wont be used in this class therefore, an exception from type NotImplementedError will be raised
        :param item:object we want to add to the array
        :param option: option for an additional variable
        """
        # not use in this class, raise exception
        raise NotImplementedError("error-not adding in collection class")

    def __getitem__(self, i):
        """
the method will returns the element in the i index in the array.
        :param i: the index in the array we want to get
        :return: the element in the i index in the array, if there is no index i, returns None.
        """
        if i < len(self.array):
            return self.array[i]
        else:
            return

    def __eq__(self, other):
        """
checks if two collection element are equal by same element in the same index.
        :param other: the second element we want to check if equals to the certain element.
        :return:boolean value if equals or not.
        """
        # check if we can use this method- only with two objects from collection class
        if not isinstance(other, Collection):
            return False
        # return boolean if the two lists have the same values inside
        else:
            return self.array == other.array

    def __ne__(self, other):
        """
        the function returns true if two collection items are different from each other, else, false.
        :param other:the second element we want to check if equals to the certain element.
        :return:boolean value if not equals or not
        """
        # if eq returns false- object are different, ne returns true.
        if not self.__eq__(other):
            return True
        else:
            return False

    def __len__(self):
        """
the function returns the len of the array by using len method of list.
        :return: the len of the array (int)
        """
        return len(self.array)

    def __contains__(self, item):
        """
    the method checks if a specific value is in the array.
        :param item: the item we want to check if is in the array
        :return: boolean value if the item is in the array
        """
        for i in self.array:
            if i == item:
                return True
        return False

    def __str__(self):
        """
the method create the str method for a collection item by combining all the elements in the array and adds them to
an empty string by order.
        :return: a string with all the elements in th array.
        """
        res = ''
        if len(self.array) == 0:
            return '[]'
        for i in self.array:
            # formatting to string type
            res += str(i)
        return res

    def __repr__(self):
        """
the method returns the str method's output which is identical to the repr method.
        :return:  a string with all the elements in th array.
        """
        return self.__str__()

