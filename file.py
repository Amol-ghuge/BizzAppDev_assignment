import pandas as pd
from datetime import datetime, date

file =("Enter the filename:- ")
data = pd.read_csv(file)
print("csvfile data:- ",data)
  
born= input("Enter the employee data:- ")
  
born = datetime.strptime(born, "%d/%m/%Y").date()

today = date.today()
  
data["Age"]=today.year - born.year - ((today.month,today.day) < (born.month,born.day)))
print("csvfile with age  ",data)
