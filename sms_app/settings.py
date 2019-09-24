import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# set the url since its required
STATIC_URL = 'static/'

ALLOWED_HOSTS = ["*"]

# use timezones
USE_TZ = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sms_app'
]

# define the database settings
if 'DJANGO_ADMIN_USERNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['DEFAULT_DB_NAME'],
            'USER': os.environ['DEFAULT_DB_USER'],
            'PASSWORD': os.environ['DEFAULT_DB_PASS'],
            'HOST': os.environ['DEFAULT_DB_HOST'],
            'PORT': os.environ['DEFAULT_DB_PORT'],
            'TIMEZONE': os.environ['TIMEZONE']
        },
    }
    SECRET_KEY = os.environ['SECRET_KEY']
    TIMEZONE = os.environ['TIMEZONE']

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'fao_sms',
            'USER': 'root',
            'PASSWORD': 'admin',
            'HOST': 'localhost',
            'PORT': '',
            'TIMEZONE': 'Africa/Nairobi'
        },
    }
    SECRET_KEY = '@%z0@a8i%_j7zdb9*4+tb)$!_na+91b--@52q^1b!#nq&0t@jn'
    TIMEZONE = 'Africa/Nairobi'

    SMS_GATEWAYS = {
        'default': 'at',            # the id of the gateway to use as a default. Select from the gateways listed below
        'gateways_priority': [],    # the priority of the listed gateways, if not defined, the gateways will be selected randomly

        'gateways': {
            'infobip': {},
            'at': {
                'KEY': 'c5fc6731409a3800c444c429b3e97252e3945e6f7d8ca3540843e3c0a0449331',
                'ENDPOINT': 'https://api.sandbox.africastalking.com/version1/messaging',
                # 'USERNAME': 'badili'
                'USERNAME': 'sandbox'
            },
            'nexmo': {}
        }
    }

# django middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/django')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'sms_app.urls'

# our custom settings

SMS_VALIDITY = 48   # the number of hours an SMS is valid since it was queued

# The default port to serve the application from
DEFAULT_PORT = 9016

AT_STATUS_CODES = {
    100: "Processed",
    101: "Sent",
    102: "Queued",
    401: "RiskHold",
    402: "InvalidSenderId",
    403: "InvalidPhoneNumber",
    404: "UnsupportedNumberType",
    405: "InsufficientBalance",
    406: "UserInBlacklist",
    407: "CouldNotRoute",
    500: "InternalServerError",
    501: "GatewayError",
    502: "RejectedByGateway"
}

AT_FAILURE_REASON = {
    'InsufficientCredit': "This occurs when the subscriber doesn’t have enough airtime for a premium subscription service/message",
    'InvalidLinkId': "This occurs when a message is sent with an invalid linkId for an onDemand service",
    'UserIsInactive': "This occurs when the subscriber is inactive or the account deactivated by the MSP (Mobile Service Provider).",
    'UserInBlackList': "This occurs if the user has been blacklisted not to receive messages from a paricular service (shortcode or keyword)",
    'UserAccountSuspended': "This occurs when the mobile subscriber has been suspended by the MSP.",
    'NotNetworkSubcriber': "This occurs when the message is passed to an MSP where the subscriber doesn’t belong.",
    'UserNotSubscribedToProduct': "This occurs when the message from a subscription product is sent to a phone number that has not subscribed to the product.",
    'UserDoesNotExist': "This occurs when the message is sent to a non-existent mobile number.",
    'DeliveryFailure': "This occurs when message delivery fails for any reason not listed above or where the MSP didn’t provide a delivery failure reason.",
}
