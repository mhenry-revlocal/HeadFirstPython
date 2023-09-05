from statistics import mean

FN = "Darius-13-100m-Fly.txt"
FOLDER = "swimdata/"

swimmer, age, distance, stroke = FN.removesuffix(".txt").split('-')

with open(FOLDER + FN) as file:
    lines = file.readlines()
    times = lines[0].strip().split(",")
    converts = []
    for t in times:
        minutes, rest = t.split(":")
        seconds, hundredths = rest.split(".")
        convertedTime = (int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundredths)
        converts.append(convertedTime)

    average = mean(converts)
    mins_secs, hundredths = str(round(average / 100, 2)).split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes * 60
    average = str(minutes) + ":" + str(seconds) + "." + hundredths
    print(swimmer, age, distance, stroke)
    print(times)
    print(average)
    