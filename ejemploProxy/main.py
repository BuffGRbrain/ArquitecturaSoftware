black_listed_sites = ['www.facebook.com', 'www.twitter.com', 'www.instagram.com']

class Proxy:
    def __init__(self,url):
        self.url = url

    def conectarse(self):
        if self.url in black_listed_sites:
            raise Exception("Acceso denegado")
        print("Conectado a",self.url)


url = input("Ingrese la url a la que desea acceder: ")
proxy = Proxy(url)
proxy.conectarse()