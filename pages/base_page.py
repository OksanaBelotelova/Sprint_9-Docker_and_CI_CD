

class BasePage:

    LOGOUT = By. XPATH, './/а[text() = "Выход"]']
    
    def __init__(self, driver):
        self.driver = driver

    
