class MySecretClass:
    def __init__(self,secret: str):
        self.secret = secret #completely public to outside modules

secretInstance = MySecretClass("secret")
print(secretInstance.secret) # can access it



class MySuperSecretClass:
        def __init__(self,secret: str):
            self.__secret = secret #kinda private

        def acccess_secret(self) -> str:
            return self.__secret
        
superSecretInstance = MySuperSecretClass("super secret")
print(secretInstance._MySuperSecretClass__secret)


    



    