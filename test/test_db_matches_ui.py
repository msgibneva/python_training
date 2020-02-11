from model.group import Group
from timeit import timeit
import allure

#передаем в тест 2 фикстуры app и db
def test_group_list(app, db):
    #print(timeit(lambda: app.group.get_group_list(), number=1))
    with allure.step('Given a ui group list'):
        ui_list = app.group.get_group_list()
        def clean(group):
            return Group(id=group.id, name=group.name.strip())

    with allure.step('Given a ui group list'):
        db_list = map(clean, db.get_group_list())
        #print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    with allure.step('Then the ui group list is equal to the db group list'):
        sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
        #assert False