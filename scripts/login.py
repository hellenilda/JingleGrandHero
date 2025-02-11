from tkinter  import *
from tkinter import Tk, ttk
import tkinter as tk
from traceback import print_list 

sprite = "/home/hellenilda/Documentos/Algoritmos/Python/JingleGrandHero-1.0/sprites/"
tel = Tk()
tel.geometry("1280x720")
tel.title("LOGIN")
Fundo = PhotoImage(file=f"{sprite}inite.png") 
echo = Label( tel, image = Fundo) 
echo.place(x = 0, y = 0) 

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)
        self.put_placeholder()
    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color
    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

name = EntryWithPlaceholder(tel, "NICKNAME","#4F4F4F")
name.place(x=470, y=460, height=44, width=344)

senha = EntryWithPlaceholder(tel, "SENHA", "#4F4F4F")
senha.place(x=470, y=530, width=344, height=44)

def entrar():
    SS = senha.get()
    NN = name.get()  
    try:
        with open(f'/home/hellenilda/Documentos/Algoritmos/Python/JingleGrandHero-1.0/resultado/LOGINS/{NN}.txt', 'r') as checke:
            sen = checke.read()
            print(f'Nome | {NN} e senha | {sen}')
            if sen == SS:
                tel.destroy()
                import game
            else:
                Label(tel, bg='white').place(x=471,y=500, height=5, width=343)
                Label(tel, bg='red').place(x=470,y=570, height=5, width=344)
    except: 
        Label(tel, bg='red').place(x=471,y=500, height=5, width=343)

def help():
    H = Tk()
    H.geometry("360x160")
    H.title("Ajuda")
    Label(H, text="""Na area 'NICKNAME' digite o nome da sua Conta. 
    E na area 'SENHA' digite a sua senha para Fazer o Login.   """).place(x=0,y=10)
    Label(H, text="  Ao encontrar uma barra vermelha como essa :").place(x=0,y=50)
    Label(H, bg='red').place(x=45,y=80, height=5, width=250)
    Label(H, text="""  Significa que em alguns dos campos de Nickname ou senha 
    estão incorretos !""").place(x=0,y=90)
    H.mainloop()

def create_login():
    def Generete():
        
        namber = str(genereteName.get())
        password = str(genereteSenha.get())
        print('Nome : ', namber)
        print('Senha : ', password)

        with open(f'/home/hellenilda/Documentos/Algoritmos/Python/JingleGrandHero-1.0/resultado/LOGINS/{namber}.txt', 'w') as createNamber:
            createNamber.write(password)
            print("Conta criada !!")
            janela.destroy()

    janela = Tk()
    janela.geometry('300x300')
    janela.title('Criação de Conta')
    Label(janela, bg='white').place(x=0,y=0, height=800, width=800)


    Label(janela, text="Nick", bg='white').place(x=20,y=5)
    
    # genereteName = Entry(janela, fg='#f7942a' ).place(x=10,y=30, height=40, width=270)

    Label(janela, text="Senha", bg='white').place(x=20,y=105)
    # genereteSenha = Entry(janela, fg='#f7942a' ).place(x=10,y=130, height=40, width=270)

    genereteName = EntryWithPlaceholder(janela, "Nome do Jogador","#f7942a")
    genereteName.place(x=10, y=30, height=40, width=270)

    genereteSenha = EntryWithPlaceholder(janela, "Senha do Jogador", "#f7942a")
    genereteSenha.place(x=10,y=130, height=40, width=270)

    Button(janela, text='Criar', command=Generete, fg='#ffffff',bg='#f7942a', font='Arial 15 bold italic').place(x=87, y=220,  height=45, width=120)
    janela.mainloop()

Exit = Button(tel, text="Sair", bd = '5', command=tel.destroy, fg='#ffffff', bg='#f7942a', font='Arial 15 bold italic').place(x=470,y=590, height=45, width=176)
Entrar = Button(tel, text="Entrar", bd = '5', command=entrar, fg='#ffffff',bg='#f7942a', font='Arial 15 bold italic').place(x=647,y=590, height=45, width=169)
Button(tel, text="Ajuda", bd = '5', command=help, fg='#ffffff', bg='#f7942a', font='Arial 15 bold italic').place(x=1160,y=0, height=45, width=120)
acconts = Button(tel, text="Criar nova Conta", bd = '5', command=create_login, fg='#ffffff',bg='#f7942a', font='Arial 15 bold italic').place(x=470,y=650, height=45, width=346)
tel.mainloop()