import unittest

# change file name below
# make sure that name of the class
# defining unit test is "unit_test"
from unit_test_file import unit_test


class assignment_test:
    def get_unit_test():
        return unittest.makeSuite(unit_test)
