from department import Department
import pytest


class TestDepartmentProperties:
    '''Test suite for Department properties'''

    @pytest.fixture(autouse=True)
    def clear_department_dictionary(self):
        '''Fixture to clear the Department class dictionary.'''
        Department.all = {}

    def test_name_location_valid(self):
        '''Validates that name and location are assigned valid non-empty strings.'''
        # Should not raise an exception
        department = Department("Payroll", "Building A, 5th Floor")

    def test_name_is_string(self):
        '''Validates that the name property is assigned a string.'''
        department = Department("Payroll", "Building A, 5th Floor")
        with pytest.raises(ValueError):
            department.name = 7

    def test_name_string_length(self):
        '''Validates that the name property length is greater than 0.'''
        department = Department("Payroll", "Building A, 5th Floor")
        with pytest.raises(ValueError):
            department.name = ''

    def test_location_is_string(self):
        '''Validates that the location property is assigned a string.'''
        department = Department("Payroll", "Building A, 5th Floor")
        with pytest.raises(ValueError):
            department.location = True

    def test_location_string_length(self):
        '''Validates that the location property length is greater than 0.'''
        department = Department("Payroll", "Building A, 5th Floor")
        with pytest.raises(ValueError):
            department.location = ''
