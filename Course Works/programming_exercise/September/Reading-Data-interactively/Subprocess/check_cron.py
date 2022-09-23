import sys
import re

logfile = sys.argv[1] # to get the second argument in CLI
usernames = {}

with open(logfile) as f:
    for line in f:
        # Check whether "CRON" letter is in logfile
        if "CRON" not in line:
            continue
        
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)

        # check whether result value is None, if it's None then Continue
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1 # Increment The Name Value, it the key has same value

print(usernames)
