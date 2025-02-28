import secrets # módulo usado para gerar números aleatórios criptograficamente fortes, contém o método choice
import string # módulo que possui um acervo de strings 
import tkinter as tk # módulo para criação de interface gráfica
from tkinter import messagebox # módulo interno do tkinter para exibir mensagens como um pop-up

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get()) # pega o tamanho da senha digitada pelo usuário

        alfabeto = string.ascii_letters # alfabeto maiúsculo e minúsculo
        numeros = string.digits # números
        caracteres_especiais = string.punctuation # caracteres especiais
        
        senha = '' # variável com string usada para guardar senha
        for _ in range(tamanho): # executa um loop do tamanhã digitado pelo usuário
            # método join, chamado a partir de uma string, usado para concatenar um iterável em um string contínua
            # método choice, do módulo secrets, é usado para selecionar um caractere aleatório de uma string
            senha = senha + ''.join(secrets.choice(alfabeto + numeros + caracteres_especiais)) # gera senha

        entry_senha.delete(0, tk.END) # apaga o campo em que é exibida a senha gerada
        entry_senha.insert(0, senha) # insere a nova senha gerada após a anterior ter sido apafada
    except ValueError:
        #tratamento de erro, caso o usuário digite um valor diferente de número no campo que recebe o tamanho da senha
        # método showerror vai exibir pop-up de erro
        # o primeiro valor é o título da janela, Erro, o segundo é a mensagem no centro dela.
        messagebox.showerror("Erro", "Digite um número válido para o tamanho da senha.")

def copiar_senha(): # função para copiar a senha ao ser clicado botão de copiar
    root.clipboard_clear() # limpa a área de transfência do SO, deixando-a pronta para receber um novo valor
    senha = entry_senha.get() # pega o valor que está no campo que exibe a nova senha
    root.clipboard_append(senha) # coloca o valor recebido como argumento na área de transferência
    root.update() # atualiza a interface gráfica, garantindo que o usuário possa colá-la
    # méto showinfo abre opo up informativo na tela
    # primeiro argumento é o título e o segundo é o conteúdo, localizado no centro do pop up
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!") #

# criando a janela
root = tk.Tk() # cria intância a janela
root.title("Gerador de Senhas") # define o título
root.geometry("300x150") # define as dimensões da janela
root.resizable(False, False) # impede que a janela possa ter o tamanho alterado

# campo de tamanho da senha
# cria um campo label, text recebe o valor que será exibido no campo
# o método pack posiciona o campo, por não ter argumento, posiciona automaticamente
tk.Label(root, text="Tamanho da senha:").pack() 
entry_tamanho = tk.Entry(root, width=10) # cria um campo de entrada de dados, na janela root, com espaço para 10 caracteres
entry_tamanho.pack() # posiciona automaticamente entre os elementos anteriores e posteriores
entry_tamanho.insert(0, "12")  # insere valor 12 na posição 0 do campo ao iniciar o janela

# botão para gerar senha
# cria um botao na janela root com textp 'Gerar Senha', que quando é clicado o parâmetro command chama a função 'gerar_senha'
btn_gerar = tk.Button(root, text="Gerar Senha", command=gerar_senha)
# argumento pady=5 adiciona um espaçamento de 5 pixels no eixo y, descolando os demais elementos do botão
btn_gerar.pack(pady=5)

# cria o campo para exibir a nova senha, com espaço para 30 caracteres
# o campo é usado na unfção gerar_senha, para carregar o valor, e na função copiar senha, para recuperar valor e ser colocado
# na área de transferência
entry_senha = tk.Entry(root, width=30) 
entry_senha.pack() # posiciona automaticamente, seguind o padrão

# botão para copiar senha
# cria um botao na janela root com texto 'Copiar', que quando é clicado o parâmetro command chama a função 'copiar_senha'
btn_copiar = tk.Button(root, text="Copiar", command=copiar_senha)
# argumento pady=5 adiciona um espaçamento de 5 pixels no eixo y, descolando os demais elementos do botão
btn_copiar.pack(pady=5)

# loop infinito que permite que a janela se matenha aberta e interações do usuário
# mantém o múdolo Tkinter esprando eventos acontecerem
root.mainloop()
# sistema é encerrado quando a janela é fechada
