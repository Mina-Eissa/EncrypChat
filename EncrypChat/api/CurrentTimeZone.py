from datetime import datetime
import pytz


def get_timenow():
    # Get the current UTC time
    current_utc_time = datetime.utcnow()

    # Convert UTC time to Cairo timezone
    cairo_timezone = pytz.timezone('Africa/Cairo')
    current_cairo_time = current_utc_time.astimezone(cairo_timezone)

    return current_cairo_time
