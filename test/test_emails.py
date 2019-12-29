import re
from random import randrange


def test_emails_on_home_page(app):
    old_sub = app.subscriber.get_sub_list()
    index = randrange(len(old_sub))
    subscriber_from_home_page = app.subscriber.get_sub_list()[index]
    subscriber_from_edit_page = app.subscriber.get_info_from_edit_page(index)
    assert subscriber_from_home_page.all_emails_frome_home_page == merge_emails_like_on_home_page(subscriber_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(subscriber):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter( lambda x: x is not None,
                                         [subscriber.email1, subscriber.email2, subscriber.email3]))))