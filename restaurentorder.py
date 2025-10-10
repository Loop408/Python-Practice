import streamlit as st
import pandas as pd

# -----------------------------
# MENU DATA
# -----------------------------
menu = {
    "Veg Starters": [
        {"name": "Paneer Tikka", "price": 180, "type": "Veg"},
        {"name": "Veg Manchurian", "price": 160, "type": "Veg"},
        {"name": "Gobi 65", "price": 150, "type": "Veg"},
        {"name": "Spring Rolls", "price": 140, "type": "Veg"},
        {"name": "Cheese Balls", "price": 200, "type": "Veg"},
        {"name": "Hara Bhara Kabab", "price": 170, "type": "Veg"},
        {"name": "Corn Tikki", "price": 160, "type": "Veg"},
        {"name": "Paneer Pakora", "price": 150, "type": "Veg"},
        {"name": "Crispy Veg", "price": 180, "type": "Veg"},
        {"name": "Chilli Paneer", "price": 190, "type": "Veg"},
    ],
    "Non-Veg Starters": [
        {"name": "Chicken 65", "price": 200, "type": "Non-Veg"},
        {"name": "Chilli Chicken", "price": 220, "type": "Non-Veg"},
        {"name": "Fish Fingers", "price": 250, "type": "Non-Veg"},
        {"name": "Prawn 65", "price": 280, "type": "Non-Veg"},
        {"name": "Mutton Seekh Kabab", "price": 300, "type": "Non-Veg"},
        {"name": "Egg Pepper Fry", "price": 180, "type": "Non-Veg"},
        {"name": "Tandoori Chicken", "price": 350, "type": "Non-Veg"},
        {"name": "Chicken Lollipop", "price": 230, "type": "Non-Veg"},
        {"name": "Fish Tikka", "price": 270, "type": "Non-Veg"},
        {"name": "Lemon Chicken", "price": 240, "type": "Non-Veg"},
    ],
    "Rice & Main Course": [
        {"name": "Veg Biryani", "price": 220, "type": "Veg"},
        {"name": "Paneer Curry", "price": 250, "type": "Veg"},
        {"name": "Dal Tadka", "price": 150, "type": "Veg"},
        {"name": "Jeera Rice", "price": 120, "type": "Veg"},
        {"name": "Chicken Biryani", "price": 300, "type": "Non-Veg"},
        {"name": "Mutton Biryani", "price": 350, "type": "Non-Veg"},
        {"name": "Fish Curry", "price": 280, "type": "Non-Veg"},
        {"name": "Egg Curry", "price": 200, "type": "Non-Veg"},
        {"name": "Prawn Curry", "price": 320, "type": "Non-Veg"},
        {"name": "Veg Pulao", "price": 180, "type": "Veg"},
    ],
    "Indian Breads": [
        {"name": "Butter Naan", "price": 40, "type": "Veg"},
        {"name": "Garlic Naan", "price": 50, "type": "Veg"},
        {"name": "Tandoori Roti", "price": 30, "type": "Veg"},
        {"name": "Plain Paratha", "price": 35, "type": "Veg"},
        {"name": "Aloo Paratha", "price": 60, "type": "Veg"},
        {"name": "Paneer Paratha", "price": 70, "type": "Veg"},
        {"name": "Kulcha", "price": 45, "type": "Veg"},
        {"name": "Lachha Paratha", "price": 55, "type": "Veg"},
        {"name": "Missi Roti", "price": 40, "type": "Veg"},
        {"name": "Rumali Roti", "price": 35, "type": "Veg"},
    ],
    "Drinks": [
        {"name": "Coke", "price": 50, "type": "Veg"},
        {"name": "Sprite", "price": 50, "type": "Veg"},
        {"name": "Sweet Lassi", "price": 70, "type": "Veg"},
        {"name": "Masala Chaas", "price": 60, "type": "Veg"},
        {"name": "Cold Coffee", "price": 90, "type": "Veg"},
        {"name": "Mango Juice", "price": 80, "type": "Veg"},
        {"name": "Water Bottle", "price": 20, "type": "Veg"},
        {"name": "Lemon Soda", "price": 60, "type": "Veg"},
        {"name": "Iced Tea", "price": 70, "type": "Veg"},
        {"name": "Filter Coffee", "price": 50, "type": "Veg"},
    ],
    "Desserts": [
        {"name": "Ice Cream", "price": 100, "type": "Veg"},
        {"name": "Gulab Jamun", "price": 80, "type": "Veg"},
        {"name": "Rasmalai", "price": 120, "type": "Veg"},
        {"name": "Brownie", "price": 150, "type": "Veg"},
        {"name": "Chocolate Lava Cake", "price": 180, "type": "Veg"},
        {"name": "Fruit Salad", "price": 90, "type": "Veg"},
        {"name": "Kheer", "price": 100, "type": "Veg"},
        {"name": "Kulfi", "price": 110, "type": "Veg"},
        {"name": "Donut", "price": 130, "type": "Veg"},
        {"name": "Cheesecake", "price": 200, "type": "Veg"},
    ]
}

# -----------------------------
# STREAMLIT CONFIG
# -----------------------------
st.set_page_config(page_title="The Flavour Spot", page_icon="🍴", layout="wide")
st.title("🍴 Welcome to *The Flavour Spot*")
st.markdown("### 🌿 Classic Menu — Collapsible Sections with Add Button Style")

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = {}

# -----------------------------
# VEG/NON-VEG MODE
# -----------------------------
mode = st.radio("Select Mode:", ["Vegetarian", "Non-Vegetarian"], horizontal=True)

# -----------------------------
# FUNCTIONS
# -----------------------------
def get_sections(mode):
    if mode == "Vegetarian":
        return [sec for sec in menu.keys() if "Non-Veg" not in sec]
    return list(menu.keys())

def add_to_cart(item_name, price, type_, qty):
    if qty > 0:
        if item_name in st.session_state.cart:
            st.session_state.cart[item_name]["quantity"] += qty
        else:
            st.session_state.cart[item_name] = {"quantity": qty, "price": price, "type": type_}
        st.success(f"✅ {item_name} x {qty} added to cart!")

def display_items(section):
    items = menu[section]
    if mode == "Vegetarian":
        items = [item for item in items if item["type"] == "Veg"]

    for item in items:
        if f"qty_{item['name']}" not in st.session_state:
            st.session_state[f"qty_{item['name']}"] = 0

        col1, col2, col3, col4 = st.columns([4,2,2,2])
        with col1:
            st.markdown(f"**{item['name']}** 🍽️")
        with col2:
            st.markdown(f"Type: {item['type']}")
        with col3:
            st.session_state[f"qty_{item['name']}"] = col3.number_input(
                "Qty", min_value=0, max_value=10,
                value=st.session_state[f"qty_{item['name']}"],
                key=f"input_{item['name']}"
            )
        with col4:
            if col4.button("Add", key=f"add_{item['name']}"):
                add_to_cart(item["name"], item["price"], item["type"], st.session_state[f"qty_{item['name']}"])

        st.markdown("---")

def show_cart():
    st.sidebar.header("🛍️ Your Cart")
    total = 0
    if st.session_state.cart:
        for name, details in st.session_state.cart.items():
            subtotal = details["quantity"] * details["price"]
            st.sidebar.write(f"{name} x {details['quantity']} = ₹{subtotal}")
            total += subtotal
        st.sidebar.markdown(f"**Total: ₹{total}**")
    else:
        st.sidebar.write("Cart is empty")
    return total

def checkout(total):
    if not st.session_state.cart:
        st.sidebar.warning("⚠️ Cart is empty!")
        return
    st.subheader("🍽️ Order Summary")
    summary = []
    for name, details in st.session_state.cart.items():
        subtotal = details["quantity"] * details["price"]
        summary.append({
            "Item": name,
            "Quantity": details["quantity"], 
            "Type": details["type"], 
            "Price (₹)": details["price"], 
            "Subtotal (₹)": subtotal
        })
    if total > 1000:
        dessert = "Free Ice Cream 🍨"
        summary.append({
            "Item": dessert, 
            "Quantity": 1, 
            "Type": "Veg", 
            "Price (₹)": 0, 
            "Subtotal (₹)": 0
        })
    st.table(pd.DataFrame(summary))
    st.success(f"💰 Total Bill: ₹{total}")
    if total > 1000:
        st.balloons()
        st.info("🎉 Free Dessert Added!")

# -----------------------------
# DISPLAY MENU WITH EXPANDERS
# -----------------------------
sections = get_sections(mode)
for section in sections:
    with st.expander(section):
        display_items(section)

# -----------------------------
# SHOW CART & CHECKOUT
# -----------------------------
total = show_cart()

if st.sidebar.button("🧾 Checkout"):
    checkout(total)

if st.sidebar.button("🗑️ Clear Cart"):
    st.session_state.cart = {}
    st.sidebar.success("🗑️ Cart cleared!")
