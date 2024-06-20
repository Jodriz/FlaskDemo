try:
    from src import app
    HOST = 'localhost'
    PORT = 4000
    DEBUG = True


    if __name__ == '__main__':
        app.run(host= HOST, port = PORT, debug = DEBUG)    
        
except ModuleNotFoundError:
    try:
        from os import system
        print("----------Iniciando instalación de dependecias-----------")
        command = "pip install -r requirements.txt"
        print(command)
        system(command)
        print("\n********* Reiniciando App ************")
        command = "python main.py\n"
        print(command)
        system(command)
    except Exception:
        print("Ha ocurrido un error inprevisto, revise si tiene a python configurado como variable de entrono")






