from firebase import Firebase
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
#conecta ao firebase
#preencha com os dados do seu firebase
config = {
    "apiKey": " ",
    "authDomain": " ",
    "databaseURL": " ",
    "projectId": " ",
    "storageBucket": " ",
    "messagingSenderId": " ",
    "appId": " ",
    "measurementId": " "
}

firebase = Firebase(config)
auth = firebase.auth()

def show_page_create_accout():
    first_page.close()
    creat_account_page.show()


#cria o  login
def creat_account():
    name = creat_account_page.lineEdit.text()
    email = creat_account_page.lineEdit_2.text()
    password = creat_account_page.lineEdit_3.text()
    confirm_password= creat_account_page.lineEdit_3.text()
   
    #verifica se a senha esttá igual a confirmção e se a senha tem mais de 8 caractres 
    if len(password) >=8 and password == confirm_password:
        try:
            account = auth.create_user_with_email_and_password(email,password)
            if account:
                error_dialog.showMessage('Conta cadastrada')
                creat_account_page.close()
                first_page.show()
        except:
            error_dialog.showMessage('E-mail invalido ou ja existe')
    else:
        error_dialog.showMessage('Verique se a confirmação da senha está coreto,a senha também deve ter mais de 8 caracteres')

# realiza o login
def login():
    email = first_page.lineEdit.text()
    password = first_page.lineEdit_2.text()
    try:
        #realiza o login no firebase
        user = auth.sign_in_with_email_and_password(email,password)

        # verifica se o login foi realizado
        if user:
            first_page.close()
            page_logged.show()
    except:
        error_dialog.showMessage('verifique o usuario e senha')



def logout():
    #auth.signOut()
    page_logged.close()
    first_page.show()



app = QtWidgets.QApplication([])

#define as telas do pyqt5
first_page = uic.loadUi('primeira_tela.ui')
page_logged = uic.loadUi('segunda_tela.ui')
creat_account_page = uic.loadUi('tela_cadastro.ui')

#conecta os botões das paginas com as funçoes 
first_page.pushButton.clicked.connect(login)
first_page.pushButton_2.clicked.connect(show_page_create_accout)
creat_account_page.pushButton.clicked.connect(creat_account)
page_logged.pushButton.clicked.connect(logout)

#mensagem de erro
error_dialog = QtWidgets.QErrorMessage()

#carreg a primeiro pagina
first_page.show()
app.exec()  
