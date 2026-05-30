%%writefile app.py
import streamlit as st
from PIL import Image, ImageDraw
import io
import urllib.request
from datetime import datetime
import pytz

st.set_page_config(page_title="BEJIN Studio: Custon shirt Studio", page_icon="👕", layout="wide")

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

# --- Mockup Engine (Accepts dynamic Text Size and Image Size parameters) ---
def create_shirt_mockup(color_name, text, text_size, uploaded_file, img_size, emoji, pos="Center"):
    color_map = {
        "Classic White ⚪": (255, 255, 255),
        "Pitch Black ⚫": (30, 30, 30),
        "Navy Blue 🔵": (20, 40, 80),
        "Deep Green 🟢": (20, 60, 40)
    }
    bg_color = color_map.get(color_name, (255, 255, 255))
    text_color = (255, 255, 255) if color_name not in ["Classic White ⚪"] else (50, 50, 50)

    img = Image.new('RGB', (400, 400), (243, 242, 238)) # Aesthetic light grid background tint
    draw = ImageDraw.Draw(img)

    # Neckline
    draw.ellipse([160, 30, 240, 70], fill=(225, 225, 225), outline=(210, 210, 210))

    # Balanced Silhouette
    shirt_points = [
        (160, 50), (240, 50),      # Collar
        (330, 90), (350, 150),     # Right Sleeve
        (290, 150), (280, 360),    # Right Torso
        (120, 360), (110, 150),    # Left Torso
        (110, 150), (50, 150),     # Left Sleeve
        (70, 90)                   # Left Shoulder
    ]
    draw.polygon(shirt_points, fill=bg_color, outline=(200, 200, 200), width=1)
    draw.line([(120, 360), (280, 360)], fill=(210, 210, 210), width=2)

    # Horizontal Alignment Logic
    x_pos = 200
    if pos == "Left": x_pos = 145
    elif pos == "Right": x_pos = 255

    # Vertical Layering (Emoji @ 105, Text @ 125, Logo @ 160)
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
            u_img.thumbnail((int(img_size), int(img_size))) # Modified to use dynamic img_size
            img.paste(u_img, (x_pos - u_img.width//2, 160 - u_img.height//2), u_img)
        except: pass

    return img

# --- Dynamic Calculation Engine (Base 25,000 | Emoji +2,000 | Logo +5,000) ---
def calculate_item_price(item):
    price = 25000
    if item['f_emoji'] != "None": price += 2000
    if item['f_img'] is not None: price += 5000
    if item['b_emoji'] != "None": price += 2000
    if item['b_img'] is not None: price += 5000
    return price

# --- Receipt Engine Updated to matching plm. studio color tones ---
def generate_jpeg_receipt(cart):
    total_qty = len(cart)
    shipping_fee = 0 if total_qty >= 2 else 5000

    receipt_height = 700 + (total_qty * 160)
    receipt = Image.new('RGB', (1000, receipt_height), (250, 249, 246)) # Off-white aesthetic cream
    draw = ImageDraw.Draw(receipt)

    korea_tz = pytz.timezone('Asia/Seoul')
    now = datetime.now(korea_tz)
    
    order_date = now.strftime("%Y-%m-%d")
    order_time = now.strftime("%H:%M:%S")

    # Outer Border with Brand Color #2F3E2B (Dark Olive Green)
    draw.rectangle([40, 40, 960, receipt_height - 40], outline=(47, 62, 43), width=3)

    # Header Branding Text
    draw.text((500, 110), "BEJIN.studio", fill=(47, 62, 43), anchor="mm", font_size=46)
    draw.text((500, 165), "Design your own clothing, your own way.", fill=(120, 130, 115), anchor="mm", font_size=20)
    draw.text((500, 110), "BEJIN.studio", fill=(47, 62, 43), anchor="mm", font_size=46)
    draw.text((500, 200), f"Order Date: {order_date}  |  Time: {order_time}", fill=(120, 130, 115), anchor="mm", font_size=18)

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
        draw.text((230, y_pos + 45), f"Size: {item['size']}  |  Color: {clean_color}  |  Front Size: {item['f_txt_size']}pt", fill=(120, 130, 115), font_size=20)
        draw.text((230, y_pos + 75), f"Logo: {'Yes (+5k)' if item['f_img'] else 'No'}  |  Emoji: {'Yes (+2k)' if item['f_emoji']!='None' else 'No'}", fill=(120, 130, 115), font_size=20)

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

    # Total Box matching bottom band style
    draw.rectangle([80, y_pos, 920, y_pos + 75], fill=(47, 62, 43))
    draw.text((110, y_pos + 38), "TOTAL PAYMENT", fill=(250, 249, 246), anchor="lm", font_size=24)
    draw.text((890, y_pos + 38), f"{grand_total:,} KRW", fill=(255, 255, 255), anchor="rm", font_size=28)

    return receipt

def go_to_step(step_name):
    st.session_state['current_step'] = step_name
    st.rerun()

# --- SIDEBAR ROUTING ---
options = ["Welcome Studio ✨", "Step 1: Design Workshop", "Step 2: Finalize Order"]
sidebar_selection = st.sidebar.radio("Navigation", options, index=options.index(st.session_state['current_step']))
if sidebar_selection != st.session_state['current_step']:
    go_to_step(sidebar_selection)

# --- WELCOME PAGE (WITH DYNAMIC PREVIEW GALLERY) ---
if st.session_state['current_step'] == "Welcome Studio ✨":
    # Header Banner Block matching BEJIN studio layout
    st.markdown("""
        <div style="background-color: #FFFFFF; padding: 40px; border-radius: 20px; border: 1px solid #D1DCB2; margin-bottom: 30px;">
            <h1 style="margin: 0; font-size: 38px; color: #2F3E2B;">[BEJIN] Your style. Your rules. Fully customized.</h1>
            <p style="color: #6B7A64; font-size: 18px; margin-top: 10px;">Design your own clothing, your own way.📮</p>
        </div>
    """, unsafe_allow_html=True)

    col_info, col_action = st.columns([1.2, 1])
    with col_info:
        st.markdown("### ✨ STUDIO PROCESS")
        st.write("1. **Design a shirt** with unique color, text size, logo, and tiny emoji motifs.")
        st.write("2. Click **'🛒 Add This Design to Cart'** to lock your creation.")
        st.write("3. Instantly change parameters to design your **second or third shirt** completely from scratch.")
        st.write("4. Finalize to get a receipt.")

        st.markdown("### 💰 ADD ON PRICING")
        st.table({
            "Component Selection": ["Plain Shirt / Pure Text Base", "Emoji Graphic Accent", "Custom Logo Upload Image"],
            "Price Rule (KRW)": ["25,000 KRW", "+ 2,000 KRW", "+ 5,000 KRW"]
        })
        st.info("🔥 **PROMO:** Buy 2 shirts or more to unlock **FREE SHIPPING**!")

    with col_action:
        st.markdown("### 🛒 LIVE CART PREVIEW")

        if not st.session_state['cart']:
            st.info("Your cart is empty. Rendering minimalist default template as inspiration:")
            sample_shirt = create_shirt_mockup("Classic White ⚪", "studio.", 20, None, 45, "None", "Center")
            st.image(sample_shirt, width=280, caption="Sample: Plain White Studio Shirt")
        else:
            st.success(f"You have {len(st.session_state['cart'])} custom shirt(s) ready in your cart!")

            for idx, item in enumerate(st.session_state['cart']):
                with st.expander(f"👕 Shirt #{idx+1} Preview - {item['color'].split()[0]} ({item['size']})", expanded=True):
                    col_p1, col_p2 = st.columns(2)
                    with col_p1:
                        f_img_thumb = create_shirt_mockup(item['color'], item['f_txt'], item['f_txt_size'], item['f_img'], item['f_img_size'], item['f_emoji'], item['f_pos'])
                        st.image(f_img_thumb, caption=f"Front Look (Text: {item['f_txt_size']}pt)", use_container_width=True)
                    with col_p2:
                        b_img_thumb = create_shirt_mockup(item['color'], item['b_txt'], item['b_txt_size'], item['b_img'], item['b_img_size'], item['b_emoji'], item['b_pos'])
                        st.image(b_img_thumb, caption=f"Back Look (Text: {item['b_txt_size']}pt)", use_container_width=True)
                    st.write(f"**Value:** {calculate_item_price(item):,} KRW")

            if st.button("Clear Cart & Reset Previews"):
                st.session_state['cart'] = []
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🛍️ START DESIGNING ➔", type="primary", use_container_width=True):
            go_to_step("Step 1: Design Workshop")

# --- DESIGN WORKSHOP (WITH NEW FONT SIZE SLIDERS) ---
elif st.session_state['current_step'] == "Step 1: Design Workshop":
    st.header(f"🎨 Step 1: Creative Canvas (Current Cart: {len(st.session_state['cart'])} Items)")

    col_basic, col_custom, col_preview = st.columns([1, 1.2, 1.5])

    with col_basic:
        st.markdown("### 1. Apparel Base")
        color = st.selectbox("Shirt Color", ["Classic White ⚪", "Pitch Black ⚫", "Navy Blue 🔵", "Deep Green 🟢"])
        size = st.select_slider("Size Config", ["S", "M", "L", "XL"])

        st.markdown("---")
        st.markdown("### 🛒 Cart Dashboard")
        if not st.session_state['cart']:
            st.caption("No shirts added yet.")
        else:
            for idx, c_item in enumerate(st.session_state['cart']):
                st.caption(f"#{idx+1}: {c_item['color'].split()[0]} ({c_item['size']}) - {calculate_item_price(c_item):,} KRW")
            if st.button("Reset All items", key="reset_workshop"):
                st.session_state['cart'] = []
                st.rerun()

    with col_custom:
        emojis = ["None", "Cute Bear 🧸", "Pink Bow 🎀", "Red Heart ❤️", "Retro Star 🌟", "Fresh Clover 🍀", "Cherries 🍒", "Sparkles ✨"]

        # --- FRONT APP DESIGN CONTROLS ---
        st.markdown("### 2. Front Parameters")
        f_pos = st.radio("Alignment", ["Left", "Center", "Right"], horizontal=True, key='fp')
        f_emoji = st.selectbox("Mini Emoji Accent (+2k)", emojis, key='fe')
        f_txt = st.text_input("Mini Text Graphic (Base)", placeholder="Type minimalist tags...", key='ft')
        f_txt_size = st.slider("Front Text Size (pt)", min_value=12, max_value=36, value=20, step=2, key='fts')
        f_img = st.file_uploader("Logo Upload (+5k)", type=['png','jpg'], key='f')
        f_img_size = st.slider("Front Logo Size (px)", min_value=20, max_value=100, value=45, step=5, key='fis') # New Image Size Slider

        st.markdown("---")

        # --- BACK APP DESIGN CONTROLS ---
        st.markdown("### 3. Back Parameters")
        b_pos = st.radio("Alignment ", ["Left", "Center", "Right"], horizontal=True, key='bp')
        b_emoji = st.selectbox("Mini Emoji Accent (+2k) ", emojis, key='be')
        b_txt = st.text_input("Mini Text Graphic (Base) ", placeholder="Type custom tags...", key='bt')
        b_txt_size = st.slider("Back Text Size (pt)", min_value=12, max_value=36, value=20, step=2, key='bts')
        b_img = st.file_uploader("Logo Upload (+5k) ", type=['png','jpg'], key='b')
        b_img_size = st.slider("Back Logo Size (px)", min_value=20, max_value=100, value=45, step=5, key='bis') # New Image Size Slider

    with col_preview:
        # --- REAL-TIME PREVIEW COLUMN (Stacked vertically in the right column) ---
        st.markdown("### 🖼️ Front Real-Time Preview")
        st.image(create_shirt_mockup(color, f_txt, f_txt_size, f_img, f_img_size, f_emoji, f_pos), use_container_width=True)

        st.markdown("### 🖼️ Back Real-Time Preview")
        st.image(create_shirt_mockup(color, b_txt, b_txt_size, b_img, b_img_size, b_emoji, b_pos), use_container_width=True)

        current_item_temp = {
            "color": color, "size": size,
            "f_txt": f_txt, "f_txt_size": f_txt_size, "f_img": f_img.getvalue() if f_img else None, "f_img_size": f_img_size, "f_pos": f_pos, "f_emoji": f_emoji,
            "b_txt": b_txt, "b_txt_size": b_txt_size, "b_img": b_img.getvalue() if b_img else None, "b_img_size": b_img_size, "b_pos": b_pos, "b_emoji": b_emoji
        }

        this_price = calculate_item_price(current_item_temp)
        st.metric("Current Design Value", f"{this_price:,} KRW")

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🛒 Add This Design to Cart", type="secondary", use_container_width=True):
                st.session_state['cart'].append(current_item_temp)
                st.success(f"Success! Shirt #{len(st.session_state['cart'])} added with size specifications.")
                st.rerun()

        with col_btn2:
            if st.button("✅ Checkout All Items ➔", type="primary", use_container_width=True):
                if not st.session_state['cart'] and (f_txt or f_img or f_emoji != "None" or b_txt or b_img or b_emoji != "None"):
                    st.session_state['cart'].append(current_item_temp)

                if not st.session_state['cart']:
                    st.error("Your cart is empty. Please add at least one design before checkout.")
                else:
                    go_to_step("Step 2: Finalize Order")

# --- MULTI-ITEM DIGITAL RECEIPT ---
elif st.session_state['current_step'] == "Step 2: Finalize Order":
    st.header("🧾 Step 2: Finalize Order")

    if not st.session_state.get('cart'):
        st.error("No active cart found. Please return to the Workshop.")
        if st.button("Back to Workshop"): go_to_step("Step 1: Design Workshop")
    else:
        st.balloons()
        cart_data = st.session_state['cart']

        col_receipt_view, col_receipt_meta = st.columns([1, 1])

        with col_receipt_view:
            final_receipt = generate_jpeg_receipt(cart_data)
            st.image(final_receipt, width=450)

        with col_receipt_meta:
            st.markdown("### 🎉 Purchase Complete!")
            st.write(f"Thank you for your order. We have successfully rendered a single receipt for all **{len(cart_data)} customized items** in your session.")

            img_buffer = io.BytesIO()
            final_receipt.save(img_buffer, format='JPEG', quality=95)

            st.markdown("<br>", unsafe_allow_html=True)
            st.download_button("📥 DOWNLOAD RECEIPT (.jpeg)", data=img_buffer.getvalue(), file_name="BEJIN_studio_receipt.jpg", mime="image/jpeg", use_container_width=True)

            if st.button("🔄 Design More Shirts (New Session)", use_container_width=True):
                st.session_state['cart'] = []
                go_to_step("Step 1: Design Workshop")eg_receipt(st.session_state['cart'])
    st.image(final_receipt)
