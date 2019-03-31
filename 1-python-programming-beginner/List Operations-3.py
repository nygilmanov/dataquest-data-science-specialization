## 2. Parsing the File ##


f=open("la_weather.csv","r")
d=f.read()
rows=d.split('\n')

weather_data=[]
for row in rows:
    lst=row.split(",")
    weather_data.append(lst)
    
print(lst)
    


## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []

for item in weather_data:
    value=item[1]
    weather.append(value)

## 4. Counting the Items in a List ##

count = 0

for item in weather:
    count=count+1
    
print(count)

## 5. Removing the Header ##

new_weather=weather[1:366]

print(new_weather)

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found=("cat" in animals)
space_monster_found=("space_monster"  in animals)
print(cat_found)
print(space_monster_found)

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for item in weather_types:
    found=(item in new_weather)
    weather_type_found.append(found)

print(weather_type_found)