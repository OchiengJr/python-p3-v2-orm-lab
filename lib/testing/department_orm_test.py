from __init__ import CONN, CURSOR
from department import Department
import pytest


class TestDepartment:
    '''Test suite for Department class'''

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        '''Fixture to drop tables prior to each test.'''
        with CONN:
            with CONN.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS employees")
                cursor.execute("DROP TABLE IF EXISTS departments")
                Department.all = {}

    def test_creates_table(self):
        '''Test whether create_table() method creates the departments table if it does not exist.'''
        Department.create_table()
        assert CURSOR.execute("SELECT * FROM departments")

    def test_drops_table(self):
        '''Test whether drop_table() method drops the departments table if it exists.'''
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        Department.drop_table()
        result = CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='departments'").fetchone()
        assert result is None

    # Add other test methods...

    def test_get_employees(self):
        '''Test whether employees() method retrieves employees for the current Department instance.'''
        # Avoid circular import by importing Employee within the method
        from employee import Employee  

        Department.create_table()
        department1 = Department.create("Payroll", "Building A, 5th Floor")
        department2 = Department.create("Human Resources", "Building C, 2nd Floor")

        Employee.create_table()
        employee1 = Employee.create("Raha", "Accountant", department1.id)
        employee2 = Employee.create("Tal", "Senior Accountant", department1.id)
        employee3 = Employee.create("Amir", "Manager", department2.id)

        employees = department1.employees()
        assert len(employees) == 2
        assert (employees[0].id, employees[0].name, employees[0].job_title, employees[0].department_id) == (
            employee1.id, employee1.name, employee1.job_title, employee1.department_id)
        assert (employees[1].id, employees[1].name, employees[1].job_title, employees[1].department_id) == (
            employee2.id, employee2.name, employee2.job_title, employee2.department_id)
