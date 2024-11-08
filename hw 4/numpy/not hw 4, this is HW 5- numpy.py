#The odd ones out
import numpy as np 

#defined the function 
def onlyOdd(arr):
    mask = np. all(arr % 2 != 0, axis=1)
    return arr[mask]

arr =  np.array([[1, 2, 3], [5, 7, 9], [2, 4, 6], [7, 7, 7]])
result = onlyOdd(arr)
print(result)

# lets play checkers
# 2.1 
 #defined the function and made sure elements are integers
def simplecheckerboard():
    matrix = np.zeros ((8, 8), dtype=int)
    return matrix 
print(simplecheckerboard())

# lets play checkers
# 2.2 
def alternatingcheckerboard():
    #first defining the matrix as a 8 x 8 matrix with zeros 
    matrix = np.zeros ((8, 8), dtype=int)
    pattern = [1, 0, 1, 0, 1, 0, 1, 0]
    #will make every other row (odd) the the same pattern thru slicing 
    matrix[::2] = pattern
    return matrix 
print (alternatingcheckerboard())

#2.3 
def evenandoddcheckerboard():
    #first defining the matrix as a 8 x 8 matrix with zeros 
    matrix = np.zeros ((8, 8), dtype=int)
    #defining them as two seperate patterns 
     #slicing them to get each pattern to show up in every other column
    pattern_odd_value_start = [1, 0, 1, 0, 1, 0, 1, 0]
    matrix[::2] = pattern_odd_value_start
    pattern_even_value_start = [0,1, 0, 1, 0, 1, 0, 1]
    matrix[1::2] = pattern_even_value_start
    return matrix
print (evenandoddcheckerboard())
   
#2.4 
def reversecheckerboard():
    #first defining the matrix as a 8 x 8 matrix with zeros 
    matrix = np.zeros ((8, 8), dtype=int)
    #defining them as two seperate patterns 
     #slicing them to get each pattern to show up in every other column
    pattern_odd_value_start = [0,1, 0, 1, 0, 1, 0, 1]
    matrix[::2] = pattern_odd_value_start
    pattern_even_value_start = [1, 0, 1, 0, 1, 0, 1, 0]
    matrix[1::2] = pattern_even_value_start
    return matrix
print (reversecheckerboard())

#3 the expanding universe 
import numpy as np
def expansion(arr, num_spaces):
    space = ' ' * num_spaces 
    expanded_arr = np.array([''.join(list(word)).replace('', space) for word in arr])
    return expanded_arr
universe = np.array (['galaxy' , 'clusters'])
print(expansion(universe, 1))    
print(expansion(universe, 2))       

#4
import numpy as np 
def second_largest(array): 
    result = []
#checking for the second largest values 
    for column in array.T:
        unique_values = np. unique(column)
        if len(unique_values) > 1: 
            result.append(unique_values[-2])
        else:
            result.append(unique_values[0])
    return np.array(result)
#geting the same randomized list of numbers on the randomized array 
np.random.seed(42)
planets = np.random.randint(100, 1000, (5, 5)) 
print (" exoplanets array:")
print (planets)
print ("second largest exoplanets:")
print(second_largest(planets))
