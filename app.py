import math
from random import randrange

import streamlit as st
from cv2 import COLOR_BGR2RGB, cvtColor, imread
from matplotlib.pyplot import axis, imshow, savefig, title


def r_function(
    x,                              # x value of the point
    y,                              # y value of the point
    t,                              # index value of the iteration
    r_parameter = '(cos,sin)',
    resolution = 800,
    amplitude = 2.5, 
    frequency = 1.0, 
    phase_x = 0.0, 
    phase_y = 0.0):
    """This function calculates the radius for the polar cordinates"""

    H_COL = resolution

    if r_parameter == '(cos,sin)':
        return amplitude*(x*math.cos(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.sin(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(sin,tan)':
        return amplitude*(x*math.sin(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.tan(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(tan,cos)':
        return amplitude*(x*math.tan(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.cos(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(cos,sinh)':
        return amplitude*(x*math.cos(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.sinh(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(tan,sinh)':
        return amplitude*(x*math.tan(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.sinh(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(sin,sinh)':
        return amplitude*(x*math.sin(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.sinh(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(cos,cosh)':
        return amplitude*(x*math.cos(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.cosh(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(tan,cosh)':
        return amplitude*(x*math.tan(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.cosh(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(sin,cosh)':
        return amplitude*(x*math.sin(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.cosh(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(cos,tanh)':
        return amplitude*(x*math.cos(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.tanh(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(tan,tanh)':
        return amplitude*(x*math.tan(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.tanh(2.0*math.pi*frequency*t/H_COL - phase_y));
    elif r_parameter == '(sin,tanh)':
        return amplitude*(x*math.sin(2.0*math.pi*frequency*t/H_COL - phase_x) + y*math.tanh(2.0*math.pi*frequency*t/H_COL - phase_y));
    
    
    
def color_function(color_algo, R, G, B, i, j, H_ROW, H_COL):
    """This changes the color"""

    if color_algo == "Ryan":
        # My color algo
        red = R*(1-((i)/resolution))
        green = G*(1-((i)/resolution))
        blue = (1.0 + i/2)
        return red, green, blue;
    elif color_algo == "Mr.Lin":
        # Mr. Lin's Colors
        red = (H_ROW - j)/20
        green = (H_COL - j)/30
        blue = (1.0 + i/23.0)
        return red, green, blue;

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
    r_parameter = '(cos,sin)',
    color_algo = "Ryan"
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

                # Color Function
                red, green, blue = color_function(color_algo, R, G, B, i, j, H_ROW, H_COL)
                # Write into file
                out_file.write(f"{int(hough[i][j]*(red))} {int(hough[i][j]*(green))} {int(hough[i][j]*(blue))} ")


def display():
    """This displays the hough art"""
    parameter = f'Parameters of: {amplitude}, {frequency}, {phase_x}, {phase_y}, {color_algo}, {drawing_selection}, {r_parameter}'

    # Save Image
    img = imread("hough_art.ppm")
    img = cvtColor(img,COLOR_BGR2RGB)
    imshow(img)
    axis('off')
    title(f'{parameter}')
    savefig('hough_art.jpg', dpi=500)

    # Display
    st.image('hough_art.jpg', caption="Hough Art!!!", output_format="JPEG")

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

color_algo = st.sidebar.selectbox(
    'Color Algo:',
    ('Mr.Lin', 'Ryan'),
    help="This changes how the color is distributed throughout the graph"
)

# Color tuning
color = st.sidebar.color_picker('Pick A Color', value='#50AADE', help="NOTE: Only compatable with Ryan's algo").lstrip('#')
st.write('The current color is', '#' + color)
color_RGB = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

# Function Tuning
st.sidebar.caption("You can tune the functions!")
drawing_selection = st.sidebar.selectbox(
    'Drawing Selection:',
    ('drawing1.ppm', 'drawing2.ppm', 'drawing3.ppm', 'drawing4.ppm', 'drawing5.ppm'),
    help="This changes the input drawing that will be hough transformed"
)
r_parameter = st.sidebar.selectbox(
    'Radius Function:',
    ('(cos,sin)', '(sin,tan)', '(tan,cos)',
    '(cos,sinh)', '(tan,sinh)', '(sin,sinh)',
    '(cos,cosh)', '(tan,cosh)', '(sin,cosh)',
    '(cos,tanh)', '(tan,tanh)', '(sin,tahh)'),
    help="This changes how the radius calculated"
)

# Upload File
st.sidebar.header("Still want to customize more?")
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
    hough(img_inp=img_inp, amplitude=amplitude, frequency=frequency, phase_x=phase_x, phase_y=phase_y, resolution=resolution, r_parameter=r_parameter, RGB=color_RGB, color_algo=color_algo)

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
    hough(img_inp=img_inp, amplitude=amplitude, frequency=frequency, phase_x=phase_x, phase_y=phase_y, resolution=resolution, r_parameter=r_parameter, RGB=color_RGB, color_algo=color_algo)

    # Display Hough
    display()

    st.header("Upload drawing to make it even more unique!")







