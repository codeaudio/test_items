from selenium import webdriver
import time, pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default= None,
                     help="Dedault browser: none. You can chooseru or es")

@pytest.fixture(scope="class") 
def browser(request):
    print("\nstart browser for test..")
    options = Options()
    language_name = request.config.getoption("language")

    prefs = {'intl.accept_languages': language_name
    }
    options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(options=options)                                                                                  
    yield browser                                                                                                                        
    time.sleep(1)                                                                                                                           
    print("\nquit browser...")
    browser.quit()
