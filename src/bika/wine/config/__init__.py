import logging
from zope.i18nmessageid import MessageFactory

PRODUCT_NAME = "bika.wine"
PROFILE_ID = "profile-{}:default".format(PRODUCT_NAME)
logger = logging.getLogger(PRODUCT_NAME)
_ = MessageFactory(PRODUCT_NAME)
