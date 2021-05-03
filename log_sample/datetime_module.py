import datetime
import logging
 
# ロガーを取得する
logger = logging.getLogger(__name__)
 
def get_datetime_now():
    """プログラム実行時点での日時を計算する。
 
    Returns:
        datetime_now (datetime.datetime): プログラム実行時点での日時
    """
 
    # ログを出力する方法(実際にはログを出力したい場所で記述する)
    logger.debug('DEBUGレベルのメッセージです')
    logger.info('INFOレベルのメッセージです')
    logger.warning('WARNINGレベルのメッセージです')
    logger.error('ERRORレベルのメッセージです')
    logger.critical('CRITICALレベルのメッセージです')
 
    datetime_now = datetime.datetime.now()
 
    return datetime_now
 
def get_monday(time):
    """指定する日時が含まれる週の月曜日を計算する。
 
    Args:
        time (datetime.datetime): 指定する日時
 
    Returns:
        result (datetime.date): 指定する日時が含まれる週の月曜日
    """
 
    # ログを出力する方法(実際にはログを出力したい場所で記述する)
    logger.debug('DEBUGレベルのメッセージです')
    logger.info('INFOレベルのメッセージです')
    logger.warning('WARNINGレベルのメッセージです')
    logger.error('ERRORレベルのメッセージです')
    logger.critical('CRITICALレベルのメッセージです')
 
    time_date = time.date()
    weekday = time_date.weekday()
    delta = datetime.timedelta(days=weekday)
    result = time_date - delta
 
    return result