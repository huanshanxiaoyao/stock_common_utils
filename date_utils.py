from trade_days import TradeDays

def get_trading_days(start_date, end_date):
    """
    获取指定日期范围内的交易日列表
    
    :param start_date: 开始日期，格式为"20240101"
    :param end_date: 结束日期，格式为"20240101"
    :return: 按时间顺序排列的交易日列表
    """
    # 确保输入格式正确
    if not (isinstance(start_date, str) and isinstance(end_date, str)):
        raise TypeError("日期必须是字符串格式")
    
    if len(start_date) != 8 or len(end_date) != 8:
        raise ValueError("日期格式必须为'YYYYMMDD'")
    
    # 获取在日期范围内的交易日
    trading_days = []
    for day in TradeDays:
        if start_date <= day <= end_date:
            trading_days.append(day)
    
    return trading_days

def get_last_trading_day(end_date, n=1):
    """
    获取指定日期前n个交易日的日期
    
    :param end_date: 结束日期，格式为"20240101"
    :param n: 向前推n个交易日
    :return: 前n个交易日的日期，格式为"20240101"
    """
    # 确保输入格式正确
    if not isinstance(end_date, str):
        raise TypeError("日期必须是字符串格式")
    
    if len(end_date) != 8:
        raise ValueError("日期格式必须为'YYYYMMDD'")
    
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n必须是正整数")
    
    # 获取所有交易日列表
    trading_days = list(TradeDays)
    
    # 找到结束日期在交易日列表中的位置
    end_index = -1
    for i, day in enumerate(trading_days):
        if day == end_date:
            end_index = i
            break
        elif day > end_date:
            end_index = i - 1
            break
    
    # 如果结束日期大于最后一个交易日，则使用最后一个交易日的索引
    if end_index == -1 and trading_days and end_date > trading_days[-1]:
        end_index = len(trading_days) - 1
    
    # 检查是否找到有效的结束日期索引
    if end_index == -1:
        raise ValueError(f"无法确定日期 {end_date} 的交易日位置")
    
    # 检查是否有足够的交易日
    if end_index < n - 1:
        raise ValueError(f"在 {end_date} 之前没有足够的交易日")
    
    # 返回前n个交易日
    return trading_days[end_index - n]
