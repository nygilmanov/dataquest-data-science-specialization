## 2. Number of Standard Deviations ##

distance = 220000 - houses['SalePrice'].mean()
st_devs_away = distance / houses['SalePrice'].std(ddof = 0)
print(st_devs_away)