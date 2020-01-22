from random import randrange
import re
from model.subscriber import Subscriber
from fixture.db import DbFixture


def test_sub_info(app):
    old_sub = app.subscriber.get_sub_list()
    index = randrange(len(old_sub))
    subscriber_from_home_page = app.subscriber.get_sub_list()[index]
    subscriber_from_edit_page = app.subscriber.get_info_from_edit_page(index)
    assert subscriber_from_home_page.homeaddress == subscriber_from_edit_page.homeaddress
    assert subscriber_from_home_page.firstname == subscriber_from_edit_page.firstname
    assert subscriber_from_home_page.lastname == subscriber_from_edit_page.lastname
    assert subscriber_from_home_page.all_phones_frome_home_page == merge_phones_like_on_home_page(subscriber_from_edit_page)
    assert subscriber_from_home_page.all_emails_frome_home_page == merge_emails_like_on_home_page(subscriber_from_edit_page)


def test_sub_db_home_page(app, db):
    subscriber_from_home_page = sorted(app.subscriber.get_sub_list(), key=Subscriber.id_or_max)
    subscriber_from_db = sorted(db.get_sub_list(), key=Subscriber.id_or_max)
    for i in range(len(subscriber_from_db)):
        sub_db = subscriber_from_db[i]
        sub_hp = subscriber_from_home_page[i]
        assert sub_hp.firstname == sub_db.firstname
        assert sub_hp.all_phones_frome_home_page == merge_phones_like_on_home_page(sub_db)
        assert sub_hp.all_emails_frome_home_page == merge_emails_like_on_home_page(sub_db)
        assert sub_hp.homeaddress == sub_db.homeaddress

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(subscriber):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                         [subscriber.homephone, subscriber.mobilephone, subscriber.work, subscriber.sechomenumber]))))

def merge_emails_like_on_home_page(subscriber):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter( lambda x: x is not None,
                                         [subscriber.email1, subscriber.email2, subscriber.email3]))))

