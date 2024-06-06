import logging
import os

from starter.app import create_app

logging.basicConfig(level=os.environ.get('ROOT_LOG_LEVEL', 'INFO'))
logging.getLogger('starter').setLevel(level=os.environ.get('STARTER_LOG_LEVEL', 'INFO'))

if __name__ == '__main__':
    create_app().run(debug=True, host="0.0.0.0", port=5001)
