class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_button=page.get_by_role("button",name="Login")
    def open_login_page(self):
        from config import BASE_URL
        self.page.goto(BASE_URL)

    def enter_username(self, username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()  