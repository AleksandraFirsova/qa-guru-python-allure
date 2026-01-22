import allure

from selene import browser, have, by


@allure.title('Проверяем название Issue используя лямбда шаги через with allure.step')
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Открываем строку поиска"):
        browser.element(".header-search-button").click()

    with allure.step("Находим пользователя 'AleksandraFirsova'"):
        browser.element(".FormControl-input").send_keys("AleksandraFirsova/qa-guru-python-allure")
        browser.element(".FormControl-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("AleksandraFirsova/qa-guru-python-allure")).click()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue"):
        browser.element("a[href='/AleksandraFirsova/qa-guru-python-allure/issues/1']").should(
            have.exact_text("Issue example"))