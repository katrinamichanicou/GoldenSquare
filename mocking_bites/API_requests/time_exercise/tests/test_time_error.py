from unittest.mock import Mock
from lib.time_error import TimeError

def test_time_error():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {
        "abbreviation":"GMT",
        "client_ip":"82.163.117.26",
        "datetime":"2024-02-08T09:51:44.141562+00:00",
        "day_of_week":4,
        "day_of_year":39,
        "dst": False,
        "dst_from": None,
        "dst_offset":0,
        "dst_until": None,
        "raw_offset":0,
        "timezone":"Europe/London",
        "unixtime":1707385904,
        "utc_datetime":"2024-02-08T09:51:44.141562+00:00",
        "utc_offset":"+00:00","week_number":6
    }
    # could just extract the part of the json needed
    # eg. response_mock.json.return_value = {"unixtime" : 1707385904}
    timer_mock = Mock()
    timer_mock.time.return_value = 1707386811.5


    time_error = TimeError(requester_mock, timer_mock)
    result = time_error.error()
    assert result == -907.5