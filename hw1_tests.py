"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        # TODO:
        self.assertEqual(hw1.vowel_count("Crazy Men"),2)
        self.fail("TODO: write the first unit test for vowel_count")

    def test_vowel_count_empty_string(self):
        # TODO:self.assertEqual(hw1.vowel_count(""),0)
        self.fail("TODO: write the second unit test for vowel_count")

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        # TODO: self.assertEqual(hw1.short_lists([[1,2,3],[2,2], [4,5], [3,2]], 3))
        self.fail("TODO: write the first unit test for short_lists")

    def test_short_lists_no_matching_lengths(self):
        # TODO: self.assertEqual(hw1.short_lists([[1,2,3],[2], [4,1,5], [3,2,6,8]], [3]), [])
        self.fail("TODO: write the second unit test for short_lists")

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        # TODO: self.assertEqual(hw1.ascending_pairs([[4,2],[3,6]]), [[2,4],[3,6]])
        self.fail("TODO: write the first unit test for ascending_pairs")

    def test_ascending_pairs_other_lengths_unchanged(self):
        # TODO: self.assertEqual(hw1.ascending_pairs([[1,6,3],[2,4],[4,5]]), [[1,6,3],[2,4],[4,5]])
        self.fail("TODO: write the second unit test for ascending_pairs")

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(12, 50), data.Price(3, 50)), data.Price(16, 00))
        self.fail("TODO: write the first unit test for add_prices")

    def test_add_prices_with_cents_carry(self):
        # TODO: self.assertEqual(hw1.add_prices(data.Price(12, 70), data.Price(3, 55)), data.Price(16, 25))
        self.fail("TODO: write the second unit test for add_prices")

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # TODO: self.assertEqual(hw1.rectangle_area(0, 0, 4, 3), 12)
        self.fail("TODO: write the first unit test for rectangle_area")

    def test_rectangle_area_negative_coordinates(self):
        # TODO: self.assertEqual(hw1.rectangle_area(-2, -3, 2, 3), 12)

        self.fail("TODO: write the second unit test for rectangle_area")

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # TODO:self.assertEqual(hw1.books_by_author([data.Book("Author 1", "Book 1"), data.Book("Author 2", "Book 2")], "Author 1"), [data.Book("Author 1", "Book 1")])
        self.fail("TODO: write the first unit test for books_by_author")

    def test_books_by_author_no_matches(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.fail("TODO: write the second unit test for books_by_author")

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # TODO: self.assertEqual(hw1.circle_bound(0, 0, 4, 4), 2 * math.sqrt(2))
        self.fail("TODO: write the first unit test for circle_bound")

    def test_circle_bound_non_square_rectangle(self):
        # TODO: self.assertEqual(hw1.circle_bound(0, 0, 4, 3), 2.5)
        self.fail("TODO: write the second unit test for circle_bound")

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # TODO: self.assertEqual(hw1.below_pay_average([data.Employee("Alice", 50000), data.Employee("Bob", 60000)]), [data.Employee("Alice", 50000)])
        self.fail("TODO: write the first unit test for below_pay_average")

    def test_below_pay_average_empty_list(self):
        # TODO: self.assertEqual(hw1.below_pay_average([]), [])
        self.fail("TODO: write the second unit test for below_pay_average")


if __name__ == '__main__':
    unittest.main()
