import streamlit as st

# Display the logo
from PIL import Image

# Load your image
logo = Image.open("download")

# Create three columns, middle one to center the image
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(logo, width=600)


# Apple input
apple_kg = st.number_input("How many apples do you want in kg? (1kg = ₹200):", min_value=0.0, step=0.1)
if apple_kg >= 0:
    Apple = f"apples = {apple_kg} kg"

# Capsicum input
capsicum_kg = st.number_input("How many capsicum do you want in kg? (1kg = ₹90):", min_value=0.0, step=0.1)
if capsicum_kg >= 0:
    capsicum = f"capsicum = {capsicum_kg} kg"

# Onion input
onion_kg = st.number_input("How many onions do you want in kg? (1kg = ₹50):", min_value=0.0, step=0.1)
if onion_kg >= 0:
    onion = f"onion = {onion_kg} kg"

# Chips input
chips = st.number_input("How many packets of chips do you want? (1 packet = ₹20):", min_value=0.0, step=1.0)
if chips >= 0:
    Chips = f"chips = {chips}"

# Coupon
coupon = st.text_input("Do you have any coupon?")

# Membership
membership = st.radio("Do you want to buy grocery+ membership for ₹200/month?", ["yes", "no"])

# Age
age = st.number_input("What is your age?", min_value=0)

# Submit button
if st.button("Calculate Total"):
    # Initial total
    total = apple_kg * 200 + capsicum_kg * 90 + onion_kg * 50 + chips * 20

    if coupon == "flat50off":
        total -= 50
        st.success("You saved ₹50 using the coupon!")

    if membership == "yes":
        total += 150  # ₹200 membership - ₹50 off benefit = ₹150 net extra charge

    
    if age >= 60 and membership == "yes":
        st.info("You got a 20% senior + member discount!")
        total *= 0.8
    elif age >= 60 and (membership == "no" or membership == ""):
        st.info("You got a 10% senior discount!")
        total *= 0.9
    elif age < 60 and membership == "yes":
        st.info("You got a 5% member discount!")
        total *= 0.95
    else:
        st.warning("You got a 0% discount. So sad ")

    st.subheader(f" Your total is ₹{total:.2f}")

    # Bill summary
    bill = [Apple, capsicum, onion, Chips]
    st.markdown("### 🧾 Your Bill:")
    for item in bill:
        st.write("-", item)

    # Address
    address = st.text_input("Enter your delivery address:")
    if address:
        st.success(f"Your order will be delivered to: {address}")
