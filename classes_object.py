class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name:str,age:int,tracks:list,score:float):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    print("New student information:")

    def change_name(self,new_name):
        self.name = new_name
        print("Name: " + new_name.title())

    def change_age(self,new_age):
        self.age = new_age
        print("Age: " + str(new_age))


    def add_track(self,new_track):
        self.tracks.append(new_track)
        print("Tracks: " + new_track)


    def get_score(self,new_score):
        self.score = new_score
        print("Score: " + str(new_score))



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(80.2)
