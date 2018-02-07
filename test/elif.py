height = 1.75
weight = 80.5

bmi = weight/(height*height)


if bmi < 18.5:
    print("ming qing")
elif bmi >= 18.5 and bmi <= 25:
    print("ming normal")
elif bmi > 25 and bmi <=28:
    print("ming heave")
elif bmi > 28 and bmi <= 32:
    print("ming too heave")
else:
    print("ming too too heave")
