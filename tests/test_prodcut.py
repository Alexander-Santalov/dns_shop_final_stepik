import allure


@allure.label('owner', 'Александр Санталов')
@allure.title('Добавление товара в корзину по результату фильтрации')
def test_add_product_through_filter(app):
    with allure.step('Открытие стартовой страницы'):
        app.main_page.open_home_page()
    with allure.step('Первичная фильтрация по категории "Телевизоры"'):
        app.main_page.choose_tv_by_search()
    with allure.step('Установка и применение различных фильтров'):
        app.filter_page.set_and_apply_filters()
    with allure.step('Проверка результатов фильтрации'):
        app.filter_page.assert_result_filters()
    with allure.step('Добавление товара в корзину и проверка параметров всплывающего окна корзины'):
        app.filter_page.assert_product_in_cart_modal()
    with allure.step('Проверка отображения корзины с товаром'):
        app.filter_page.assert_display_cart()
    with allure.step('Проверка товара в корзине и в итоговой карточке'):
        app.cart_page.assert_result_in_cart()
