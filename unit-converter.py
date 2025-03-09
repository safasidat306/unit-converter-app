import streamlit as st
st.title("Unit Converter App")
st.markdown("### Converts Mathematics, Physics & Chemistry Units")
st.write("Welcome! Select your Subject, enter a value and get the converted result in real-time")
Subject = st.selectbox("Choose a Subject" , ["Mathematics", "Physics", "Chemistry"])
def convert_units( Subject , Value , Unit ):
    if Subject == "Mathematics":
        if Unit == "Miles to Kilometers":
            return Value * 1.609
        elif Unit == "Kilometers to Miles":
            return Value * 0.621371
        elif Unit == "Pounds to Kilograms":
            return Value * 2.20462
        elif Unit == "Kilograms to Pounds":
            return Value * 2.20462
        elif Unit == "Feet to Meters":
            return Value * 0.3048
        elif Unit == "Meters to Feet":
            return Value / 0.3048
        elif Unit == "Inches to cm":
            return Value * 2.54
        elif Unit == "cm to Inches":
            return Value / 2.54
        elif Unit == "Yards to Meters":
            return Value * 0.9144
        elif Unit == "Meters to Yards":
            return Value / 0.9144
        elif Unit == "Km/hr to m/s":
            return Value * 0.2778
        elif Unit == "m/s to Km/hr":
            return Value / 0.2778

    elif Subject == "Physics":
        if Unit == "Newton to Dyne":
            return Value * 1e5
        elif Unit == "Dyne to Newton":
            return Value / 1e5
        elif Unit == "Joule to Calorie":
            return Value * 0.239
        elif Unit == "Calorie to Joule":
            return Value / 0.239
        elif Unit == "Watt to HP":
            return Value * 0.00134
        elif Unit == "HP to Watt":
            return Value / 0.00134
        elif Unit == "Pascal to atm":
            return Value / 101325
        elif Unit == "Atm to Pascal":
            return Value * 101325
        elif Unit == "Celsius to Fahrenheit":
            return (Value * 9/5) + 32  
        
    elif Subject == "Chemistry":
        if Unit == "Gram to Mole":
            return Value / 18.015
        elif Unit == "Mole to Gram":
            return Value * 0.621371
        elif Unit == "Mole to Atoms":
            return Value * 6.022e23
        elif Unit == "Atoms to Mole":
            return Value * 0.3048
        elif Unit == "Molality to Molarity":
            return Value * 1.5
        elif Unit == "Molarity to Molarity":
            return Value * 2.54
        elif Unit == "pH to H+ Concentration":
            return  10 ** -Value
        elif Unit == "H+ concentration to pH":
            return Value * 0.9144
        elif Unit == "Kg to mg":
            return Value * 1e6
        elif Unit == "mg to Kg":
            return Value * 0.2778

if Subject == "Mathematics":
    unit = st.selectbox("Select Conversation" , ["Miles to Kilometers" , "Kilometers to Miles" , "Pounds to Kilograms" , "Kilograms to Pounds" , "Feet to Meters" , "Meters to Feet" , "Inches to cm" , "cm to Inches" , "Yards to Meters" , "Meters to Yards" ,  "Km/hr to m/s" , "m/s to Km/hr"] )   
elif Subject == "Physics":
    unit = st.selectbox("Select Conversation" , ["Newton to Dyne" , "Dyne to Newton" , "Joule to Calorie" , "Calorie to Joule" , "Watt to HP" , "HP to Watt" , "Pascal to atm" , "Atm to Pascal" , "Celsius to Fahrenheit"] )   
elif Subject == "Chemistry":
    unit = st.selectbox("Select Conversation" , ["Gram to Mole", "Mole to Gram" , "Mole to Atoms" , "Atoms to Mole" , "Molality to Molarity" , "Molarity to Molarity" , "pH to H+ Concentration" , "H+ concentration to pH" , "Kg to mg" , "mg to Kg"] )

Value = st.number_input("Enter the value")

if st.button("Convert"):
    result = convert_units(Subject , Value , unit )  
    st.success(f"The result is {result:.2f}")      
        
        