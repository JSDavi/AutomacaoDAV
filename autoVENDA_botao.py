import random
import time
import keyboard
import PySimpleGUI as sg

def random_cliente():
    return random.choice([2, 3, 4])

def random_produto():
    return random.choice([1, 2, 3])

def random_planopag():
    return random.choice([2, 3, 99])

def random_avistapix():
    return random.choice([17, 1])

def random_prazo():
    return random.choice([4, 5, 16])
time.sleep(5)
# Define o layout da janela
layout = [[sg.Text('Pressione o botão para parar a execução do código')],
          [sg.Button('Parar')]]

# Cria a janela
window = sg.Window('Automação de teclado', layout)

while True:
    event, values = window.read(timeout=100)  # Verifica se o botão 'Parar' foi pressionado
    
    if event == sg.WIN_CLOSED or event == 'Parar':  # Sai do loop se o botão 'Parar' foi pressionado
        break

    keyboard.press_and_release('alt+n')
    time.sleep(0.5)
    window.refresh()
    
    keyboard.write(str(random_cliente()))
    
    keyboard.press_and_release('alt+v')
    time.sleep(0.5)
    keyboard.write(str(random_produto()))
    
    for i in range(random.randint(1, 3)):
        keyboard.press_and_release('alt+g')
        time.sleep(0.5)
        keyboard.write(str(random_produto()))
        
    keyboard.press_and_release('f6')
    time.sleep(0.5)
    n = random_planopag()
    keyboard.write(str(n))
    
    if n == 99:
        keyboard.press_and_release('enter')
        time.sleep(0.5)
        keyboard.press_and_release('enter')
        time.sleep(0.5)
        keyboard.write(str(random_avistapix()))
    else:
        keyboard.press_and_release('enter')
        time.sleep(0.5)
        keyboard.press_and_release('enter')
        time.sleep(0.5)
        keyboard.write(str(random_prazo()))
    
    keyboard.press_and_release('end')
    time.sleep(0.5)
    keyboard.press_and_release('f7')
    time.sleep(0.5)
    keyboard.write('122')
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    time.sleep(4)
    keyboard.press_and_release('f2')
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    keyboard.write('n')
    time.sleep(0.5)
    keyboard.press_and_release('esc')
    time.sleep(0.5)

# Fecha a janela
window.close()

# Sinaliza o final do código
print("Fim do código.")