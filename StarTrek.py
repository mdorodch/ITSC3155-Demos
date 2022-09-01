class StarTrek:
    ship = "USS Enterprise"
    
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __repr__(self) -> str:
        return f"{self.name} is {self.role} of {self.ship}."

    def beamMe(self):
        return f"{self.name} says: Scotty, beam me!"
    
if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    s1 = StarTrek("Jim Kirt","Captain")
    s2 = StarTrek("Leonard McCoy", "Chief Medical Officer") 
    print(s1) 
    print(s2)
    print(s1.beamMe())
    print(s2.beamMe())
        
        