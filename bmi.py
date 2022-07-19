print("Python BMI Calculator")

print("Here is the JSON Data listed below\n")

d1={"Gender": "Male","HeightCm": 171,"WeightKg":96}
print("The data in the first dictionary is:",d1)

d2={"Gender": "Male","HeightCm":161,"WeightKg": 85}
print("The data in the second dictionary is:",d2)

d3={"Gender": "Male","HeightCm" : 180,"WeightinKg":77}
print("The data in third dictionary is:",d3)

d4={"Gender": "Female","HeightCm": 166,"WeightKg":62}
print("The data in the fourth dictionary is:",d4)

d5={"Gender": "Female","HeightCm":150,"WeightKg":70}
print("The data in the fifth dictionary is:",d5)


d6={"Gender": "Female","HeightCm":167,"WeightinKg":82}
print("The data in the sixth dictionary is:",d6)


opt=int(input('''

Kindly Choose from the following options
1) Calculate the BMI(Body Mass Index) of first dictionary
2) Calculate the BMI(Body Mass Index) of second dictionary
3) Calcualte the BMI(Body Mass Index) of third dictionary
4) Calculate the BMI(Body Mass Index) of fourth dictionary
5) Calculate the BMI(Body Mass Index) of fifth dictionary
6) Calculate the BMI(Body Mass Index) of sixth dictionary
7) BMI Category and Health Risk

Press only one option at a time!

'''))

match(opt):


    case 1:
        print("Calculation of BMI Index!")

        print("The first dictionary is:",d1)

        for i in d1.values():
            print(i)
        
        def fmi(mass,height):
            print("Functions!")
            print("The body mass is:",mass)
            print("The height is:",height)
            dheight=height/100
            finalheight=dheight*dheight
            print("Height in meterers is:",finalheight)
            bmi=mass/finalheight
            print("The First Body Mass Index is:",bmi)

            if bmi<=18.4:
                print("You are underweight and have malnutrition risk")
            elif bmi>=18.5 and bmi<=24.9:
                print("You are normal weight and have low risk!")
            elif bmi>=25 and bmi<=29.9:
                print("You are overweight and have enhanced heart rate risk!")
            elif bmi>=30 and bmi<=34.9:
                print("You are Moderately obese and have medium health risk!")
            elif bmi>=35 and bmi<=39.9:
                print("You are severly obese and have high health risk!")
            else:
                 print("You are very severly obese and have high health risk!")
                

            
        fmi(96,171)

    case 2:


        print("Calculation of BMI Index!")

        print("The second dictionary is:",d2)

        for i in d2.values():
            print(i)
        
        def fmi(mass,height):
            print("The body mass is:",mass)
            print("The height is:",height)
            dheight=height/100
            finalheight=dheight*dheight
            print("Height in meterers is:",finalheight)
            bmi2=mass/finalheight
            print("The Second Body Mass Index is:",bmi2)
            if bmi2<=18.4:
                print("You are underweight and have malnutrition risk")
            elif bmi2>=18.5 and bmi2<=24.9:
                print("You are normal weight and have low risk!")
            elif bmi2>=25 and bmi2<=29.9:
                print("You are overweight and have enhanced heart rate risk!")
            elif bmi2>=30 and bmi2<=34.9:
                print("You are Moderately obese and have medium health risk!")
            elif bmi2>=35 and bmi2<=39.9:
                print("You are severly obese and have high health risk!")
            else:
                 print("You are very severly obese and have high health risk!")
                


        fmi(85,161)
    case 3:

        print("Calculation of BMI Index!")

        print("The third dictionary is:",d3)

        for i in d3.values():
            print(i)
        def fmi(mass,height):
            print("The body mass is:",mass)
            print("The height is:",height)
            dheight=height/100
            print("Height in meters is:",dheight)
            finalheight=dheight*dheight
            print("Height in meterers is:",finalheight)
            bmi3=mass/finalheight
            print("The Third Body Mass Index is:",bmi3)
            if bmi3<=18.4:
                print("You are underweight and have malnutrition risk")
            elif bmi3>=18.5 and bmi3<=24.9:
                print("You are normal weight and have low risk!")
            elif bmi3>=25 and bmi3<=29.9:
                print("You are overweight and have enhanced heart rate risk!")
            elif bmi3>=30 and bmi3<=34.9:
                print("You are Moderately obese and have medium health risk!")
            elif bmi3>=35 and bmi3<=39.9:
                print("You are severly obese and have high health risk!")
            else:
                 print("You are very severly obese and have high health risk!")
            

        fmi(77,180)
  
        
        
    case 4:

        print("Calculation of BMI Index!")

        print("The fourth dictionary is:",d4)

        for i in d4.values():
            print(i)
        
        def fmi(mass,height):
            print("Functions!")
            print("The body mass is:",mass)
            print("The height is:",height)
            dheight=height/100
            print("Height in meters is:",dheight)
            bmi4=mass/dheight*dheight
            print("The fourth Body Mass Index is:",bmi4)

            if bmi4<=18.4:
                print("You are underweight and have malnutrition risk")
            elif bmi4>=18.5 and bmi4<=24.9:
                print("You are normal weight and have low risk!")
            elif bmi4>=25 and bmi4<=29.9:
                print("You are overweight and have enhanced heart rate risk!")
            elif bmi4>=30 and bmi4<=34.9:
                print("You are Moderately obese and have medium health risk!")
            elif bmi4>=35 and bmi4<=39.9:
                print("You are severly obese and have high health risk!")
            else:
                 print("You are very severly obese and have high health risk!")
            

            
        fmi(62,166)

    case 5:

        print("Calculation of BMI Index!")

        print("The fifth dictionary is:",d5)

        for i in d5.values():
            print(i)
        
        def fmi(mass,height):
            print("Functions!")
            print("The body mass is:",mass)
            print("The height is:",height)
            dheight=height/100
            print("Height in meters is:",dheight)
            bmi5=mass/dheight*dheight
            print("The fifth Body Mass Index is:",bmi5)
            if bmi5<=18.4:
                print("You are underweight and have malnutrition risk")
            elif bmi5>=18.5 and bmi5<=24.9:
                print("You are normal weight and have low risk!")
            elif bmi5>=25 and bmi5<=29.9:
                print("You are overweight and have enhanced heart rate risk!")
            elif bmi5>=30 and bmi5<=34.9:
                print("You are Moderately obese and have medium health risk!")
            elif bmi5>=35 and bmi5<=39.9:
                print("You are severly obese and have high health risk!")
            else:
                 print("You are very severly obese and have high health risk!")
            

            
        fmi(70,150)

    case 6:

        print("Calculation of BMI Index!")

        print("The fifth dictionary is:",d5)

        for i in d6.values():
            print(i)
        
        def fmi(mass,height):
            print("Functions!")
            print("The body mass is:",mass)
            print("The height is:",height)
            dheight=height/100
            print("Height in meters is:",dheight)
            bmi6=mass/dheight*dheight
            print("The sixth Body Mass Index is:",bmi6)
            if bmi6<=18.4:
                print("You are underweight and have malnutrition risk")
            elif bmi6>=18.5 and bmi6<=24.9:
                print("You are normal weight and have low risk!")
            elif bmi6>=25 and bmi6<=29.9:
                print("You are overweight and have enhanced heart rate risk!")
            elif bmi6>=30 and bmi6<=34.9:
                print("You are Moderately obese and have medium health risk!")
            elif bmi6>=35 and bmi6<=39.9:
                print("You are severly obese and have high health risk!")
            else:
                 print("You are very severly obese and have high health risk!")
            

            
        fmi(82,167)

        

        
  
        
  
        

 
        
        
        



        
