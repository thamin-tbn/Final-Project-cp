from PIL import Image
import numpy as np

# تابع اعمال فیلتر بر روی تصویر

def apply_convolution(img:np.array, kernel:np.array):
    
    #محاسبه ابعاد و تعداد کانال های تصویر
    height,width,c =img.shape[0],img.shape[1],img.shape[2]
    
    # محاسبه ابعاد فیلتر
    kernel_height,kernel_width = kernel.shape[0],kernel.shape[1]
    
# انتخاب بخشی از تصویر که امکان اعمال کانوولوشن در آن وجود دارد(کل تصویر به جز مرز ها)
    new_img = np.zeros((height-kernel_height+1,width-kernel_width+1,3)) 
    
# انجام کانوولوشن بر روی بخش انتخاب شده
    for i in range(kernel_height//2, height-kernel_height//2-1):
        for j in range(kernel_width//2, width-kernel_width//2-1):

            window = img[i-kernel_height//2 : i+kernel_height//2+1,j-kernel_width//2 : j+kernel_width//2+1]
            
            new_img[i, j, 0] = int((window[:,:,0] * kernel).sum())
            new_img[i, j, 1] = int((window[:,:,1] * kernel).sum())
            new_img[i, j, 2] = int((window[:,:,2] * kernel).sum())
      
    # محدود کردن مقادیر به عدد 255
    new_img = np.clip(new_img, 0, 255)
    return new_img.astype(np.uint8)

if __name__ == "__main__":

# فیلتر تشخیص لبه
    kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
    
    img = Image.open('lena.jpg')
    or_img = np.asarray(img)
    
    new_img = apply_convolution(or_img, kernel)

   
    sImg = Image.fromarray(new_img)
    sImg.show() 