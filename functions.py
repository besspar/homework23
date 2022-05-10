def process_query(f, cmd, value):
    if cmd == "filter":
        result = filter(lambda v, txt=value: txt in v, f)
    if cmd == "limit":
        value = int(value)
        result = list(f)[:value]
    if cmd == "map":
        result = map(lambda v, idx=int(value): v.split(" ")[idx], f)
    if cmd == "unique":
        result = set(f)
    if cmd == 'sort':
        if value == 'desc':
            reverse = True
        else:
            reverse = False
        result = sorted(f, reverse=reverse)
    return result
