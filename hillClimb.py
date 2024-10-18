import random

def objective_function(x):
    #quadratic function to maximize
    return -x**2+5*x

def generate_neighbour(current_x,step_size):
    #generate neighbouring solution by adding or substracting a step size
    return current_x+random.uniform(-step_size,step_size)

def hill_climbing(starting_point,step_size,max_iterations):
    current_x=starting_point
    current_value=objective_function(current_x)

    for i in range(max_iterations):
        neighbour_x=generate_neighbour(current_x,step_size)
        neighbour_value=objective_function(neighbour_x)

        if (neighbour_value>current_value):
            current_x=neighbour_x
            current_value=neighbour_value
        return current_x,current_value

starting_point=random.uniform(0,4)
step_size=0.1
max_iterations=100
best_x,best_value=hill_climbing(starting_point,step_size,max_iterations)
print(f"Best X : {best_x}, \nBest value : {best_value}")
