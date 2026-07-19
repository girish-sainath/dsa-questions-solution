import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Find all managers with their reports count and average age of reports.
    
    Args:
        employees: DataFrame with columns [employee_id, name, reports_to, age]
    
    Returns:
        DataFrame with managers' employee_id, name, reports_count, and average_age
        ordered by employee_id
    """
    
    # Self-join: merge employees table with itself
    # Left side: managers (employee_id, name)
    # Right side: reports (reports_to -> employee_id, age)
    merged = employees.merge(
        employees[['reports_to', 'age']],  # Select only needed columns from reports side
        left_on='employee_id',              # Manager's employee_id
        right_on='reports_to',              # Matches reports_to in subordinates
        suffixes=('_manager', '_report')    # Distinguish overlapping column names
    )
    
    # Group by manager's employee_id and name
    result = merged.groupby(['employee_id', 'name'], as_index=False).agg(
        reports_count=('reports_to', 'count'),      # Count number of direct reports
        average_age=('age_report', lambda x: round(x.mean()))  # Average age, rounded
    )
    
    # Sort by employee_id
    result = result.sort_values('employee_id').reset_index(drop=True)
    
    return result


# -------------------- Test Cases --------------------

# Test Case 1
employees1 = pd.DataFrame({
    'employee_id': [9, 6, 4, 2],
    'name': ['Hercy', 'Alice', 'Bob', 'Winston'],
    'reports_to': [None, 9, 9, None],
    'age': [43, 41, 36, 37]
})

print("Test Case 1:")
print("Input:")
print(employees1.to_string(index=False))
print("\nOutput:")
print(count_employees(employees1).to_string(index=False))

print("\n" + "="*60 + "\n")

# Test Case 2
employees2 = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Michael', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'reports_to': [None, 1, 1, 2, 2, 3, None, None],
    'age': [45, 38, 42, 34, 40, 37, 50, 48]
})

print("Test Case 2:")
print("Input:")
print(employees2.to_string(index=False))
print("\nOutput:")
print(count_employees(employees2).to_string(index=False))