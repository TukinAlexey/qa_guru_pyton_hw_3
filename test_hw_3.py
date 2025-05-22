from selene import browser, be, have

def test_one(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Мы зарегистрировали подозрительный трафик'))

def test_second(open_browser):
    browser.element('[name="q"]').should(be.blank).type('sfgsdfgdsfgsdfgdfgdf').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу sfgsdfgdsfgsdfgdfgdf ничего не найдено.'))
