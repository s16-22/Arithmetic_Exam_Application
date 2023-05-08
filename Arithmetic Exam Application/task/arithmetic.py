# write your code here
import random
import sys


class InputError(Exception):
    def __str__(self):
        return "Incorrect format."


class Calculator(InputError):
    def __init__(self):
        self.level = None
        self.description = None
        self.task1 = None
        self.result1 = None
        self.task2 = None
        self.result2 = None
        self.answer = None
        self.number = None
        self.right_answer = 0
        self.attempts = 5

    def generator(self):
        self.task1 = f'{random.randint(2, 9)}{random.choice("+-*")}{random.randint(2, 9)}'
        self.result1 = eval(self.task1)
        self.task2 = random.randint(11, 29)
        self.result2 = pow(self.task2, 2)
        return self.task1, self.result1, self.task2, self.result2

    def intro(self):
        try:
            print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
            self.answer = input()
            if not self.answer.isdigit() or int(self.answer) > 2:
                raise InputError
            else:
                if int(self.answer) == 1:
                    self.simple_operations()
                elif int(self.answer) == 2:
                    self.integral_squares()
        except InputError as err:
            print(err)
            return self.intro()

    def check_input(self):
        try:
            self.number = int(input())
            return self.number
        except ValueError:
            print("Incorrect format.")
        return self.check_input()

    def simple_operations(self):
        task1, result1, task2, result2 = self.generator()
        self.level = 1
        self.description = '(simple operations with numbers 2-9)'
        print(task1)
        number = self.check_input()
        if int(number) == result1:
            print('Right!')
            self.right_answer += 1
        else:
            print("Wrong!")
        self.attempts -= 1
        if self.attempts == 0:
            self.save()
        return self.simple_operations()

    def integral_squares(self):
        task1, result1, task2, result2 = self.generator()
        self.level = 2
        self.description = '(integral squares 11-29)'
        print(task2)
        number = self.check_input()
        if int(number) == result2:
            print('Right!')
            self.right_answer += 1
        else:
            print("Wrong!")
        self.attempts -= 1
        if self.attempts == 0:
            self.save()
        return self.integral_squares()

    def save(self):
        print(f"Your mark is {self.right_answer}/5. Would you like to save your result to the file? Enter yes or no.")
        decision = input()
        if decision == "yes" or decision == "YES" or decision == "y" or decision == "Yes":
            print("What is your name?")
            name = input()
            file = open('results.txt', 'a')
            file.write(f'{name}: {self.right_answer}/5 in level {self.level} {self.description}\n')
            file.close()
            print('The results are saved in "results.txt".')
            sys.exit()
        else:
            sys.exit()


calc = Calculator()

if __name__ == '__main__':
    calc.intro()
