import re
from random import randrange


def test_phones_on_home_page(app):
    old_sub = app.subscriber.get_sub_list()
    index = randrange(len(old_sub))
    subscriber_from_home_page = app.subscriber.get_sub_list()[index]
    subscriber_from_edit_page = app.subscriber.get_info_from_edit_page(index)
    assert subscriber_from_home_page.all_phones_frome_home_page == merge_phones_like_on_home_page(subscriber_from_edit_page)

def test_phones_on_sub_view_page(app):
    subscriber_from_view_page = app.subscriber.get_sub_from_view_page(0)
    subscriber_from_edit_page = app.subscriber.get_info_from_edit_page(0)
    assert subscriber_from_view_page.homephone == subscriber_from_edit_page.homephone
    assert subscriber_from_view_page.mobilephone == subscriber_from_edit_page.mobilephone
    assert subscriber_from_view_page.work == subscriber_from_edit_page.work
    assert subscriber_from_view_page.sechomenumber == subscriber_from_edit_page.sechomenumber

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(subscriber):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                         [subscriber.homephone, subscriber.mobilephone, subscriber.work, subscriber.sechomenumber]))))

