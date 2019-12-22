from sys import maxsize


class Subscriber:

    def __init__(self, firstname=None, secondname=None, lastname=None, nick=None, title=None, companyname=None, homeaddress=None, homephone=None,
                              mobilephone=None, work=None, faxnumber=None, email1=None, email2=None, email3=None, homesite=None, addresssec=None, sechomenumber=None, notes=None, id=None):
        self.firstname = firstname
        self.secondname = secondname
        self.lastname = lastname
        self.nick = nick
        self.title = title
        self.companyname = companyname
        self.homeaddress = homeaddress
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.work = work
        self.faxnumber = faxnumber
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homesite = homesite
        self.addresssec = addresssec
        self.sechomenumber = sechomenumber
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize