def calculate(**kwargs):
    operations_summary = {
    "add": kwargs.get("first", 0) + kwargs.get("second", 0), "subtract": kwargs.get("first", 0) - kwargs.get("second", 0),
    "divide": kwargs.get("first", 0) / kwargs.get("second", 1), "multiply": kwargs.get("first", 0) * kwargs.get("second", 0)
    }
    third = operations_summary[kwargs.get("operation")]
    if kwargs.get("make_float") and "message" in kwargs: return "{} {}".format(kwargs["message"], third)
    return "{} {}".format(kwargs["message"], int(third)) if "message" in kwargs else "The result is {}".format(third)

#example
#print(calculate(operation='divide', make_float = True, message= 'easy pz', first=5, second=2))
