arr=(input("enter numbers")) #take input, it is string type : 1 2 3 4
arr=list(arr.split()) #split the string based on space between them and then convert to list
arr = list(map(int, arr)) #each element in the list is a string, so convert it to integer

out=[] #array for the output
grt=0 #stores greatest value from the right of the array

for i in range (len(arr)-1,0,-1): #to iterate from last element to first
    if(i==(len(arr)-1)): #by default last element is always considered since thers no element after it
        grt=arr[i]  
        out.append(arr[i]) #this is appended 

    elif (arr[i]>grt):
        grt=arr[i] #stores greatest value from the last
        out.append(grt) #this is appended 
out=out[-1::-1] #we have stored in reverse order, hence to store in right order we need to reverse the string

print(out)


    


 
