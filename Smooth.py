import numpy as np
from matplotlib.colors import rgb2hex, hex2color
import os

def hex_to_rgb(hex_color):
    return np.array(hex2color(hex_color))

def rgb_to_hex(rgb_color):
    return rgb2hex(rgb_color)

def interpolate_color(color1, color2, t):
    return color1 * (1 - t) + color2 * t

def smooth_color_transition(color1, color2, num_steps=100): # Change num_steps number to how many lines you want (higher = smoother // too high = chance of repeating colors)
    color1_rgb = hex_to_rgb(color1)
    color2_rgb = hex_to_rgb(color2)
    
    transition_colors = [interpolate_color(color1_rgb, color2_rgb, t) for t in np.linspace(0, 1, num_steps)]
    
    return transition_colors

def save_transition_to_txt(transition_colors, filename):
    output_folder = 'Output'
    os.makedirs(output_folder, exist_ok=True)  # Make an output folder
    
    output_path = os.path.join(output_folder, filename) 
    
    with open(output_path, 'w') as file:
        for color in transition_colors:
            hex_color = rgb_to_hex(color) 
            file.write(hex_color + '\n')

    # Reverse!!!!!!!!
    reversed_colors = transition_colors[::-1]
    
    temp_filename = output_path + '.temp'
    with open(temp_filename, 'w') as temp_file:
        for color in reversed_colors:
            hex_color = rgb_to_hex(color)
            temp_file.write(hex_color + '\n')
    
    # temp file > main file
    with open(temp_filename, 'r') as temp_file:
        with open(output_path, 'a') as file:
            file.write(temp_file.read())
    
    # Banish temp to the shadow realm
    os.remove(temp_filename)

color1 = input("Enter the first hex color: ")
color2 = input("Enter the second hex color: ")
output_file = input("Enter the output file name (with .txt extension): ")

transition_colors = smooth_color_transition(color1, color2)
save_transition_to_txt(transition_colors, output_file)
