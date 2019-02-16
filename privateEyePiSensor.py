# function to get readings from wifi temp & humidity sensor

from __main__ import *
import requests

def getWifiTempHumidityReadings(input_dict):
    logger = logging.getLogger('getWifiTempHumidityReadings')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # initialize output dict
    response_dict = {}

    for s in input_dict:
        logger.debug(s)
        logger.info("Current sensor name: %s" % s)
        logger.info("Current sensor config ID: %s" % input_dict[s]['config_id'])
        r = requests.get(input_dict[s]['url'])
        response = r.text
        logger.debug("Raw binary response: %s" % response.encode('utf-8'))
        response = response.replace('\r', '')
        list_data = response.split(",")
        if input_dict[s]['version'] == 1:
            sensor_type = list_data[0]
            temperature = list_data[1]
            humidity = list_data[2]
        elif input_dict[s]['version'] == 2:
            sensor_type = list_data[1]
            temperature = list_data[2]
            humidity = list_data[3]
        else:
            logger.error("Unsupported sensor version")
        logger.debug("Parameter 1 =%s" % sensor_type)
        logger.debug("Parameter 2 =%s" % temperature)
        logger.debug("Parameter 3 =%s" % humidity)

        # build response dict
        response_dict[s] = {}
        response_dict[s]['temperature'] = temperature
        response_dict[s]['humidity'] = humidity

        return response_dict


if __name__ == "__main__":
    import logging
    log_name = 'privateEyePiSensorTest.log'
    logger = logging.getLogger('privateEyePiSensorTest.py')
    handler = logging.FileHandler('privateEyePiSensorTest.log')
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.info("Main started")

    sensor_dict = {}
    #sensor_dict['sensor_qty'] = 1
    sensor_dict['ESP_1853FE'] = {}
    sensor_dict['ESP_1853FE']['config_id'] = 'sensor.1'
    sensor_dict['ESP_1853FE']['url'] = 'http://192.168.0.184/temp'
    sensor_dict['ESP_1853FE']['version'] = 2
    logger.debug(sensor_dict)
    
    x = getWifiTempHumidityReadings(sensor_dict)
    logger.debug(x)
    logger.info("Main finished")