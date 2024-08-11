import streamlit as st
from datetime import datetime, date

# Function to calculate if a task is due
def is_due(last_service_date, interval_days):
    days_since_service = (datetime.now().date() - last_service_date).days
    return days_since_service >= interval_days

# Maintenance Parameters for Two-Wheelers and Four-Wheelers
maintenance_schedule_two_wheeler = {
    "Engine Oil": {"interval_miles": 2500, "interval_days": 180},
    "Brake Inspection": {"interval_miles": 5000, "interval_days": 365},
    "Battery Check": {"interval_miles": 0, "interval_days": 180},
    "Chain Lubrication": {"interval_miles": 1000, "interval_days": 90},
    "Coolant Check": {"interval_miles": 3000, "interval_days": 180},
}

maintenance_schedule_four_wheeler = {
    "Engine Oil": {"interval_miles": 5000, "interval_days": 180},
    "Tire Rotation": {"interval_miles": 7500, "interval_days": 365},
    "Brake Inspection": {"interval_miles": 10000, "interval_days": 365},
    "Battery Check": {"interval_miles": 0, "interval_days": 180},
    "Coolant Check": {"interval_miles": 5000, "interval_days": 180},
    "Transmission Fluid": {"interval_miles": 30000, "interval_days": 730},
    "Air Filter": {"interval_miles": 20000, "interval_days": 365},
    "Wiper Blades": {"interval_miles": 0, "interval_days": 180},
}

# Expanded list of brands and models
brands_and_models = {
    "Toyota": ["Corolla", "Camry", "RAV4", "Prius", "Highlander", "Land Cruiser"],
    "Ford": ["Fiesta", "Mustang", "Explorer", "Focus", "F-150", "Escape"],
    "Honda": ["Civic", "Accord", "CR-V", "Fit", "Pilot", "Odyssey"],
    "BMW": ["3 Series", "5 Series", "X3", "X5", "M3", "i8"],
    "Mercedes-Benz": ["C-Class", "E-Class", "S-Class", "GLA", "GLE", "G-Class"],
    "Yamaha": ["YZF-R3", "MT-07", "FZ-09", "R15", "FZ-S", "MT-15"],
    "Suzuki": ["GSX-R600", "V-Strom 650", "Hayabusa", "Gixxer", "Intruder", "Access 125"],
    "Harley-Davidson": ["Street 750", "Iron 883", "Fat Boy", "Sportster", "Street Bob", "Road King"],
    "Kawasaki": ["Ninja 300", "Z900", "Versys 650", "Vulcan S", "Ninja H2", "KLX 140"],
    "Ducati": ["Panigale V4", "Monster 821", "Multistrada 950", "Scrambler", "Diavel 1260", "SuperSport"],
    "Tata":["Tiago", "Altroz", "Tigor", "Nexon", "Harrier", "Safari", "Punch", "Nexon EV ", "Nexon EV", "Tigor EV", "Tiago EV"],
    'pulsar': ['Pulsar 150', 'Pulsar NS200', 'Pulsar RS200'], 
    'splendor': ['Splendor Plus', 'Super Splendor', 'Splendor Xtend'],
    'discover': ['Discover 110', 'Discover 125'],
    'ktm': ['Duke 200', 'RC 390', 'Adventure 390'],
    'royal-enfield': ['Classic 350', 'Bullet 350', 'Himalayan'],
    "Maruti-Suzuki":['Alto', 'Swift', 'Baleno', 'Ignis','Dzire', 'Ciaz','Brezza', 'Vitara Brezza', 'Grand Vitara', 'S-Cross','Ertiga', 'XL6']
}

st.title("Garage Owner's Vehicle Maintenance Management")

# Select Vehicle Type
st.header("Select Vehicle Type")
vehicle_type = st.radio("Vehicle Type", ("Two-Wheeler", "Four-Wheeler"))

# Set the maintenance schedule based on vehicle type
if vehicle_type == "Two-Wheeler":
    maintenance_schedule = maintenance_schedule_two_wheeler
    available_brands = ["Yamaha", "Suzuki", "Harley-Davidson", "Kawasaki", "Ducati","pulsar","splendor","discover","ktm","royal-enfield"]
else:
    maintenance_schedule = maintenance_schedule_four_wheeler
    available_brands = ["Toyota", "Ford", "Honda", "BMW", "Mercedes-Benz","Tata","Maruti-Suzuki"]

# Vehicle Info
st.header("Vehicle Information")
selected_brand = st.selectbox("Select Brand", available_brands)
selected_model = st.selectbox("Select Model", brands_and_models[selected_brand])
vehicle_year = st.text_input("Year")
vehicle_mileage = st.number_input("Current Mileage", min_value=0)

# Service Records
st.header("Service Records")
last_service_dates = {}
miles_since_last_service = {}

for task in maintenance_schedule:
    st.subheader(task)
    last_service_date = st.date_input(f"Last {task} Service Date", value=date.today())
    last_service_dates[task] = last_service_date
    if maintenance_schedule[task]["interval_miles"] > 0:
        miles_since_last_service[task] = st.number_input(f"Miles Since Last {task}", min_value=0)

# Maintenance Due
st.header("Maintenance Due")
for task, schedule in maintenance_schedule.items():
    last_service_date = last_service_dates[task]
    interval_days = schedule["interval_days"]
    interval_miles = schedule["interval_miles"]

    due_by_miles = False
    due_by_date = is_due(last_service_date, interval_days)
    
    if interval_miles > 0:
        service_miles = miles_since_last_service[task]
        due_by_miles = service_miles >= interval_miles
    
    if due_by_miles or due_by_date:
        st.warning(f"{task} is due for service!")
    else:
        st.success(f"{task} is not due yet.")

# Summary
st.header("Maintenance Summary")
st.write(f"Brand: {selected_brand}")
st.write(f"Model: {selected_model}")
st.write(f"Year: {vehicle_year}")
for task in maintenance_schedule:
    st.write(f"{task}: Last serviced on {last_service_dates[task]}")

# Save Data
if st.button("Save Service Records"):
    st.success("Service records saved successfully!")
