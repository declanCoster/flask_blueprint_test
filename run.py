import logging

from test_blueprints import create_app

app = create_app()

if __name__ == '__main__':
    logging.basicConfig(filename='log_file.log', level=logging.DEBUG, 
                        format='%(levelname)s: %(asctime)s - %(message)s')
    logging.info('App started')
    app.run()