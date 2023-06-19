def get_personal_details():
    name = input("What is your name? ")
    age = input("How old are you? ")
    address = input("What is your address? ")
    return name, age, address

def get_exam_scores():
    math_score = input("What is your math score? ")
    physics_score = input("What is your physics score? ")
    chemistry_score = input("What is your chemistry score? ")
    return math_score, physics_score, chemistry_score

def calculate_total_score(scores):
    math_score, physics_score, chemistry_score = scores
    total_score = int(math_score) + int(physics_score) + int(chemistry_score)
    return total_score

def assess_eligibility(total_score):
    if total_score >= 250:
        return "Congratulations! You are eligible for admission."
    else:
        return "Sorry, you are not eligible for admission."

def main():
    print("Welcome to the School/College Admission Chatbot!")
    print("Please provide the following details to check your eligibility.")
    
    name, age, address = get_personal_details()
    scores = get_exam_scores()
    total_score = calculate_total_score(scores)
    eligibility_result = assess_eligibility(total_score)
    
    print("\n--- Admission Result ---")
    print("Name:", name)
    print("Age:", age)
    print("Address:", address)
    print("Total Score:", total_score)
    print(eligibility_result)

if __name__ == "__main__":
    main()
