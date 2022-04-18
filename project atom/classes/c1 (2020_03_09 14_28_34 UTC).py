#EACH CLASS TAKES THE INSTANCE AS A FIRST ARGUMENT SO WE NEED TO INITIALISE AS SELF
class node:
    rasise=3.14
    def __init__(self,head,name,call):
        self.head=head
        self.name=name
        self.call=call
    def applyraise(self):
        self.call=self.rasise
    #this
n1=node("good","not so good",990)
print(n1.applyraise())
print(n1.call)
