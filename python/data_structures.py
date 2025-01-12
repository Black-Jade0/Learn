class Datastructures:
    def __init__(self):
        self.example_list = [1,2,3,4,5]

    def list_operation(self):
        print("\n --- list operation ---")
        print("example_list : {}".format(self.example_list))
        print(f"example_list : {self.example_list}")
        print(f"example_list :"self.example_list)

if __name__ =="__main__":
    data_structures = Datastructures()
    data_structures.list_operation()