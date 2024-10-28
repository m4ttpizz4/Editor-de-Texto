#bibliotecas:
import tkinter as tk
from tkinter import filedialog, ttk

#abrir arquivo:
def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if arquivo:
        with open(arquivo, 'r') as f:
            texto_editor.delete(1.0, tk.END)
            texto_editor.insert(1.0, f.read())

#salvar arquivo:
def salvar_arquivo():
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
    if arquivo:
        with open(arquivo, 'w') as f:
            f.write(texto_editor.get(1.0, tk.END))

#tema escuro:
def configurar_tema_escuro():
    texto_editor.config(bg="#202020", fg="white")
    menu.config(bg="#303030", fg="white")
    arquivo_menu.config(bg="#303030", fg="white")
    tema_menu.config(bg="#303030", fg="white")

#tema ruim:
def configurar_tema_claro():
    texto_editor.config(bg="white", fg="black")
    menu.config(bg="lightgrey", fg="black")
    arquivo_menu.config(bg="lightgrey", fg="black")
    tema_menu.config(bg="lightgrey", fg="black")

#alternar tema:
def alternar_tema():
    if texto_editor.cget("bg") == "#202020":
        configurar_tema_claro()
    else:
        configurar_tema_escuro()

#abrir interface:
root = tk.Tk()
root.title("Editor de Texto")

#adiciona o ícone:
root.iconbitmap('icon.ico')

#editor de texto com barra de rolagem:
frame_texto = tk.Frame(root)
frame_texto.pack(expand=True, fill="both")
texto_editor = tk.Text(frame_texto, wrap="word", bg="#202020", fg="white")
scrollb = ttk.Scrollbar(frame_texto, command=texto_editor.yview)
texto_editor['yscrollcommand'] = scrollb.set
scrollb.pack(side="right", fill="y")
texto_editor.pack(expand=True, fill="both")

#menu:
menu = tk.Menu(root)
root.config(menu=menu)

#cria o menu de arquivo:
arquivo_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Arquivo", menu=arquivo_menu)
arquivo_menu.add_command(label="Abrir", command=abrir_arquivo)
arquivo_menu.add_command(label="Salvar", command=salvar_arquivo)
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=root.quit)

#cria o menu de tema:
tema_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Tema", menu=tema_menu)
tema_menu.add_command(label="Alternar Tema", command=alternar_tema)

#configura o tema escuro por padrão:
configurar_tema_escuro()

#inicia o loop principal da interface gráfica:
root.mainloop()