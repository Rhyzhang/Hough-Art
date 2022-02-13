import math
from random import randrange

import cv2
import matplotlib.pyplot as plt
import streamlit as st


@st.cache(suppress_st_warning=True)
def hough(img_inp,  amplitude = 2.5, frequency = 1.0, phase_x = 0.0, phase_y = 0.0): 
    """This is the hough art function"""
    # Program Constants
    file_type = 'P3'
    ppm_color = 255
    COL = 300
    ROW = 200
    H_COL = 800
    H_ROW = 800

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
                out_file.write(f"{int(hough[i][j]*(1.0 + i/23.0))} {int(hough[i][j]*(H_COL - j)/20)} {int(hough[i][j]*(H_ROW - j)/30)} ")


# --- Main -------------------------------------------------------------------------

# Manipluatable Variables
ppm_upload = st.sidebar.file_uploader("Choose a PPM file", accept_multiple_files=False)

st.sidebar.header("Random")
if st.sidebar.button('Random'):
    # Random button to randomly generate
    amplitude = st.sidebar.slider("amplitude", value=randrange(3, 10))
    frequency = st.sidebar.slider("frequency", value=randrange(0, 10))
    phase_x = st.sidebar.slider("phase_x", value=randrange(0, 10))
    phase_y = st.sidebar.slider("phase_y", value=randrange(0, 10))
else:
    amplitude = st.sidebar.slider("amplitude")
    frequency = st.sidebar.slider("frequency")
    phase_x = st.sidebar.slider("phase_x")
    phase_y = st.sidebar.slider("phase_y")


if ppm_upload is not None:
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
    hough(img_inp=img_inp, amplitude=amplitude, frequency=frequency, phase_x=phase_x, phase_y=phase_y)

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
else:
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
    hough(img_inp=img_inp, amplitude=amplitude, frequency=frequency, phase_x=phase_x, phase_y=phase_y)

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








# Attempts to display ppm on streamlit

    # stringio = StringIO(ppm_upload.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)



    
# import streamlit.components.v1 as components
# components.html(
#     """
#     <head>
#         <meta charset="UTF-8">
#         <style type="text/css">
#             form, div, p {
#                 text-align:center;
#             }
#             div {
#                 margin-top: 5px;
#                 margin-bottom: 5px;
#             }
#             form,div {
#                 margin-left:auto;
#                 margin-right:auto;
#             }
#             #instruct {
#             }
#             #name {
#                 font-size: 1.4em;
#                 font-weight: bold;
#             }
#             #errorDiv {
#                 text-align:center;
#             }
#             .error {
#                 display:inline-block;
#                 text-align:left;
#                 margin-left:auto;
#                 margin-right:auto;
#                 font-weight:bold;
#             }
#         </style>
#         <script type="text/javascript">
#             var reloadButton;
#             var canvas;
#             var ctx;

#             function showError(msg) {
#                 var errorDiv = document.getElementById("errorDiv");
#                 errorDiv.innerHTML = '<div class="error">Error: ' + msg + '</div>';
#                 ctx.clearRect(0, 0, canvas.width, canvas.height);
#             }

#             function processPPM(fileContents) {
#                 ctx.clearRect(0, 0, canvas.width, canvas.height);
             
#                 fileContents = fileContents.replace(/^\s+/, '').replace(/\s+$/, '');
#                 var data = fileContents.split(/\s+/);

#                 if (fileContents.substr(0, 2) != 'P3' || data[0] != 'P3') {
#                     showError('File is not a PPM');
#                     return;
#                 } 

#                 var width = data[1];
#                 var height = data[2];
#                 var maxColors = data[3];

#                 if (data[3] != 255) {
#                     showError('MaxColors is not 255');
#                     return;
#                 }

#                 if (data.length != 3 * width * height + 4) {
#                     showError('Not enough pixel data.<br>'
#                               + 'Found: ' + (data.length  -  4) + '<br>'
#                               + 'Expecting: ' + (3 * width * height) + '<br>'
#                               + 'Based on width = ' + width 
#                               + ' and height = ' + height);
#                     return;
#                 }

#                 errorDiv.innerHTML = '';

#                 canvas.width=width; 
#                 canvas.height=height; 

#                 var img = ctx.getImageData(0, 0, width, height);
#                 var pixels = img.data;

#                 var imageIndex = 0;
#                 for (var i = 4; i < data.length; i += 3) {
#                     pixels[imageIndex++] = data[i]; // r
#                     pixels[imageIndex++] = data[i+1]; // g
#                     pixels[imageIndex++] = data[i+2]; // b
#                     pixels[imageIndex++] = 255; // a
#                 }
#                 ctx.putImageData(img, 0, 0);
#                 reloadButton.disabled = false;
#             }

#             function processFiles(files) {
#                 if (! reloadButton) {
#                     reloadButton = document.getElementById("reloadBtn");
#                 }
#                 if (! canvas) {
#                     canvas = document.getElementById("imageCanvas");
#                     ctx = canvas.getContext("2d");
#                 }

#                 reloadButton.disabled = true;

#                 var file = files[0];
#                 var filenameDiv = document.getElementById("filenameDiv");
#                 filenameDiv.innerHTML = "File: " + file.name;

#                 if (file.name.substr(file.name.length-4) != ".ppm") {
#                     showError('file name does not end with ".ppm"');
#                     return
#                 }


#                 var r = new FileReader();

#                 r.onload = function(e) { 
#                     var contents = e.target.result;
#                     processPPM(contents);
#                 } 
#                 r.readAsText(file);

#             }
#         </script>
#     </head>
#     <body>
#         <div id="name">PPM Viewer</div>
#         <div id="instruct">Choose a PPM image to view</div>
#         <form name="fileForm" id="fileForm">
#             <input type="file" name="filedata" id="filedata" onchange="processFiles(this.files);">
#             <br>
#             <button id="reloadBtn" onclick="processFiles(this.form.filedata.files); return false;" disabled>Reload image</button>
#         </form>
#         <div id="filenameDiv"></div>
#         <div id="errorDiv"></div>
#         <div><canvas id="imageCanvas" width="100" height="100"></canvas></div>
#     </body>
#     """
# )
