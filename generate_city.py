import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

os.makedirs('public', exist_ok=True)

def draw_stylized_car(ax, x, y, color):
    # Body
    body = FancyBboxPatch((x, y + 0.3), 2.8, 0.6,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          ec=None, fc=color, alpha=1.0, mutation_scale=1)
    ax.add_patch(body)
    # Cabin
    cabin = FancyBboxPatch((x + 0.6, y + 0.9), 1.4, 0.45,
                           boxstyle="round,pad=0.1,rounding_size=0.2",
                           ec=None, fc=color, alpha=1.0, mutation_scale=1)
    ax.add_patch(cabin)
    # Wheels
    wheel_r = 0.25
    ax.add_patch(patches.Circle((x + 0.6, y + 0.25), wheel_r, color=color))
    ax.add_patch(patches.Circle((x + 2.2, y + 0.25), wheel_r, color=color))

def draw_airplane(ax, x, y, color, contrail_color):
    """Draws a stylized airplane flying left-to-right with a SINGLE clean contrail."""
    # Contrail (One single fade line, cleaner than two)
    trail_length = 35
    trail = patches.Rectangle((x - trail_length, y + 0.2), trail_length, 0.3, 
                              color=contrail_color, alpha=0.15, lw=0) # Very subtle alpha
    ax.add_patch(trail)

    # Fuselage
    fuselage = FancyBboxPatch((x, y), 3.5, 0.7,
                              boxstyle="round,pad=0.1,rounding_size=0.3",
                              ec=None, fc=color, alpha=1.0, mutation_scale=1)
    ax.add_patch(fuselage)

    # Tail Fin
    tail_wing = patches.Polygon([(x + 0.2, y + 0.5), (x + 0.8, y + 1.5), (x + 1.2, y + 0.5)],
                                color=color, lw=0)
    ax.add_patch(tail_wing)

    # Main Wing
    main_wing = patches.Polygon([(x + 1.5, y + 0.3), (x + 2.2, y - 0.5), (x + 3.0, y + 0.3)],
                                color=color, alpha=0.9, lw=0)
    ax.add_patch(main_wing)


def draw_tiered_building(ax, x, w, h, ground, color, light_color, is_foreground=True):
    alpha = 0.8 if is_foreground else 0.4
    ax.add_patch(patches.Rectangle((x, ground), w, h, color=color, alpha=alpha, lw=0))
    
    if is_foreground and h > 8 and w > 2:
        win_cols = int(w // 0.6); win_rows = int(h // 1.2)
        for r in range(win_rows):
            for c in range(win_cols):
                if np.random.rand() > 0.3:
                    wx = x + 0.2 + (c * 0.6); wy = ground + 1 + (r * 1.2)
                    if wy < ground + h - 1:
                        ax.add_patch(patches.Rectangle((wx, wy), 0.3, 0.7, color=light_color, alpha=0.6, lw=0))

    if h > 15:
        tier2_w = w * 0.6; tier2_h = h * 0.3; tier2_x = x + (w - tier2_w) / 2
        ax.add_patch(patches.Rectangle((tier2_x, ground + h), tier2_w, tier2_h, color=color, alpha=alpha, lw=0))
        if is_foreground:
            mid = tier2_x + tier2_w/2
            ax.plot([mid, mid], [ground + h + tier2_h, ground + h + tier2_h + np.random.uniform(2, 6)], color=color, lw=1.2)

def draw_cloud(ax, x, y, color):
    # Smaller, simpler clouds
    size = np.random.uniform(1.2, 2.0)
    ax.add_patch(patches.Circle((x, y), size, color=color, alpha=0.3, lw=0))
    ax.add_patch(patches.Circle((x + size*0.8, y + size*0.2), size*0.8, color=color, alpha=0.3, lw=0))

def generate_cityscape(filename, primary_color, secondary_color, tree_color, window_light_color, street_color, sky_color, is_night):
    print(f"Painting Architect V11 (Clean Sky) - {filename}...")
    fig, ax = plt.subplots(figsize=(24, 4))
    ax.set_xlim(-5, 105)
    ax.set_ylim(0, 40)
    ax.axis('off')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ground_level = 4 

    # --- LAYER 0: THE SKY (Simplified) ---
    if is_night:
        ax.add_patch(patches.Circle((88, 34), 2.2, color='#ffffff', alpha=0.9)) # Moon
    else:
        ax.add_patch(patches.Circle((12, 32), 3.0, color='#fcd34d', alpha=0.5)) # Sun

    # Clouds: ONLY 2 now, placed at edges so they don't crowd the plane
    draw_cloud(ax, 5, 30, sky_color)  # Far left
    draw_cloud(ax, 90, 28, sky_color) # Far right

    # Airplane: Centered in the clear air
    plane_color = '#e4e4e7' if not is_night else '#94a3b8'
    contrail_color = '#ffffff'
    draw_airplane(ax, 50, 35, plane_color, contrail_color)

    # --- LAYER 1: DISTANT SKYLINE ---
    dx = -5
    while dx < 105:
        w = np.random.uniform(3, 8); h = np.random.uniform(10, 30)
        draw_tiered_building(ax, dx, w, h, ground_level, primary_color, None, is_foreground=False)
        dx += w - 0.5

    # --- LAYER 2: FOREGROUND BUILDINGS ---
    current_x = -2; num_buildings = 45
    for i in range(num_buildings):
        w = np.random.uniform(2, 5.5); h = np.random.uniform(8, 25)
        if current_x + w > 105: break
        draw_tiered_building(ax, current_x, w, h, ground_level, primary_color, window_light_color, is_foreground=True)
        current_x += w + np.random.uniform(0.1, 0.5)

    # --- LAYER 3: STREET LIFE ---
    ax.add_patch(patches.Rectangle((-10, 0), 120, ground_level, color=street_color, alpha=1.0, lw=0))
    ax.plot([-10, 110], [ground_level, ground_level], color=street_color, lw=2)
    ax.plot([-10, 110], [ground_level/2, ground_level/2], color=primary_color, lw=1.5, ls='--')

    for x in range(2, 108, 14): 
        ax.plot([x, x], [ground_level, ground_level + 8], color=street_color, lw=1.5, alpha=1.0)
        ax.add_patch(patches.Circle((x + 0.8, ground_level + 8), 0.8, color=street_color, alpha=1.0, lw=0))

    car_x_positions = np.cumsum(np.random.uniform(5, 12, 10))
    for cx in car_x_positions:
        if cx < 100: draw_stylized_car(ax, cx, ground_level, street_color)

    tree_positions = np.sort(np.random.uniform(0, 100, 25))
    for tx in tree_positions:
        th = np.random.uniform(3, 7)
        ax.add_patch(patches.Rectangle((tx, ground_level - 0.5), 0.4, th*0.6, color=street_color))
        ax.add_patch(patches.Circle((tx + 0.2, ground_level + th*0.6), th*0.35, color=tree_color, alpha=0.95))
        ax.add_patch(patches.Circle((tx - 0.3, ground_level + th*0.5), th*0.25, color=tree_color, alpha=0.95))
        ax.add_patch(patches.Circle((tx + 0.6, ground_level + th*0.5), th*0.25, color=tree_color, alpha=0.95))

    plt.savefig(filename, bbox_inches='tight', pad_inches=0, transparent=True, dpi=180)
    plt.close(fig)
    print(f"Success: {filename}")

if __name__ == "__main__":
    generate_cityscape('public/city-light.png', 
                       primary_color='#71717a', secondary_color='#fafafa', 
                       tree_color='#4a6741', window_light_color='#f4f4f5',
                       street_color='#27272a', sky_color='#e4e4e7', is_night=False)
    generate_cityscape('public/city-dark.png', 
                       primary_color='#475569', secondary_color='#fef08a', 
                       tree_color='#a78bfa', window_light_color='#fef08a',
                       street_color='#e2e8f0', sky_color='#3f3f46', is_night=True)