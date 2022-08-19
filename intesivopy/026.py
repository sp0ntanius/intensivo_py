from tkinter import *
def clicabotao():
    print("Olá mundo!")

janela = Tk()
janela.geometry("500x300")
janela.title("Teste de Janela.")
#janela.configure(background="red")
txt1 = Label(
    janela,
    text="OS MELHORES DO MUNDO",
    font=(
        'Helvetica', 18, 'bold'
    )
)
txt1.place(
    x=40,
    y=0,
    width=400,
    height=30
)
entrada = Entry(
    janela,

)
botao = Button(
    janela,
    text="clique em mim",
)    
botao.place(
    x=40,
    y=150,
    width=300,
    height=30
)












janela.mainloop() 