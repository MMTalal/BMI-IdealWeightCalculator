print("BMI and Ideal Weight Calculator")
# Prompt user for weight in kilograms
weight = float(input("Please input your weight in kilograms: ").strip())

# Prompt user for height in centimeters
height = float(input("Please input your height in centimeters: ").strip())

# Prompt user for age
age = int(input("Please input your age: ").strip())

# Prompt user for gender (f/m)
gender = input("Please input your gender (choose f/m): ").strip()

# Check if the user is female
if gender == "f":
    print("based on you are Female")
    
    # Body Mass Index (BMI) calculation: weight (in kilograms) / (height)^2 (in meters)
    bmi = (weight / ((height) / 100) ** 2)
    
    # Check the BMI range and provide corresponding message
    if bmi < 18.5:
        print("You are underweight")
    elif 18.5 <= bmi < 24.9:
        print("Your weight is healthy/normal")
    elif 24.9 <= bmi < 29.9:
        print("You are overweight")
    elif 29.9 <= bmi < 34.9:
        print("You are in Obesity Class I")
    elif 34.9 <= bmi < 39.9:
        print("You are in Obesity Class II")
    else:
        print("You are in Obesity Class III (Severe/Morbid Obesity)")
    
    print(f"Your BMI is {bmi:.5f}")
    print("Note: This medical calculator is not intended for children, pregnant or breastfeeding women")

    #Ideal weight according to height and age for Women            
    if 18 <= age <= 24:
        if 150 <= height <= 160:
            print("Your ideal weight is between 50 and 55 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 55 and 60 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 60 and 65 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 65 and 70 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 70 and 75 kg.")
    elif 25 <= age <= 34:
        if 150 <= height <= 160:
            print("Your ideal weight is between 52 and 57 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 57 and 62 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 62 and 67 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 67 and 72 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 72 and 77 kg.")
    elif 35 <= age <= 44:
        if 150 <= height <= 160:
            print("Your ideal weight is between 54 and 59 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 59 and 64 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 64 and 69 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 69 and 74 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 74 and 79 kg.")
    elif 45 <= age <= 54:
        if 150 <= height <= 160:
            print("Your ideal weight is between 56 and 61 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 61 and 66 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 66 and 71 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 71 and 76 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 76 and 81 kg.")
    elif 55 <= age <= 64:
        if 150 <= height <= 160:
            print("Your ideal weight is between 58 and 63 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 63 and 68 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 68 and 73 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 73 and 78 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 78 and 83 kg.")
    elif age >= 65:
        if 150 <= height <= 160:
            print("Your ideal weight is between 60 and 65 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 65 and 70 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 70 and 75 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 75 and 80 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 80 and 85 kg.")
    else:
        print("Invalid age or height entered.")

    # Ideal weight calculation for females
    ideal_weight = 45 + 0.9 * (height - 150)
    print(f"Your exact ideal weight is {ideal_weight} Kg")

    # Check if the user's weight is above or below the ideal weight
    if weight > ideal_weight:
        print(f"You need to decrease {weight - ideal_weight} kilograms\n- Eat healthy, whole foods such as fresh vegetables and fruits, low-fat dairy products, lean protein, whole grains, nuts, etc.")
        print("- Monitoring calories, as this helps in losing weight and achieving the ideal weight by burning more calories than the body consumes. Therefore, the number of calories consumed and the size of the food portion must be monitored.")
    elif weight < ideal_weight:
        print(f"- You need to increase {ideal_weight - weight} kilograms\nIt is important to get approximately 150 minutes of a variety of aerobic and resistance exercises.")
    else:
        print("You have the perfect weight")
    
# Check if the user is male
elif gender == "m":
    print("based on you are Male")
    
    # Body Mass Index (BMI) calculation: weight (in kilograms) / (height)^2 (in meters)
    bmi = (weight / ((height) / 100) ** 2)
    
    # Check the BMI range and provide corresponding message
    if bmi < 18.5:
        print("You are underweight")
    elif 18.5 <= bmi < 24.9:
        print("Your weight is healthy/normal")
    elif 24.9 <= bmi < 29.9:
        print("You are overweight")
    elif 29.9 <= bmi < 34.9:
        print("You are in Obesity Class I")
    elif 34.9 <= bmi < 39.9:
        print("You are in Obesity Class II")
    else:
        print("You are in Obesity Class III (Severe/Morbid Obesity)")
    
    print(f"Your BMI is {bmi:.5f}")
    print("Note: This medical calculator is not intended for children, pregnant or breastfeeding women")

    #Ideal weight according to height and age for men        
    if 18 <= age <= 24:
        if 150 <= height <= 160:
            print("Your ideal weight is between 57 and 65 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 65 and 72 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 72 and 79 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 79 and 86 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 86 and 93 kg.")
    elif 25 <= age <= 34:
        if 150 <= height <= 160:
            print("Your ideal weight is between 60 and 68 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 68 and 76 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 76 and 84 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 84 and 92 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 92 and 99 kg.")
    elif 35 <= age <= 44:
        if 150 <= height <= 160:
            print("Your ideal weight is between 63 and 71 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 71 and 79 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 79 and 87 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 87 and 95 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 95 and 103 kg.")
    elif 45 <= age <= 54:
        if 150 <= height <= 160:
            print("Your ideal weight is between 66 and 74 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 74 and 82 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 82 and 90 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 90 and 98 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 98 and 106 kg.")
    elif 55 <= age <= 64:
        if 150 <= height <= 160:
            print("Your ideal weight is between 69 and 77 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 77 and 85 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 85 and 93 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 93 and 101 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 101 and 109 kg.")
    elif age >= 65:
        if 150 <= height <= 160:
            print("Your ideal weight is between 72 and 80 kg.")
        elif 161 <= height <= 170:
            print("Your ideal weight is between 80 and 88 kg.")
        elif 171 <= height <= 180:
            print("Your ideal weight is between 88 and 96 kg.")
        elif 181 <= height <= 190:
            print("Your ideal weight is between 96 and 104 kg.")
        elif 191 <= height <= 200:
            print("Your ideal weight is between 104 and 112 kg.")
    else:
        print("Invalid age or height entered.")

    # Ideal weight calculation for males
    ideal_weight = 48 + 1.1 * (height - 150)
    print(f"Your exact ideal weight is {ideal_weight} Kg")

    # Check if the user's weight is above or below the ideal weight
    if weight > ideal_weight:
        print(f"You need to decrease {weight - ideal_weight} kilograms\n- Eat healthy, whole foods such as fresh vegetables and fruits, low-fat dairy products, lean protein, whole grains, nuts, etc.")
        print("- Monitoring calories, as this helps in losing weight and achieving the ideal weight by burning more calories than the body consumes. Therefore, the number of calories consumed and the size of the food portion must be monitored.")
    elif weight < ideal_weight:
        print(f"- You need to increase {ideal_weight - weight} kilograms\nIt is important to get approximately 150 minutes of a variety of aerobic and resistance exercises.")
    else:
        print("You have the perfect weight")
    
# If the gender input is neither 'f' nor 'm'
else:
    print("You are not human! Please try again and choose the correct answer (f/m)")