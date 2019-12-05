from model.subscriber import Subscriber


def test_add_sub(app):
    app.session.login(username = "admin", password = "secret")
    app.subscriber.edit_first_sub(Subscriber(name ="newname", secondname ="newsecondname", surname="newsurname", nick="newnic", title="newtitle", companyname="newcompany", homeaddress="newaddress", homephone="newhomephone",
                                     mobilephone="newmobile", work="newwork", faxnumber="newfax", email1="newemail1", email2="newemail2", email3="newemail3", homesite="newhomesite", bday="11", bmonth="November",
                                     aday="11", amonth="December", byear="1999", ayear="2222", addresssec="newaddresssec", sechomenumber="newsechome", notes="newnotes"))
    app.session.logout()