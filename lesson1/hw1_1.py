''' ЗАДАНИЕ:

1. Создать класс Employee. При инициализации класса (т.е. создании объекта) должны передаваться параметры:
	name - Имя сотрудника
	salary - Зарплата сотрудника.
	Для этого нужен метод __init__

2. класс Employee будет иметь общие аттрибуты (для всех создаваемых объектов):
	emp_count = 0
	work_rate = 2

3. Внутри класса Employee создать метод display_count и установить в нем pass. На следующем занятии он пригодится.

4. Внутри класса Employee создать метод display_employee, который будет печатать
	'Имя: <здесь_должно_печататься Имя сотрудника>. Зарплата: <здесь_должно_печататься Зарплата сотрудника>'

5. Внутри класса Employee создать метод change_name, который будет менять имя у конкретного объекта.

6. Внутри класса Employee создать метод get_total_salary, которая будет возвращать значение из аттрибута salary
'''

class Employee:
    emp_count = 0
    work_rate = 2

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_count(self):
       pass

    def display_employee(self):
        print('Имя:'+ self.name + '   ' 'Зарплата:' + self.salary)

    def change_name(self, name):
        self.name = name

    def get_total_salary(self, salary):
        return self.salary

p1 = Employee('Иван', '200000')
p1.display_employee()
p1.change_name('Саша')
p1.display_employee()
