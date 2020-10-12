class Zoo:
    def __init__(self, name='no', visitors=0, how_many_animals=0):
        self.name = name
        self.visitors = visitors
        self.how_many_animals = how_many_animals

    def __str__(self):
        return  "[Name="+self.name+ "; Visitors="+ str(self.visitors) +"; How many animals="+ str(self.how_many_animals)+";]"
