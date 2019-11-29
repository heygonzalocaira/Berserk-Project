
class AnonymousName():

    def __init__(self, Name):
        ### Store a Name, and prepare to store score_name
        self.Name = Name
        self.score_name = []

    def show_Name(self):
        print(self.Name)

    def store_response(self, new_response):
        self.score_name.append(new_response)

    def show_results(self):
        print("Name results: ")
        for response in self.score_name:
            print('- '+response)    
