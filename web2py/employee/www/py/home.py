from browser import document as doc, window as win, html
import urllib.request
import json

response = None
retail = doc['detail']


def title_header():
    h1 = html.H1("Employee Directory",
                 Class="w3-wide w3-myfont w3-xlarge",
                 id="title", style={"text-align":"center"})
    return h1


def searchbar():
    css = {"padding": "1.01em 16px"}
    div = html.DIV(Class="w3-panel w3-border w3-round-xxlarge",
                   id="searchpanel", style=css)
    search = html.INPUT(Class="w3-input w3-border",
                        type="search", id='search')
    div <= search
    return div


def employee_list():
    global response
    try:
        hide = {'display': "none"}
        response = urllib.request.urlopen("http://127.0.0.1:8001/employee/default/liste_employee.json")
        response = response.read()
        response = json.loads(response)
        li = html.UL(id="id01", Class="w3-ul w3-card-4")
        for x in response['employee']:
            ul = html.LI(Class="w3-bar",style=hide)
            img = html.IMG(Class="w3-bar-item w3-circle",
                           src="img/img_avatar2.png", style={"width":"85px"})
            divbar = html.DIV(Class="w3-bar-item")
            a = html.A(x['full_name'],id=str(x['id']),href="#employee" + str(x['id']))
            divbar <=a
            ul <= img + divbar
            li <= ul
        return li
    except:
        div = html.DIV("We're sorry, server is busy")
        return div




def homepage():
    div1 = html.DIV()
    header = title_header()
    search = searchbar()
    list_empl = employee_list()
    div1 <= header + search + list_empl
    win.location.hash = "home"
    return div1


doc['container'] <= homepage()

@doc['search'].bind("input")
def filter_html(ev):
    print(ev.target.value)
    win.w3.filterHTML('#id01', 'li', ev.target.value)


def route(ev):
    global response
    if win.location.hash == "#home":
        win.w3.show("#container")
        retail.innerHTML = ''
    elif win.location.hash != "#home" and retail.innerHTML=='':
        win.location.hash = 'home'
        win.w3.show("#container")
    else:
        win.w3.hide("#container")
        doc['search'].value =''
        print(retail.innerHTML == '')

win.addEventListener("hashchange", route)


def back(ev):
    win.location.hash = "home"

def office(ev):
    doc['number'].click()

def mobile(ev):
    doc['mobile'].click()

def sms(ev):
    doc['sendsms'].click()

def email(ev):
    print("dqsdqsd")
    doc['sendemail'].click()


def detail_employee(ev):
    global response
    test = eval(ev.target.id)
    if isinstance(test, int):
        div = html.DIV(Class="w3-animate-left")
        div1 = html.DIV(Class="w3-border-bottom w3-bar w3-animate-left")
        i = html.I(Class="fa fa-angle-left w3-xxxlarge w3-text-cyan")
        a = html.A(Class="w3-bar-item",id="back", style={"width": "10%"})
        a <= i
        h1 =  html.H1("Employee Details",
                      Class="w3-wide w3-myfont w3-xlarge w3-bar-item w3-center",
                      style={"width": "90%"})
        div1 <= a + h1
        for x in response['employee']:
            ul = html.UL(Class="w3-ul w3-border w3-animate-left")
            if x['id'] == int(ev.target.id):
                li = html.LI(Class="w3-bar")
                img = html.IMG(Class="w3-bar-item w3-circle",
                           src="img/img_avatar2.png", style={"width":"85px"})
                #first li
                div2 = html.DIV(Class="w3-bar-item")
                span1 = html.SPAN(x['full_name']) + html.BR()
                span2 = html.SPAN(x['job'])
                div2 <= span1 + span2
                li <= img + div2
                #second li
                li2=  html.LI(Class="w3-bar w3-button w3-hover-cyan",id="office")
                div3 = html.DIV(Class="w3-bar-item")
                span3 = html.SPAN("Call Office") + html.BR()
                span4 = html.SPAN("781-000-002")
                a1 = html.A(href="tel:781-000-002",id="number" ,style={"display":"none"})
                span = html.SPAN(html.I(Class="fa fa-angle-right w3-xxlarge"),
                                 Class="w3-right w3-bar-item")
                div3 <= span3 + span4 + a1
                li2 <= span + div3
                #third li
                li3 = html.LI(Class="w3-bar w3-button w3-hover-cyan", id="call")
                div4 = html.DIV(Class="w3-bar-item")
                span5 = html.SPAN("Call Mobile") + html.BR()
                span6 = html.SPAN("615-000-002", href="tel:615-000-002")
                a2 = html.A(href="tel:615-000-002",id="mobile" ,style={"display":"none"} )
                spanbis = html.SPAN(html.I(Class="fa fa-angle-right w3-xxlarge"),
                                 Class="w3-right w3-bar-item")
                div4 <= span5 + span6 + a2
                li3 <= spanbis + div4
                # fourth li
                li4 = html.LI(Class="w3-bar w3-button w3-hover-cyan", id="sms")
                div5 = html.DIV(Class="w3-bar-item")
                span7 = html.SPAN("Number Sms") + html.BR()
                span8 = html.SPAN("615-000-002", href="tel:615-000-002")
                a3 = html.A(href="sms:615-000-002", id="sendsms", style={"display": "none"})
                spanbis1 = html.SPAN(html.I(Class="fa fa-angle-right w3-xxlarge"),
                                 Class="w3-right w3-bar-item")
                div5 <= span7 + span8 + a3
                li4 <= spanbis1 + div5
                #five li
                li5 = html.LI(Class="w3-bar w3-button w3-hover-cyan", id="email")
                div6 = html.DIV(Class="w3-bar-item")
                span9 = html.SPAN("Email Professional") + html.BR()
                span10 = html.SPAN("Freerelk@yahoo.fr",href="mailto:FREE@YAHOO.FR")
                a4 = html.A(href="mailto:FREE@YAHOO.FR", id="sendemail",style={"display": "none"})
                spanbis1 = html.SPAN(html.I(Class="fa fa-angle-right w3-xxlarge"),
                                     Class="w3-right w3-bar-item")
                div6 <= span9 + span10 + a4
                li5 <= spanbis1  + div6
                #end
                ul <= li + li2 + li3 + li4 +li5
                retail <= div1 + html.BR() + ul
                doc['back'].bind("click", back)
                doc['office'].bind("click", office)
                doc['call'].bind("click", mobile)
                doc['sms'].bind("click",sms)
                doc['email'].bind("click", email)
                return  retail



def ver():
    if response is not None:
        doc['id01'].bind("click",detail_employee)

win.onload = ver()