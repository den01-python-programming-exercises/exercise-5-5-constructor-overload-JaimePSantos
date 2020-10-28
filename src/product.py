class Product:

    def __init__(self,name,location="shelf",weight=1):
        self.name = name
        self.location = location
        self.weight = weight
    
    @classmethod
    def with_location(cls,name,location):
      return cls(name,location)
    
    @classmethod
    def with_weight(cls,name,weight):
      return cls(name,"shelf",weight)
    
    def __str__(self):
      return "%s (%s kg) can be found from the %s"%(self.name,self.weight,self.location)