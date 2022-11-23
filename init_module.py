import argparse
import logging
import os
import time

import analyzer
import config
from database import db_connector
from database.db_engine import db_session


def init_argparser():
    parser = argparse.ArgumentParser(description='Define mood of the text.')
    parser.add_argument('--log-path', '-lp', type=str, default=config.PATH_ROOT + config.LOG_PATH)
    return parser.parse_args()


def init_logger(log_path: str):
    if not os.path.isdir(log_path):
        os.mkdir(log_path)
    logging.basicConfig(filename=log_path + 'SentimentAnalyzer.log',
                        filemode='a',
                        format='[%(asctime)s] [%(levelname)s] - %(message)s',
                        level=logging.INFO)


def analyze_data_from_database():
    while True:
        result = db_connector.get_all_unprocessed_body()
        for row in result:
            logging.debug("Received data by id %d: %s", row.id, row.body)
            row.mood = analyzer.process_sentiment_intensity_analysis(row.body)
            logging.debug("Definition of sentiment: %s", row.mood)
        db_session.commit()
        logging.info("Data processing is completed")
        time.sleep(60)


if __name__ == "__main__":
    args = init_argparser()
    init_logger(args.log_path)
    analyze_data_from_database()
