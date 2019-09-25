from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Database

#Criando a janela (Painel de acesso)
janela = Tk()
janela.title("Interative - Painel de acesso")
janela.geometry("600x300")
janela.configure(background="white")
janela.attributes("-alpha",0.9) #Deixando transparente
janela.resizable(width=False, height=False) #Não permitindo maximizar ou alterar o tamanho da tela

#Passando logo tipo para a variável logo
logo = PhotoImage(file="Imagem/Logo.png")

#Dividindo a tela nas cores MidNightblue
LeftFrame = Frame(janela,width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela,width=395, height=300, bg="MIDNIGHTBLUE", relief="raise") #395 pra deixar uma faixa branca separando
RightFrame.pack(side=RIGHT)

# Carregando o logo tipo no painel
LogoLabel = Label(LeftFrame,image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50,y=100)

#Criando campo usuário e senha
UserLabel = Label(RightFrame,text="Usuário:",font=("Century Gothic", 20), bg="MIDNIGHTBLUE",fg="White")
UserLabel.place(x=5,y=100)
UserEntry = ttk.Entry(RightFrame,width=30)
UserEntry.place(x=150,y=110)

PassLabel= Label(RightFrame,text="Senha:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
PassLabel.place(x=5,y=150)
PassEntry = ttk.Entry(RightFrame,width=30,show="*")
PassEntry.place(x=150,y=162)

def Login():
    User = UserEntry.get()
    Senha = PassEntry.get()
    Database.cursor.execute("""
    SELECT 
        Usuario,
        Senha 
    FROM 
        Usuarios
    WHERE
        Usuario = %s AND Senha = %s
    """,(User,Senha))
    VerificaLogin = Database.cursor.fetchone()
    try:
        if (User in VerificaLogin) and (Senha in VerificaLogin):
            messagebox.showinfo(title="Login",message="Acesso confirmado. Bem Vindo!")
    except:
        messagebox.showerror(title="Erro de login",message="Acesso Negado. Confirme seus dados ou faça o registro")


#Botões
LoginButton = ttk.Button(RightFrame,text="Entrar",width=15, command=Login)
LoginButton.place(x=235,y=200)

def Register():
    LoginButton.place(x=5000) #Pro botão "entrar" sumir
    RegisterButton.place(x=5000)

    #Inserindo novos botões
    NomeLabel = Label(RightFrame,text="Nome:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
    NomeLabel.place(x=5,y=5)
    NomeEntry = ttk.Entry(RightFrame,width=30)
    NomeEntry.place(x=150,y=20)

    EmailLabel = Label(RightFrame,text="E-mail:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
    EmailLabel.place(x=5,y=45)
    EmailEntry = ttk.Entry(RightFrame,width=30)
    EmailEntry.place(x=150,y=60)

    def RegistrandoNoBanco():
        Name = NomeEntry.get() #Variavel Name recebe valor da variável NomeEntry
        Email = EmailEntry.get()
        User = UserEntry.get()
        Senha = PassEntry.get()
        Database.cursor.execute("""
        SELECT 
            Usuario,
            Email 
        FROM 
            Usuarios
        WHERE
            Usuario = %s or Email = %s
        """,(User,Email))
        VerificaRegis = Database.cursor.fetchone()
        if User in VerificaRegis or Email in VerificaRegis:
            messagebox.showerror(title="Erro de Registro",message="Usuário já cadastrado")
        elif Name == "" or Email == "" or User == "" or Senha=="":
            messagebox.showerror(title="Erro de Registro",message="Preencha todos os campos")
        else:
            Database.cursor.execute("""
            INSERT INTO Usuarios (Nome,Email,Usuario,Senha) VALUES (%s,%s,%s,%s)
            """,(Name,Email,User,Senha))
            Database.conn.commit()
            messagebox.showinfo(title="Informação de Registro",message="Conta criada com sucesso!")
    Registra = ttk.Button(RightFrame,text="Registrar",width=15,command=RegistrandoNoBanco)
    Registra.place(x=235,y=200)
    def VoltarLogin():
        #Removendo Widgets de cadastro
        NomeLabel.place(x=50000)
        NomeEntry.place(x=50000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Registra.place(x=5000)
        Voltar.place(x=5000)
        #Trazendo de volta os widgets de login
        LoginButton.place(x=235,y=200) 
        RegisterButton.place(x=150,y=200)
    Voltar = ttk.Button(RightFrame,text="Voltar",width=14, command=VoltarLogin)
    Voltar.place(x=150,y=200)

RegisterButton = ttk.Button(RightFrame,text="Registre-se",width=14, command=Register)
RegisterButton.place(x=150,y=200)


janela.mainloop()