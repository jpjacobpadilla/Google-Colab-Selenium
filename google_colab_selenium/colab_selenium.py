import subprocess
import shutil

from google_colab_selenium.spinner import Spinner
from google_colab_selenium.exceptions import (
    ChromeDriverPathError, InstallChromeError,
    StartingChromeDriverError
)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.selenium_manager import SeleniumManager

import undetected_chromedriver as uc


class ColabSeleniumManager:
    default_colab_options = [
        '--headless',
        '--no-sandbox',
        '--disable-dev-shm-usage',
        '--lang=en'
    ]

    _downloaded_chrome = False

    download_command = ['curl', '-o', 'google-chrome-stable_current_amd64.deb', 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb']
    install_command = ['sudo', 'apt', 'install', './google-chrome-stable_current_amd64.deb', '-y']
    clean_up_command = ['rm', 'google-chrome-stable_current_amd64.deb']

    chromedriver_path: str = None

    def __init__(self, base_options: Options):
        if not self._downloaded_chrome:
            # Checks if Chrome was already installed. The class may of been reset.
            if shutil.which("google-chrome-stable") is None:
                self.install_chrome()
            else:
                self._downloaded_chrome = True

        self.options = self.default_options(base_options or Options())
        self.service = self.get_service()

    @classmethod
    def install_chrome(cls, *args, **kwargs) -> None:
        """
        To Install Google-Chrome-Stable, the first command uses CURL to download
        the debian file. Next Advanced Package Tool installs the file and once
        it's installed, the .deb file, which is no longer needed, is deleted.
        """
        try:
            with Spinner('Downloading Google Chrome', done='Downloaded Google Chrome'):
                subprocess.run(cls.download_command, check=True)
                subprocess.run(cls.install_command, check=True)
                subprocess.run(cls.clean_up_command, check=True)

        except Exception as e:
            raise InstallChromeError("Failed to install Google Chrome.") from e

        else:
            cls._downloaded_chrome = True

    @classmethod
    def default_options(cls, options: Options) -> Options:
        for default in cls.default_colab_options:
            options.add_argument(default)

        return options

    @classmethod
    def get_service(cls) -> Service:
        path = cls.chromedriver_path or cls.prepare_driver()
        return Service(path)

    @classmethod
    def prepare_driver(cls) -> str:
        try:
            path = SeleniumManager().driver_location(Options())
            cls.chromedriver_path = path
            return path

        except Exception as e:
            raise ChromeDriverPathError("Failed to find ChromeDriver.") from e


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