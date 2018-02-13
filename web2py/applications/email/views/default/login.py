"""this script control event welcome page(first page)"""

from browser import document as doc
from browser.html import DIV, BUTTON, INPUT, H1, BR

"""select container id"""
container = doc['container']


def login(ev):
    """event login hide  welcome div
    show login div
    Arguments:
        if but_login id is clicked
    """
    doc['welcome'].style.display = "none"
    doc['login'].style.display = "block"


def register(ev):
    """ event register  hide welcome div
        show register div
    Arguments:
        if but_register id is clicked
    """

    doc['welcome'].style.display = "none"
    doc['register'].style.display = "block"


def back(ev):
    """back event show welcome id  and hide
       div id register or div id login
    Arguments:
        if ev.target.id == "back_login
            hide login id div
        elif ev.target.id == "back_register
            hide register id div
    """
    if ev.target.id == "back_login":
        doc['login'].style.display = "none"
        doc['welcome'].style.display = "block"
    elif ev.target.id == "back_register":
        doc['register'].style.display = "none"
        doc['welcome'].style.display = "block"


"""welcome page with two buttons  login and register"""
div1 = DIV(id="welcome")
button1 = BUTTON("Register", id="but_register")
button2 = BUTTON("Login", id="but_login")
div1 <= button1 + button2
container <= div1
"""event button for show login div and show register div """
doc['but_login'].bind('click', login)
doc['but_register'].bind('click', register)


"""login page""""
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

"""register page"""
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
