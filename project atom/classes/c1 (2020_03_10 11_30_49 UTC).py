#EACH CLASS TAKES THE INSTANCE AS A FIRST ARGUMENT SO WE NEED TO INITIALISE AS SELF
class node:
    s=12
    def __init__(self,head):
        self.head=head
        self.next=None
    def applyraise(self):
        self.next=self.s
    @classmethod
    def seetapplyraise(cls,amt):
        cls.next=13+amt
n1=node(21)
#n1.applyraise()
n1.seetapplyraise(10)
print(n1.next)
