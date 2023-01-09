
class TestClass:
    def __init__(self, name:str, age:int, male:bool=True) -> None:
        """Dummy class to validate pytest and typing
        
        Args:
            name (str)           : user name
            age  (int)           : user age
            male (bool, optional): user gender, true if user is male
        
        return:
            None
        """
        
        self.name = name
        self.age  = age
        self.male = male
        
        return
    
    # Validate type initialization input
    @property
    def name(self)->str:
        if not hasattr(self,'_name'):
            self._name = None
        return self._name

    @name.setter
    def name(self, val:str):
        if not isinstance(val, str):
            raise TypeError(f"Name parameter expects 'str' not '{str(val.__class__.__name__)}'")
        self._name = val
        
    @property
    def age(self)->int:
        if not hasattr(self,'_age'):
            self._age = None
        return self._age

    @age.setter
    def age(self, val:int):
        if not isinstance(val, int):
            raise TypeError(f"Age parameter expects 'int' not '{str(val.__class__.__name__)}'")
        self._age = val
        
    @property
    def male(self)->bool:
        if not hasattr(self,'_male'):
            self._male = None
        return self._male

    @male.setter
    def male(self, val:int):
        if not isinstance(val, int):
            raise TypeError(f"Age parameter expects 'bool' not '{str(val.__class__.__name__)}'")
        self._male = val
    
    # End validation
    
    def addAgeToList(self, years:list)->list:
        self._validateYearList(years)
        sumYears = [i+self.age for i in years]
        return sumYears
    
    @staticmethod
    def _validateYearList(val):
        # Validate type
        if not isinstance(val, list):
            raise TypeError(f"Years parameter expects 'list' not '{str(val.__class__.__name__)}'")
        # Validate minimum length
        minVal = 1
        if len(val)<=minVal:
            raise ValueError(f"Years requires a mininum list lenght of {str(minVal)}")
        # Validate maximum length
        maxVal = 10
        if len(val)>=maxVal:
            raise ValueError(f"Years has a maximum list lenght of {str(maxVal)}")
        # Validate item types
        if not all(isinstance(i, int) for i in val):
            raise TypeError("All items in parameter years need to be 'int'")
        return


# MAIN
A = TestClass('bob', 15)

for i in dir(A):
    if i.startswith('__'): continue
    print(i, getattr(A, i))

print(A.addAgeToList([0,1000,2000]))