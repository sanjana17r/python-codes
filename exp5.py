def ishyp(arr):
    calc=((arr[0]**2)+(arr[1]**2))**0.5

    if(calc==arr[2]):
        return True
    else:
        return False


arr=(input("enter numbers")) #take input, it is string type : 1 2 3 4
arr=list(arr.split()) #split the string based on space between them and then convert to list
arr = list(map(int, arr)) #each element in the list is a string, so convert it to integer

arr.sort()
print(ishyp(arr))




    


 
