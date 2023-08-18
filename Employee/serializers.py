from rest_framework import serializers
from Employee.models import Departments,Employees,User,result

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=('UserId','UserName','DateOfJoining','PhotoFileName')
class resultSerializer(serializers.ModelSerializer):
    class Meta:
        model=result 
        fields=('UserId','Result')
        
