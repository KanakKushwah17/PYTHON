from Mypackage.for_add import students
from Mypackage.for_total import total

def percentage():
    return total(students["marks"])/len(students["marks"])