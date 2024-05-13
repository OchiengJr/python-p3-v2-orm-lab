from department import Department
from employee import Employee
from faker import Faker
import pytest


class TestEmployee:
    '''Test suite for Employee class'''

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        '''Fixture to drop tables prior to each test.'''
        CURSOR.execute("DROP TABLE IF EXISTS employees")
        CURSOR.execute("DROP TABLE IF EXISTS departments")
        Department.all = {}
        Employee.all = {}

    def test_creates_table(self):
        '''Test method for create_table() that creates table "employees" if it does not exist.'''
        Department.create_table()  # Ensure Department table exists due to FK constraint
        Employee.create_table()
        assert CURSOR.execute("SELECT * FROM employees")

    # Add other test methods following the same structure
    # Ensure each test method is well-commented, isolated, and covers specific functionality
    # Consider refactoring common setup/teardown code into fixtures for better reuse and readability
