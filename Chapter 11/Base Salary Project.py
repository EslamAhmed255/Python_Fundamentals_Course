# Import module 
import time

# Welcome message and inputs
print('Welcome to base salary calculator!')
salary = float(input('Enter your base salary: '))
bonus = float(input('How much bonus did you get: '))
tax = 0.15

# Calculate total salary
def total_salary(salary, bonus):
    return salary + bonus

# Calculate salary after tax
def salary_after_tax(total, tax):
    return total - (total * tax)

# Compute and print result
total = total_salary(salary, bonus)
final_salary = salary_after_tax(total, tax)

time.sleep(2)
print('Calculating your salary...')

time.sleep(1.5)
print('Finding the tax amount in Egypt...')

time.sleep(1.5)
print('Calculating your final salary...')

time.sleep(1.5)
print(f'Your salary after tax = {final_salary}')
print('Thank you for using our app!')