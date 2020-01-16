
try:
    from Tkinter import *
    import tkFileDialog as filedialog
except ImportError:
    from tkinter import *
    from tkinter import filedialog
from PIL import Image,ImageTk
import matplotlib.pyplot as plot
import numpy as np
import cv2
import time

root =Tk()
root.withdraw()

root.configure(background='#202835')
#root.iconbitmap('logo.ico')
#root.state('zoomed')
w = 1250
h = 650
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/1.9)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.overrideredirect(1)
root.attributes('-topmost', True)
root.deiconify()

def file_save():
    global enhanced_img
    filename = filedialog.asksaveasfilename(initialdir = "/",title = "Location of output Image",filetypes = [("all files","*.*")])
    print (filename)
    enhanced_img.save(filename)
def show_popup(event):
    global poppup
    popup.entryconfig("Save Image", command=file_save)
    popup.tk_popup(event.x_root, event.y_root)
def display_Target_img(Event):
    global mylabel1,img_list,photo_img_list,file_path1
    try:
        file_path1=filedialog.askopenfilename(initialdir="/", title="Select Target Image", filetypes=[("Image files", "*jpeg; *.jpg; *.png")])
        img_list[0]=Image.open(file_path1).convert('RGB').resize((600,500),Image.BICUBIC)
        img = ImageTk.PhotoImage(img_list[0])
        photo_img_list[0]=img

        mylabel1.grid_forget()
        mylabel1=Label(root,image=photo_img_list[0],bg='#202835')
        mylabel1.bind("<Button-1>",display_Target_img)
        mylabel1.bind("<Button-3>", show_popup)
        mylabel1.grid(column=0,row=0,padx=10) 
    except:
        print('Load error in display_Ref_img module')   
def display_Ref_img(Event):
    global mylabel2,b,img_list,photo_img_list,file_path2
    try:
        file_path2=filedialog.askopenfilename(initialdir="/", title="Select Reference Image", filetypes=[("Image files", "*jpeg; *.jpg; *.png")])
        img_list[1]=Image.open(file_path2).convert('RGB').resize((600,500),Image.BICUBIC)
        img = ImageTk.PhotoImage(img_list[1])
        photo_img_list[1]=img

        mylabel2.grid_forget()
        mylabel2=Label(root,image=photo_img_list[1],bg='#202835')
        mylabel2.bind("<Button-1>",display_Ref_img)
        mylabel2.bind("<Button-3>", show_popup)
        mylabel2.grid(column=1,row=0,padx=10)
        b.config(state = ACTIVE)
    except:
        print('Load error in display_Ref_img module')
def flip_Img1_l (Event,num):
    global mylabel1,img_label1,photo_img_list,img_list,left

    photo_img_list[left] = ImageTk.PhotoImage(img_list[num].resize((600,500),Image.BICUBIC))
    photo_img_list[num] = ImageTk.PhotoImage(img_list[left].resize((50,50),Image.BICUBIC))
    
    temp=img_list[num]
    img_list[num]=img_list[left]
    img_list[left]= temp

    mylabel1.grid_forget()
    mylabel1=Label(root,image=photo_img_list[left],bg='#202835')
    mylabel1.bind("<Button-1>",display_Target_img)
    mylabel1.bind('<Button-3>', show_popup)
    mylabel1.grid(column=0,row=0,padx=10)
    img_label1 = Label(myframe,image=photo_img_list[num],bg='#202835',fg='white')
    img_label1.bind("<Button-1>",lambda event, arg=2: flip_Img1_l(event, arg))
    img_label1.bind("<Button-3>",lambda event, arg=2: flip_Img1_r(event, arg))
    img_label1.grid(column=1,row=0,padx=105,pady=1,sticky=N+W)
def flip_Img1_r (Event,num):
    global mylabel2,img_label1,photo_img_list,img_list,right

    photo_img_list[right] = ImageTk.PhotoImage(img_list[num].resize((600,500),Image.BICUBIC))
    photo_img_list[num] = ImageTk.PhotoImage(img_list[right].resize((50,50),Image.BICUBIC))
    
    temp=img_list[num]
    img_list[num]=img_list[right]
    img_list[right]= temp

    mylabel2.grid_forget()
    mylabel2=Label(root,image=photo_img_list[right],bg='#202835')
    mylabel2.bind("<Button-1>",display_Ref_img)
    mylabel2.bind('<Button-3>', show_popup)
    mylabel2.grid(column=1,row=0,padx=10)
    img_label1 = Label(myframe,image=photo_img_list[num],bg='#202835',fg='white')
    img_label1.bind("<Button-3>",lambda event, arg=2: flip_Img1_r(event, arg))
    img_label1.bind("<Button-1>",lambda event, arg=2: flip_Img1_l(event, arg))
    img_label1.grid(column=1,row=0,padx=105,pady=1,sticky=N+W)
def flip_Img2_l (Event,num):
    global mylabel1,img_label2,photo_img_list,img_list,left

    photo_img_list[left] = ImageTk.PhotoImage(img_list[num].resize((600,500),Image.BICUBIC))
    photo_img_list[num] = ImageTk.PhotoImage(img_list[left].resize((50,50),Image.BICUBIC))
    
    temp=img_list[num]
    img_list[num]=img_list[left]
    img_list[left]= temp

    mylabel1.grid_forget()
    mylabel1=Label(root,image=photo_img_list[left],bg='#202835')
    mylabel1.bind("<Button-1>",display_Target_img)
    mylabel1.bind('<Button-3>', show_popup)
    mylabel1.grid(column=0,row=0,padx=10)
    img_label2 = Label(myframe,image=photo_img_list[num],bg='#202835',fg='white')
    img_label2.bind("<Button-1>",lambda event, arg=3: flip_Img2_l(event, arg))
    img_label2.bind("<Button-3>",lambda event, arg=3: flip_Img2_r(event, arg))
    img_label2.grid(column=2,row=0,padx=105,pady=1,sticky=N+W)
def flip_Img2_r (Event,num):
    global mylabel2,img_label2,photo_img_list,img_list,right

    photo_img_list[right] = ImageTk.PhotoImage(img_list[num].resize((600,500),Image.BICUBIC))
    photo_img_list[num] = ImageTk.PhotoImage(img_list[right].resize((50,50),Image.BICUBIC))
    
    temp=img_list[num]
    img_list[num]=img_list[right]
    img_list[right]= temp
    
    mylabel2.grid_forget()
    mylabel2=Label(root,image=photo_img_list[right],bg='#202835')
    mylabel2.bind("<Button-1>",display_Target_img)
    mylabel2.bind('<Button-3>', show_popup)
    mylabel2.grid(column=1,row=0,padx=10)
    img_label2 = Label(myframe,image=photo_img_list[num],bg='#202835',fg='white')
    img_label2.bind("<Button-1>",lambda event, arg=3: flip_Img2_l(event, arg))
    img_label2.bind("<Button-3>",lambda event, arg=3: flip_Img2_r(event, arg))
    img_label2.grid(column=2,row=0,padx=105,pady=1,sticky=N+W)
def flip_Img3_l (Event,num):
    global mylabel1,img_label3,photo_img_list,img_list,left

    photo_img_list[left] = ImageTk.PhotoImage(img_list[num].resize((600,500),Image.BICUBIC))
    photo_img_list[num] = ImageTk.PhotoImage(img_list[left].resize((50,50),Image.BICUBIC))
    
    temp=img_list[num]
    img_list[num]=img_list[left]
    img_list[left]= temp

    mylabel1.grid_forget()
    mylabel1=Label(root,image=photo_img_list[left],bg='#202835')
    mylabel1.bind("<Button-1>",display_Target_img)
    mylabel1.bind('<Button-3>', show_popup)
    mylabel1.grid(column=0,row=0,padx=10)
    img_label3 = Label(myframe,image=photo_img_list[num],bg='#202835',fg='white')
    img_label3.bind("<Button-1>",lambda event, arg=4: flip_Img3_l(event, arg))
    img_label3.bind("<Button-3>",lambda event, arg=4: flip_Img3_r(event, arg))
    img_label3.grid(column=3,row=0,padx=105,pady=1,sticky=N+W)
def flip_Img3_r (Event,num):
    global mylabel2,img_label3,photo_img_list,img_list,right

    photo_img_list[right] = ImageTk.PhotoImage(img_list[num].resize((600,500),Image.BICUBIC))
    photo_img_list[num] = ImageTk.PhotoImage(img_list[right].resize((50,50),Image.BICUBIC))
    
    temp=img_list[num]
    img_list[num]=img_list[right]
    img_list[right]= temp
    
    mylabel2.grid_forget()
    mylabel2=Label(root,image=photo_img_list[right],bg='#202835')
    mylabel2.bind("<Button-1>",display_Target_img)
    mylabel2.bind('<Button-3>', show_popup)
    mylabel2.grid(column=1,row=0,padx=10)
    img_label3 = Label(myframe,image=photo_img_list[num],bg='#202835',fg='white')
    img_label3.bind("<Button-1>",lambda event, arg=4: flip_Img3_l(event, arg))
    img_label3.bind("<Button-3>",lambda event, arg=4: flip_Img3_r(event, arg))
    img_label3.grid(column=3,row=0,padx=105,pady=1,sticky=N+W)
def flip_Img4_l (Event,num):
    global mylabel1,img_label4,photo_img_list,img_list,left

    photo_img_list[left] = ImageTk.PhotoImage(img_list[num].resize((600,500),Image.BICUBIC))
    photo_img_list[num] = ImageTk.PhotoImage(img_list[left].resize((50,50),Image.BICUBIC))
    
    temp=img_list[num]
    img_list[num]=img_list[left]
    img_list[left]= temp

    mylabel1.grid_forget()
    mylabel1=Label(root,image=photo_img_list[left],bg='#202835')
    mylabel1.bind("<Button-1>",display_Target_img)
    mylabel1.bind('<Button-3>', show_popup)
    mylabel1.grid(column=0,row=0,padx=10)
    img_label4 = Label(myframe,image=photo_img_list[num],bg='#202835',fg='white')
    img_label4.bind("<Button-1>",lambda event, arg=5: flip_Img4_l(event, arg))
    img_label4.bind("<Button-3>",lambda event, arg=5: flip_Img4_r(event, arg))
    img_label4.grid(column=4,row=0,padx=105,pady=1,sticky=N+W)
def flip_Img4_r (Event,num):
    global mylabel2,img_label4,photo_img_list,img_list,right

    photo_img_list[right] = ImageTk.PhotoImage(img_list[num].resize((600,500),Image.BICUBIC))
    photo_img_list[num] = ImageTk.PhotoImage(img_list[right].resize((50,50),Image.BICUBIC))
    
    temp=img_list[num]
    img_list[num]=img_list[right]
    img_list[right]= temp
    
    mylabel2.grid_forget()
    mylabel2=Label(root,image=photo_img_list[right],bg='#202835')
    mylabel2.bind("<Button-1>",display_Target_img)
    mylabel2.bind('<Button-3>', show_popup)
    mylabel2.grid(column=1,row=0,padx=10)
    img_label4 = Label(myframe,image=photo_img_list[num],bg='#202835',fg='white')
    img_label4.bind("<Button-1>",lambda event, arg=5: flip_Img4_l(event, arg))
    img_label4.bind("<Button-3>",lambda event, arg=5: flip_Img4_r(event, arg))
    img_label4.grid(column=4,row=0,padx=105,pady=1,sticky=N+W)
def plot_histogram(b1,b2,b3,img_name,index):
    #global img_list,photo_img_list
    fig, ax = plot.subplots(1,3,sharex=True, sharey=True)
    ax[0].hist(b1,bins=256, facecolor='red',label='red band')
    ax[1].hist(b2,bins=256, facecolor='blue',label='blue band')
    ax[2].hist(b3,bins=256, facecolor='green',label='green band')
    plot.title(img_name, size=20)
    ax[0].set_xlabel(xlabel='GREY LEVELS', size=10)
    ax[0].set_ylabel(ylabel='GREY LEVELS', size=10)
    plot.savefig("System_Images/temp.png")
    img = Image.open('System_Images/temp.png','r').convert('RGB')
    return img
def find_nearest_above(my_array, target):
    diff = my_array - target
    mask = np.ma.less_equal(diff, -1)
    if np.all(mask):
        c = np.abs(diff).argmin()
        return c
    masked_diff = np.ma.masked_array(diff, mask)
    return masked_diff.argmin()
def hist_match(original, specified):
    oldshape = original.shape
    original = original.ravel()
    specified = specified.ravel()
    s_values, bin_idx, s_counts = np.unique(original, return_inverse=True,return_counts=True)
    t_values, t_counts = np.unique(specified, return_counts=True)
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]
    sour = np.around(s_quantiles*255)
    temp = np.around(t_quantiles*255)
    b=[]
    for data in sour[:]:
        b.append(find_nearest_above(temp,data))
    b= np.array(b,dtype='uint8')
    return b[bin_idx].reshape(oldshape)
def compute():
    global img_list,enhanced_img,his1,his2,his3

    original = cv2.imread(file_path1)
    specified = cv2.imread(file_path2)
    image_i_data=Image.Image.split(img_list[1])
    image_o_data=Image.Image.split(img_list[0])
    i_b1,i_b2,i_b3 = list(image_i_data[0].getdata()),list(image_i_data[1].getdata()),list(image_i_data[2].getdata())
    o_b1,o_b2,o_b3 = list(image_o_data[0].getdata()),list(image_o_data[1].getdata()),list(image_o_data[2].getdata())
    o_total_pxls   = len(o_b1)
    a = hist_match(original, specified)
    a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(a)
    enhanced_img_data=Image.Image.split(im_pil.resize((600,500),Image.BICUBIC))
    e_b1,e_b2,e_b3 = list(enhanced_img_data[0].getdata()),list(enhanced_img_data[1].getdata()),list(enhanced_img_data[2].getdata())
    his1=plot_histogram(i_b1,i_b2,i_b3,'REFERENCE IMAGE',2)
    his2=plot_histogram(o_b1,o_b2,o_b3,'INPUT IMAGE',3)
    his3=plot_histogram(e_b1,e_b1,e_b1,'ENHANCED IMAGE',4)
    enhanced_img=im_pil
def click_process():
    global img_Label1,img_Label2,img_Label3,img_Label4,b,mylabel1,mylabel2,myframe,img_list,photo_img_list,his1,his2,his3,enhanced_img
    compute()
    time.sleep(5)
    img_list[2]=his2
    img_list[3]=his1
    img_list[4]=his3
    img_list[5]=img_list[1]
    img_list[1]=enhanced_img
    
    photo_img_list[1]=ImageTk.PhotoImage(img_list[1].resize((600,500),Image.BICUBIC))
    photo_img_list[2]=ImageTk.PhotoImage(img_list[2].resize((50,50),Image.BICUBIC))
    photo_img_list[3]=ImageTk.PhotoImage(img_list[3].resize((50,50),Image.BICUBIC))
    photo_img_list[4]=ImageTk.PhotoImage(img_list[4].resize((50,50),Image.BICUBIC))
    photo_img_list[5]=ImageTk.PhotoImage(img_list[5].resize((50,50),Image.BICUBIC))
    
    mylabel2.grid_forget()
    mylabel2=Label(root,image=photo_img_list[1],bg='#202835')
    mylabel2.bind("<Button-1>",display_Ref_img)
    mylabel2.bind("<Button-3>", show_popup)
    
    img_label1 = Label(myframe,image=photo_img_list[2],bg='#202835',fg='white')
    img_label2 = Label(myframe,image=photo_img_list[3],bg='#202835',fg='white')
    img_label3 = Label(myframe,image=photo_img_list[4],bg='#202835',fg='white')
    img_label4 = Label(myframe,image=photo_img_list[5],bg='#202835',fg='white')

    img_label1.bind("<Button-1>",lambda event, arg=2: flip_Img1_l(event, arg))
    img_label1.bind("<Button-3>",lambda event, arg=2: flip_Img1_r(event, arg))
    
    img_label2.bind("<Button-1>",lambda event, arg=3: flip_Img2_l(event, arg))
    img_label2.bind("<Button-3>",lambda event, arg=3: flip_Img2_r(event, arg))

    img_label3.bind("<Button-1>",lambda event, arg=4: flip_Img3_l(event, arg))
    img_label3.bind("<Button-3>",lambda event, arg=4: flip_Img3_r(event, arg))
    
    img_label4.bind("<Button-1>",lambda event, arg=5: flip_Img4_l(event, arg))
    img_label4.bind("<Button-3>",lambda event, arg=5: flip_Img4_r(event, arg))

    b.grid(column=0,row=0,padx=10,pady=10,sticky=N+W)

    img_label1.grid(column=1,row=0,padx=105,pady=1,sticky=N+W)
    img_label2.grid(column=2,row=0,padx=105,pady=1,sticky=N+W)
    img_label3.grid(column=3,row=0,padx=105,pady=1,sticky=N+W)
    img_label4.grid(column=4,row=0,padx=105,pady=1,sticky=N+W)


    mylabel1.grid(column=0,row=0,padx=10)
    mylabel2.grid(column=1,row=0,padx=10)
    myframe.grid(columnspan=2,padx=10,sticky=W+E)
def refresh_all():
    global icon,img_list,photo_img_list,enhanced_img,his1,his2,his3,mylabel1,mylabel2,myframe,b,img_label1,img_label2,img_label3,img_label4
    img_list = [Image.open('System_Images/sample1.png').resize((600,500),Image.BICUBIC),
                Image.open('System_Images/sample2.png').resize((600,500),Image.BICUBIC),
                Image.open('System_Images/c.png').resize((50,50),Image.BICUBIC),
                Image.open('System_Images/s.png').resize((50,50),Image.BICUBIC),
                Image.open('System_Images/R.png').resize((50,50),Image.BICUBIC),
                Image.open('System_Images/e.png').resize((50,50),Image.BICUBIC)]
    photo_img_list=[ImageTk.PhotoImage(Image.open('System_Images/sample1.png').resize((600,500),Image.BICUBIC)),
                    ImageTk.PhotoImage(Image.open('System_Images/sample2.png').resize((600,500),Image.BICUBIC)),
                    ImageTk.PhotoImage(Image.open('System_Images/c.png').resize((50,50),Image.BICUBIC)),
                    ImageTk.PhotoImage(Image.open('System_Images/s.png').resize((50,50),Image.BICUBIC)),
                    ImageTk.PhotoImage(Image.open('System_Images/R.png').resize((50,50),Image.BICUBIC)),
                    ImageTk.PhotoImage(Image.open('System_Images/e.png').resize((50,50),Image.BICUBIC))]             
    enhanced_img =Image.open('System_Images/sample1.png').resize((600,500),Image.BICUBIC)
    his1=his2=his3=Image.new(img_list[0].mode,(600,500),'white')
    #Layouts
    img_label1.grid_forget()
    img_label2.grid_forget()
    img_label3.grid_forget()
    img_label4.grid_forget()

    mylabel1=Label(root,image=photo_img_list[0],padx=20,pady=20,bg='#202835')
    mylabel1.bind("<Button-1>",display_Target_img)
    mylabel1.bind('<Button-3>', show_popup)
    mylabel2=Label(root,image=photo_img_list[1],padx=20,pady=20,bg='#202835')
    mylabel2.bind("<Button-1>",display_Ref_img)
    mylabel2.bind('<Button-3>', show_popup)

    mylabel1.grid(row=0,column=0)
    mylabel2.grid(row=0,column=1)

    #myframe=LabelFrame(root,labelanchor='n',text='SIP Project On Histogram Specification(2021 Batch)',bg='#202835',fg='white',height=30,width=1000,padx=10,pady=10,font=("Courier", 20))
    b=Button(myframe,image=icon,bg='#202835',highlightthickness=0,relief='flat',command=click_process)
    b.config(state = DISABLED)
    img_label1 = Label(myframe,image=photo_img_list[2],bg='#202835',fg='white')
    img_label2 = Label(myframe,image=photo_img_list[3],bg='#202835',fg='white')
    img_label3 = Label(myframe,image=photo_img_list[4],bg='#202835',fg='white')
    img_label4 = Label(myframe,image=photo_img_list[5],bg='#202835',fg='white')

    img_label1.bind("<Button-1>",lambda event, arg=2: flip_Img1_l(event, arg))
    img_label1.bind("<Button-3>",lambda event, arg=2: flip_Img1_r(event, arg))
    img_label2.bind("<Button-1>",lambda event, arg=3: flip_Img2_l(event, arg))
    img_label2.bind("<Button-3>",lambda event, arg=3: flip_Img2_r(event, arg))
    img_label3.bind("<Button-1>",lambda event, arg=4: flip_Img3_l(event, arg))
    img_label3.bind("<Button-3>",lambda event, arg=4: flip_Img3_r(event, arg))
    img_label4.bind("<Button-1>",lambda event, arg=5: flip_Img4_l(event, arg))
    img_label4.bind("<Button-3>",lambda event, arg=5: flip_Img4_r(event, arg))

    b.grid(column=0,row=0,padx=10,pady=10,sticky=N+W)
    img_label1.grid(column=1,row=0,padx=105,pady=1,sticky=N+W)
    img_label2.grid(column=2,row=0,padx=105,pady=1,sticky=N+W)
    img_label3.grid(column=3,row=0,padx=105,pady=1,sticky=N+W)
    img_label4.grid(column=4,row=0,padx=105,pady=1,sticky=N+W)

    mylabel1.grid(column=0,row=0,padx=10)
    mylabel2.grid(column=1,row=0,padx=10)
    myframe.grid(columnspan=2,padx=10,sticky=W+E)
# Required data Structures
left=0
right=1
filepath1='Tagret_Image'
filepath2='Referenced_Image'
img_list = [Image.open('System_Images/sample1.png').resize((600,500),Image.BICUBIC),
            Image.open('System_Images/sample2.png').resize((600,500),Image.BICUBIC),
            Image.open('System_Images/c.png').resize((50,50),Image.BICUBIC),
            Image.open('System_Images/s.png').resize((50,50),Image.BICUBIC),
            Image.open('System_Images/R.png').resize((50,50),Image.BICUBIC),
            Image.open('System_Images/e.png').resize((50,50),Image.BICUBIC)]
photo_img_list=[ImageTk.PhotoImage(Image.open('System_Images/sample1.png').resize((600,500),Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open('System_Images/sample2.png').resize((600,500),Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open('System_Images/c.png').resize((50,50),Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open('System_Images/s.png').resize((50,50),Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open('System_Images/R.png').resize((50,50),Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open('System_Images/e.png').resize((50,50),Image.BICUBIC))]             
enhanced_img =Image.open('System_Images/sample1.png').resize((600,500),Image.BICUBIC)
his1=his2=his3=Image.new(img_list[0].mode,(600,500),'white')
# create a toplevel menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
savemenu = Menu(filemenu, tearoff=0)
popup = Menu(root, tearoff=False)
popup.add_command(label="Save Image")
filemenu.add_command(label="Refresh all", command=refresh_all)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Options", menu=filemenu)
root.config(background='#202835',menu=menubar)
#Layouts
mylabel1=Label(root,image=photo_img_list[0],padx=20,pady=20,bg='#202835')
mylabel1.bind("<Button-1>",display_Target_img)
mylabel1.bind('<Button-3>', show_popup)
mylabel2=Label(root,image=photo_img_list[1],padx=20,pady=20,bg='#202835')
mylabel2.bind("<Button-1>",display_Ref_img)
mylabel2.bind('<Button-3>', show_popup)
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=0,column=1)
icon=ImageTk.PhotoImage(Image.open("System_Images/output.png").resize((50,50),Image.BICUBIC))
myframe=LabelFrame(root,labelanchor='n',text='SIP Project On Histogram Specification(2021 Batch)',bg='#202835',fg='white',height=30,width=1000,padx=10,pady=10,font=("Courier", 20))
b=Button(myframe,image=icon,bg='#202835',highlightthickness=0,relief='flat',command=click_process)
b.config(state = DISABLED)
img_label1 = Label(myframe,image=photo_img_list[2],bg='#202835',fg='white')
img_label2 = Label(myframe,image=photo_img_list[3],bg='#202835',fg='white')
img_label3 = Label(myframe,image=photo_img_list[4],bg='#202835',fg='white')
img_label4 = Label(myframe,image=photo_img_list[5],bg='#202835',fg='white')
img_label1.bind("<Button-1>",lambda event, arg=2: flip_Img1_l(event, arg))
img_label1.bind("<Button-3>",lambda event, arg=2: flip_Img1_r(event, arg))
img_label2.bind("<Button-1>",lambda event, arg=3: flip_Img2_l(event, arg))
img_label2.bind("<Button-3>",lambda event, arg=3: flip_Img2_r(event, arg))
img_label3.bind("<Button-1>",lambda event, arg=4: flip_Img3_l(event, arg))
img_label3.bind("<Button-3>",lambda event, arg=4: flip_Img3_r(event, arg))
img_label4.bind("<Button-1>",lambda event, arg=5: flip_Img4_l(event, arg))
img_label4.bind("<Button-3>",lambda event, arg=5: flip_Img4_r(event, arg))
b.grid(column=0,row=0,padx=10,pady=10,sticky=N+W)
img_label1.grid(column=1,row=0,padx=105,pady=1,sticky=N+W)
img_label2.grid(column=2,row=0,padx=105,pady=1,sticky=N+W)
img_label3.grid(column=3,row=0,padx=105,pady=1,sticky=N+W)
img_label4.grid(column=4,row=0,padx=105,pady=1,sticky=N+W)
mylabel1.grid(column=0,row=0,padx=10)
mylabel2.grid(column=1,row=0,padx=10)
myframe.grid(columnspan=2,padx=10,sticky=W+E)
root.mainloop()


