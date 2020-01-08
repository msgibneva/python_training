import random
import string
from model.subscriber import Subscriber
import os.path
import jsonpickle
import json


def random_string (prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Subscriber(firstname ="", secondname ="", lastname="", nick="", title="", companyname="", homeaddress="", homephone="",
                                     mobilephone="", work="", faxnumber="", email1="", email2="", email3="", homesite="", addresssec="", sechomenumber="", notes="")] + [
    Subscriber(firstname=random_string("firstname", 10), secondname=random_string("secondname", 20), lastname=random_string("lastname", 20))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/sub.json")

with open(file, "w") as f:
    #f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))
