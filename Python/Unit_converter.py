import streamlit as st
st.title("UNIT CONVERTER")
st.write("It can convert:")
st.write("📏 Length (km → m → mm)")
st.write("⚖️ Weight (kg → g) ")
st.write("💧 Volume (litre → ml)")
st.write("🌡️ Temperature (Celsius → Fahrenheit) ")

n = st.selectbox("From :",["kilometer(km)","meter(m)","millimeter(mm)","kilogram(kg)","gram(g)","celsius(c)","Fahrenheit(F)","liter(L)","milliliter(mL)"])
m = st.selectbox("To:",["km","m","mm","kg","g","c","F","L","mL"])
unit_1 = st.number_input(f"Enter the {n}:",min_value=0)


b = st.button("Calculate")
if b == True:
    if n == "kilometer(km)" and m == "m":
         st.write(f"{unit_1}*{1000} = {unit_1*1000} meters")
    elif n=="meter(m)" and m == "km":
          st.write(f"{unit_1}/{1000} = {unit_1/1000} kilometers")
    elif n == "meter(m)" and m == "mm":
         st.write(f"{unit_1}*{1000} = {unit_1*1000}")    
    elif n=="millimeter(mm)" and m == "km":
         st.write(f"{unit_1}/{1000000} = {unit_1/1000000} kilometers")
    elif n == "kilometer(km)" and m == "mm":
         st.write(f"{unit_1}*{1000000} = {unit_1*1000000} millimeter") 
    elif n=="kilogram(kg)" and m =="g":
          st.write(f"{unit_1}*{1000} = {unit_1*1000} grams")
    elif n == "gram(g)" and m == "kg":
          st.write(f"{unit_1}/{1000} = {unit_1/1000} kilograms")
    elif n == "celsius(c)" and m == "F":
          st.write(f"({unit_1}*{9}/{5})+ {32} = {(unit_1*1.8)+32} degrees Fahrenheit")
    elif n == "Fahrenheit(F)" and m == "c":
         st.write(f"({unit_1}-{32})*({5}\{9}) = {(unit_1-32)*(5)/(9)} degrees celsius")
    elif n == "liter(L)" and m == "mL":
          st.write(f"{unit_1}*{1000} = {unit_1*1000} milliliters")
    elif n == "milliliter(mL)" and m == "L":
         st.write(f"{unit_1}/{1000} = {unit_1/1000} liters")
    elif n == "kilometer(km)" and m == "km":
         st.write(f"{unit_1} = {unit_1} kilometers")
    elif n == "meter(m)" and m == "m":
         st.write(f"{unit_1} = {unit_1} meters")
    elif n == "millimeter(mm)" and m == "mm":
         st.write(f"{unit_1} = {unit_1} millimeters")
    elif n == "kilogram(kg)" and m == "kg":
         st.write(f"{unit_1} = {unit_1} kilograms")
    elif n == "gram(g)" and m == "g":
         st.write(f"{unit_1} = {unit_1} grams")
    elif n == "kilometer(km)" and m == "km":
         st.write(f"{unit_1} = {unit_1} kilometers")
    elif  n == "Fahrenheit(F)" and m == "F":
         st.write(f"{unit_1} = {unit_1} degrees Fahrenheit")
    elif  n == "celsius(c)" and m == "c":
         st.write(f"{unit_1} = {unit_1} celsius")
    elif  n == "liter(L)" and m == "L":
         st.write(f"{unit_1} = {unit_1} liters")
    elif  n == "milliliter(mL)" and m == "mL":
         st.write(f"{unit_1} = {unit_1} milliliters")
     
    else:
         st.error("enter the correct unit")
else:
     pass

