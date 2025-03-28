from . import *
from custom_components.localtuya.core.ha_entities import (
    gen_localtuya_entities,
    DATA_PLATFORMS,
)
from custom_components.localtuya.const import PLATFORMS


COVER_DEVICE_DATA = {
    "device_config": {
        "friendly_name": "Cover",
        "dps_strings": [
            "1 ( code: control , value: open )",
            "2 ( code: percent_control , value: 100 )",
            "3 ( code: percent_state , value: 100 )",
            "5 ( code: control_back_mode , value: forward )",
            "7 ( code: work_state , value: opening )",
            "11 ( code: situation_set , value: fully_open )",
            "12 ( code: fault , value: 0 )",
            "101 ( code: remote_register , value: False, cloud pull )",
            "102 ( code: reset_limit , value: False, cloud pull )",
            "103 ( code: up_confirm , value: True )",
            "104 ( code: middle_confirm , value: False )",
            "105 ( code: down_confirm , value: True )",
            "106 ( code: motor_mode , value: contiuation )",
        ],
    },
    "device_cloud_info": {
        "active_time": 1660859328,
        "biz_type": 18,
        "category": "cl",
        "create_time": 1660859328,
        "icon": "smart/icon/ay1535532217868NsRD0/d303688e83885c9920b0b2dcf3872aa3.png",
        "id": "bfa2f86e3068440a449dhd",
        "ip": "2...1",
        "lat": "",
        "local_key": "999...420",
        "lon": "",
        "model": "",
        "name": "Blind",
        "online": True,
        "owner_id": "13377642",
        "product_id": "jzmy5ut0vishwscm",
        "product_name": "zemismart curtain motor",
        "status": [
            {"code": "control", "value": "open"},
            {"code": "percent_control", "value": 0},
            {"code": "percent_state", "value": 0},
            {"code": "control_back_mode", "value": "forward"},
            {"code": "work_state", "value": "opening"},
            {"code": "situation_set", "value": "fully_open"},
            {"code": "fault", "value": 0},
        ],
        "sub": False,
        "time_zone": "+03:00",
        "uid": "eu1...Hyb",
        "update_time": 1737849634,
        "uuid": "d3a81500860ab39c",
        "dps_data": {
            "1": {
                "code": "control",
                "custom_name": "",
                "dp_id": 1,
                "time": 1737581443559,
                "type": "Enum",
                "value": "open",
                "values": '{"type": "enum", "range": ["open", "stop", "close", "continue"]}',
                "id": 1,
                "accessMode": "rw",
            },
            "2": {
                "code": "percent_control",
                "custom_name": "",
                "dp_id": 2,
                "time": 1738097484455,
                "type": "Integer",
                "value": 0,
                "values": '{"type": "value", "max": 100, "min": 0, "scale": 0, "step": 1, "unit": "%"}',
                "id": 2,
                "accessMode": "rw",
            },
            "3": {
                "code": "percent_state",
                "custom_name": "",
                "dp_id": 3,
                "time": 1738097508589,
                "type": "value",
                "value": 0,
                "id": 3,
                "accessMode": "ro",
                "values": '{"type": "value", "max": 100, "min": 0, "scale": 0, "step": 1, "unit": "%"}',
            },
            "5": {
                "code": "control_back_mode",
                "custom_name": "",
                "dp_id": 5,
                "time": 1734388862581,
                "type": "Enum",
                "value": "forward",
                "values": '{"type": "enum", "range": ["forward", "back"]}',
                "id": 5,
                "accessMode": "rw",
            },
            "7": {
                "code": "work_state",
                "custom_name": "",
                "dp_id": 7,
                "time": 1735420780853,
                "type": "enum",
                "value": "opening",
                "id": 7,
                "accessMode": "ro",
                "values": '{"type": "enum", "range": ["opening", "closing"]}',
            },
            "11": {
                "code": "situation_set",
                "custom_name": "",
                "dp_id": 11,
                "time": 1734388860575,
                "type": "enum",
                "value": "fully_open",
                "id": 11,
                "accessMode": "ro",
                "values": '{"type": "enum", "range": ["fully_open", "fully_close"]}',
            },
            "12": {
                "code": "fault",
                "custom_name": "",
                "dp_id": 12,
                "time": 1734388860586,
                "type": "bitmap",
                "value": 0,
                "id": 12,
                "accessMode": "ro",
                "values": '{"type": "bitmap", "label": ["motor_fault"], "maxlen": 1}',
            },
            "101": {
                "code": "remote_register",
                "custom_name": "",
                "dp_id": 101,
                "time": 1660859328099,
                "type": "bool",
                "value": False,
                "id": 101,
                "accessMode": "rw",
                "values": '{"type": "bool"}',
            },
            "102": {
                "code": "reset_limit",
                "custom_name": "",
                "dp_id": 102,
                "time": 1660859328099,
                "type": "bool",
                "value": False,
                "id": 102,
                "accessMode": "rw",
                "values": '{"type": "bool"}',
            },
            "103": {
                "code": "up_confirm",
                "custom_name": "",
                "dp_id": 103,
                "time": 1734388860596,
                "type": "bool",
                "value": True,
                "id": 103,
                "accessMode": "rw",
                "values": '{"type": "bool"}',
            },
            "104": {
                "code": "middle_confirm",
                "custom_name": "",
                "dp_id": 104,
                "time": 1734388860605,
                "type": "bool",
                "value": False,
                "id": 104,
                "accessMode": "rw",
                "values": '{"type": "bool"}',
            },
            "105": {
                "code": "down_confirm",
                "custom_name": "",
                "dp_id": 105,
                "time": 1734388860616,
                "type": "bool",
                "value": True,
                "id": 105,
                "accessMode": "rw",
                "values": '{"type": "bool"}',
            },
            "106": {
                "code": "motor_mode",
                "custom_name": "",
                "dp_id": 106,
                "time": 1736952575226,
                "type": "enum",
                "value": "contiuation",
                "id": 106,
                "accessMode": "rw",
                "values": '{"type": "enum", "range": ["contiuation", "point"]}',
            },
        },
    },
}


async def test_auto_configure():

    for k in PLATFORMS.values():
        assert k in DATA_PLATFORMS

    category = COVER_DEVICE_DATA["device_cloud_info"]["category"]
    entities = gen_localtuya_entities(COVER_DEVICE_DATA["device_config"], category)
    assert len(entities) > 4
