import tkinter as tk
import tkinter.ttk as ttk
import pyautogui
import subprocess

# Define as funções de atalho dos botões
def run_cmd():
    pyautogui.hotkey('win', 'r')

def other_shortcut():
    pyautogui.hotkey('ctrl', 'shift', 'esc')

def teams():
    pyautogui.hotkey('win', 'c' )

def arquivos():
    pyautogui.hotkey('win', 'e')

def microfone():
    pyautogui.hotkey('win', 'h')

def configurações():
    pyautogui.hotkey('win', 'i')

def programa_cmd():
    subprocess.run(["cmd", "/c", "start"])

# Cria a janela
root = tk.Tk()
root.title("Atalhos do Windows")
root.geometry("300x300")

# Cria estilo para os botões
btn_style = ttk.Style()
btn_style.configure("TButton", font=("Helvetica", 12), width=20)

# Cria os botões com estilo
btn1 = ttk.Button(root, text="Arquivos", command=arquivos, style="TButton")
btn2 = ttk.Button(root, text="Configurações", command=configurações, style="TButton")
btn7 = ttk.Button(root, text="Cmd", command=programa_cmd, style="TButton")
btn4 = ttk.Button(root, text="Executar", command=run_cmd, style="TButton")
btn5 = ttk.Button(root, text="Gerenciador de Tarefas", command=other_shortcut, style="TButton")
btn6 = ttk.Button(root, text="Microfone", command=microfone, style="TButton")
btn7 = ttk.Button(root, text="Teams", command=teams, style="TButton")

# Posiciona os botões na janela
btn1.pack()
btn2.pack()
btn7.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()

# Inicia a janela
root.mainloop()