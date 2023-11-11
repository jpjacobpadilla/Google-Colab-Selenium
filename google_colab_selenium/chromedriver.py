from google_colab_selenium.colab_selenium_manager import ColabSeleniumManager
from google_colab_selenium.spinner import Spinner
from google_colab_selenium.exceptions import StartingChromeDriverError

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class ChromeDriver(webdriver.Chrome):
    """
    A thin wrapper around the Selenium Chrome Webdriver which makes it easy
    to use in Google Colab Notebooks.

    The ColabSeleniumManager class installs Google-Chrome-Stable and adds the
    nessasary headers to use in a Colab Notebook.

    The headers that are automatically added are:
        --headless
        --no-sandbox
        --disable-dev-shm-usage
        --lang=en
    """
    def __init__(self, options: Options = None, keep_alive: bool = True):
        self.manager = ColabSeleniumManager(options)

        try:
            with Spinner('Initializing Chromedriver', done='Initialized Chromedriver'):
                super().__init__(
                    service=self.manager.service,
                    options=self.manager.options,
                    keep_alive=keep_alive
                )

        except Exception as e:
            raise StartingChromeDriverError("""
                Failed to start ChromeDriver. This could be due to a number
                of factors, such as missing dependencies or incorrect
                configuration settings.
            """) from e