from time import sleep
from time import strftime
import winsound
from tkinter import *


# função para centralizar e dimensionar a janela
def geo_config_and_central(root, width, height):
    
    # Definindo uma posição centralizada para a janela
    # Definido o tamanho da janela
    larg_wind = width 
    alt_wind = height

    # Obtendo as medidas (largura e altura) da tela do computador
    larg_tela = root.winfo_screenwidth()
    alt_tela = root.winfo_screenheight()

    # Configurando os eixos x, y da janela
    x = (larg_tela / 2) - (larg_wind / 2)
    y = (alt_tela / 2) - (alt_wind / 2)

    # Posicionando a janela
    root.geometry("%dx%d+%d+%d" %(larg_wind, alt_wind, x, y))


# função para mostrar o horário na janela root
def time_now():
    string = strftime('%H:%M:%S')
    time_container.config(text = string)
    time_container.after(1000, time_now)


root = Tk()
root.title("Pomodoro's Timer")
geo_config_and_central(root, 400, 150)

time_container = Label(root, font = ('calibri', 40, 'bold'), 
                             background = 'blue',
                             foreground = 'white')
time_container.pack(anchor = 'center')
time_now()

root.mainloop()