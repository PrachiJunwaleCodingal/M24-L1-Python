#pip install numpy (on terminal)
#sorting in ascending order
import numpy as np

data_type = [('name', 'S15'), ('class', int), ('roll', int)]
studDetails = [('Prachi', 5, 32), ('Aryan', 5, 21),('Ayush', 5, 42), ('Sanjay', 5, 11)]


stud = np.array(studDetails, dtype=data_type)   
print("OriginalArray:")
print(stud)
print("Sorting with RollNumber")
print(np.sort(stud, order='roll'))