#base class
class parent:
    def __init__(self,name,gene,age):
        self.name=name
        self.age=age
        self.gene=gene
        print("hdgha")
    def capability(self):
        print("The patient name is:",self.name)
        print("The patient age is:",self.age)
        print("And the gene value is:",self.gene)
class child(parent):
    def __init__(self,name,gene,age):
        super().__init__(name,gene,age)
        print("child")

    #def __init__(self,name,gene):
    #    super().__init__(gene)
    #def capability(self):
    #    print("the child name is:",self.name)
    #    print("The gene value of child is:",self.gene)
c=child("bishop",6.324,12)
c.capability()
