import allure

from selene import browser, by, have


@allure.title('Проверяем название Issue и делаем разметку тестов всеми аннотациями')
@allure.epic('Веб-интерфейс GitHub')
@allure.feature('Задачи в репозитории')
@allure.story('Поиск и проверка названия Issue через поиск пользователя')
@allure.tag('issue', 'search')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('owner', 'AleksandraFirsova')
@allure.description('Этот тест проверяет полный сценарий поиска Issue через поиск пользователя на GitHub')
@allure.link('https://github.com', name='Testing')
def test_dynamic_labels():
    open_main_page()
    search_for_repository("AleksandraFirsova/qa-guru-python-allure")
    go_to_repository("AleksandraFirsova/qa-guru-python-allure")
    open_issue_tab()
    should_see_issue_with_name("Issue example")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    browser.element(".header-search-button").click()
    browser.element(".FormControl-input").send_keys(repo)
    browser.element(".FormControl-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с названием {name}")
def should_see_issue_with_name(name):
    browser.element("a[href='/AleksandraFirsova/qa-guru-python-allure/issues/1']").should(
        have.exact_text(name))