# HCL




import pandas as pd

data = {
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Department': ['IT', 'IT', 'HR', 'HR', 'Finance', 'Finance'],
    'Salary': [70000, 80000, 50000, 60000, 90000, 95000]
}


# determing max salary from each department

df =  pd.DataFrame(data)
max_salary_by_dept = df.groupby('Department')['Salary'].max().reset_index()
print(max_salary_by_dept)
# print(df)
# print(df['Department'])
# print(df['Salary'])
# print(df['Employee'])
# select salary

# emp_id, emp_name, mgr_id , you need mgr name
# 1, Nitin, 1
# 2, Chandra,2
# 3, Sahil, 1
# mmgr name
# empname, mgr name

# Where does the python package gets installed from - #Pypi,  python package index
# have you used any design patterns?
# have you used ORM?

