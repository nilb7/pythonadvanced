import streamlit as st

# Page title
st.title("BMI Calculator")

# Store people in session state
if "people" not in st.session_state:
    st.session_state.people = []

# Input fields
name = st.text_input("Enter name:")
age = st.number_input("Enter age:", min_value=1, max_value=120, value=24)
weight = st.number_input("Enter weight in kilograms:", min_value=1.0, value=85.0, step=0.1)
height = st.number_input("Enter height in meters:", min_value=0.5, value=1.80, step=0.01)

# BMI calculation function
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# BMI category function
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Add person button
if st.button("Add Person"):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    person = {
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "bmi": round(bmi, 2),
        "category": category
    }

    st.session_state.people.append(person)
    st.success(f"{name} has been added.")

# Display results
st.subheader("Results")

for person in st.session_state.people:
    st.write(
        f"{person['name']}, "
        f"Age: {person['age']}, "
        f"Weight: {person['weight']} kg, "
        f"Height: {person['height']} m, "
        f"BMI: {person['bmi']}, "
        f"Category: {person['category']}"
    )