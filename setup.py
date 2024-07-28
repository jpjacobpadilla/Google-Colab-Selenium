from setuptools import setup


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='google-colab-selenium',
    description='Easily use Selenium in Google Colab Notebooks!',
    version='1.0.14',
    packages=['google_colab_selenium'],
    install_requires=['selenium'],
    extras_require={
        'undetected': ['undetected-chromedriver']
    },
    author = 'Jacob Padilla',
    author_email = 'jp@jacobpadilla.com',
    url='https://github.com/jpjacobpadilla/Google-Colab-Selenium',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='selenium google-colab webdriver automation chromedriver'
)
