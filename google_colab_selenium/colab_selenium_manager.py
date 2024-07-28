import threading
import subprocess

from google_colab_selenium.spinner import Spinner
from google_colab_selenium.exceptions import (
    ChromeDriverPathError, InstallChromeError, GoogleColabSeleniumError
)

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.driver_finder import DriverFinder


class ColabSeleniumManager:
    default_colab_options = [
        '--headless',
        '--no-sandbox',
        '--disable-dev-shm-usage',
        '--lang=en'
    ]

    _downloaded_chrome = False
    _updated_apt = False

    update_apt = ['sudo', 'apt', 'update']
    upgrade_apt = ['sudo', 'apt', 'upgrade']

    download_command = ['curl', '-o', 'google-chrome-stable_current_amd64.deb', 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb']
    install_command = ['sudo', 'apt', 'install', './google-chrome-stable_current_amd64.deb', '-y']
    clean_up_command = ['rm', 'google-chrome-stable_current_amd64.deb']

    chromedriver_path: str = None

    __initialization_lock = threading.Lock()

    def __init__(self, base_options: Options):
        with ColabSeleniumManager.__initialization_lock:
            if not self._updated_apt:
                self.update_upgrade_apt()

            if not self._downloaded_chrome:
                self.install_chrome()

            self.options = self.default_options(base_options or Options())
            self.service = self.get_service()

    @classmethod
    def update_upgrade_apt(cls) -> None:
        try:
            with Spinner('Updating and upgrading APT', done='Updated and upgraded APT'):
                subprocess.run(cls.update_apt, check=True)
                subprocess.run(cls.upgrade_apt, check=True)
        
        except Exception as e:
            raise GoogleColabSeleniumError('Failed to update and upgrade APT') from e

        else:
            cls._updated_apt = True

    @classmethod
    def install_chrome(cls) -> None:
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

    def get_service(self) -> Service:
        path = ColabSeleniumManager.chromedriver_path or self.prepare_driver()
        return Service(path)

    def prepare_driver(self) -> str:
        try:
            path = DriverFinder(Service(), self.options).get_driver_path()
            ColabSeleniumManager.chromedriver_path = path
            return path

        except Exception as e:
            raise ChromeDriverPathError("Failed to find ChromeDriver.") from e





