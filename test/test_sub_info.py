from random import randrange


def test_sub_info_on_home_page(app):
    old_sub = app.subscriber.get_sub_list()
    index = randrange(len(old_sub))
    subscriber_from_home_page = app.subscriber.get_sub_list()[index]
    subscriber_from_edit_page = app.subscriber.get_info_from_edit_page(index)
    assert subscriber_from_home_page.homeaddress == subscriber_from_edit_page.homeaddress
    assert subscriber_from_home_page.firstname == subscriber_from_edit_page.firstname
    assert subscriber_from_home_page.lastname == subscriber_from_edit_page.lastname



