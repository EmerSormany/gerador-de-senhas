# **Documentação do Sistema: Gerador de Senhas em Python**

## **1. Introdução**
Este documento descreve o funcionamento do sistema de **Gerador de Senhas**, desenvolvido em **Python** utilizando a biblioteca **Tkinter** para a interface gráfica. O sistema permite que o usuário defina o tamanho da senha, gere uma senha aleatória e a copie para a área de transferência.

Em execução, o sistema recebe um valor numérico que indica o tamanho da senha desejada pelo usuário. Abaixo há um botão *Gerar Senha*, que quando clicado deverá retornar uma senha de caracteres aleatórios variando entre letras maiúsculas, minúsculas, síbolos e números. Abaixo do campo onde aparece a senha gerada há o botão *Copiar Senha*, que ao ser clicado copiará a senha gerada e o usuário poderá colá-la onde quiser.

## **2. Módulos Utilizados**
O sistema faz uso de quatro módulos nativos python: `secrets`, `string`, `tkinter` e `messagebox`. Abaixo está uma descrição detalhada de cada um e sua função dentro do sistema. Como os módulos são nativos não há necessidade de instalá-los, apenas a importação deles é necessária:
```python
import secrets
import string
import tkinter as tk
from tkinter import messagebox
```

### **2.1 Módulo `secrets`**
O módulo `secrets` é utilizado para gerar senhas seguras e criptograficamente fortes.

**Uso no sistema:**
- A função `secrets.choice(alfabeto + numeros + caracteres_especiais)` é usada para selecionar aleatoriamente um elemento de um item iterável. A concatenação das variáveis alfabeto, numeros e caracteres_especiais formam esse iterável do qual o loop repetirá a execução o número de vezes passado pelo usuário, garantindo que a senha gerada seja **forte e imprevisível**.

```python
secrets.choice(alfabeto + numeros + caracteres_especiais)
```

### **2.2 Módulo `string`**
O módulo `string` contém constantes com diferentes tipos de caracteres, como letras, dígitos e símbolos.

**Uso no sistema:**
- Utilizei três constantes do módulo para criar um conjunto de caracteres iterável que pode ser usado como parâmetro para no método choice, que irá selecionar um caractere a cada iteração:

```python
alfabeto = string.ascii_letters
numeros = string.digits
caracteres_especiais = string.punctuation

for _ in range(tamanho):
    senha = senha + ''.join(secrets.choice(alfabeto + numeros + caracteres_especiais))
```

Isso permite que a senha tenha uma combinação de **letras maiúsculas e minúsculas**, **números** e **símbolos**.

### **2.3 Módulo `tkinter`**
`tkinter` é um módulo padrão do Python usado para criar interfaces gráficas.

**Uso no sistema:**
- Cria uma instância da janela principal do aplicativo com:

```python
root = tk.Tk()
```

- Define componentes como **rótulos (`Label`)**, **campos de entrada (`Entry`)** e **botões (`Button`)** para interação do usuário.
- Gerencia o layout com o método `pack()` para organizar os elementos na tela. Se não receber nenhum argumento ele fará a organização padrão, deixando um elemento após o outro.
- Exemplo de valor usado para editar layout de acordo com a necessidade, que cria um espaço no eixo y, separando os elementos antes e depois do botão:

```python
btn_gerar.pack(pady=5)
```

- O método mainloop mantém a interface ativa, em loop infinite e aguardando interações do usuário:

```python
root.mainloop()
```

### **2.4 Módulo `messagebox`**
`messagebox` faz parte do `tkinter` e é utilizado para exibir mensagens pop-up.

**Uso no sistema:**

- Utilizo para gerar 2 pop-ups, de sucesso, ao copiar senha, e de erro, quando o usuário digitar valor não numérico para indicar o tamanho da senha. 
- O método showinfo cria um pop-up informativo.
- O método showerror cria um pop-up de erro.
- Ambos recebem o primeiro argumento, que é o título, e o segundo argumento, que é o conteúdo exibido no centro do pop-up.

```python
messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")
messagebox.showerror("Erro", "Digite um número válido para o tamanho da senha.")
```

## **3. Utilização do Projeto**
Para usar este sistema você precisará ter **Python** - o sistema foi desenvolvido na versão ***Python 3.13.0***  - instalado em sua máquina. Baixe o código fonte deste repositório, abra o prompt de comando na pasta em que o código fonte foi baixado e execute algum dos seguintes comandos, de acordo com seu sistema operacional:

- Windows
```sh
python app.py
```
- MacOS ou Linux
```sh
python3 app.py
```

## **4. Conclusão**
Este sistema utiliza os módulos `secrets` e `string` para gerar senhas seguras, enquanto `tkinter` e `messagebox` garantem uma interface intuitiva e funcional. O resultado é um gerador de senhas simples e eficiente, que pode ser instalado no computador do usuário e utilizado sempre que for necessário.

