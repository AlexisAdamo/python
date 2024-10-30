import pyautogui

# Posición del click
x = 100
y = 100

# Tiempo de espera entre clicks
tiempo_espera = 1

# Número de clicks
num_clicks = 10

for i in range(num_clicks):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    print(f"Click número {i+1}")
    pyautogui.sleep(tiempo_espera)