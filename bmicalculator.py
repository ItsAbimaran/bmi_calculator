def cal(mass,height):
      if a==1:
         #bmi formula
         bmi= (703*(mass/(height**2)))
         bmi=(round(bmi,2))
         return bmi
      elif a==2:
         bmi=mass/(height**2)
         bmi=(round(bmi,2))
         return bmi

print("1-to use imperial system(lbs,inch)")
print("2-to use metric system(kg,m)")
#choosing imperial system or metric system
a=int(input('enter 1/2 :'))
mass=float(input('enter ur weight:'))
height=float(input('enter ur height:'))
bmi=cal(mass,height)
#bmi prime formula
prime=round((bmi/25),2)
print("\nyour weight:",mass)
print("your height:",height)
if bmi<16:
      print("your BMI Value:",bmi)
      print("your BMI PRIME Value:",prime)
      print("you are indicated as severe thinness \n you should aware of some points!!!!!! \n")
      print("Consequences of Severe Thinness:\n Nutrient Deficiencies\n Weakened Immune System\n Muscle Wasting\n organ Dysfunction:\n")
      print("Prevention of Severe Thinness:\n Adequate Caloric Intake\n Balanced Diet\n Nutrient-Rich Foods\n Hydration\n")
elif bmi>=16 and bmi<=17:
      print("your BMI Value:",bmi)
      print("your BMI PRIME Value:",prime)
      print("you are indicated as moderate thinness \n you should aware of some points!!!!!! \n")
      print("Consequences of moderate Thinness:\n Nutrient Deficiencies\n Weakened Immune System\n Reduced Bone Density\n Cognitive Impairments\n")
      print("Prevention of moderate thinness:\n Healthy Snacking\n Regular Health Check-ups\n Monitor Portion Sizes\n Regular Exercise\n")
elif bmi>=17 and bmi<=18.5:
      print("your BMI Value:",bmi)
      print("your BMI PRIME Value:",prime)
      print("you are mild thinness \n you should aware of some points!!!!!! \n")
      print("Consequences of mild Thinness:\n Nutritional Deficiencies\n Osteoporosis\n Low Energy Levels\n Weakened Immune System\n")
      print("Prevention of mild thinness:\n Exercise Regularly\n Medical Evaluation\n Regular Meals\n Regular Meals\n")
elif bmi>=18.5 and bmi<=25:
      print("your BMI Value:",bmi)
      print("your BMI PRIME Value:",prime)
      print("you are normal")
      print("To maintain a Normal diet:\n Limit Added Sugars and Salt\n Intake nutritious food\n Hydration\n Avoid processed food")
elif bmi>=25 and  bmi<=30:
      print("your BMI Value:",bmi)
      print("your BMI PRIME Value:",prime)
      print("you are overweight \n you should aware of some points!!!!!! \n")
      print("Consequences of overweight:\n Cardiovascular Diseases\n Type 2 Diabetes\n Cancer Risk\n Fatty Liver Disease\n")
      print("Prevention of overweight:\n Stay Hydrated\n Limit Sugary Drinks\n Sleep Well\n Regular Exercise\n")
elif bmi>=30 and bmi<=35:
      print("your BMI Value:",bmi)
      print("your BMI PRIME Value:",prime)
      print("you are obese class I \n you should aware of some points!!!!!! \n")
      print("Consequences of obese class I:\n Joint Problems\n Sleep Apnea\n Type 2 Diabetes\n Cardiovascular Issues\n")
      print("Prevention of obese class I:\n Stay Hydrated\n Regular Physical Activity\n Stress Management\n Medical Intervention\n")
elif bmi>=35 and bmi<=40:
      print("your BMI Value:",bmi)
      print("your BMI PRIME Value:",prime)
      print("you are obese class II \n you should aware of some points!!!!!! \n")
      print("Consequences of obese class II:\n Increased Cancer Risk\n Metabolic Disorders\n Cardiovascular Issues\n Reduced Quality of Life\n")
      print("Prevention of obese class II:\n Medical Supervision\n Portion Control\n Regular Physical Activity\n Healthy Eating\n")
elif bmi>40:
      print("your BMI Value:",bmi)
      print("your BMI PRIME Value:",prime)
      print("you are obese class III\n you should aware of some points!!!!!! \n")
      print("Consequences of obese class III:\n Increased Risk of Chronic Diseases\n Joint Problems\n Respiratory Issues\n")
      print("Prevention of obese class III:\n Healthy Diet\n Set Realistic Goals\n Create a Balanced Diet\n Consult a Healthcare Professional\n") 
