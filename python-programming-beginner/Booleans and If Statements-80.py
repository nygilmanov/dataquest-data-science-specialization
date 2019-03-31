## 1. Booleans ##

cat = True
dog = False
print(type(cat))

## 2. Boolean Operators ##

print(cities)

first_alb=(cities[0]=='Albuquerque')
second_alb=(cities[1]=='Albuquerque')
last_element_index=len(cities)-1
first_last=(cities[0]==cities[last_element_index])
print(first_alb,second_alb,first_last)

## 3. Booleans with "Greater Than" ##

first_500=(crime_rates[0]>500)
first_749=(crime_rates[0]>=749)
last_index=len(crime_rates)-1
first_last=(crime_rates[0]>crime_rates[last_index])

## 4. Booleans with "Less Than" ##

print(crime_rates)
second_500=(crime_rates[1]<500)
second_371=(crime_rates[1]<=371)
last_index=len(crime_rates)-1
second_last=(crime_rates[1]<crime_rates[last_index])
print(second_500,second_371,second_last,last_index)


## 5. If Statements ##

result = 0
if cities[2]=="Anchorage":
     result =1
    
print(result)

## 6. Nesting If Statements ##

both_conditions = False

if crime_rates[0]>500:
    if crime_rates[0]>300:
        both_conditions=True
        
print(both_conditions)       
        

## 7. If Statements and For Loops ##

five_hundred_list=[]
for cr in crime_rates:
    if cr>500:
       five_hundred_list.append(cr)
  

## 8. Find the Highest Crime Rate ##

print(crime_rates)
highest=0

for cr in crime_rates:
    if cr>highest:
        highest=cr
    
print(highest)        