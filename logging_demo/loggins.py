import logging

def main()->None:
    
    logging.basicConfig(
        filename="basic.log",
        level = logging.DEBUG,
        format ="%(asctime)s %(levelname)s %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
    )
   

    logging.debug("this is a debug message")
    logging.info("this is info message")
    logging.warning("this is warning message")
    logging.error("this is error message")
    logging.critical("this is a critical message")

if __name__=="__main__":
        main()