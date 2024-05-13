from department import Department
from employee import Employee
import pytest


class TestEmployeeProperties:
    '''Test suite for Employee class properties validation'''

    @pytest.fixture(autouse=True)
    def reset_db(self):
        '''Fixture to drop and recreate tables prior to each test.'''
        Employee.drop_table()
        Department.drop_table()
        Employee.create_table()
        Department.create_table()
        Department.all = {}
        Employee.all = {}

    def test_valid_name(self):
        '''Validates name property is assigned a valid string'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Lee", "Manager", department.id)
        assert employee.name == "Lee"

    def test_name_type(self):
        '''Validates name property type'''
        with pytest.raises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create(7, "Manager", department.id)

    def test_name_length(self):
        '''Validates name property length > 0'''
        with pytest.raises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create("", "Manager", department.id)

    # Similar tests for job_title, department_id, and their respective validations

    def test_valid_department(self):
        '''Validates department property'''
        department = Department.create("Payroll", "Building C, 3rd Floor")
        employee = Employee.create("Raha", "Accountant", department.id)
        assert employee.department_id == department.id

    def test_invalid_department_fk(self):
        '''Validates department property foreign key constraint'''
        with pytest.raises(ValueError):
            employee = Employee.create("Raha", "Accountant", 7)

    def test_invalid_department_type(self):
        '''Validates department property type'''
        with pytest.raises(ValueError):
            employee = Employee.create("Raha", "Accountant", "abc")

    # Add more test methods as needed to cover additional scenarios
