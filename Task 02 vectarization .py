#mathematical function and vectorization
#vectorization means performing a mathematical operation on many 
#value at once instead of using a loop to proces each value

#Examle of  calculate the sine  of  every number


import numpy as np
x=np.array([0, np.pi/2,np.pi])
result=np.sin(x)
print(result)


#understanding the mathematical concept
#y=sin**2(x)+cos**2(x)
#in mathematic we now that sin**2(2)+cos**2(x)=1


import numpy as np
x=np.array([0,np.pi/2,np.pi])
y=np.sin(x)**2+np.cos(x)**2
print(y)

 
# simple one
#squaring a number
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9])
y=x**2
print("First five readings:",y[:5])
print(y)

#my own example
# Real-world example: Calculating marks for
# Computer Science students at Mount Kenya University

import numpy as np
import matplotlib.pyplot as plt

# Students doing Computer Science
names = np.array(["Amina", "Ali", "Ifrah", "Fatma", "Grace"])

# Marks for five units
marks = np.array([
    [40, 60, 50, 80, 70],
    [79, 56, 78, 50, 66],
    [60, 70, 70, 60, 80],
    [40, 50, 50, 60, 70],
    [70, 50, 70, 80, 40]
])

# Calculate each student's mean mark
mean_marks = np.mean(marks, axis=1)

# Display student results and assign grades
print("MKU COMPUTER SCIENCE STUDENT RESULTS")

grades = []

for i in range(len(names)):

    if mean_marks[i] >= 70:
        grade = "A"
    elif mean_marks[i] >= 60:
        grade = "B"
    elif mean_marks[i] >= 50:
        grade = "C"
    elif mean_marks[i] >= 40:
        grade = "D"
    else:
        grade = "E"

    grades.append(grade)

    print("Student:", names[i])
    print("Unit marks:", marks[i])
    print("Mean mark:", mean_marks[i])
    print("Mean grade:", grade)
   
# Plot students' mean marks
plt.bar(names, mean_marks)

plt.axhline(50, linestyle="--", label="Pass mark (50)")

plt.xlabel("Students")
plt.ylabel("Mean Marks")
plt.title("MKU Computer Science Students' Mean Marks")

plt.legend()
plt.show()




