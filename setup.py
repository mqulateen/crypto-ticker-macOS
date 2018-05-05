from setuptools import setup

APP = ['crypto_ticker.py']
DATA_FILES = []
OPTIONS = {
	'packages': [
        'requests',
        'rumps'
    ],
    'plist': {
        'CFBundleName': 'Crypto Ticker',
        'CFBundleIdentifier': 'com.mqul.crypto.ticker',
        'LSPrefersPPC': True,
        'LSUIElement': True,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
