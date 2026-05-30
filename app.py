import streamlit as st
from PIL import Image, ImageDraw
import io
import urllib.request
from datetime import datetime
import pytz

st.set_page_config(page_title="BEJIN Studio: Custom shirt Studio", page_icon="👕", layout="wide")

# --- Initialize Global Session States ---
if 'cart' not in st.session_state:
    st.session_state['cart'] = []
if 'current_step' not in st.session_state:
    st.session_state['current_step'] = "Welcome Studio ✨"

# --- Helper function to fetch open-source emoji PNGs safely over HTTP ---
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
    color_map = {
        "Classic White ⚪": (255, 255, 255),
        "Pitch Black ⚫": (30, 30, 30),
        "Navy Blue 🔵": (20, 40, 80),
        "Deep Green 🟢": (20, 60, 40)
    }
    bg_color = color_map.get(color_name, (255, 255, 255))
    text_color = (255, 255, 255) if color_name not in ["Classic White ⚪"] else (50, 50, 50)
    img = Image.new('RGB', (400, 400), (243, 242, 238))
    draw = ImageDraw.Draw(img)
    draw.ellipse([160, 30, 240, 70], fill=(225, 225, 225), outline=(210, 210, 210))
    shirt_points = [(160, 50), (240, 50), (330, 90), (350, 150), (290, 150), (280, 360), (120, 360), (110, 150), (50, 150), (70, 90)]
    draw.polygon(shirt_points, fill=bg_color, outline=(200, 200, 200), width=1)
    draw.line([(120, 360), (280, 360)], fill=(210, 210, 210), width=2)
    x_pos = 200
    if pos == "Left": x_pos = 145
    elif pos == "Right": x_pos = 255
    if emoji and emoji != "None":
        e_img = fetch_emoji_image(emoji)
        if e_img:
            try:
                e_img.thumbnail((26, 26))
                img.paste(e_img, (x_pos - e_img.width//2, 105 - e_img.height//2), e_img)
            except: pass
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
    if item['f_emoji'] != "None": price += 2000
    if item['f_img'] is not None: price += 5000
    if item['b_emoji'] != "None": price += 2000
    if item['b_img'] is not None: price += 5000
    return price

def generate_jpeg_receipt(cart):
    total_qty = len(cart)
    shipping_fee = 0 if total_qty >= 2 else 5000
    receipt_height = 700 + (total_qty * 160)
    receipt = Image.new('RGB', (1000, receipt_height), (250, 249, 246))
    draw = ImageDraw.Draw(receipt)
    korea_tz = pytz.timezone('Asia/Seoul')
    now = datetime.now(korea_tz)
    order_date = now.strftime("%Y-%m-%d")
    order_time = now.strftime("%H:%M:%S")
    draw.rectangle([40, 40, 960, receipt_height - 40], outline=(47, 62, 43), width=3)
    draw.text((500, 110), "BEJIN.studio", fill=(47, 62, 43), anchor="mm", font_size=46)
    draw.text((500, 165), "Design your own clothing, your own way.", fill=(120, 130, 115), anchor="mm", font_size=20)
    draw.text((500, 200), f"Order Date: {order_date} | Time: {order_time}", fill=(120, 130, 115), anchor="mm", font_size=18)
    y_pos = 240
    subtotal_accum = 0
    for i, item in enumerate(cart):
        draw.line([(80, y_pos), (920, y_pos)], fill=(225, 230, 220), width=1)
        y_pos += 20
        thumb = create_shirt_mockup(item['color'], item['f_txt'], item['f_txt_size'], item['f_img'], item['f_img_size'], item['f_emoji'], item['f_pos']).resize((110, 110))
        draw.rectangle([89, y_pos - 1, 201, y_pos + 111], outline=(210, 215, 205), width=1)
        receipt.paste(thumb, (90, y_pos))
        item_price = calculate_item_price(item)
        subtotal_accum += item_price
        clean_color = item['color'].split()[0]
        draw.text((230, y_pos + 10), f"BEJIN Custom Shirt Order // #0{i+1}", fill=(47, 62, 43), font_size=26)
        draw.text((230, y_pos + 45), f"Size: {item['size']} | Color: {clean_color} | Front Size: {item['f_txt_size']}pt", fill=(120, 130, 115), font_size=20)
        draw.text((910, y_pos + 40), f"{item_price:,} KRW", fill=(47, 62, 43), anchor="ra", font_size=26)
        y_pos += 140
    y_pos += 20
    draw.line([(80, y_pos), (920, y_pos)], fill=(47, 62, 43), width=2)
    y_pos += 40
    draw.text((100, y_pos), "Subtotal Amount", fill=(120, 130, 115), font_size=24)
    draw.text((900, y_pos), f"{subtotal_accum:,} KRW", fill=(47, 62, 43), anchor="ra", font_size=24)
    y_pos += 50
    draw.text((100, y_pos), "Shipping Fee", fill=(120, 130, 115), font_size=24)
    draw.text((900, y_pos), "Complimentary" if shipping_fee == 0 else f"{shipping_fee:,} KRW", fill=(47, 62, 43), anchor="ra", font_size=24)
    y_pos += 70
    grand_total = subtotal_accum + shipping_fee
    draw.rectangle([80, y_pos, 920, y_pos + 75], fill=(47, 62, 43))
    draw.text((110, y_pos + 38), "TOTAL PAYMENT", fill=(250, 249, 246), anchor="lm", font_size=24)
    draw.text((890, y_pos + 38), f"{grand_total:,} KRW", fill=(255, 255, 255), anchor="rm", font_size=28)
    return receipt

def go_to_step(step_name):
    st.session_state['current_step'] = step_name
    st.rerun()

# --- Main App Logic ---
options = ["Welcome Studio ✨", "Step 1: Design Workshop", "Step 2: Finalize Order"]
sidebar_selection = st.sidebar.radio("Navigation", options, index=options.index(st.session_state['current_step']))
if sidebar_selection != st.session_state['current_step']:
    go_to_step(sidebar_selection)

if st.session_state['current_step'] == "Welcome Studio ✨":
    st.markdown("""<div style="background-color: #FFFFFF; padding: 40px; border-radius: 20px; border: 1px solid #D1DCB2; margin-bottom: 30px;">
                <h1 style="margin: 0; font-size: 38px; color: #2F3E2B;">[BEJIN] Your style. Your rules.</h1></div>""", unsafe_allow_html=True)
    if st.button("🛍️ START DESIGNING ➔", type="primary", use_container_width=True):
        go_to_step("Step 1: Design Workshop")

elif st.session_state['current_step'] == "Step 1: Design Workshop":
    color = st.selectbox("Shirt Color", ["Classic White ⚪", "Pitch Black ⚫", "Navy Blue 🔵", "Deep Green 🟢"])
    f_pos = st.radio("Alignment", ["Left", "Center", "Right"], horizontal=True)
    f_emoji = st.selectbox("Emoji", ["None", "Cute Bear 🧸", "Pink Bow 🎀", "Red Heart ❤️"])
    f_txt = st.text_input("Text")
    f_txt_size = st.slider("Text Size", 12, 36, 20)
    f_img = st.file_uploader("Logo", type=['png','jpg'])
    f_img_size = st.slider("Logo Size", 20, 100, 45)
    
    if st.button("🛒 Add to Cart"):
        current_item = {"color": color, "size": "M", "f_txt": f_txt, "f_txt_size": f_txt_size, 
                        "f_img": f_img.getvalue() if f_img else None, "f_img_size": f_img_size, 
                        "f_pos": f_pos, "f_emoji": f_emoji, "b_txt": "", "b_txt_size": 20, 
                        "b_img": None, "b_img_size": 45, "b_pos": "Center", "b_emoji": "None"}
        st.session_state['cart'].append(current_item)
        st.success("Added!")

elif st.session_state['current_step'] == "Step 2: Finalize Order":
    st.header("🧾 Receipt")
    final_receipt = generate_jpeg_receipt(st.session_state['cart'])
    st.image(final_receipt)
