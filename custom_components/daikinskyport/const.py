import logging

_LOGGER = logging.getLogger(__package__)

DOMAIN = "daikinskyport"

from homeassistant.components.weather import (
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_HAIL,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
    ATTR_CONDITION_WINDY,
)

DAIKIN_WEATHER_SYMBOL_TO_HASS = {
    0: ATTR_CONDITION_SUNNY,
    1: ATTR_CONDITION_PARTLYCLOUDY,
    2: ATTR_CONDITION_PARTLYCLOUDY,
    3: ATTR_CONDITION_CLOUDY,
    4: ATTR_CONDITION_CLOUDY,
    5: ATTR_CONDITION_CLOUDY,
    6: ATTR_CONDITION_RAINY,
    7: ATTR_CONDITION_SNOWY_RAINY,
    8: ATTR_CONDITION_POURING,
    9: ATTR_CONDITION_HAIL,
    10: ATTR_CONDITION_SNOWY,
    11: ATTR_CONDITION_SNOWY,
    12: ATTR_CONDITION_SNOWY_RAINY,
    13: "snowy-heavy",
    14: ATTR_CONDITION_HAIL,
    "tstorms": ATTR_CONDITION_LIGHTNING_RAINY,
    16: ATTR_CONDITION_WINDY,
    17: "tornado",
    18: ATTR_CONDITION_FOG,
    19: "hazy",
    20: "hazy",
    21: "hazy",
    -2: None,
}

# The multiplier applied by the API to percentage values.
DAIKIN_PERCENT_MULTIPLIER = 2

