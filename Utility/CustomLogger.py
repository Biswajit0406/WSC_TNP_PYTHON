import logging

class CustomLogger:
    @staticmethod
    def logger_message():
        logging.basicConfig(filename="C:/Users/KIIT/PycharmProjects/pythonProject6/Logger/wsc.log", format="%(asctime)s - %(levelname)s - %(message)s")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
