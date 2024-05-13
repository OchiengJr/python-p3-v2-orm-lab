#!/usr/bin/env python3

import random
from department import Department
from employee import Employee
from review import Review
import ipdb


def reset_database():
    try:
        # Drop existing tables and create new ones
        Review.drop_table()
        Employee.drop_table()
        Department.drop_table()
        Department.create_table()
        Employee.create_table()
        Review.create_table()

        # Create seed data
        payroll = Department.create("Payroll", "Building A, 5th Floor")
        human_resources = Department.create(
            "Human Resources", "Building C, East Wing")
        employee1 = Employee.create("Lee", "Manager", payroll.id)
        employee2 = Employee.create("Sasha", "Manager", human_resources.id)
        Review.create(2023, "Efficient worker", employee1.id)
        Review.create(2022, "Good work ethic", employee1.id)
        Review.create(2023, "Excellent communication skills", employee2.id)

        # Optionally, you can add code here to generate random seed data
        # For example:
        # for _ in range(10):
        #     name = generate_random_name()
        #     job_title = generate_random_job_title()
        #     department_id = random.choice([payroll.id, human_resources.id])
        #     employee = Employee.create(name, job_title, department_id)
        #     year = random.randint(2010, 2025)
        #     summary = generate_random_review_summary()
        #     Review.create(year, summary, employee.id)

    except Exception as e:
        print(f"An error occurred: {e}")

# Function to generate random name, job title, and review summary
# You can implement these functions based on your requirements

# def generate_random_name():
#     # Implement logic to generate random name
#     pass

# def generate_random_job_title():
#     # Implement logic to generate random job title
#     pass

# def generate_random_review_summary():
#     # Implement logic to generate random review summary
#     pass


reset_database()
ipdb.set_trace()
