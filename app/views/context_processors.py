from app import app

import numpy as np
import datetime


@app.context_processor
def utility_processor():
    def get_interval(value, log_interval_width):
        if value:
            log_value = np.log10(value)
            log_low, log_high = log_value - log_interval_width, log_value + log_interval_width
            low, high = 10 ** log_low, 10 ** log_high
            return int(low), int(high)
        else:
            return "", ""

    def lowercase(s):
        if s:
            return s.lower()
        else:
            return ""

    def parse_number(number, n_decimals=0):
        if number:
            if n_decimals > 0:
                return f"{round(number, n_decimals):,}"
            elif n_decimals == 0:
                return f"{round(number):,}"
            else:
                return ""
        else:
            return ""

    def parse_seconds(number):
        if number:
            return str(datetime.timedelta(seconds=666))
        else:
            return ""

    def parse_date(date):
        return date.year, str(date.month).zfill(2), str(date.day).zfill(2)

    def get_screenshot_path(store_url):
        assert isinstance(store_url, str)
        return f"{app.config.get('STORE_SCREENSHOT_URI')}/{store_url}.png"

    return dict(get_interval=get_interval, lowercase=lowercase, parse_number=parse_number,
                parse_seconds=parse_seconds, parse_date=parse_date,
                get_screenshot_path=get_screenshot_path)