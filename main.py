#bibliotecas:
import tkinter as tk
from tkinter import filedialog

#abrir arquivo:
def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes = [("Arquivos de Texto", "*.txt")])
    if arquivo:
        with open(arquivo, 'r') as f:
            texto_editor.delete(1.0, tk.END)
            texto_editor.insert(1.0, f.read())

#salvar arquivo:
def salvar_arquivo():
    arquivo = filedialog.asksaveasfilename(defaultextension = ".txt", filetypes = [("Arquivos de Texto", "*.txt")])
    if arquivo:
        with open(arquivo, 'w') as f:
            f.write(texto_editor.get(1.0, tk.END))

#tema escuro:
def configurar_tema_escuro():
    texto_editor.config(bg = "#202020", fg = "white")
    menu.config(bg = "#303030", fg = "white")
    arquivo_menu.config(bg = "#303030", fg = "white")

#abrir interface:
root = tk.Tk()
root.title("Editor de Texto")

#adiciona o ícone:
root.iconbitmap('icon.ico')

#editor de texto:
texto_editor = tk.Text(root, wrap = "word", bg = "#202020", fg = "white")
texto_editor.pack(expand = True, fill = "both")

#menu:
menu = tk.Menu(root)
root.config(menu = menu)

#cria o menu de arquivo:
arquivo_menu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Arquivo", menu = arquivo_menu)
arquivo_menu.add_command(label = "Abrir", command = abrir_arquivo)
arquivo_menu.add_command(label = "Salvar", command = salvar_arquivo)
arquivo_menu.add_separator()
arquivo_menu.add_command(label = "Sair", command = root.quit)

#configura o tema escuro:
configurar_tema_escuro()

#inicia o loop principal da interface gráfica:
root.mainloop()