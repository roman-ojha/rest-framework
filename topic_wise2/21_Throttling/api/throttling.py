from rest_framework.throttling import UserRateThrottle


class RomanRateThrottle(UserRateThrottle):
    # here we will create a scope for this Throttle class which we can now use on 'settings.py' file
    scope = 'roman'
