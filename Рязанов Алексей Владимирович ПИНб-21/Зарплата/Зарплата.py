with open('INPUT.TXT', 'r') as file:
    salaries = list(map(int, file.read().strip().split()))
     
max_salary = max(salaries)
min_salary = min(salaries)
 
difference = max_salary - min_salary
 
with open('OUTPUT.TXT', 'w') as file:
    file.write(str(difference))
