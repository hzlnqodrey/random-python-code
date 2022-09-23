#!/usr/bin/env python3

import re

def rearrange_name(name):
        result = re.search(r"^([\w .]*), ([\w .]*)$", name)
        # add this block to basically check whether result is None or not
        if result is None:
            return name
        return "{} {}".format(result[2], result[1])

