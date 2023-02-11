__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    time = ''
    if seconds < 60:
        time += f'{seconds:02}s'
    elif 60 <= seconds < 3600:
        minutes = seconds // 60
        time += f'{minutes:02}m{seconds - minutes * 60:02}s'
    elif 3600 <= seconds < 86400:
        hours = seconds // 3600
        minutes = (seconds - hours * 3600) // 60
        time += f'{hours:02}h{minutes:02}m{seconds - hours * 3600 - minutes * 60:02}s'
    else:
        days = seconds // 86400
        hours = (seconds - days * 86400) // 3600
        minutes = (seconds - days * 86400 - hours * 3600) // 60
        time += f'{days:02}d{hours:02}h{minutes:02}m{seconds - days * 86400 - hours * 3600 - minutes * 60:02}s'
    return time






