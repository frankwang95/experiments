import plotting_standards.colors as colors

def set_layout(layout):
    layout['plot_bgcolor'] = "#FFFFFF"

    for key in layout:
        if 'xaxis' in key or 'yaxis' in key:
            layout[key]['zeroline'] = False
            layout[key]['color'] = colors.neutral_1
            layout[key]['title']['font'] = dict(family='sans serif', size=10, color=colors.neutral_1)
            layout[key]['gridcolor'] = colors.neutral_2

    for ann in layout['annotations']:
        ann['font'] = dict(family='sans serif', size=14, color=colors.neutral_1)
