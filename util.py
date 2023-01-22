

def name_formatter(raw_name: str) -> str:
    result = raw_name
    if ', ' in raw_name:
        parts = raw_name.split(', ')
        result = parts[1] + " " + parts[0]
    result = result.lower().title()
    return result

