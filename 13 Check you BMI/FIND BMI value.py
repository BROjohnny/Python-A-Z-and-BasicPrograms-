def getbmi():
    height = input("Please input your height in centimeter :")
    weight = input("please input your weight in Kilogram :")
    bmi_value = int(weight) / (int(height) / 100) ** 2
    print("your BMI value is {}".format(round(bmi_value , 2)))
    if bmi_value < 18.5:
        print("you should improve your serail plan to better than now")
    elif bmi_value >= 18.5 and bmi_value <= 24:
        print("GREAT JOB! keep your body like this,you are helthy")
    else:
        print("you are in danger ,Please control your foods!!!!")
getbmi()