
def test_sub_info_on_home_page(app):
    subscriber_from_home_page = app.subscriber.get_sub_list()[0]
    subscriber_from_edit_page = app.subscriber.get_info_from_edit_page(0)
    assert subscriber_from_home_page.homeaddress == subscriber_from_edit_page.homeaddress
    assert subscriber_from_home_page.firstname == subscriber_from_edit_page.firstname
    assert subscriber_from_home_page.lastname == subscriber_from_edit_page.lastname



