import curses
def print_menu(stdscr, selected_row_idx, menu_options, start_y):
    """Helper function to draw the menu items."""
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    if "New Game" in menu_options:
        x_center = w // 2 - len("Project David") // 2
        y_position = 4
        stdscr.addstr(y_position, x_center, "Project David", curses.A_BOLD)
    for idx, option in enumerate(menu_options):
        x = w // 2 - len(option) // 2
        y = start_y + idx
        
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, option)
            stdscr.attroff(curses.A_REVERSE)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, option)

    stdscr.refresh()