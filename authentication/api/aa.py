class A:
    @staticmethod
    def send_otp():
        print("123")


class B:

    @staticmethod
    def create_otp():
        A.send_otp()


test = B()
test.get_otp()
