year=int(input("enter the year  "))
month=input("enter the month like jan,feb,etc  ")
#----------------------for year: if its leap year or not and then add odd days on the basis--------------------------------------------
if(year%100==0):
    if(year%400==0):
        yrodd=2 #using it for counting the total number of odd days for that year
        flag=1
    else:
        yrodd=1
        flag=0
elif(year%4==0):
    yrodd=2
    flag=1
else:
    yrodd=1
    flag=0

#------------------------odd days for month------------------------------------------

if(month in 'jan'):
    no=31
    monodd=0
if(month in 'feb'):
    no=28
    monodd=3
    if(flag==1):
        no=29
if(month in 'march'):
    no=31
    monodd=3
if(month in 'april'):
    no=30
    monodd=6
if(month in 'may'):
    no=31
    monodd=8
if(month in 'june'):
    no=30
    monodd=11
if(month in 'july'):
    no=31
    monodd=13
if(month in 'aug'):
    no=31
    monodd=16
if(month in 'sept'):
    no=30
    monodd=19
if(month in 'oct'):
    no=31
    monodd=21
if(month in 'nov'):
    no=30
    monodd=24
if(month in 'dec'):
    no=31
    monodd=26

if(flag==1 and month not in 'jan' and month not in 'feb'): 
    monodd=monodd+1 #if its leap year: the months after feb will add an extra odd day

rem=year%400


x=year#dummy
quo=int(year/400)#dummy variable
ref=quo*400#dummy variable


if rem>100:    #    example for 1921- remiander will be 321
    newquo=int(rem/100) #only for convenience to write 100's in tems of 1's
#in this ex: newquo--321/100---> 3
    rem=rem%100 #check the remainder, i.e 21 in this case for 321
    if (newquo==1): #from the table of centuries, to calculate, which century has how mnay odd days
        yrodd=5
    if (newquo==2):
        yrodd=3
    if (newquo==3):
        yrodd=1

if(rem!=0):#need to calculate odd days if rem is not 0

    lpyears=int(rem/4)
    lpyears=lpyears+1
    noryears=rem-lpyears
    yrodd=lpyears*2+noryears

monodd=int(monodd+yrodd)

monodd=monodd%7
monodd=monodd-1
if(monodd<0):
    monodd=monodd+7


#---------------------------------------

dayno=no
#-------------printing the calendar---------------------------
print()
print()

print(month,end="      ")
print(year)

print()


print('mon     tue     wed     thu     fri     sat     sun')
monodd=monodd-1
if(monodd==0):
    monodd=7
count=0

for i in range(0,monodd):

        
    print(' ',end="")
    print('       ',end="")
    count=count+1


for i in range(1,dayno+1):

        if(count==7):
            print()
            count=0    

        
        
        print(i,end="")
        count=count+1
        
        if(i>9):
            print('      ',end="")
        if(i<=9):
            print('       ',end="")
