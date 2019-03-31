## 2. Sets ##

gender=[]
for item in legislators:
    gender.append(item[3])
 

gender=set(gender)
print(gender)
   


## 3. Exploring the Dataset ##

party=[]

for item in legislators:
    party.append(item[6])
party=set(party)
    
    

## 4. Missing Values ##

gender=[]

for item in legislators:
    if  item[3]=="":
        item[3]="M"
         
    
gender.append(item[3])
    


## 5. Parsing Birth Years ##

birth_years=[]

for item in legislators:
    date=item[2]
    parts=date.split("-")
    birth_years.append(parts[0])
                       
print(birth_years)
                             

## 6. Try/except Blocks ##

string="hello"

try:
    float(string)
except Exception:
    print("Error converting to float.")

## 7. Exception Instances ##

string=""

try: 
     int(string)
except Exception as exc:
       print(type(exc))
       print(str(exc))
    

## 8. The Pass Keyword ##

converted_years = []

for item in birth_years:
    try:
        int_year=int(item)
        converted_years.append(int_year)
    except Exception:
        pass
    
    

## 9. Convert Birth Years to Integers ##

for row in legislators:
    birthday = row[2]
    birth_year = birthday.split("-")[0]
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
    row.append(birth_year)
    print(row)
        
    
    
    
    
    

## 10. Fill in Years Without a Value ##

last_value=1
for item in legislators:
    if item[7]==0:
        item[7]=last_value
    last_value=item[7]
        
    