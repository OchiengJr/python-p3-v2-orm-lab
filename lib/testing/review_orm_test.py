from employee import Employee, CURSOR
from department import Department
from review import Review
import pytest


class TestReview:
    '''Test suite for Review class functionality'''

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        '''Fixture to drop tables prior to each test'''
        CURSOR.execute("DROP TABLE IF EXISTS reviews")
        CURSOR.execute("DROP TABLE IF EXISTS employees")
        CURSOR.execute("DROP TABLE IF EXISTS departments")

    def test_create_table(self):
        '''Test creating reviews table'''
        Department.create_table()
        Employee.create_table()
        Review.create_table()
        assert CURSOR.execute("SELECT * FROM reviews")

    def test_drop_table(self):
        '''Test dropping reviews table'''
        Department.create_table()
        Employee.create_table()
        Review.create_table()
        Review.drop_table()
        assert not CURSOR.execute("SELECT * FROM reviews").fetchone()

    def test_save_review(self):
        '''Test saving a review'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Sasha", "Manager", department.id)
        review = Review(2023, "Excellent Python skills!", employee.id)
        review.save()
        saved_review = Review.find_by_id(review.id)
        assert saved_review.year == 2023
        assert saved_review.summary == "Excellent Python skills!"
        assert saved_review.employee_id == employee.id

    def test_create_review(self):
        '''Test creating a review'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Kai", "Web Developer", department.id)
        review = Review.create(2023, "Excellent Python skills!", employee.id)
        assert review.year == 2023
        assert review.summary == "Excellent Python skills!"
        assert review.employee_id == employee.id

    def test_instance_from_db(self):
        '''Test creating Review instance from database row'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Raha", "Accountant", department.id)
        CURSOR.execute("INSERT INTO reviews (year, summary, employee_id) VALUES (2022, 'Amazing coder!', ?)", (employee.id,))
        row = CURSOR.execute("SELECT * FROM reviews").fetchone()
        review = Review.instance_from_db(row)
        assert review.year == 2022
        assert review.summary == "Amazing coder!"
        assert review.employee_id == employee.id

    def test_find_by_id(self):
        '''Test finding a review by id'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Raha", "Accountant", department.id)
        review1 = Review.create(2020, "Great coder!", employee.id)
        id1 = review1.id
        review2 = Review.create(2000, "Awesome coder!", employee.id)
        id2 = review2.id
        found_review1 = Review.find_by_id(id1)
        found_review2 = Review.find_by_id(id2)
        assert found_review1.year == 2020
        assert found_review1.summary == "Great coder!"
        assert found_review1.employee_id == employee.id
        assert found_review2.year == 2000
        assert found_review2.summary == "Awesome coder!"
        assert found_review2.employee_id == employee.id
        assert Review.find_by_id(3) is None

    def test_update(self):
        '''Test updating a review'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Raha", "Accountant", department.id)
        review1 = Review.create(2020, "Usually double checks their work", employee.id)
        id1 = review1.id
        review2 = Review.create(2000, "Takes long lunches", employee.id)
        id2 = review2.id
        review1.year = 2023
        review1.summary = "Always double checks their work"
        review1.update()
        updated_review1 = Review.find_by_id(id1)
        assert updated_review1.year == 2023
        assert updated_review1.summary == "Always double checks their work"
        assert updated_review1.employee_id == employee.id
        assert Review.find_by_id(id2) == review2

    def test_delete(self):
        '''Test deleting a review'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Raha", "Accountant", department.id)
        review1 = Review.create(2020, "Usually double checks their work", employee.id)
        id1 = review1.id
        review2 = Review.create(2000, "Takes long lunches", employee.id)
        id2 = review2.id
        review1.delete()
        assert Review.find_by_id(id1) is None
        assert Review.find_by_id(id2) == review2

    def test_get_all(self):
        '''Test getting all reviews'''
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Raha", "Accountant", department.id)
        review1 = Review.create(2020, "Great coder!", employee.id)
        id1 = review1.id
        review2 = Review.create(2000, "Awesome coders!", employee.id)
        id2 = review2.id
        reviews = Review.get_all()
        assert len(reviews) == 2
        assert reviews[0].id == id1
        assert reviews[0].year == 2020
        assert reviews[0].summary == "Great coder!"
        assert reviews[0].employee_id == employee.id
        assert reviews[1].id == id2
        assert reviews[1].year == 2000
        assert reviews[1].summary == "Awesome coders!"
        assert reviews[1].employee_id == employee.id
