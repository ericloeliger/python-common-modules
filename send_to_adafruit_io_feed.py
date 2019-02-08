# generic module to send data to Adafruit IO

from Adafruit_IO import *
from __main__ import *
logger = logging.getLogger('send_to_adafruit_io_feed.py')
handler = logging.FileHandler('%s%s' % (log_path_linux,  log_name))
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def sendToAdafruitIOFeed(clientUser, clientKey, feedDictionary):
    # setup to adafruit IO feed
    aio = Client(clientUser, clientKey)

    for x in feedDictionary:
        logger.info("Sending %s value %s to Adafruit feed %s" % (x,feedDictionary[x]['value'],feedDictionary[x]['feedID'] ))
        aio.send(feedDictionary[x]['feedID'],feedDictionary[x]['value'])
        logger.info("%s sent successfully" % x)



if __name__ == "__main__":
    import logging
    log_name = 'send_to_adafruit_io_feed.log'
    logger = logging.getLogger('send_to_adafruit_io_feed.py')
    handler = logging.FileHandler('send_to_adafruit_io_feed.log')
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # define feed dictionary
    feedDictionary = {}
    feedDictionary['testParameter'] = {}
    feedDictionary['testParameter']['feedID'] = 'testfeed'
    feedDictionary['testParameter']['value'] = 720

    ClientUser = ''
    ClientKey = ''
    sendToAdafruitIOFeed(ClientUser,ClientKey,feedDictionary)

    print("Adafruit feed dictionary: %s" % feedDictionary)