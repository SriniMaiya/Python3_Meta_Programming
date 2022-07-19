class Spam:
    def imethod(self):
        print("Instance method")
        pass

    @classmethod
    def cmethod(cls):
        print("Class method")
        pass

    @staticmethod
    def smethod():
        pass


if __name__ == "__main__":
    s = Spam()
    s.imethod()

    Spam.cmethod()

    Spam().imethod()
