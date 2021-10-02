# Author: Gan Li
# Date: 10/1/21 12:54 下午
# Description:
class Bird:
    def __init__(self):
        pass

    def call(self):
        return 'chirp'


class Duck(Bird):
    def __init__(self):
        super().__init__()

    def call(self):
        return 'quack'


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def gross_monthly_pay(self):
        return self._salary / 12


class SeniorEmployee(Employee):
    def gross_monthly_pay(self):
        return super().gross_monthly_pay() + 500
