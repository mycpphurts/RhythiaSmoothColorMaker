import numpy as np
from matplotlib.colors import rgb2hex, hex2color
import os
import curses

def hex_to_rgb(hex_color):
    return np.array(hex2color(hex_color))

def rgb_to_hex(rgb_color):
    return rgb2hex(rgb_color)

def interpolate_color(color1, color2, t):
    return color1 * (1 - t) + color2 * t

def smooth_color_transition(colors, num_steps=100):
    all_transition_colors = []
    num_transitions = len(colors) - 1
    steps_per_transition = num_steps // num_transitions
    remainder_steps = num_steps % num_transitions

    for i in range(num_transitions):
        color1_rgb = hex_to_rgb(colors[i])
        color2_rgb = hex_to_rgb(colors[i + 1])
        current_steps = steps_per_transition + (1 if i < remainder_steps else 0)
        transition_colors = [interpolate_color(color1_rgb, color2_rgb, t) for t in np.linspace(0, 1, current_steps, endpoint=False)]
        all_transition_colors.extend(transition_colors)
    all_transition_colors.append(hex_to_rgb(colors[-1]))  # Ensure the last color is included

    return all_transition_colors

def smooth_chroma_transition(num_steps=100):
    chroma_colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#9400D3']
    return smooth_color_transition(chroma_colors, num_steps)

def save_transition_to_txt(transition_colors, filename):
    output_folder = 'Output'
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, filename)

    with open(output_path, 'w') as file:
        for color in transition_colors:
            hex_color = rgb_to_hex(color)
            file.write(hex_color + '\n')

    reversed_colors = transition_colors[::-1]

    temp_filename = output_path + '.temp'
    with open(temp_filename, 'w') as temp_file:
        for color in reversed_colors:
            hex_color = rgb_to_hex(color)
            temp_file.write(hex_color + '\n')

    with open(temp_filename, 'r') as temp_file:
        with open(output_path, 'a') as file:
            file.write(temp_file.read())

    os.remove(temp_filename)

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.refresh()

    menu = ['Smooth Color Generator', 'Smooth Chroma Generator', 'Exit']
    current_row = 0

    while True:
        stdscr.clear()
        for idx, row in enumerate(menu):
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx + 1, 1, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx + 1, 1, row)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                smooth_color_generator(stdscr)
            elif current_row == 1:
                smooth_chroma_generator(stdscr)
            elif current_row == 2:
                break

def smooth_color_generator(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, "Enter hex colors separated by commas (without spaces): ")
    stdscr.refresh()
    curses.echo()
    curses.curs_set(1)
    colors_input = stdscr.getstr(2, 1, 100).decode('utf-8')
    colors = [color.strip() for color in colors_input.split(',')]
    stdscr.addstr(3, 1, "Enter the number of steps: ")
    stdscr.refresh()
    num_steps = int(stdscr.getstr(4, 1, 5).decode('utf-8'))
    stdscr.addstr(5, 1, "Enter the output file name (with .txt extension): ")
    stdscr.refresh()
    output_file = stdscr.getstr(6, 1, 20).decode('utf-8')
    curses.noecho()
    curses.curs_set(0)

    transition_colors = smooth_color_transition(colors, num_steps)
    save_transition_to_txt(transition_colors, output_file)

    stdscr.addstr(8, 1, "File saved successfully. Press any key to return to the main menu.")
    stdscr.refresh()
    stdscr.getch()

def smooth_chroma_generator(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, "Enter the number of steps: ")
    stdscr.refresh()
    curses.echo()
    curses.curs_set(1)
    num_steps = int(stdscr.getstr(2, 1, 5).decode('utf-8'))
    stdscr.addstr(3, 1, "Enter the output file name (with .txt extension): ")
    stdscr.refresh()
    output_file = stdscr.getstr(4, 1, 20).decode('utf-8')
    curses.noecho()
    curses.curs_set(0)

    transition_colors = smooth_chroma_transition(num_steps)
    save_transition_to_txt(transition_colors, output_file)

    stdscr.addstr(6, 1, "File saved successfully. Press any key to return to the main menu.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
