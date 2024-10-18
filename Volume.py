import streamlit as st
import math

# Function to calculate volume based on shape and dimensions
def calculate_volume(shape, dimensions):
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

    elif shape == 'Tetrahedron':
        a = dimensions['edge_length']
        volume = (a ** 3) / (6 * math.sqrt(2))

    elif shape == 'Ellipsoid':
        a = dimensions['semi_axis_a']
        b = dimensions['semi_axis_b']
        c = dimensions['semi_axis_c']
        volume = (4/3) * math.pi * a * b * c

    elif shape == 'Triangular Prism':
        base_area = dimensions['base_area']
        height = dimensions['height']
        volume = base_area * height

    else:
        return "Shape not recognized."

    return volume

# Streamlit app
def main():
    st.title("🌈 Volume Calculator for Geometric Shapes 🌈")
    st.markdown(
        """
        Welcome to the Volume Calculator! 
        Choose a shape below to calculate its volume.
        """
    )

    # Shape selection with a sidebar layout
    st.sidebar.header("Select a Shape")
    shape = st.sidebar.selectbox(
        "Choose a geometric shape:", 
        ['Cylinder', 'Cone', 'Sphere', 
         'Rectangular Prism', 'Cube', 'Pyramid',
         'Tetrahedron', 'Ellipsoid', 'Triangular Prism']
    )

    dimensions = {}
    
    # Collecting input based on the shape selected
    if shape in ['Cylinder', 'Cone']:
        dimensions['radius'] = st.sidebar.number_input("Enter the radius:", min_value=0.0)
        dimensions['height'] = st.sidebar.number_input("Enter the height:", min_value=0.0)

    elif shape == 'Sphere':
        dimensions['radius'] = st.sidebar.number_input("Enter the radius:", min_value=0.0)

    elif shape == 'Rectangular Prism':
        dimensions['length'] = st.sidebar.number_input("Enter the length:", min_value=0.0)
        dimensions['width'] = st.sidebar.number_input("Enter the width:", min_value=0.0)
        dimensions['height'] = st.sidebar.number_input("Enter the height:", min_value=0.0)

    elif shape == 'Cube':
        dimensions['side'] = st.sidebar.number_input("Enter the length of a side:", min_value=0.0)

    elif shape == 'Pyramid':
        dimensions['base_area'] = st.sidebar.number_input("Enter the base area:", min_value=0.0)
        dimensions['height'] = st.sidebar.number_input("Enter the height:", min_value=0.0)

    elif shape == 'Tetrahedron':
        dimensions['edge_length'] = st.sidebar.number_input("Enter the edge length:", min_value=0.0)

    elif shape == 'Ellipsoid':
        dimensions['semi_axis_a'] = st.sidebar.number_input("Enter the semi-axis length (a):", min_value=0.0)
        dimensions['semi_axis_b'] = st.sidebar.number_input("Enter the semi-axis length (b):", min_value=0.0)
        dimensions['semi_axis_c'] = st.sidebar.number_input("Enter the semi-axis length (c):", min_value=0.0)

    elif shape == 'Triangular Prism':
        dimensions['base_area'] = st.sidebar.number_input("Enter the base area:", min_value=0.0)
        dimensions['height'] = st.sidebar.number_input("Enter the height:", min_value=0.0)

    # Calculate volume button
    if st.sidebar.button("Calculate Volume"):
        volume = calculate_volume(shape, dimensions)
        if isinstance(volume, str):
            st.error(volume)  # Print error message if shape is not recognized
        else:
            st.success(f"The volume of the **{shape}** is: **{volume:.2f} cubic units**")

    # Developer Information
    st.markdown("---")
    st.markdown("### Developed by: mak3.2")
    st.markdown("Thank you for using the Volume Calculator! Have a great day!")

if __name__ == "__main__":
    main()
