import logging
import sys
import os # Thêm thư viện os

def setup_logger():
    # Tự động tạo thư mục logs nếu chưa có
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("FinanceAgent")
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Log to file
    file_handler = logging.FileHandler(os.path.join(log_dir, "agent_activity.log"), encoding='utf-8')
    file_handler.setFormatter(formatter)

    # Log to console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

agent_logger = setup_logger()