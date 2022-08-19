from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('utilities-py').version
except DistributionNotFound:
    __version__ = '(local)'

del DistributionNotFound
del get_distribution
