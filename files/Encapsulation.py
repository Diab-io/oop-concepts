from abc import ABC, abstractmethod
# _(single underscore): protected
# __(Double underscore): private

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self._raise = 0.1  # Encapsulation
    
    def set_raise(self, increase):
        self._raise = increase
    
    def get_raise(self):
        return self._raise

    #Abstraction
    @abstractmethod
    def increment(self):
        pass

class Salesmen(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        Salesmen.set_raise(self, 0.2)

    def increment(self):
        self.salary = self.salary + (self.salary * self._raise)
        return self.salary


class Engineers(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        Engineers.set_raise(self, 0.5)

    def increment(self):
        self.salary = self.salary + (self.salary * self._raise)
        return self.salary


class Guards(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        Guards.set_raise(self, 0.1)
    
    def increment(self):
        self.salary = self.salary + (self.salary * self._raise)
        return self.salary
    

salesman = Salesmen("Adeshina", 75_000)
engineer = Engineers("Paul", 120_000)
guard = Guards("Wasiu", 40_000)

print(f"{salesman.name}'s salary has been increased by {salesman.get_raise()*100}% to {salesman.increment()}\n")
print(f"{engineer.name}'s salary has been increased by {engineer.get_raise()*100}% to {engineer.increment()}\n")
print(f"{guard.name}'s salary has been increased by {guard.get_raise()*100}% to {guard.increment()}")