class User:
    _total_users = 0

    def __init__(self, email, password, idade):
        self.email = email
        self.password = password
        self.idade = idade
        type(self)._total_users += 1

    @classmethod
    def total_users(cls):
        return cls._total_users

# função utilitaria, para definir uma faixa etária do usuario.

    @staticmethod
    def faixa_etaria(idade):
        return "Adult" if idade >= 18 else "jovem"
    

    @email.setter
    def email(self, email):
        self.__email = email
    

    @property
    def password (self):
        return "*"*10
    
    @password.setterdef password(self, new_pass):
    if len (new_pass) >=8:
        self.__password = new_pass

        print(User.total_users())
        
