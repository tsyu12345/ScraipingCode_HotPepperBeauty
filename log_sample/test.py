# loggingと自作のdatetime_moduleをインポート
import logging
import datetime_module

LOG_LEVEL_FILE = 'DEBUG'
LOG_LEVEL_CONSOLE = 'INFO'

# フォーマットを指定 (https://docs.python.jp/3/library/logging.html#logrecord-attributes)
_detail_formatting = '%(asctime)s %(levelname)-8s [%(module)s#%(funcName)s %(lineno)d] %(message)s'


"""
LOG_LEVEL_FILEレベル以上のログをファイルに出力する設定
"""
# datetime_moduleモジュールを呼び出す側(test.py)で出力形式などの基本設定をする
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL_FILE), # LOG_LEVEL_FILE = 'DEBUG' なら logging.DEBUGを指定していることになる
    format=_detail_formatting,
    filename='./logs/sample.log'
)


"""
LOG_LEVEL_CONSOLEレベル以上のログをコンソール(std.stderr)に出力する設定
"""
# ログをコンソールに送るハンドラconsoleを作成
console = logging.StreamHandler()
console.setLevel(getattr(logging, LOG_LEVEL_CONSOLE)) # LOG_LEVEL_CONSOLE = 'INFO' なら logging.INFOを指定していることになる
console_formatter = logging.Formatter(_detail_formatting)
console.setFormatter(console_formatter)


"""
consoleハンドラをロガーに追加する
"""
# test用のロガーを取得し、consoleハンドラを追加する
logger = logging.getLogger(__name__)
logger.addHandler(console)
# datetime_module用のロガーを取得し、consoleハンドラを追加する。他に追加したいモジュールがあれば同じ形式で追加する
logging.getLogger("datetime_module").addHandler(console)


if __name__ == '__main__':

    datetime_now = datetime_module.get_datetime_now()

    # ログを出力する方法(実際にはログを出力したい場所で記述する)
    logger.debug('DEBUGレベルのメッセージです')
    logger.info('INFOレベルのメッセージです')
    logger.warning('WARNINGレベルのメッセージです')
    logger.error('ERRORレベルのメッセージです')
    logger.critical('CRITICALレベルのメッセージです')

    monday_of_current_week = datetime_module.get_monday(datetime_now)