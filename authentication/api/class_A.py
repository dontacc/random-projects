class Test:

    def show_name(self, name):
        print(f"{name} is converting ...")
        return name


class Test2(Test):

    def show_name(self, name):
        name = name.upper()

        return super().show_name(name)


test = Test2()
print(test.show_name("nima"))
