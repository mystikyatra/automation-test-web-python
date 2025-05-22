import pytest
from selenium import webdriver
from utils.video_recorder import start_recording, stop_recording

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def record_session_video():
    process = start_recording("videos/test_run.mp4")
    yield
    stop_recording(process)