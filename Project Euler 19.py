import numpy as np

months= ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
year = np.linspace(1901,2000,100)
leapyears = np.linspace(1904,2000,25)
days = []

for i in year:
    for j in months:
        if j == "sep" or j == "apr" or j == "jun" or j == "nov":
            for k in range(1,30+1):
                days.append(k)
        elif j != "feb":
            for k in range(1,31+1):
                days.append(k)
        else:
            if i in leapyears:
                for k in range(1,29+1):
                    days.append(k)
            else:
                for k in range(1,29+1):
                    days.append(k)
#jan 1 1901 was a tuesday
sundays = []                    
for i in range(5,len(days),7):
    sundays.append(days[i])

answer = 0
for i in sundays:
    if i == 1:
        answer += 1
print(answer)


    
