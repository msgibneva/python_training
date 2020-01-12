from model.subscriber import Subscriber
import random
import string


def random_string (prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Subscriber(firstname ="", secondname ="", lastname="", nick="", title="", companyname="", homeaddress="", homephone="",
                                     mobilephone="", work="", faxnumber="", email1="", email2="", email3="", homesite="", addresssec="", sechomenumber="", notes="")] + [
    Subscriber(firstname=random_string("firstname", 10), secondname=random_string("secondname", 20), lastname=random_string("lastname", 20))
    for i in range(5)
]

constant = [
    Subscriber(firstname="firstname1", secondname="secondname1", lastname="lastname1"),
    Subscriber(firstname="firstname2", secondname="secondname2", lastname="lastname2"),
]

