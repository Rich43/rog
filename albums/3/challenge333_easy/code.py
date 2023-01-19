import re


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


# read strings into a list
lst = []
with open('333_challenge.txt') as f:
    for line in f:
        line = line.strip()
        lst.append(line)

# extract message id's into a set
message_ids = set()
for msg in lst:
    msg_id = re.findall('^\d+', msg)
    message_ids.add(msg_id[0])

# message id's into a list for indexing
message_id_list = list(message_ids)

# group messages together by id's
for x in range(0, len(message_id_list)):
    first_list = []
    for strng in lst:
        if  strng.startswith(message_id_list[x]):
            first_list.append(strng)

    first_list = natural_sort(first_list)

    for item in first_list:
        print(item)