import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestSauceDemo:
    @pytest.mark.login
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_visible(inventory_page.SHOPPING_CART), "Login failed"

    @pytest.mark.login
    def test_failed_login(self, driver):
        login_page = LoginPage(driver)

        login_page.navigate()
        login_page.login("locked_out_user", "secret_sauce")

        assert "Epic sadface" in login_page.get_error_message()

    @pytest.mark.inventory
    def test_add_item_to_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_to_cart("Sauce Labs Backpack")
        # Add verification for cart badge or item added

    @pytest.mark.inventory
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.logout()
        assert login_page.is_visible(login_page.USERNAME_INPUT), "Logout failed"