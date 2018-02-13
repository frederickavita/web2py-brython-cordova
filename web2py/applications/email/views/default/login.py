from browser import document as doc
from browser.html import DIV, BUTTON, INPUT, H1,BR


container = doc['container']

def login(ev):
    doc['welcome'].style.display = "none"
    doc['login'].style.display = "block"

def register(ev):
    doc['welcome'].style.display = "none"
    doc['register'].style.display = "block"


def back(ev):
    if ev.target.id == "back_login":
        doc['login'].style.display = "none"
        doc['welcome'].style.display = "block"
    elif ev.target.id == "back_register":
        doc['register'].style.display = "none"
        doc['welcome'].style.display = "block"


# page d'acceuil avec les deux bouttons login et register
div1 = DIV(id="welcome")
button1 = BUTTON("Register", id="but_register")
button2 = BUTTON("Login", id="but_login")
div1 <= button1 + button2
container <= div1
# event pour boutton show login et show register
doc['but_login'].bind('click', login)
doc['but_register'].bind('click', register)
# page cacher de login

div2 = DIV(id="login", Class="w3-center")
title1 = H1("Login in")
input1 = INPUT(placeholder="Your email")
input2 = INPUT(placeholder="Your password")
back_button = BUTTON("Back", id="back_login")
button_submit = BUTTON("Submit")
div2 <= title1 + input1 + input2 + BR() + \
    back_button + BR() + button_submit
container <= div2
doc['back_login'].bind('click', back)

# page cacher de register
div3 = DIV(id="register", Class="w3-center")
title2 = H1("Register")
input3 = INPUT(placeholder="Your email")
input4 = INPUT(placeholder="Your password")
back_button = BUTTON("Back", id="back_register")
button_submit = BUTTON("Submit")
div3 <= title2 + input3 + input4 + BR() + \
    back_button + BR() + button_submit
container <= div3
doc['back_register'].bind('click', back)