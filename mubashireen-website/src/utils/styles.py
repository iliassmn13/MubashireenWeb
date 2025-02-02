def get_styles():
    return {
        "background_color": "#f5f5dc",  # beige
        "text_color": "#000000",        # black
        "header_color": "#ffffff",      # white
        "button_color": "#d3d3d3",      # light gray
        "border_color": "#a9a9a9",      # dark gray
        "font_family": "Arial, sans-serif",
        "image_border_radius": "10px",
        "padding": "10px",
        "margin": "10px",
    }

def apply_styles():
    styles = get_styles()
    st.markdown(
        f"""
        <style>
        body {{
            background-color: {styles['background_color']};
            color: {styles['text_color']};
            font-family: {styles['font_family']};
        }}
        .header {{
            background-color: {styles['header_color']};
            padding: {styles['padding']};
            margin: {styles['margin']};
        }}
        .button {{
            background-color: {styles['button_color']};
            border: 1px solid {styles['border_color']};
            border-radius: {styles['image_border_radius']};
            padding: {styles['padding']};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )