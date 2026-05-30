import streamlit as st
from PIL import Image, ImageDraw
import io
import urllib.request
from datetime import datetime
import pytz

# --- ตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="BEJIN Studio: Custom shirt Studio", page_icon="👕", layout="wide")

# --- Initialize Global Session States ---
if 'cart' not in st.session_state:
    st.session_state['cart'] = []
if 'current_step' not in st.session_state:
    st.session_state['current_step'] = "Welcome Studio ✨"

# --- Helper function ---
@st.cache_data(show_spinner=False)
def fetch_emoji_image(emoji_name):
    emoji_urls = {
        "Cute Bear 🧸": "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f43b.png",
        "Pink Bow 🎀": "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f380.png",
        "Red Heart ❤️": "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/2764.png",
        "Retro Star 🌟": "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f31f.png",
        "Fresh Clover 🍀": "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f340.png",
        "Cherries 🍒": "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f352.png",
        "Sparkles ✨": "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/2728.png"
    }
    url = emoji_urls.get(emoji_name)
    if url:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=3) as response:
                return Image.open(io.BytesIO(response.read())).convert("RGBA")
        except:
            return None
    return None

# --- Mockup Engine ---
def create_shirt_mockup(color_name, text, text_size, uploaded_file, img_size, emoji, pos="Center"):
    color_map = {"Classic White ⚪": (255, 255, 255), "Pitch Black ⚫": (30, 30, 30), "Navy Blue 🔵": (20, 40, 80), "Deep Green 🟢": (20, 60, 40)}
    bg_color = color_map.get(color_name, (255, 255, 255))
    text_color = (255, 255, 255) if color_name not in ["Classic White ⚪"] else (50, 50, 50)
    img = Image.new('RGB', (400, 400), (243, 242, 238))
    draw = ImageDraw.Draw(img)
    draw.ellipse([160, 30, 240, 70], fill=(225, 225, 225), outline=(210, 210, 210))
    shirt_points = [(160, 50), (240, 50), (330, 90), (350, 150), (290, 150), (280, 360), (120, 360), (110, 150), (110, 150), (50, 150), (70, 90)]
    draw.polygon(shirt_points, fill=bg_color, outline=(200, 200, 200), width=1)
    draw.line([(120, 360), (280, 360)], fill=(210, 210, 210), width=2)
    x_pos = 145 if pos == "Left" else (255 if pos == "Right" else 200)
    if emoji and emoji != "None":
        e_img = fetch_emoji_image(emoji)
        if e_img:
            e_img.thumbnail((26, 26))
            img.paste(e_img, (x_pos - e_img.width//2, 105 - e_img.height//2), e_img)
    if text:
        draw.text((x_pos, 125), text, fill=text_color, anchor="mm", font_size=int(text_size))
    if uploaded_file:
        try:
            file_bytes = uploaded_file if isinstance(uploaded_file, bytes) else uploaded_file.read()
            u_img = Image.open(io.BytesIO(file_bytes)).convert("RGBA")
            u_img.thumbnail((int(img_size), int(img_size)))
            img.paste(u_img, (x_pos - u_img.width//2, 160 - u_img.height//2), u_img)
        except: pass
    return img

def calculate_item_price(item):
    price = 25000
    if item.get('f_emoji') != "None": price += 2000
    if item.get('f_img') is not None: price += 5000
    if item.get('b_emoji') != "None": price += 2000
    if item.get('b_img') is not None: price += 5000
    return price

def generate_jpeg_receipt(cart):
    total_qty = len(cart)
    receipt = Image.new('RGB', (1000, 700 + (total_qty * 160)), (250, 249, 246))
    draw = ImageDraw.Draw(receipt)
    draw.rectangle([40, 40, 960, receipt.height - 40], outline=(47, 62, 43), width=3)
    draw.text((500, 110), "BEJIN.studio", fill=(47, 62, 43), anchor="mm", font_size=46)
    y_pos = 240
    subtotal = 0
    for i, item in enumerate(cart):
        thumb = create_shirt_mockup(item['color'], item['f_txt'], item['f_txt_size'], item['f_img'], item['f_img_size'], item['f_emoji'], item['f_pos']).resize((110, 110))
        receipt.paste(thumb, (90, y_pos))
        price = calculate_item_price(item)
        subtotal += price
        draw.text((230, y_pos + 10), f"Item #{i+1}", fill=(47, 62, 43), font_size=26)
        draw.text((910, y_pos + 40), f"{price:,} KRW", fill=(47, 62, 43), anchor="ra", font_size=26)
        y_pos += 140
    draw.text((100, y_pos + 40), "TOTAL PAYMENT", fill=(47, 62, 43), font_size=24)
    draw.text((900, y_pos + 40), f"{subtotal:,} KRW", fill=(47, 62, 43), anchor="ra", font_size=28)
    return receipt

def go_to_step(step_name):
    st.session_state['current_step'] = step_name
    st.rerun()

# --- เมนูหลัก ---
options = ["Welcome Studio ✨", "Step 1: Design Workshop", "Step 2: Finalize Order"]
sidebar_selection = st.sidebar.radio("Navigation", options, index=options.index(st.session_state['current_step']))
if sidebar_selection != st.session_state['current_step']:
    go_to_step(sidebar_selection)

if st.session_state['current_step'] == "Welcome Studio ✨":
    st.markdown("<h1>[BEJIN] Your style. Your rules.</h1>", unsafe_allow_html=True)
    if st.button("🛍️ START DESIGNING ➔", type="primary"): go_to_step("Step 1: Design Workshop")

elif st.session_state['current_step'] == "Step 1: Design Workshop":
    color = st.selectbox("Shirt Color", ["Classic White ⚪", "Pitch Black ⚫", "Navy Blue 🔵", "Deep Green 🟢"])
    f_txt = st.text_input("Front Text")
    f_txt_size = st.slider("Text Size", 12, 36, 20)
    f_img = st.file_uploader("Logo", type=['png','jpg'])
    if st.button("🛒 Add to Cart"):
        st.session_state['cart'].append({"color": color, "size": "M", "f_txt": f_txt, "f_txt_size": f_txt_size, "f_img": f_img.getvalue() if f_img else None, "f_img_size": 45, "f_pos": "Center", "f_emoji": "None", "b_txt": "", "b_txt_size": 20, "b_img": None, "b_img_size": 45, "b_pos": "Center", "b_emoji": "None"})
    if st.button("✅ Checkout"): go_to_step("Step 2: Finalize Order")

elif st.session_state['current_step'] == "Step 2: Finalize Order":
    if st.session_state['cart']:
        st.image(generate_jpeg_receipt(st.session_state['cart']))
    if st.button("🔄 New Session"):
        st.session_state['cart'] = []
        go_to_step("Welcome Studio ✨")
