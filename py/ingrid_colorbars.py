from matplotlib import colors as colors
import matplotlib.pyplot as plt

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

cmap_data = [(0, 'navy'),(0.1, 'blue'),(0.2,'DeepSkyBlue'),
             (0.3,'turquoise'),(0.4,'PaleTurquoise'),(0.45,'moccasin'),
             (0.55,'moccasin'),(.6,'yellow'),(.7,'DarkOrange'),
             (.8,'red'),(1.0,'DarkRed')]
cmap = colors.LinearSegmentedColormap.from_list('correlationcolorscale', cmap_data)
plt.register_cmap('correlationcolorscale', cmap)


cmap_data = [(0, rgb2hex(130, 90, 80)), 
             (0.0625, rgb2hex(150, 110, 100)), 
             (0.125, rgb2hex(170, 130, 120)), 
             (0.1875, rgb2hex(180, 140, 130)), 
             (0.25, rgb2hex(190, 150, 140)), 
             (0.3125, rgb2hex(200, 160, 150)), 
             (0.375, rgb2hex(220, 185, 175)), 
             (0.475, rgb2hex(240, 215, 210)), 
             (0.495, rgb2hex(255, 255, 255)), 
             (0.505, rgb2hex(255, 255, 255)), 
             (0.525, rgb2hex(210, 255, 215)), 
             (0.5625, rgb2hex(150, 230, 155)), 
             (0.625, rgb2hex(110, 210, 115)), 
             (0.6875, rgb2hex(45, 180, 50)), 
             (0.75, rgb2hex(20, 170, 25)), 
             (0.8125, rgb2hex(10, 150, 15)), 
             (0.875, rgb2hex(0, 130, 5)), 
             (1,rgb2hex(0, 110, 4))]
cmap = colors.LinearSegmentedColormap.from_list('prcp_anomaly', cmap_data)
plt.register_cmap('prcp_anomaly', cmap)
