# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from utils.video_recorder import start_recording, stop_recording

# @pytest.fixture
# def driver():
#     options = Options()
#     options.add_argument("--disable-infobars")
#     options.add_argument("--disable-extensions")
#     options.add_argument("--disable-notifications")
#     options.add_argument("--disable-popup-blocking")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-save-password-bubble")
#     options.add_argument("--disable-features=AutofillServerCommunication,PasswordManagerEnableAccountStorage")
#     options.add_argument("--incognito")
#     options.add_argument("--disable-features=AutofillServerCommunication,PasswordManagerEnableAccountStorage")
#     options.add_argument("--incognito")

#     # Disable password manager popups
#     prefs = {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False
#     }
#     options.add_experimental_option("prefs", prefs)

#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# @pytest.fixture(scope="session", autouse=True)
# def record_session_video():
#     process = start_recording("videos/test_run.mp4")
#     yield
#     stop_recording(process)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.video_recorder import start_recording, stop_recording

@pytest.fixture(scope="session", autouse=True)
def record_session_video():
    process = start_recording("videos/test_run.mp4")
    yield
    stop_recording(process)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=AutofillServerCommunication,PasswordManagerEnableAccountStorage")
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1080")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
