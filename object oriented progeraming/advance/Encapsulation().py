class ITManager:

    def __init__(self) -> None:
        self._IT_admin_files = "abc" #protected
        self.__IT_manager_files = "ert" #privet members

    def access_for_ceo(self):
        print(self.__IT_manager_files)

    def print_file(self):
        print("Public Files")

    def __print_file(self):
        print("Privet files")

class ITAdmin(ITManager):
    def __init__(self) -> None:
        super().__init__()
        self.id = 12345


h1 = ITAdmin()
h1._IT_admin_files
#h1.__IT_manager_files # catch eror cause it was privet
h1.access_for_ceo() #access for privet member with method
#python name mangling
#obj._classname__private
print(h1._ITManager__IT_manager_files)
h1._ITManager__print_file()