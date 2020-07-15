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
    string = strftime('%H:%M:%S %p')
    time_container.config(text = string)
    time_container.after(1000, time_now)


def alarm():
    frequence = 2800
    how_long = 200
    for c in range(0, 20):
        winsound.Beep(frequence, how_long)


def start_pomodoro():
    sleep(10)
    what_do['text'] = 'Fim do 1º Pomodoro, pode descansar!'
    alarm()
    sleep(5)
    what_do['text'] = 'Início do 2º Pomodoro, vamos estudar!'
    alarm()

    sleep(10)
    what_do['text'] = 'Fim do 2º Pomodoro, pode descansar!'
    alarm()
    sleep(5)
    what_do['text'] = 'Início do 3º Pomodoro, vamos estudar!'
    alarm()

    sleep(10)
    what_do['text'] = 'Fim do 3º Pomodoro, pode descansar!'
    alarm()
    sleep(5)
    what_do['text'] = 'Início do 4º Pomodoro, vamos estudar!'
    alarm()

    sleep(10)
    what_do['text'] = 'Fim do 4º Pomodoro, pode descansar!'
    alarm()
    sleep(5)
    what_do['text'] = 'Parabéns, você concluiu 2 horas de estudo. Reinicie o programa para estudar mais!'
    alarm()



root = Tk()
root.title("Pomodoro's Timer")
geo_config_and_central(root, 750, 350)
root.resizable(False, False)

time_container = Label(root, font = ('calibri', 50, 'bold'), 
                             background = 'blue',
                             foreground = 'white')
time_container.pack(anchor = 'center')
time_now()

what_do = Label(root, text = 'This method consists of 2 hours of study. Every 25 minutes of \n' +
                             'total concentration you rest for 5.', font = ('calibri', 20))
what_do.pack(anchor = 'center')

init_button = Button(root, text = 'Start a Pomodoro!', font = ('calibri', 20), command = start_pomodoro)
init_button.pack(anchor = 'center')

root.mainloop()