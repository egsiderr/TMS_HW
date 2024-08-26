class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        return (f"Pizza(size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni}, "
                f"mushrooms={self.mushrooms}, onions={self.onions}, bacon={self.bacon})")
    
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def add_cheese(self):
        self.pizza.cheese = True
        return self
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self
    
    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self
    
    def add_onions(self):
        self.pizza.onions = True
        return self
    
    def add_bacon(self):
        self.pizza.bacon = True
        return self
    
    def build(self):
        return self.pizza
    
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_pizza(self):
        return self.builder.build()
    
builder = PizzaBuilder()
builder.set_size("Big").add_cheese().add_pepperoni().add_mushrooms().add_onions().add_bacon()
director = PizzaDirector(builder)
pizza = director.build_pizza()
print(pizza)
