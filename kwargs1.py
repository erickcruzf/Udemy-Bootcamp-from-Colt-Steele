def calculate(**kwargs):
    """Uma funcao que recebe uma lista de KeyWord argumentos, make_float = True ou False, operation = add ou subtract ou divide ou multiply.
    first,second = números e message = string. Retorna a mensagem com o resultado da operação."""
    if kwargs.get("operation", "add") == "add": third = kwargs.get("first", 0) + kwargs.get("second", 0)
    elif kwargs.get("operation", "subtract") == "subtract": third = kwargs.get("first", 0) - kwargs.get("second", 0)
    elif kwargs.get("operation", "divide") == "divide": third = kwargs.get("first", 0) / kwargs.get("second", 1)
    else: third = kwargs.get("first", 0) * kwargs.get("second", 0)
    if kwargs.get("make_float", False) and "message" in kwargs: return "{} {}".format(kwargs["message"], third)
    return "{} {}".format(kwargs["message"], int(third)) if "message" in kwargs else "The result is {}".format(third)
