from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta, timezone as dt_timezone
from .models import USDCurrentRate
from .utils import fetch_current_usd_rate
import time

last_request_time = None
UTC_PLUS_3 = dt_timezone(timedelta(hours=3))


def get_current_usd(request):
    global last_request_time
    if last_request_time:
        elapsed_time = (timezone.now() - last_request_time).total_seconds()
        if elapsed_time < 10:
            time.sleep(10 - elapsed_time)

    rate, current_time = fetch_current_usd_rate()
    if rate is not None:
        USDCurrentRate.objects.create(rate=rate, timestamp=current_time)
        last_request_time = timezone.now()

    last_rates = USDCurrentRate.objects.order_by("-timestamp")[:10]
    response_data = {
        "last_10_rates": [
            {"rate": rate.rate, "time": rate.timestamp.astimezone(UTC_PLUS_3).strftime("%Y-%m-%d %H:%M:%S UTC%z")
             } for rate in last_rates
        ],
    }
    return JsonResponse(response_data)
