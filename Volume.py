import streamlit as st
import math

def calculate_volume(shape, dimensions):
    """Calculate the volume of a given shape based on its dimensions."""
    if shape == 'Cylinder':
        r = dimensions['radius']
        h = dimensions['height']
        volume = math.pi * (r ** 2) * h

    elif shape == 'Cone':
        r = dimensions['radius']
        h = dimensions['height']
        volume = (1/3) * math.pi * (r ** 2) * h

    elif shape == 'Sphere':
        r = dimensions['radius']
        volume = (4/3) * math.pi * (r ** 3)

    elif shape == 'Rectangular Prism':
        l = dimensions['length']
        w = dimensions['width']
        h = dimensions['height']
        volume = l * w * h

    elif shape == 'Cube':
        s = dimensions['side']
        volume = s ** 3

    elif shape == 'Pyramid':
        b = dimensions['base_area']
        h = dimensions['height']
        volume = (1/3) * b * h

    else:
        return "Shape not recognized."

    return volume

# Streamlit app
def main():
    st.title("Volume Calculator for Various Vessel Shapes")

    # Shape selection
    shape = st.selectbox("Select a shape:", 
                         ['Cylinder', 'Cone', 'Sphere', 
                          'Rectangular Prism', 'Cube', 'Pyramid'])

    dimensions = {}
    
    # Collecting input based on the shape selected
    if shape in ['Cylinder', 'Cone']:
        dimensions['radius'] = st.number_input("Enter the radius:", min_value=0.0)
        dimensions['height'] = st.number_input("Enter the height:", min_value=0.0)

    elif shape == 'Sphere':
        dimensions['radius'] = st.number_input("Enter the radius:", min_value=0.0)

    elif shape == 'Rectangular Prism':
        dimensions['length'] = st.number_input("Enter the length:", min_value=0.0)
        dimensions['width'] = st.number_input("Enter the width:", min_value=0.0)
        dimensions['height'] = st.number_input("Enter the height:", min_value=0.0)

    elif shape == 'Cube':
        dimensions['side'] = st.number_input("Enter the length of a side:", min_value=0.0)

    elif shape == 'Pyramid':
        dimensions['base_area'] = st.number_input("Enter the base area:", min_value=0.0)
        dimensions['height'] = st.number_input("Enter the height:", min_value=0.0)

    # Calculate volume
    if st.button("Calculate Volume"):
        volume = calculate_volume(shape, dimensions)
        if isinstance(volume, str):
            st.error(volume)  # Print error message if shape is not recognized
        else:
            st.success(f"The volume of the {shape} is: {volume:.2f} cubic units")

    st.write("Thank you for using the Volume Calculator! Have a great day!")

if __name__ == "__main__":
    main()
