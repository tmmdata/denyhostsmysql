import re

#################################################################################
# REGULAR EXPRESSIONS ARE COOL.  Test Regex at (https://regex101.com/) #
#################################################################################

#DATE_FORMAT_REGEX = re.compile(r"""(?P<month>[A-z]{3,3})\s*(?P<day>\d+)""")

MYSQLD_FORMAT_REGEX = re.compile(r""".* (\[Note\]) (?P<message>.*)""")

#Access denied for user 'username'@'host' (using password: NO|YES)
FAILED_ENTRY_REGEX = re.compile(r"""[Aces\sdni\sforu]+'(?P<user>.*)['@]{3}(?P<host>.*)'[\s\(usingpaword:\sYESNO)]+""")

# these are reserved for future versions
FAILED_ENTRY_REGEX2 = None

# this should match the highest num failed_entry_regex + 1
FAILED_ENTRY_REGEX_NUM = 2

FAILED_ENTRY_REGEX_RANGE = list(range(1, FAILED_ENTRY_REGEX_NUM))
FAILED_ENTRY_REGEX_MAP = {}

# create a hash of the failed entry regex'es indexed from 1 .. FAILED_ENTRY_REGEX_NUM
for i in FAILED_ENTRY_REGEX_RANGE:
    if i == 1: extra = ""
    else: extra = "%i" % i
    rx = eval("FAILED_ENTRY_REGEX%s" % extra)
    FAILED_ENTRY_REGEX_MAP[i] = rx

TIME_SPEC_REGEX = re.compile(r"""(?P<units>\d*)\s*(?P<period>[smhdwy])?""")

ALLOWED_REGEX = re.compile(r"""(?P<first_3bits>\d{1,3}\.\d{1,3}\.\d{1,3}\.)((?P<fourth>\d{1,3})|(?P<ip_wildcard>\*)|\[(?P<ip_range>\d{1,3}\-\d{1,3})\])""")

PREFS_REGEX = re.compile(r"""(?P<name>.*?)\s*[:=]\s*(?P<value>.*)""")

FAILED_DOVECOT_ENTRY_REGEX = re.compile(r"""dovecot.*authentication failure.*ruser=(?P<user>\S+).*rhost=(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*""")
