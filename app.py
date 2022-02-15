import math
from difflib import restore
from random import randrange

import cv2
import matplotlib.pyplot as plt
import streamlit as st


def r_function(
    x,                              # x value of the point
    y,                              # y value of the point
    t,                              # index value of the iteration
    r_parameter = '(cos,sin)',
    resolution = 800,
    amplitude = 2.5, 
    frequency = 1.0, 
    phase_x = 0.0, 
    phase_y = 0.0, 
    ):
    H_COL = resolution

    if r_parameter == '(cos,sin)':
        return amplitude*(x*math.cos(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.sin(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(sin,tan)':
        return amplitude*(x*math.sin(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.tan(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(tan,cos)':
        return amplitude*(x*math.tan(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.cos(2.0*math.pi*frequency*t/H_COL - phase_y));
    

# Hough Function
@st.cache(suppress_st_warning=True)
def hough(
    img_inp,  
    amplitude = 2.5, 
    frequency = 1.0, 
    phase_x = 0.0, 
    phase_y = 0.0, 
    RGB = (255,255,255), 
    resolution = 800,
    r_parameter = '(cos,sin)'
    
    ): 
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
                    r = r_function(x, y, t, r_parameter=r_parameter, resolution=resolution, amplitude=amplitude, frequency=frequency, phase_x=phase_x, phase_y=phase_y)
                    xx = r * math.cos(2.0*math.pi*t/H_COL - phase_x);
                    yy = r * math.sin(2.0*math.pi*t/H_ROW - phase_y);
                    if xx >= -H_COL/2 and xx < H_COL/2 and yy >= -H_ROW/2 and yy < H_ROW/2:
                        hough[int(xx+H_COL/2)][int(yy+H_ROW/2)] = hough[int(xx+H_COL/2)][int(yy+H_ROW/2)] + 1

    # Write into art.ppm
    with open("hough_art.ppm", "w") as out_file:
        out_file.write(f"{file_type} {str(H_COL)} {str(H_ROW)} {ppm_color} ")
        for i in range(H_ROW):
            for j in range(H_COL):
                out_file.write(f"{int(hough[i][j]*(H_ROW - j)/30)} {int(hough[i][j]*(H_COL - j)/20)} {int(hough[i][j]*(1.0 + i/23.0))} ")
                # Mr.Lins colors
                # out_file.write(f"{int(hough[i][j]*(H_ROW - j)/30)} {int(hough[i][j]*(H_COL - j)/20)} {int(hough[i][j]*(1.0 + i/23.0))} ")
                # out_file.write(f"{int(hough[i][j]+R)} {int(hough[i][j]+G)} {int(hough[i][j]+B)} ")


def display():
    """This displays the hough art"""
    # Save Image
    img = cv2.imread("hough_art.ppm")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis('off')
    plt.savefig('hough_art.jpg', dpi=500)

    # Display
    st.image('hough_art.jpg', caption="Hough Art!!!", output_format="JPEG")
    st.success(f'Parameters of: {amplitude}, {frequency}, {phase_x}, {phase_y}')

    # Download Buttons
    col1, col2 = st.columns(2)
    with col1:
        # Download PPM Button
        with open("hough_art.ppm", "r") as file:
            ppm_btn = st.download_button(
                    label="Download PPM",
                    data=file,
                    file_name="art.ppm",
                )
    with col2:
        # Download JPG Button
        with open("hough_art.jpg", "rb") as file:
            jpg_btn = st.download_button(
                    label="Download JPG",
                    data=file,
                    file_name="hough_art.jpg",
                )



    st.write("For a better view go here: https://www.cs.rhodes.edu/welshc/COMP141_F16/ppmReader.html")




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

# Function Tuning
st.sidebar.header("Still want to customize more?")
st.sidebar.caption("You can tune the functions!")
drawing_selection = st.sidebar.selectbox(
    'Drawing Selection:',
    ('drawing1.ppm', 'drawing2.ppm', 'drawing3.ppm', 'drawing4.ppm', 'drawing5.ppm'),
    help="This changes how the radius calculated"
)
r_parameter = st.sidebar.selectbox(
    'Radius Function:',
    ('(cos,sin)', '(sin,tan)', '(tan,cos)'),
    help="This changes how the radius calculated"
)



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
    hough(img_inp=img_inp, amplitude=amplitude, frequency=frequency, phase_x=phase_x, phase_y=phase_y, resolution=resolution, r_parameter=r_parameter)

    # Display Hough
    display()

else:
    ### Use the default PPM File
    # Read default drawing file
    with open(drawing_selection, "r") as in_file:
        file_type = next(in_file)
        width, height = next(in_file).split()
        ppm_color = next(in_file)

        img_inp = []
        for row in in_file:
            row_lst = [int(i) for  i in row.split()]
            color_row = row_lst[3-1::3]
            img_inp.append(color_row) 

    # Calling hough Function
    hough(img_inp=img_inp, amplitude=amplitude, frequency=frequency, phase_x=phase_x, phase_y=phase_y, resolution=resolution, r_parameter=r_parameter)

    # Display Hough
    display()

    st.header("Upload drawing to make it even more unique!")







