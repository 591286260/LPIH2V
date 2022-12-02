with open('data/location_negative_sample.txt') as pid:
    NOLPI = pid.readlines()
TRAIN = []
TEST = []
for index, item in enumerate(NOLPI):
    if index < 3663:
        TRAIN.append(item)
    else:
        TEST.append(item)
with open('train/3663_location_negative_pair.txt', 'w') as pid:
    pid.writelines(TRAIN)
with open('test/915_location_negative_pair.txt', 'w') as pid:
    pid.writelines(TEST)