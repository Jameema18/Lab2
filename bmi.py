height = float(input('Enter height: '))
weight = float(input('Enter weight: '))

def BMI(height, weight) :
    bmi = weight/(height**2) * 703

    if (bmi < 18.5) :
        return 'underweight', bmi

    elif (bmi >= 18.5 and bmi <= 25) :
        return 'healthy', bmi

    elif (bmi > 25) :
        return 'overweight', bmi

quote, bmi = BMI(height, weight)
print('Your BMI is {} and you are {}' .format(bmi,quote))
