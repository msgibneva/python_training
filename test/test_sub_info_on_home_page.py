from random import randrange
import re


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

