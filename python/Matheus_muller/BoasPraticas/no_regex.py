import re

PATTERN = r"^M"

"""if re.match(PATTERN, "Tonho"):
    print("tonho")
else:
    print("no match")"""

if "Tonho".startswith("T"):
    print("match")
else:
    print("no match")