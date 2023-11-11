from google_colab_selenium.colab_selenium_manager import ColabSeleniumManager
from google_colab_selenium.spinner import Spinner
from google_colab_selenium.exceptions import StartingChromeDriverError

from selenium.webdriver.chrome.options import Options

try:
    import undetected_chromedriver as uc
except ImportError as e:
    raise ImportError('''
        Please install google-colab-selenium with the "undetected" 
        extra -> pip3 install google-colab-selenium[undetected]
    ''')

    
class UndetectedChromeDriver(uc.Chrome):
    """
    Instead of using ChromeDriver, which is easy to detect, you can use undetected-chromedriver.

    https://github.com/ultrafunkamsterdam/undetected-chromedriver

    This package is a great start to making Selenium undetectable,
    but you still need to act like a human.

    The ColabSeleniumManager class installs Google-Chrome-Stable and adds the
    nessasary headers to use in a Colab Notebook.

    The headers that are automatically added are:
        --headless
        --no-sandbox
        --disable-dev-shm-usage
        --lang=en
    """
    def __init__(self, options: Options = None, keep_alive: bool = True):

        self.manager = ColabSeleniumManager(options or uc.ChromeOptions())

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