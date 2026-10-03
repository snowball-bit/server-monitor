from server_monitor.system import get_system_status
from monitor import get_status_label
from monitor import positive_int
from monitor import parse_args

def test_sys_status():

	status = get_system_status()

	assert isinstance(status, dict)
	assert "cpu" in status
	assert "memory" in status
	assert "disk" in status
	assert "hostname" in status

	#check type
	assert isinstance(status["cpu"], (int, float))
	assert isinstance(status["memory"], (int, float))
	assert isinstance(status["disk"], (int, float))
	assert isinstance(status["hostname"], str)
	
	#

	assert 0 <= status["cpu"] <= 100
	assert 0 <= status["memory"] <= 100
	assert 0 <= status["disk"] <= 100


def test_status_label():
    assert get_status_label(50, 80) == "[OK]"
    assert get_status_label(80, 80) == "[HIGH]"
    assert get_status_label(90, 80) == "[HIGH]"

def test_positive_int():
    assert positive_int("5") == 5
    assert positive_int("1") == 1


def test_positive_int_invalid():
    import pytest

    with pytest.raises(ValueError):
        positive_int("0")

    with pytest.raises(ValueError):
        positive_int("-1")

def test_parse_args_once(monkeypatch):
    monkeypatch.setattr("sys.argv", ["monitor.py", "--once"])

    args = parse_args()

    assert args.once is True

def test_parse_args_interval(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["monitor.py", "--interval", "2"]
    )

    args = parse_args()

    assert args.interval == 2
