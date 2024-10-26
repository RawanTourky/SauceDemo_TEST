class TestData:
    BASE_URL = "https://www.saucedemo.com"
    VALID_PASSWORD = "secret_sauce"

    USERS = {
        "standard_user": {
            "expected_result": "success"
        },
        "locked_out_user": {
            "expected_result": "error"
        },
        "problem_user": {
            "expected_result": "success"
        },
        "performance_glitch_user": {
            "expected_result": "success"
        }
    }

    CUSTOMER_INFO = {
        "firstname": "John",
        "lastname": "Doe",
        "postal_code": "12345"
    }

    INVENTORY_ITEMS = {
        "backpack": "Sauce Labs Backpack",
        "bike_light": "Sauce Labs Bike Light",
        "bolt_shirt": "Sauce Labs Bolt T-Shirt"
    }

    ERROR_MESSAGES = {
        "locked_out": "Epic sadface: Sorry, this user has been locked out.",
        "invalid_credentials": "Epic sadface: Username and password do not match any user in this service"
    }

    CHECKOUT_INFO = {
        "success_message": "THANK YOU FOR YOUR ORDER",
        "error_firstname": "Error: First Name is required",
        "error_lastname": "Error: Last Name is required",
        "error_postal": "Error: Postal Code is required"
    }