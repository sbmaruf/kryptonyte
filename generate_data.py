from __future__ import print_function
import os
import time
import datetime
import argparse
from kryptonyte.utils.logging import build_logger
from kryptonyte.utils.args import dataset_args, \
    add_md_help_argument
from kryptonyte.utils.asserts import AssertBase


def get_logger(arg):
    folder_name = arg.save_data
    if (folder_name == '' and arg.force_run)\
            or not os.path.isdir(folder_name):
        time_stamp = datetime.datetime.fromtimestamp(
            time.time()).strftime('%S-%M-%H-%m-%d-%Y')
        if folder_name == '':
            folder_name = 'pretrained-model'
        folder_name = os.path.join(folder_name, time_stamp)
    arg.save_data = folder_name
    os.makedirs(arg.save_data, exist_ok=True)
    arg.logger_address = os.path.join(arg.save_data, 'log')
    logger = build_logger(arg.logger_address)
    logger.info("logger created at {}".format(arg.logger_address))
    return logger


def main(arg):
    logger = get_logger(arg)





if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='generate_data.py : Generate the data for the model',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    add_md_help_argument(parser)
    dataset_args(parser)
    arg = parser.parse_args()
    main(arg)
