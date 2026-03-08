# Problem: MovingTotal
#
# Design a data structure with two methods:
#
# 1. append(numbers)
#    - numbers is a list of integers to add to the existing sequence
#
# 2. contains(total)
#    - return True if any 3 consecutive numbers in the full sequence
#      sum to total
#    - otherwise return False
#
# Example:
#   append([1, 2, 3, 4])
#   consecutive groups of 3:
#       1 + 2 + 3 = 6
#       2 + 3 + 4 = 9
#
#   contains(6)  -> True
#   contains(9)  -> True
#   contains(12) -> False
#
#   append([5])
#   new consecutive group:
#       3 + 4 + 5 = 12
#
#   contains(12) -> True
#
# Key idea:
# - store all numbers that have been appended
# - every time a new number is added, check whether it completes a new
#   group of 3 consecutive numbers
# - store each 3-number sum in a set for fast O(1) lookup in contains()


class MovingTotal:
    def __init__(self):
        # Store every number that has been appended so far
        self.numbers = []

        # Store sums of all 3-consecutive-number windows
        # A set is used because membership checking is fast: O(1) average
        self.totals = set()

    def append(self, numbers):
        """
        Add new numbers to the data structure.

        For each new number:
        - append it to self.numbers
        - if there are now at least 3 numbers total,
          compute the sum of the last 3 consecutive numbers
          and store that sum in self.totals
        """
        for num in numbers:
            # Add the new number to our running list
            self.numbers.append(num)

            # Only compute a 3-number total if we have at least 3 numbers
            if len(self.numbers) >= 3:
                # Last 3 consecutive numbers:
                # self.numbers[-3], self.numbers[-2], self.numbers[-1]
                current_total = (
                    self.numbers[-3] +
                    self.numbers[-2] +
                    self.numbers[-1]
                )

                # Store this total for fast future lookup
                self.totals.add(current_total)

    def contains(self, total):
        """
        Return True if any 3 consecutive numbers sum to total.
        Otherwise return False.
        """
        return total in self.totals


if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))    # True  -> 1+2+3
    print(movingtotal.contains(9))    # True  -> 2+3+4
    print(movingtotal.contains(12))   # False
    print(movingtotal.contains(7))    # False

    movingtotal.append([5])
    print(movingtotal.contains(6))    # True
    print(movingtotal.contains(9))    # True
    print(movingtotal.contains(12))   # True  -> 3+4+5
    print(movingtotal.contains(7))    # False