from browser import document as doc, window as win, html



def title_header():
    h1 = html.H1("Employee Directory",Class="title")
    return h1


def searchbar():
    search = html.INPUT(type="search")
    return search


def employee_list():
    employe = ['Christophe Coenraets', 'Lisa Jones']
    li = html.UL()
    for x in employe:
        ul = html.LI(x)
        li <= ul
    return li


def homepage():
    div1 = html.DIV()
    header = title_header()
    search = searchbar()
    list_empl = employee_list()
    div1 <= header + search + list_empl
    return div1


doc['container'] <= homepage()