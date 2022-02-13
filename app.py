import math
from difflib import restore
from random import randrange

import cv2
import matplotlib.pyplot as plt
import streamlit as st


@st.cache(suppress_st_warning=True)
def hough(img_inp,  amplitude = 2.5, frequency = 1.0, phase_x = 0.0, phase_y = 0.0, RGB = (255,255,255), resolution = 800): 
    """This is the hough art function"""
    # Program Constants
    file_type = 'P3'
    ppm_color = 255
    COL = 300
    ROW = 200
    H_COL = resolution
    H_ROW = resolution
    R = RGB[0]
    G = RGB[1]
    B = RGB[2]

    # Image lists
    hough = [ [ 0 for y in range(H_COL) ] for x in range(H_ROW) ]


    # Create Hough Space
    for i in range(ROW):
        for j in range(COL):
            if img_inp[i][j] == int(ppm_color):
                x = j - COL/2
                y = i - ROW/2
                for t in range(H_COL):
                    r = amplitude*(x*math.cos(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.sin(2.0*math.pi*frequency*t/H_COL - phase_y));
                    xx = r * math.cos(2.0*math.pi*t/H_COL - phase_x);
                    yy = r * math.sin(2.0*math.pi*t/H_ROW - phase_y);
                    if xx >= -H_COL/2 and xx < H_COL/2 and yy >= -H_ROW/2 and yy < H_ROW/2:
                        hough[int(xx+H_COL/2)][int(yy+H_ROW/2)] = hough[int(xx+H_COL/2)][int(yy+H_ROW/2)] + 1

    # Write into art.ppm
    with open("py_art.ppm", "w") as out_file:
        out_file.write(f"{file_type} {str(H_COL)} {str(H_ROW)} {ppm_color} ")
        for i in range(H_ROW):
            for j in range(H_COL):
                out_file.write(f"{int(hough[i][j]*(H_ROW - j)/30)} {int(hough[i][j]*(H_COL - j)/20)} {int(hough[i][j]*(1.0 + i/23.0))} ")
                # out_file.write(f"{int(hough[i][j]+R)} {int(hough[i][j]+G)} {int(hough[i][j]+B)} ")


# --- Main -------------------------------------------------------------------------

###### Sidebar ##################################################################


### Manipluatable Variables

# Parameter tuning
st.sidebar.header("Random")
if st.sidebar.button('Random'):
    # Random button to randomly generate
    st.sidebar.header("Generated Parameters")
    resolution = st.sidebar.slider("resolution", min_value=800, max_value=1600, step=200, value=800)
    amplitude = st.sidebar.slider("amplitude", value=randrange(3, 10))
    frequency = st.sidebar.slider("frequency", value=randrange(0, 10))
    phase_x = st.sidebar.slider("phase_x", value=randrange(0, 10))
    phase_y = st.sidebar.slider("phase_y", value=randrange(0, 10))
else:
    # User chooses parameters
    st.sidebar.header("Parameters")
    resolution = st.sidebar.slider("resolution", min_value=800, max_value=1600, step=200)
    amplitude = st.sidebar.slider("amplitude")
    frequency = st.sidebar.slider("frequency")
    phase_x = st.sidebar.slider("phase_x")
    phase_y = st.sidebar.slider("phase_y")

# Color tuning
# color = st.sidebar.color_picker('Pick A Color', '#00f900').lstrip('#')
# st.write('The current color is', '#' + color)
# color_RGB = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

# Upload File
ppm_upload = st.sidebar.file_uploader("Choose a PPM file", accept_multiple_files=False)


###### Body ##################################################################

if ppm_upload is not None:
    ### If there is an uploaded PPM File

    # Reading Uploaded PPM File
    ppm = []
    for row in ppm_upload:
        ppm.append(row)
    img_inp = []
    for i in range(3, len(ppm)):
        row_lst = [int(i) for i in ppm[i].split()]
        color_row = row_lst[3-1::3]
        img_inp.append(color_row)

    # Calling hough
    hough(img_inp=img_inp, amplitude=amplitude, frequency=frequency, phase_x=phase_x, phase_y=phase_y, resolution=resolution)

    # Display Image
    img = cv2.imread("py_art.ppm")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.savefig('img.png', dpi=500)
    st.image('img.png')
    st.success(f'Parameters of: {amplitude}, {frequency}, {phase_x}, {phase_y}')

    # Download Button
    with open("py_art.ppm", "r") as file:
        btn = st.download_button(
                label="Download Art!",
                data=file,
                file_name="art.ppm",
            )
    st.write("For a better view go here: https://www.cs.rhodes.edu/welshc/COMP141_F16/ppmReader.html")
else:
    ### Use the default PPM File
    # Read default drawing file
    with open("drawing.ppm", "r") as in_file:
        file_type = next(in_file)
        width, height = next(in_file).split()
        ppm_color = next(in_file)

        img_inp = []
        for row in in_file:
            row_lst = [int(i) for  i in row.split()]
            color_row = row_lst[3-1::3]
            img_inp.append(color_row) 

    # Calling hough Function
    hough(img_inp=img_inp, amplitude=amplitude, frequency=frequency, phase_x=phase_x, phase_y=phase_y, resolution=resolution)
    st.success(f'Parameters of: {amplitude}, {frequency}, {phase_x}, {phase_y}')

    # Display Image
    img = cv2.imread("py_art.ppm")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.savefig('img.png', dpi=500)
    st.image('img.png')

    # Download Button
    with open("py_art.ppm", "r") as file:
        btn = st.download_button(
                label="Download Art!",
                data=file,
                file_name="art.ppm",
            )
    st.write("For a better view go here: https://www.cs.rhodes.edu/welshc/COMP141_F16/ppmReader.html")

    st.header("Upload drawing to make it even more unique!")







