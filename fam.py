from graphviz import Digraph

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.parents = []
        self.children=[]

    def add_parent(self, parent):
        self.parents.append(parent)
        parent.children.append(self)

# Create instances
john = Person("John", "male")
susan = Person("Susan", "female")
peter = Person("Peter", "male")
lisa = Person("Lisa", "female")
michael = Person("Michael", "male")
mary = Person("Mary", "female")
james = Person("James", "male")
anna = Person("Anna", "female")

# Parent-child relationships
peter.add_parent(john)
peter.add_parent(susan)
lisa.add_parent(john)
lisa.add_parent(susan)
michael.add_parent(peter)
michael.add_parent(mary)
anna.add_parent(james)
anna.add_parent(lisa)

# Father condition
def father(child):
    for parent in child.parents:
        if parent.gender == "male":
            return parent
    return None
# Mother condition
def mother(child):
    for parent in child.parents:
        if parent.gender == "female":
            return parent
    return None

# Grandfather condition
def grandfather(child):
    dad=father(child)
    if dad:
        return father(dad)
    return None

# Grandmother condition
def grandmother(child):
    mom=mother(child)
    if mom:
        return mother(mom)
    return None

# Siblings condition
def siblings(person):
    result = []
    for parent in person.parents:
        for sibling in parent.children:
            if sibling != person and sibling not in result:
                result.append(sibling)
    return result

def brother(person):
    return [sibling.name for sibling in siblings(person) if sibling.gender == "male"]

def sister(person):
    return [sibling.name for sibling in siblings(person) if sibling.gender == "female"]

# Uncle condition
def uncle(child):
    for parent in child.parents:
        for sibling in siblings(parent):
            if sibling.gender == "male":
                return sibling.name
    return None

# Aunt condition
def aunt(child):
    for parent in child.parents:
        for sibling in siblings(parent):
            if sibling.gender == "female":
                return sibling.name
    return None

# Cousins condition
def cousin(person):
    cousins = []
    for parent in person.parents:
        for sibling in siblings(parent):
            cousins.extend(cousin.name for cousin in sibling.children)
    return cousins

# Draw tree function
def draw_tree():
    tree = Digraph(comment='Family Tree')
    # Adding individuals
    tree.node('J', 'John')
    tree.node('S', 'Susan')
    tree.node('P', 'Peter')
    tree.node('L', 'Lisa')
    tree.node('M', 'Michael')
    tree.node('Mary', 'Mary')
    tree.node('James', 'James')
    tree.node('A', 'Anna')

    # Adding edges
    tree.edge('J', 'P', label='father')
    tree.edge('S', 'P', label='mother')
    tree.edge('J', 'L', label='father')
    tree.edge('S', 'L', label='mother')
    tree.edge('P', 'M', label='father')
    tree.edge('Mary', 'M', label='mother')
    tree.edge('James', 'A', label='father')
    tree.edge('L', 'A', label='mother')

    # Rendering tree
    tree.render('family_tree', view=True, format='png')

# Testing the functions
print("Father of Peter: ", father(peter).name if father(peter) else None)
print("Mother of Peter: ", mother(peter).name if mother(peter) else None)
print("Grandfather of Michael: ", grandfather(michael).name if grandfather(michael) else None)
print("Grandmother of Michael: ", grandmother(michael).name if grandmother(michael) else None)
print("Brother of Lisa: ", brother(lisa))
print("Sister of Peter: ", sister(peter))
print("Uncle of Michael: ", uncle(michael))
print("Aunt of Anna: ", aunt(anna))
print("Cousins of Michael: ", cousin(michael))

draw_tree()
