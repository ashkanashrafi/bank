while True:
    print("\n___________Bank____________\n")
    print("1-Add a customer")
    print("2-Show list of all customers")
    print("3-Search for a customer by ID")
    print("4-Change customer information")
    print("5-Delete a customer by ID")
    print("6- Apply for a loan")
    print("7-Add an employee")
    print("8-Show list of employees")
    print("9-Search for an employee by ID")
    print("10-Change employee information")
    print("11-Delete an employee by ID")
    print("12-Exit")
    options=int(input("\nPlease select an option: "))
    class Customer:
        def init(self):
            self._name=None
            self._fatherName=None
            self._Dcustomer_ID=None
        def set_name(self,name):
            self._name=name
        def set_fatherName(self,fatherName):
            self._fatherName=fatherName
        def set_Dcustomer_ID(self,Dcustomer_ID):
            self._Dcustomer_ID=Dcustomer_ID
        def get_name(self):
            return self._name
        def get_fatherName(self):
            return self._fatherName
        def get_Dcustomer_ID(self):
            return self._Dcustomer_ID
        def customer_info(self):
            print(f"name: {self._name}\nfatherName: {self._fatherName}\nDcustomer_ID: {self._Dcustomer_ID} ")
        if options==1:
            name=input("Please enter name: ")
            fatherName=input("Please enter your father Name: ")
            dcustomer_ID=input("please enter Dcustomer_ID: ")
        
        elif options==2:
            print("self._name")
            
            
        elif options==3:
            search_id=input("Please enter ID: ")
            
        elif options==4:
            search_id=input("Please enter ID: ")
            
        elif options==5:
            search_id=input("Please enter ID: ")
            
            
        elif options==6:
            search_id=input("Please enter ID: ")
            
            
            
            
            
            
            
        
            
            
            
            
            
    class Employee:
        def init(self):
            self._name=None
            self._salary=None
            self._personnel_code=None
        def set_name(self,name):
            self._name=name
        def set_salary(self,salary):
            self._salary=salary
        def set_personnel_code(self,personnel_code):
            self._personnel_code=personnel_code
        def get_name(self):
            return self._name
        def get_salary(self):
            return self._salary
        def get_personnel_code(self):
            return self._personnel_code
        def print_info(self):
            print(f"name: {self._name}\nsalary: {self._salary}\npersonnel_code: {self._personnel_code} ")

