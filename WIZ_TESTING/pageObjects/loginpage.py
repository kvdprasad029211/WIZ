class LoginPage:
    textbox_username_name="username"
    textbox_password_name="PSWD"
    button_login_id="Enter"
    link_logout_linktext="Exit"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_name(self.textbox_username_name).clear()
        self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_name(self.textbox_password_name).clear()
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
