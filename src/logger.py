
from __future__ import annotations
from typing import Optional, Union
import logging
import datetime

#ref: https://www.nomuramath.com/kv8wr0mp/
#ref: https://kaworu.jpn.org/kaworu/2018-05-19-1.php

def _RGB(r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m"

def _BG_RGB(r: int, g: int, b: int) -> str:
    return f"\033[48;2;{r};{g};{b}m"

class Colors:
    BLACK     = '\033[30m'
    RED       = '\033[31m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    BLUE      = '\033[34m'
    MAGENTA   = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
    BG_BLACK       = '\033[40m'#(背景)黒
    BG_RED         = '\033[41m'#(背景)赤
    BG_GREEN       = '\033[42m'#(背景)緑
    BG_YELLOW      = '\033[43m'#(背景)黄
    BG_BLUE        = '\033[44m'#(背景)青
    BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
    BG_CYAN        = '\033[46m'#(背景)シアン
    BG_WHITE       = '\033[47m'#(背景)白
    BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す
    
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE   = '\033[07m'
    END       = '\033[0m'
    
    ORANGE    = _RGB(255, 165, 0)


class MyStreamFormatter(logging.Formatter):
    """ターミナルへの出力をフォーマットするクラス。
    デフォルトのものと異なり、DEBUGなどのレベルに応じてそのレベルの文字に色付けを行う。
    """
    def __init__(self, fmt: Optional[str] = None, datefmt: Optional[str] = None, style: logging._FormatStyle = "%") -> None:
        if fmt is not None:
            fmt = fmt.replace("%(name)s", Colors.CYAN + "%(name)s" + Colors.END)
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)
        
    def format(self, record: logging.LogRecord) -> str:
        fmt = self._style._fmt
        rep = {
            "DEBUG": Colors.ORANGE,
            "INFO": Colors.GREEN,
            "WARNING": Colors.YELLOW,
            "ERROR": Colors.RED,
            "CRITICAL": Colors.BOLD + Colors.RED
        }[record.levelname]+ "%(levelname)s" + Colors.END
        
        fmt = fmt.replace("%(levelname)s", rep)
        
        self._style._fmt = fmt
        return super().format(record)

class Logger(logging.Logger):
    """ロギング用クラス
    """
    def __init__(self, name: str, level: Union[str, int] = logging.DEBUG, log_file: Optional[str] = None) -> None:
        super().__init__(name)
        
        format_string: str = f'[%(name)s] [%(levelname)s] %(message)s'
        
        sh = logging.StreamHandler()
        formatter = MyStreamFormatter(format_string)
        sh.setFormatter(formatter)
        self.addHandler(sh)
        
        if log_file:
            fh = logging.FileHandler((log_file.replace("${name}", name)))
            fh.setFormatter(logging.Formatter(format_string))
            fh.setLevel(logging.DEBUG)
            self.addHandler(fh)

        self.setLevel(level)
    
    def timestamp(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        self.debug(f"timestamp: {now}")
