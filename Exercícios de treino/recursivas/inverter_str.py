def inverter_str(str):
    if len(str) == 0:
        return ""
    return str[-1] + inverter_str(str[:-1])

print(inverter_str("parara"))