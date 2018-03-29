import bmi_package

test = bmi_package.bmi.Bmi()
test.get(89, 185)

print("Your BMI is: {0}".format(test.BMI))
print("Based on this, you are: {0}".format(test.category))
