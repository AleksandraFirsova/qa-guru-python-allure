import allure

from selene import browser, have, by


@allure.title('Проверяем название Issue на чистом Selene')
def test_github():
    browser.open("https://github.com")

    browser.element(".header-search-button").click()
    browser.element(".FormControl-input").send_keys("AleksandraFirsova/qa-guru-python-allure")
    browser.element(".FormControl-input").submit()
    browser.element(by.link_text("AleksandraFirsova/qa-guru-python-allure")).click()
    browser.element("#issues-tab").click()
    browser.element("a[href='/AleksandraFirsova/qa-guru-python-allure/issues/1']").should(
        have.exact_text("Issue example"))