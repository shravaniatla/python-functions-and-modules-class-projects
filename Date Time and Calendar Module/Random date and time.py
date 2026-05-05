import random

import time

def random_date(startDate, endDate):

    print("Random date between", startDate, "and", endDate )

    ranGen = random.random()

    dateFormat = '%m %d %y'


    startTime = time.mktime(time.strptime(startDate, dateFormat))

    endTime = time.mktime(time.strptime(endDate, dateFormat))


    randomTime = startTime + ranGen * (endTime - startTime)

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))


    return randomDate

print("Random Date is:", random_date("1 1 20", "12 31 22"))