class Protected:
    def __init__(self, name):
        self._name = name #protected attribute       
    
        
p1 = Protected("Protected")
print(p1._name)


# Mangled names
class Private:
    def __init__(self, name):
        self.__name = name #private attribute('__name' ia mangled)
        
    
        
pv1 = Private("Private")
# print(pv1.__name)# 'print(p1._Private__name)'
print(pv1._Private__name)
# print(p1._Private__name)