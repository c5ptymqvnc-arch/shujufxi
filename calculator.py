"""A simple calculator module supporting basic arithmetic operations."""

from typing import Callable, Dict


def calculator(operation: str, left: float, right: float) -> float:
    """
    实现一个简单的计算器，支持加、减、乘、除操作。

    Parameters
    ----------
    operation: str
        运算符号或名称，例如 "+"、"-"、"*"、"/"、"add"、"subtract" 等。
    left: float
        左操作数。
    right: float
        右操作数。

    Returns
    -------
    float
        运算结果。

    Raises
    ------
    ValueError
        当传入不支持的运算符时抛出。
    ZeroDivisionError
        当尝试进行除以零操作时抛出。
    """

    operations: Dict[str, Callable[[float, float], float]] = {
        "+": lambda x, y: x + y,
        "add": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "subtract": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "multiply": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "÷": lambda x, y: x / y,
        "divide": lambda x, y: x / y,
    }

    operation_key = operation.lower()
    if operation_key not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    if operation_key in {"/", "÷", "divide"} and right == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return operations[operation_key](left, right)


__all__ = ["calculator"]
