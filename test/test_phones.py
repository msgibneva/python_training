import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.subscriber.get_sub_list()[0]
    contact_from_edit_page = app.subscriber.get_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_frome_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_sub_view_page(app):
    contact_from_view_page = app.subscriber.get_sub_from_view_page(0)
    contact_from_edit_page = app.subscriber.get_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.sechomenumber == contact_from_edit_page.sechomenumber

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(subscriber):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter( lambda x: x is not None,
                                         [subscriber.homephone, subscriber.mobilephone, subscriber.work, subscriber.sechomenumber]))))

