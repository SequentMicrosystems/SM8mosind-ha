FULL_NAME = "Eight MOSFETS"
LINK = "https://sequentmicrosystems.com/products/eight-mosfets-8-layer-stackable-card-for-raspberry-pi"

import lib8mosind
API = lib8mosind
DOMAIN = "SM8mosind"
NAME_PREFIX = "sm8m"
SM_MAP = {
    "switch": {
        "mos": {
                "chan_no": 8,
                "com": {
                    "get": "get",
                    "set": "set"
                },
        }
    },
    "number": {
        "pwm": {
                "chan_no": 8,
                "uom": "%",
                "min_value": 0.0,
                "max_value": 100.0,
                "step": 0.1,
                "com": {
                    "get": "get_pwm",
                    "set": "set_pwm"
                },
        },
    },
}
