import winsound                               # Eu importei esta lib para poder emitir os sons dos alarmes
from time import sleep                        # já essa lib, é para esperar e cronometrar o tempo correto para os alarmes


def line():                                       # criei a função line() apenas para organizar melhor as saídas no terminal
    print()
    print('-=' * 40)
    print()

def alarm():                                      # esta função é responsável pela emissão dos alarmes


    fr = 2600                                     # a variavel fr armazena a frequencia do alarme (37 ate 3200), quanto maior mais agudo
    how_long = 2000                                   # tempo de duração do alarme em milissegundos

    for c in range(0, 3):
        winsound.Beep(fr, how_long)                 # chamando o alarme
def entry_task():                                   # função para entrada de tarefas e adicionar na lista
    while(True):
        task_var = input('  -> ')
        if (task_var == '--stop'):
            break
        task_list.append(task_var)


def print_tasks():                                  # função para mostrar as tarefas
    for task in task_list:
        print(f'    => {task}')


def cycle():                                                # função que define o ciclo de 4 pomodoros, 2 horas totais 
    for cycle in range(0, 4):                               # 1 pomodoro = 25 minutos de estudo, 5 de descanso
        if ((cycle + 1) == 4):
            what_do = 'You finish all the cycles!'
        else:
            what_do = "Let's study!"
        
        print_tasks()
        sleep(1500) # 1500                                                # espera os 25 minutos de estudo
        print(f'\nEnd of the {cycle + 1} Pomodoro. You can rest!')
        alarm()                                                         # dispara o alarme para o inicio descanso

        sleep(300) # 300                                                  # espera os 5 minutos de descanso
        print(f'End of the {cycle + 1} rest. {what_do}!')
        line()                                                          
        alarm()                                                         # dispara o alarme do fim do descanso


def start():                                                            # função principal que chama todas as outras
    while (True):                                           
        input('\nPress <enter> and start your studies!')
        line()

        cycle()
        
        new_pomodoro = input('To start a new Pomodoro, type --new. If you wants stop, type --cancel: ') # pergunta se o usuário quer 
        if (new_pomodoro ==  '--cancel'):                                                               # começar um novo Pomodoro
            break


task_list = list()
line()

print('Before starting the pomodoro, list your tasks and choose an initial task. \n' +
        'Add your tasks down here... To stop, type "--stop" \n')
print('     TASKS')
entry_task()
start()

