from typing import Literal, overload
import traceback

__OKBLUE = '\033[94m'
__OKCYAN = '\033[96m'
__OKGREEN = '\033[92m'
__WARNING = '\033[93m'
__ERROR = '\033[91m'
__ENDC = '\033[0m'

def __log(level: Literal["debug"] | Literal["info"] | Literal["warn"] | Literal["error"], message: str):
    color = ""
    if level == "debug": color = __OKBLUE
    if level == "info": color = __OKGREEN
    if level == "warn": color = __WARNING
    if level == "error": color = __ERROR

    print(f"{color}[{level.upper()}]{__ENDC} {message}")

@overload
def debug(message: str) -> None: ...

@overload
def debug(message: BaseException) -> None: ...

def debug(message: str | BaseException) -> None:
    if isinstance(message, str):
        __log("debug", message)
        return

    __log("debug", "\n".join(traceback.format_exception(message)))

@overload
def info(message: str) -> None: ...

@overload
def info(message: BaseException) -> None: ...

def info(message: str | BaseException) -> None:
    if isinstance(message, str):
        __log("info", message)
        return

    __log("info", "\n".join(traceback.format_exception(message)))

@overload
def warn(message: str) -> None: ...

@overload
def warn(message: BaseException) -> None: ...

def warn(message: str | BaseException) -> None:
    if isinstance(message, str):
        __log("warn", message)
        return

    __log("warn", "\n".join(traceback.format_exception(message)))

@overload
def error(message: str) -> None: ...

@overload
def error(message: BaseException) -> None: ...

def error(message: str | BaseException) -> None:
    if isinstance(message, str):
        __log("error", message)
        return

    __log("error", "\n".join(traceback.format_exception(message)))
