#!/usr/bin/python

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
 
@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на тестируемую страницу
    driver.get('https://b2c.passport.rt.ru/')
    driver.implicitly_wait(5)
    
    yield driver
 
    driver.quit()
 
# Autotest 1
# "Дымовой" тест - проверка основных элементов на странице
def test_smoke_test(driver):
    result_state = False

    try:
        # Логотип в левом верхнем углу страницы (в левой части "шапки" страницы)
        header_logo = driver.find_element(By.CSS_SELECTOR, 'header#app-header > div > div > svg')
        result_state = bool(header_logo)

        # Левая часть страницы
        # Логотип в левой части страницы
        left_side_logo = driver.find_element(By.CSS_SELECTOR, '#page-left > div > div.what-is-container__logo-container > svg')
        result_state = bool(left_side_logo)
        # Заголовок "Личный кабинет" в левой части страницы
        left_side_title = driver.find_element(By.CSS_SELECTOR, '#page-left > div > div.what-is > h2')
        # Текст в левой части страницы
        left_side_caption = driver.find_element(By.CSS_SELECTOR, '#page-left > div > div.what-is > p')
    
        # Правая часть страницы
        # Заголовок формы авторизации
        right_side_auth_form_title = driver.find_element(By.XPATH, '//*[@id="card-title"]')
        # Табы методов авторизации
        right_side_auth_form_tabs = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.tabs-input-container > div.rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs')
        # Поле ввода мобильного телефона
        right_side_auth_form_cellphone = driver.find_element(By.CSS_SELECTOR, '#username')
        # Поле ввода пароля
        right_side_auth_form_password = driver.find_element(By.CSS_SELECTOR, '#password')
        # Кнопка отправки формы
        right_side_auth_form_submit_btn = driver.find_element(By.CSS_SELECTOR, '#kc-login')

        # "Подвал" страницы
        # Copyright в левой части "подвала"
        footer_copyright = driver.find_element(By.CSS_SELECTOR, '#app-footer > div.rt-footer-left > div.rt-footer-left__item.rt-footer-copyright.rt-footer-side-item')
        # Текст в центре "подвала"
        footer_message = driver.find_element(By.CSS_SELECTOR, '#app-footer > div.rt-footer-left > div:nth-child(2)')
        # Телефон техподдержки в правой части "подвала"
        footer_ts = driver.find_element(By.XPATH, '//*[@id="app-footer"]/div[2]/a')

        result_state = True
    except NoSuchElementException:
        pass

    assert result_state == True

# Autotest 2
# Отображение компонетов формы авторизации
def test_auth_form_comps(driver):
    result_state = False
    
    try:
        # Заголовок формы авторизации
        right_side_auth_form_title = driver.find_element(By.XPATH, '//*[@id="card-title"]')
        # Табы методов авторизации
        right_side_auth_form_tabs = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.tabs-input-container > div.rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs')
        # Поле ввода мобильного телефона (логина)
        right_side_auth_form_cellphone = driver.find_element(By.CSS_SELECTOR, '#username')
        # Поле ввода пароля
        right_side_auth_form_password = driver.find_element(By.CSS_SELECTOR, '#password')
        # checkbox "Запомнить меня"
        chckbx_rem_me = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.login-form__remember-forgot-con > div > span.rt-checkbox__label-desc > span.rt-checkbox__label')
        # Ссылка "Забыл пароль"
        frgt_passwd_link = driver.find_element(By.CSS_SELECTOR, '#forgot_password')
        # Кнопка отправки формы
        right_side_auth_form_submit_btn = driver.find_element(By.CSS_SELECTOR, '#kc-login')
        # Сообщение о согласии с пользовательским соглашением
        sbmt_ua_text = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.auth-policy')
        # Кнопка авторизации по T-ID
        tid_auth_button = driver.find_element(By.CSS_SELECTOR, '#oidc_tinkoff')
        # Кнопка авторизации по Яндекс ID
        yid_auth_button = driver.find_element(By.CSS_SELECTOR, '#oidc_ya')
        # Кнопка авторизации через VK
        vk_auth_button = driver.find_element(By.CSS_SELECTOR, '#oidc_vk')
        # Кнопка авторизации через Mail.ru
        mr_auth_button = driver.find_element(By.CSS_SELECTOR, '#oidc_mail')
        # Кнопка авторизации через Одноклассники
        ok_auth_button = driver.find_element(By.CSS_SELECTOR, '#oidc_ok')
        # Текст и ссылка на регистрацию
        reg_text_link = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.login-form__register-con')
        # Ссылка на помощь
        help_link = driver.find_element(By.CSS_SELECTOR, '#faq-open > a')

        result_state = True
    except NoSuchElementException:
        pass

    assert result_state == True
    
# Autotest 3
# Переключение на метод авторизации по E-mail
def test_sw_to_eml_auth(driver):
    # Нажать ЛКМ на таб авторизации по почте
    eml_auth_tab = driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail')
    eml_auth_tab.click()

    # Считать placeholder поля логина
    lgn_ph = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.tabs-input-container > div.rt-input-container.tabs-input-container__login > div > span')
    
    # Проверка, что placeholder поля логина сменился на "Электронная почта"
    assert lgn_ph.text == "Электронная почта"

# Autotest 4
# Переключение на метод авторизации по Логину
def test_sw_to_lgn_auth(driver):
    # Нажать ЛКМ на таб авторизации по логину
    lgn_auth_tab = driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login')
    lgn_auth_tab.click()
    
    # Считать placeholder поля логина
    lgn_ph = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.tabs-input-container > div.rt-input-container.tabs-input-container__login > div > span')
    
    # Проверка, что placeholder поля логина сменился на "Логин"
    assert lgn_ph.text == "Логин"
    
# Autotest 5
# Переключение на метод авторизации по Лицевому счёту
def test_sw_to_pacc_auth(driver):
    # Нажать ЛКМ на таб авторизации по Лицевому счёту
    pacc_auth_tab = driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-ls')
    pacc_auth_tab.click()
        
    # Считать placeholder поля логина
    lgn_ph = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.tabs-input-container > div.rt-input-container.tabs-input-container__login > div > span')
        
    # Проверка, что placeholder поля логина сменился на "Лицевой счёт"
    assert lgn_ph.text == "Лицевой счёт"

# Autotest 6
# Переключение на метод авторизации по Телефону
def test_sw_to_phn_auth(driver):
    # Нажать ЛКМ на таб авторизации по Телефону
    phn_auth_tab = driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone')
    phn_auth_tab.click()
        
    # Считать placeholder поля логина
    lgn_ph = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.tabs-input-container > div.rt-input-container.tabs-input-container__login > div > span')
        
    # Проверка, что placeholder поля логина сменился на "Лицевой счёт"
    assert lgn_ph.text == "Мобильный телефон"

# Autotest 7
# Вывод помощи
def test_disp_help(driver):
    # Нажать ЛКМ на ссылку "Помощь" внизу формы авторизации
    driver.find_element(By.CSS_SELECTOR, '#faq-open > a').click()

    # Считать заголовок появившегося модального окна
    mdl_hdr = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.base-modal-wrapper.faq-modal > div > div > div > h1')

    # Проверка, что заголовок появившегося модального окна - "Ваш безопасный ключ к сервисам Ростелекома"
    assert mdl_hdr.text == "Ваш безопасный ключ к сервисам Ростелекома"

# Autotest 8
# Осуществляется переход на страницу регистрации
def test_reg_href(driver):
    # Нажать ЛКМ на ссылку "Зарегистрироваться" внизу формы регистрации
    driver.find_element(By.CSS_SELECTOR, '#kc-register').click()
    # Подождать загрузки страницы
    driver.implicitly_wait(5)

    # Считать заголовок появившейся формы
    frm_hdr = driver.find_element(By.CSS_SELECTOR, '#card-title')

    # Проверка, что заголовок появившейся формы - "Регистрация"
    assert frm_hdr.text == "Регистрация"

# Autotest 9
# Осуществляется переход на страницу авторизации по T-ID
def test_tid_href(driver):
    # Нажать ЛКМ на кнопку T-ID внизу формы регистрации
    driver.find_element(By.CSS_SELECTOR, '#oidc_tinkoff').click()
    # Подождать загрузки страницы
    driver.implicitly_wait(5)

    # Считать заголовок появившейся формы
    frm_hdr = driver.find_element(By.CSS_SELECTOR, '#form-title')

    # Проверка, что заголовок появившейся формы - "Вы входите в Ростелеком ID"
    assert frm_hdr.text == "Вы входите в Ростелеком ID"

# Autotest 10
# Осуществляется переход на страницу авторизации по Яндекс ID
def test_yid_href(driver):
    # Нажать ЛКМ на кнопку Яндекс ID внизу формы регистрации
    driver.find_element(By.CSS_SELECTOR, '#oidc_ya').click()
    # Подождать загрузки страницы
    driver.implicitly_wait(5)

    # Считать заголовок появившейся формы
    frm_hdr = driver.find_element(By.CSS_SELECTOR, '#root > div > div.passp-page > div.passp-flex-wrapper > div > div > div.passp-auth-content > div:nth-child(3) > div > form > div.Phone.Phone_0_layout_container > div.Phone-head.layout_head > h1')

    # Проверка, что заголовок появившейся формы - "Войдите с Яндекс ID"
    assert frm_hdr.text == "Войдите с Яндекс ID"

# Autotest 11
# Осуществляется переход на страницу авторизации по VK ID
def test_vkid_href(driver):
    # Нажать ЛКМ на кнопку VK ID внизу формы регистрации
    driver.find_element(By.CSS_SELECTOR, '#oidc_vk').click()
    # Подождать загрузки страницы
    driver.implicitly_wait(5)

    # Считать заголовок появившейся формы
    frm_hdr = driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div > div.vkuiSplitLayout__inner.vkc__AuthRoot__root > div > div.vkuiSplitCol.vkuiSplitCol--viewWidth-none.vkuiInternalSplitCol--viewWidth-none.vkc__AuthRoot__col.vkc__AuthRoot__contentCol > div > div > div > form > div:nth-child(1) > div > h1 > div')

    # Проверка, что заголовок появившейся формы - "Sign in to «РТК Паспорт»"
    assert frm_hdr.text == 'Sign in to «РТК Паспорт»'

# Autotest 12
# Осуществляется переход на страницу авторизации по Mail.ru ID
def test_mrid_href(driver):
    # Нажать ЛКМ на кнопку Mail.ru ID внизу формы регистрации
    driver.find_element(By.CSS_SELECTOR, '#oidc_mail').click()
    # Подождать загрузки страницы
    driver.implicitly_wait(5)

    # Считать заголовок появившейся формы
    frm_hdr = driver.find_element(By.CSS_SELECTOR, '#wrp > div.header > span')

    # Проверка, что заголовок появившейся формы - "My World@Mail.Ru"
    assert frm_hdr.text == 'My World@Mail.Ru'

# Autotest 13
# Осуществляется переход на страницу авторизации по OK ID
def test_okid_href(driver):
    # Нажать ЛКМ на кнопку OK ID внизу формы регистрации
    driver.find_element(By.CSS_SELECTOR, '#oidc_ok').click()
    # Подождать загрузки страницы
    driver.implicitly_wait(5)

    # Считать заголовок появившейся формы
    frm_hdr = driver.find_element(By.CSS_SELECTOR, '#widget-el > div.ext-widget_h > div')

    # Проверка, что заголовок появившейся формы - "OK"
    assert frm_hdr.text == 'OK'

# Autotest 14
# Стандартная авторизация по логину и паролю
def test_lgn_passwd_auth(driver):
    # Перейти на таб "Логин" формы авторизации.
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').click()
    # Ввести логин
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('')     # Ввести существующий в системе логин
    # Ввести пароль
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')     # Ввести валидный пароль
    # Нажать ЛКМ на кнопку отправки формы
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    # Подождать загрузки страницы
    driver.implicitly_wait(5)
    
    # Считать заголовок появившейся страницы
    pg_hdr = driver.find_element(By.CSS_SELECTOR, '#app > main > div.app-container__top > h1')

    # Проверка, что заголовок появившейся страницы - "Вход и безопасность"
    assert pg_hdr.text == 'Вход и безопасность'

# Autotest 15
# Стандартная авторизация по номеру телефона и паролю
def test_ph_passwd_auth(driver):
    # Перейти на таб "Телефон" формы авторизации.
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone').click()
    # Ввести логин
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('')      # Ввести существующий в системе мобильный телефон
    # Ввести пароль
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')      # Ввести валидный пароль
    # Нажать ЛКМ на кнопку отправки формы
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    # Подождать загрузки страницы
    driver.implicitly_wait(5)
    
    # Считать заголовок появившейся страницы
    pg_hdr = driver.find_element(By.CSS_SELECTOR, '#app > main > div.app-container__top > h1')

    # Проверка, что заголовок появившейся страницы - "Вход и безопасность"
    assert pg_hdr.text == 'Вход и безопасность'

# Autotest 16
# Стандартная авторизация по E-mail и паролю
def test_eml_passwd_auth(driver):
    # Перейти на таб "Почта" формы авторизации.
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()
    # Ввести логин
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('')      # Ввести существующий в системе E-mail
    # Ввести пароль
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')      # Ввести валидный пароль
    # Нажать ЛКМ на кнопку отправки формы
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    # Подождать загрузки страницы
    driver.implicitly_wait(5)
    
    # Считать заголовок появившейся страницы
    pg_hdr = driver.find_element(By.CSS_SELECTOR, '#app > main > div.app-container__top > h1')

    # Проверка, что заголовок появившейся страницы - "Вход и безопасность"
    assert pg_hdr.text == 'Вход и безопасность'

# Autotest 17
# Авторизация по несуществующему в системе логину
def test_wrng_lgn_auth(driver):
    # Перейти на таб "Логин" формы авторизации.
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').click()
    # Ввести логин
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('rtkid')
    # Ввести пароль
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')     # Ввести валидный пароль
    # Нажать ЛКМ на кнопку отправки формы
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    # Подождать загрузки страницы
    driver.implicitly_wait(5)
    
    # Найти сообщение о неверном логине или пароле
    err_msg = driver.find_element(By.CSS_SELECTOR, '#form-error-message')

    # Проверка, что сообщение - "Неверный логин или пароль"
    assert err_msg.text == 'Неверный логин или пароль'

# Autotest 18
# Авторизация по существующему в системе логину с неверным паролем
def test_lgn_wrng_passwd_auth(driver):
    # Перейти на таб "Логин" формы авторизации.
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').click()
    # Ввести логин
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('')      # Ввести существующий в системе логин
    # Ввести пароль
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('abrakadabra')
    # Нажать ЛКМ на кнопку отправки формы
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    # Подождать загрузки страницы
    driver.implicitly_wait(5)
    
    # Найти сообщение о неверном логине или пароле
    err_msg = driver.find_element(By.CSS_SELECTOR, '#form-error-message')

    # Проверка, что сообщение - "Неверный логин или пароль"
    assert err_msg.text == 'Неверный логин или пароль'

# Autotest 19
# Авторизация по несуществующему в системе мобильному телефону
def test_wrng_ph_auth(driver):
    # Перейти на таб "Телефон" формы авторизации.
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone').click()
    # Ввести логин
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('71234567890')
    # Ввести пароль
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')     # Ввести валидный пароль
    # Нажать ЛКМ на кнопку отправки формы
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    # Подождать загрузки страницы
    driver.implicitly_wait(5)
    
    # Найти сообщение о неверном логине или пароле
    err_msg = driver.find_element(By.CSS_SELECTOR, '#form-error-message')

    # Проверка, что сообщение - "Неверный логин или пароль"
    assert err_msg.text == 'Неверный логин или пароль'

# Autotest 20
# Авторизация по существующему в системе мобильному телефону с неверным паролем
def test_ph_wrng_pass_auth(driver):
    # Перейти на таб "Телефон" формы авторизации.
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone').click()
    # Ввести логин
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('')      # Ввести существующий в системе мобильный телефон
    # Ввести пароль
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('abrakadabra')
    # Нажать ЛКМ на кнопку отправки формы
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    # Подождать загрузки страницы
    driver.implicitly_wait(5)
    
    # Найти сообщение о неверном логине или пароле
    err_msg = driver.find_element(By.CSS_SELECTOR, '#form-error-message')

    # Проверка, что сообщение - "Неверный логин или пароль"
    assert err_msg.text == 'Неверный логин или пароль'

# Autotest 21
# Авторизация по несуществующему в системе E-mail
def test_wrng_eml_auth(driver):
    # Перейти на таб "Почта" формы авторизации.
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()
    # Ввести логин
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('pochta@mail.com')
    # Ввести пароль
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')     # Ввести валидный пароль
    # Нажать ЛКМ на кнопку отправки формы
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    # Подождать загрузки страницы
    driver.implicitly_wait(5)
    
    # Найти сообщение о неверном логине или пароле
    err_msg = driver.find_element(By.CSS_SELECTOR, '#form-error-message')

    # Проверка, что сообщение - "Неверный логин или пароль"
    assert err_msg.text == 'Неверный логин или пароль'

# Autotest 22
# Авторизация по существующему в системе E-mail с неверным паролем 
def test_eml_wrng_pass_auth(driver):
    # Перейти на таб "Почта" формы авторизации.
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()
    # Ввести логин
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('')      # Ввести существующий в системе E-mail
    # Ввести пароль
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('abrakadabra')
    # Нажать ЛКМ на кнопку отправки формы
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    # Подождать загрузки страницы
    driver.implicitly_wait(5)
    
    # Найти сообщение о неверном логине или пароле
    err_msg = driver.find_element(By.CSS_SELECTOR, '#form-error-message')

    # Проверка, что сообщение - "Неверный логин или пароль"
    assert err_msg.text == 'Неверный логин или пароль'
