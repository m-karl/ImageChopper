import math
from PIL import Image
import PySimpleGUI as sg

# IMAGE FUNCTION
def imagechop(imagepath, numchops: int): #saves image crops in list, returns list of Image
    image_list = []
    numchops = int(math.sqrt(int(numchops)))
    fullimage = Image.open(imagepath)
    chopw = fullimage.width/numchops
    choph = fullimage.height/numchops

    for i in range(numchops): # nested loop for cropping
        for j in range(numchops): 
            top = i*choph
            left = j*chopw 
            chop = fullimage.crop((left, top, left+chopw-1, top+choph-1))
            image_list.append(chop)
    return image_list

# PySimpleGUI
layout = [
    [sg.Text("Select Image")],
    [sg.Input(key='-IPATH-'), sg.FileBrowse(target='-IPATH-')],
    [sg.Push(), sg.Text("Number of chops"), sg.Combo([4, 9, 16], default_value=4, key="-NUMCHOPS-", readonly=True), sg.Push()],
    [sg.Push(), sg.Button("Chop", key='-CHOP-'), sg.Button("Cancel"), sg.Push()]
]
layout_popup = [
    [sg.Text("Success! Check the \"chops\" folder")],
    [sg.Push(), sg.Button("OK"), sg.Push()]
]
layout_popup2 = [
    [sg.Text("Wrong file type, choose .png or .jpg")],
    [sg.Push(), sg.Button("OK"), sg.Push()]
]
window = sg.Window("Image Chopper", layout)


# GUI logic loop
while True:
    event, values = window.read()
    # If Chop button is pressed
    if event == "-CHOP-":
        # Check if file is .png or .jpg
        if values["-IPATH-"][-3:].lower() == 'png' or values["-IPATH-"][-3:].lower() == 'jpg':
            imglist = imagechop(values["-IPATH-"], values["-NUMCHOPS-"])
            for i in range(len(imglist)):
                imglist[i].save("chops/"+"chop"+str(i)+values["-IPATH-"][-4:])
            window_popup = sg.Window("Image Chopper", layout_popup)
            while True:
                event2, values2 = window_popup.read()
                if event2 == "OK":
                    break
            break
        else:
            window_popup = sg.Window("Image Chopper", layout_popup2)
            while True:
                event2, values2 = window_popup.read()
                if event2 == "OK":
                    break
            break
    # End program if user closes window or presses Cancel
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    
window.close()
