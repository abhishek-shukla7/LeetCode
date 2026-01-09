import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged=employee.merge(
        employee,
        left_on="managerId",
        right_on="id",
        how="inner",
        suffixes=("_emp","_mrg")
    )
    result=merged[merged["salary_emp"]>merged["salary_mrg"]]
    return result[["name_emp"]].rename(columns={"name_emp":"Employee"}) 
    
    