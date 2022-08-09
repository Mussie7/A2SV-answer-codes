"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dic = {}
        for employee in employees:
            employee_dic[employee.id] = employee
        
        total = employee_dic[id].importance
        stack = [id]
        
        while stack:
            for subordinate in employee_dic[stack.pop()].subordinates:
                total += employee_dic[subordinate].importance
                stack.append(subordinate)
        
        return total
