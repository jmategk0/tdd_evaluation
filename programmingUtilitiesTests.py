import unittest
import programmingUtilities


class TestComparisonToolsMethods(unittest.TestCase):

    def setUp(self):
        self.programing_utilities = programmingUtilities.ComparisonTools()
        self.example_string1 = "ABC123"
        self.example_string2 = "XYZ123"
        self.example_list1 = ["Cat", "Dog", "Panda", "Rat", "Cat", "Human", "Panda", "Left", "Dog"]
        self.example_list2 = ["Car", "The", "Sky", "Panda", "No", "Ink", "Blue", "Yes", "Life", "Cat", "Bird"]
        self.example_list3 = [{"user_ID": 1, "username": "John Doe"},
                              {"user_ID": 23, "username": "Jane Doe"},
                              {"user_ID": 8, "username": "James Doe"}]
        self.example_list4 = [{"phone_ID": 3, "user_ID": 23, "phone_type": "Cell", "phone_number": 2068675309},
                              {"phone_ID": 5, "user_ID": 1, "phone_type": "Cell", "phone_number": 2068775309},
                              {"phone_ID": 90, "user_ID": 8, "phone_type": "Cell", "phone_number": 2069675309},
                              {"phone_ID": 12, "user_ID": 23, "phone_type": "Home", "phone_number": 2068672309},
                              {"phone_ID": 4, "user_ID": 8, "phone_type": "Work", "phone_number": 2064675309}]
        self.example_list5 = ["user_ID", "phone_ID", "phone_type", "username", "phone_number"]
        self.example_string3 = "racecar"
        self.example_string4 = "Computer"
        self.example_list6 = [72, 100, 11, 51, 80, 90, 75, 83, 88, 75, 97]

    def test_compare_two_strings(self):
        # arrange
        test_string1 = self.example_string1
        test_string2 = self.example_string2

        # act
        unique_substring = self.programing_utilities.compare_two_strings(test_string1, test_string2)

        # assert
        self.assertEqual(unique_substring, "XYZ")

    def test_clean_strings(self):
        # arrange
        test_list = self.example_list5
        final_list = ["User ID", "Phone ID", "Phone Type", "Username", "Phone Number"]

        # act
        clean_string_list = self.programing_utilities.clean_strings(test_list)

        # assert
        self.assertEqual(clean_string_list, final_list)

    def test_is_string_palindrome_true(self):
        # arrange
        test_string = self.example_string3
        final_boolean = True

        # act
        is_pal = self.programing_utilities.is_string_palindrome(test_string)

        # assert
        self.assertEqual(is_pal, final_boolean)

    def test_is_string_palindrome_false(self):
        # arrange
        test_string = self.example_string4
        final_boolean = False

        # act
        is_pal = self.programing_utilities.is_string_palindrome(test_string)

        # assert
        self.assertEqual(is_pal, final_boolean)

    def test_remove_duplicates_from_list(self):
        # arrange
        test_list = self.example_list1
        final_list = ["Cat", "Dog", "Human", "Left", "Panda", "Rat"]

        # act
        unique_values_from_list = self.programing_utilities.remove_duplicates_from_list(test_list)

        # assert
        self.assertEqual(unique_values_from_list, final_list)

    def test_compare_two_lists(self):
        # arrange
        list1 = self.example_list1
        list2 = self.example_list2
        final_list = ["Cat", "Panda"]

        # act
        values_in_both_lists = self.programing_utilities.compare_two_lists(list1, list2)

        # assert
        self.assertEqual(values_in_both_lists, final_list)

    def test_join_two_lists_of_dictionaries(self):
        # arrange
        list1 = self.example_list3
        list2 = self.example_list4

        final_list = [
            {"phone_ID": 3, "user_ID": 23, "phone_type": "Cell", "phone_number": 2068675309, "username": "Jane Doe"},
            {"phone_ID": 5, "user_ID": 1, "phone_type": "Cell", "phone_number": 2068775309, "username": "John Doe"},
            {"phone_ID": 90, "user_ID": 8, "phone_type": "Cell", "phone_number": 2069675309, "username": "James Doe"},
            {"phone_ID": 12, "user_ID": 23, "phone_type": "Home", "phone_number": 2068672309, "username": "Jane Doe"},
            {"phone_ID": 4, "user_ID": 8, "phone_type": "Work", "phone_number": 2064675309, "username": "James Doe"}]

        # act
        values_in_both_lists = self.programing_utilities.join_two_lists_of_dictionaries(list1, list2)

        # assert
        self.assertEqual(values_in_both_lists, final_list)

    def test_calculate_mean(self):
        # arrange
        list1 = self.example_list6
        final_value = 74.73

        # act
        mean = self.programing_utilities.calculate_mean(list1)

        # assert
        self.assertEqual(mean, final_value)

    def test_calculate_mode(self):
        # arrange
        list1 = self.example_list6
        final_value = 75

        # act
        mode = self.programing_utilities.calculate_mode(list1)

        # assert
        self.assertEqual(mode, final_value)

    def test_calculate_median(self):
        # arrange
        list1 = self.example_list6
        final_value = 80.00

        # act
        median = self.programing_utilities.calculate_median(list1)

        # assert
        self.assertEqual(median, final_value)

programming_utilities_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestComparisonToolsMethods)
unittest.TextTestRunner(verbosity=2).run(programming_utilities_test_suite)
