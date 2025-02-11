def divide(a, b):
    """
    执行两个数字的除法运算
    
    参数:
        a (float): 被除数
        b (float): 除数
    
    返回:
        float: 除法运算的结果
        
    异常:
        ZeroDivisionError: 当除数为0时抛出
        TypeError: 当输入参数不是数字类型时抛出
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("输入必须是数字类型")
        
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
        
    return a / b 