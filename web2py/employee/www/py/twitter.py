from browser import document as doc, window as win, html
posting = False
response = ''
xhttp = win.XMLHttpRequest.new()



def hideshow(ide1, ide2, hash):
    doc[ide1].style.display = "block"
    doc[ide2].style.display = "none"
    win.location.hash = hash


def remove(ev):
    win.localStorage.clear()
    win.location.reload()



def callresponsepost():
    if len(response) > 40:
        win.localStorage.user = response
        r = win.JSON.parse(win.localStorage.user)
        r = r.screen_name
        button = html.BUTTON("Remove data",Class="w3-button w3-blue w3-center",
                 id="remove")
        name = "Hi {nam} welcome !".format(nam=r)
        h1 = html.H1(name)
        doc['user'] <= h1  + button
        doc['remove'].bind("click", remove)
        hideshow("user", "loading", "user")



    else:
        win.swal(
            "Sorry, Request failed, press the sign up button again to log you")
        hideshow("login", "loading", "login")
        win.localStorage.clear()


def callresponseget():
    global response
    win.localStorage.twitter = response
    url = win.JSON.parse(win.localStorage.twitter)
    url = url.url
    win.location.href = url


def askapitwitter(ev):
    global response
    global posting
    if ev.target.status == 200:
        response = ev.target.responseText
        if response != "Invalid response":
            if posting is False:
                if response != "Invalid response":
                    win.setTimeout(callresponseget, 50)
                else:
                    hideshow("login", "loading", "login")
                    win.swal("Sorry, Request failed")
            else:
                win.setTimeout(callresponsepost, 50)


def onError(ev):
    hideshow("login", "loading", "login")
    win.swal("Sorry, Request failed")


def endtime(ev):
    print("time")
    hideshow("login", "loading", "login")
    win.swal("Sorry, Request failed")

@doc['buttonsend'].bind("click")
def getbuton(ev):
    if win.navigator.onLine:
        url = 'https://www.perlamode.com/twitter/connecte.html'
        hideshow('loading', 'login', "loading")
        xhttp.onerror = onError
        xhttp.onload = askapitwitter
        xhttp.timeout = 8000
        xhttp.ontimeout = endtime
        xhttp.open("GET", url, True)
        xhttp.send()
    else:
        win.swal("Sorry, you are offline")


def envoiepost(url, variable):
    global posting
    posting = True
    sendvariable = "href=" + variable
    xhttp.onerror = onError
    xhttp.onload = askapitwitter
    xhttp.timeout = 7000
    xhttp.ontimeout = endtime
    xhttp.open("POST", url, True)
    xhttp.setRequestHeader(
        "Content-Type", "application/x-www-form-urlencoded")
    xhttp.send(sendvariable)


def register():
    if (win.navigator.onLine and
            "twitter" in win.localStorage):
        twitter = win.localStorage.twitter
        twitter = win.JSON.parse(twitter)
        href = twitter.href
        envoiepost("https://www.perlamode.com/twitter/registering.html", href)
    else:
        hideshow("login", "loading", "login")
        win.swal("Sorry, Request failed, press the"
                 "sign up button again to log you")


if 'twitter' in win.localStorage and \
        'user' not in win.localStorage:
    register()
elif "twitter" in win.localStorage and \
        'user' in win.localStorage:
    posting = True
    register()
else:
    hideshow('login', 'loading', "loading")
