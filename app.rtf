{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red131\green0\blue165;\red255\green255\blue255;\red0\green0\blue0;
\red144\green1\blue18;\red15\green112\blue1;\red0\green0\blue255;\red86\green65\blue25;\red0\green0\blue109;
\red19\green85\blue52;\red31\green99\blue128;\red191\green28\blue37;}
{\*\expandedcolortbl;;\cssrgb\c59216\c13725\c70588;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c50196\c0;\cssrgb\c0\c0\c100000;\cssrgb\c41569\c32157\c12941;\cssrgb\c0\c6275\c50196;
\cssrgb\c6667\c40000\c26667;\cssrgb\c14510\c46275\c57647;\cssrgb\c80392\c19216\c19216;}
\paperw11900\paperh16840\margl1440\margr1440\vieww15320\viewh12940\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  streamlit \cf2 \strokec2 as\cf0 \strokec4  st\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  PIL \cf2 \strokec2 import\cf0 \strokec4  Image, ImageDraw\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  io\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  urllib.request\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  datetime \cf2 \strokec2 import\cf0 \strokec4  datetime\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  pytz\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 st.set_page_config(page_title=\cf5 \strokec5 "BEJIN Studio: Custon shirt Studio"\cf0 \strokec4 , page_icon=\cf5 \strokec5 "\uc0\u55357 \u56405 "\cf0 \strokec4 , layout=\cf5 \strokec5 "wide"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # --- Initialize Global Session States ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  \cf5 \strokec5 'cart'\cf0 \strokec4  \cf7 \strokec7 not\cf0 \strokec4  \cf7 \strokec7 in\cf0 \strokec4  st.session_state:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ] = []\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  \cf5 \strokec5 'current_step'\cf0 \strokec4  \cf7 \strokec7 not\cf0 \strokec4  \cf7 \strokec7 in\cf0 \strokec4  st.session_state:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.session_state[\cf5 \strokec5 'current_step'\cf0 \strokec4 ] = \cf5 \strokec5 "Welcome Studio \uc0\u10024 "\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # --- Helper function to fetch open-source emoji PNGs safely over HTTP ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 @st.cache_data\cf0 \strokec4 (show_spinner=\cf7 \strokec7 False\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf0 \strokec4  \cf8 \strokec8 fetch_emoji_image\cf0 \strokec4 (\cf9 \strokec9 emoji_name\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     emoji_urls = \{\cb1 \
\cb3         \cf5 \strokec5 "Cute Bear \uc0\u55358 \u56824 "\cf0 \strokec4 : \cf5 \strokec5 "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f43b.png"\cf0 \strokec4 ,\cb1 \
\cb3         \cf5 \strokec5 "Pink Bow \uc0\u55356 \u57216 "\cf0 \strokec4 : \cf5 \strokec5 "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f380.png"\cf0 \strokec4 ,\cb1 \
\cb3         \cf5 \strokec5 "Red Heart \uc0\u10084 \u65039 "\cf0 \strokec4 : \cf5 \strokec5 "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/2764.png"\cf0 \strokec4 ,\cb1 \
\cb3         \cf5 \strokec5 "Retro Star \uc0\u55356 \u57119 "\cf0 \strokec4 : \cf5 \strokec5 "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f31f.png"\cf0 \strokec4 ,\cb1 \
\cb3         \cf5 \strokec5 "Fresh Clover \uc0\u55356 \u57152 "\cf0 \strokec4 : \cf5 \strokec5 "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f340.png"\cf0 \strokec4 ,\cb1 \
\cb3         \cf5 \strokec5 "Cherries \uc0\u55356 \u57170 "\cf0 \strokec4 : \cf5 \strokec5 "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/1f352.png"\cf0 \strokec4 ,\cb1 \
\cb3         \cf5 \strokec5 "Sparkles \uc0\u10024 "\cf0 \strokec4 : \cf5 \strokec5 "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/2728.png"\cf0 \cb1 \strokec4 \
\cb3     \}\cb1 \
\cb3     url = emoji_urls.get(emoji_name)\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  url:\cb1 \
\cb3         \cf2 \strokec2 try\cf0 \strokec4 :\cb1 \
\cb3             req = urllib.request.Request(url, headers=\{\cf5 \strokec5 'User-Agent'\cf0 \strokec4 : \cf5 \strokec5 'Mozilla/5.0'\cf0 \strokec4 \})\cb1 \
\cb3             \cf2 \strokec2 with\cf0 \strokec4  urllib.request.urlopen(req, timeout=\cf10 \strokec10 3\cf0 \strokec4 ) \cf2 \strokec2 as\cf0 \strokec4  response:\cb1 \
\cb3                 \cf2 \strokec2 return\cf0 \strokec4  Image.\cf8 \strokec8 open\cf0 \strokec4 (io.BytesIO(response.read())).convert(\cf5 \strokec5 "RGBA"\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 except\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  \cf7 \strokec7 None\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  \cf7 \strokec7 None\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # --- Mockup Engine (Accepts dynamic Text Size and Image Size parameters) ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf0 \strokec4  \cf8 \strokec8 create_shirt_mockup\cf0 \strokec4 (\cf9 \strokec9 color_name\cf0 \strokec4 , \cf9 \strokec9 text\cf0 \strokec4 , \cf9 \strokec9 text_size\cf0 \strokec4 , \cf9 \strokec9 uploaded_file\cf0 \strokec4 , \cf9 \strokec9 img_size\cf0 \strokec4 , \cf9 \strokec9 emoji\cf0 \strokec4 , \cf9 \strokec9 pos\cf0 \strokec4 =\cf5 \strokec5 "Center"\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     color_map = \{\cb1 \
\cb3         \cf5 \strokec5 "Classic White \uc0\u9898 "\cf0 \strokec4 : (\cf10 \strokec10 255\cf0 \strokec4 , \cf10 \strokec10 255\cf0 \strokec4 , \cf10 \strokec10 255\cf0 \strokec4 ),\cb1 \
\cb3         \cf5 \strokec5 "Pitch Black \uc0\u9899 "\cf0 \strokec4 : (\cf10 \strokec10 30\cf0 \strokec4 , \cf10 \strokec10 30\cf0 \strokec4 , \cf10 \strokec10 30\cf0 \strokec4 ),\cb1 \
\cb3         \cf5 \strokec5 "Navy Blue \uc0\u55357 \u56629 "\cf0 \strokec4 : (\cf10 \strokec10 20\cf0 \strokec4 , \cf10 \strokec10 40\cf0 \strokec4 , \cf10 \strokec10 80\cf0 \strokec4 ),\cb1 \
\cb3         \cf5 \strokec5 "Deep Green \uc0\u55357 \u57314 "\cf0 \strokec4 : (\cf10 \strokec10 20\cf0 \strokec4 , \cf10 \strokec10 60\cf0 \strokec4 , \cf10 \strokec10 40\cf0 \strokec4 )\cb1 \
\cb3     \}\cb1 \
\cb3     bg_color = color_map.get(color_name, (\cf10 \strokec10 255\cf0 \strokec4 , \cf10 \strokec10 255\cf0 \strokec4 , \cf10 \strokec10 255\cf0 \strokec4 ))\cb1 \
\cb3     text_color = (\cf10 \strokec10 255\cf0 \strokec4 , \cf10 \strokec10 255\cf0 \strokec4 , \cf10 \strokec10 255\cf0 \strokec4 ) \cf2 \strokec2 if\cf0 \strokec4  color_name \cf7 \strokec7 not\cf0 \strokec4  \cf7 \strokec7 in\cf0 \strokec4  [\cf5 \strokec5 "Classic White \uc0\u9898 "\cf0 \strokec4 ] \cf2 \strokec2 else\cf0 \strokec4  (\cf10 \strokec10 50\cf0 \strokec4 , \cf10 \strokec10 50\cf0 \strokec4 , \cf10 \strokec10 50\cf0 \strokec4 )\cb1 \
\
\cb3     img = Image.new(\cf5 \strokec5 'RGB'\cf0 \strokec4 , (\cf10 \strokec10 400\cf0 \strokec4 , \cf10 \strokec10 400\cf0 \strokec4 ), (\cf10 \strokec10 243\cf0 \strokec4 , \cf10 \strokec10 242\cf0 \strokec4 , \cf10 \strokec10 238\cf0 \strokec4 )) \cf6 \strokec6 # Aesthetic light grid background tint\cf0 \cb1 \strokec4 \
\cb3     draw = ImageDraw.Draw(img)\cb1 \
\
\cb3     \cf6 \strokec6 # Neckline\cf0 \cb1 \strokec4 \
\cb3     draw.ellipse([\cf10 \strokec10 160\cf0 \strokec4 , \cf10 \strokec10 30\cf0 \strokec4 , \cf10 \strokec10 240\cf0 \strokec4 , \cf10 \strokec10 70\cf0 \strokec4 ], fill=(\cf10 \strokec10 225\cf0 \strokec4 , \cf10 \strokec10 225\cf0 \strokec4 , \cf10 \strokec10 225\cf0 \strokec4 ), outline=(\cf10 \strokec10 210\cf0 \strokec4 , \cf10 \strokec10 210\cf0 \strokec4 , \cf10 \strokec10 210\cf0 \strokec4 ))\cb1 \
\
\cb3     \cf6 \strokec6 # Balanced Silhouette\cf0 \cb1 \strokec4 \
\cb3     shirt_points = [\cb1 \
\cb3         (\cf10 \strokec10 160\cf0 \strokec4 , \cf10 \strokec10 50\cf0 \strokec4 ), (\cf10 \strokec10 240\cf0 \strokec4 , \cf10 \strokec10 50\cf0 \strokec4 ),      \cf6 \strokec6 # Collar\cf0 \cb1 \strokec4 \
\cb3         (\cf10 \strokec10 330\cf0 \strokec4 , \cf10 \strokec10 90\cf0 \strokec4 ), (\cf10 \strokec10 350\cf0 \strokec4 , \cf10 \strokec10 150\cf0 \strokec4 ),     \cf6 \strokec6 # Right Sleeve\cf0 \cb1 \strokec4 \
\cb3         (\cf10 \strokec10 290\cf0 \strokec4 , \cf10 \strokec10 150\cf0 \strokec4 ), (\cf10 \strokec10 280\cf0 \strokec4 , \cf10 \strokec10 360\cf0 \strokec4 ),    \cf6 \strokec6 # Right Torso\cf0 \cb1 \strokec4 \
\cb3         (\cf10 \strokec10 120\cf0 \strokec4 , \cf10 \strokec10 360\cf0 \strokec4 ), (\cf10 \strokec10 110\cf0 \strokec4 , \cf10 \strokec10 150\cf0 \strokec4 ),    \cf6 \strokec6 # Left Torso\cf0 \cb1 \strokec4 \
\cb3         (\cf10 \strokec10 110\cf0 \strokec4 , \cf10 \strokec10 150\cf0 \strokec4 ), (\cf10 \strokec10 50\cf0 \strokec4 , \cf10 \strokec10 150\cf0 \strokec4 ),     \cf6 \strokec6 # Left Sleeve\cf0 \cb1 \strokec4 \
\cb3         (\cf10 \strokec10 70\cf0 \strokec4 , \cf10 \strokec10 90\cf0 \strokec4 )                   \cf6 \strokec6 # Left Shoulder\cf0 \cb1 \strokec4 \
\cb3     ]\cb1 \
\cb3     draw.polygon(shirt_points, fill=bg_color, outline=(\cf10 \strokec10 200\cf0 \strokec4 , \cf10 \strokec10 200\cf0 \strokec4 , \cf10 \strokec10 200\cf0 \strokec4 ), width=\cf10 \strokec10 1\cf0 \strokec4 )\cb1 \
\cb3     draw.line([(\cf10 \strokec10 120\cf0 \strokec4 , \cf10 \strokec10 360\cf0 \strokec4 ), (\cf10 \strokec10 280\cf0 \strokec4 , \cf10 \strokec10 360\cf0 \strokec4 )], fill=(\cf10 \strokec10 210\cf0 \strokec4 , \cf10 \strokec10 210\cf0 \strokec4 , \cf10 \strokec10 210\cf0 \strokec4 ), width=\cf10 \strokec10 2\cf0 \strokec4 )\cb1 \
\
\cb3     \cf6 \strokec6 # Horizontal Alignment Logic\cf0 \cb1 \strokec4 \
\cb3     x_pos = \cf10 \strokec10 200\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  pos == \cf5 \strokec5 "Left"\cf0 \strokec4 : x_pos = \cf10 \strokec10 145\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  pos == \cf5 \strokec5 "Right"\cf0 \strokec4 : x_pos = \cf10 \strokec10 255\cf0 \cb1 \strokec4 \
\
\cb3     \cf6 \strokec6 # Vertical Layering (Emoji @ 105, Text @ 125, Logo @ 160)\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  emoji \cf7 \strokec7 and\cf0 \strokec4  emoji != \cf5 \strokec5 "None"\cf0 \strokec4 :\cb1 \
\cb3         e_img = fetch_emoji_image(emoji)\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  e_img:\cb1 \
\cb3             \cf2 \strokec2 try\cf0 \strokec4 :\cb1 \
\cb3                 e_img.thumbnail((\cf10 \strokec10 26\cf0 \strokec4 , \cf10 \strokec10 26\cf0 \strokec4 ))\cb1 \
\cb3                 img.paste(e_img, (x_pos - e_img.width//\cf10 \strokec10 2\cf0 \strokec4 , \cf10 \strokec10 105\cf0 \strokec4  - e_img.height//\cf10 \strokec10 2\cf0 \strokec4 ), e_img)\cb1 \
\cb3             \cf2 \strokec2 except\cf0 \strokec4 : \cf2 \strokec2 pass\cf0 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 if\cf0 \strokec4  text:\cb1 \
\cb3         draw.text((x_pos, \cf10 \strokec10 125\cf0 \strokec4 ), text, fill=text_color, anchor=\cf5 \strokec5 "mm"\cf0 \strokec4 , font_size=\cf11 \strokec11 int\cf0 \strokec4 (text_size))\cb1 \
\
\cb3     \cf2 \strokec2 if\cf0 \strokec4  uploaded_file:\cb1 \
\cb3         \cf2 \strokec2 try\cf0 \strokec4 :\cb1 \
\cb3             file_bytes = uploaded_file \cf2 \strokec2 if\cf0 \strokec4  \cf8 \strokec8 isinstance\cf0 \strokec4 (uploaded_file, \cf11 \strokec11 bytes\cf0 \strokec4 ) \cf2 \strokec2 else\cf0 \strokec4  uploaded_file.read()\cb1 \
\cb3             u_img = Image.\cf8 \strokec8 open\cf0 \strokec4 (io.BytesIO(file_bytes)).convert(\cf5 \strokec5 "RGBA"\cf0 \strokec4 )\cb1 \
\cb3             u_img.thumbnail((\cf11 \strokec11 int\cf0 \strokec4 (img_size), \cf11 \strokec11 int\cf0 \strokec4 (img_size))) \cf6 \strokec6 # Modified to use dynamic img_size\cf0 \cb1 \strokec4 \
\cb3             img.paste(u_img, (x_pos - u_img.width//\cf10 \strokec10 2\cf0 \strokec4 , \cf10 \strokec10 160\cf0 \strokec4  - u_img.height//\cf10 \strokec10 2\cf0 \strokec4 ), u_img)\cb1 \
\cb3         \cf2 \strokec2 except\cf0 \strokec4 : \cf2 \strokec2 pass\cf0 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 return\cf0 \strokec4  img\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # --- Dynamic Calculation Engine (Base 25,000 | Emoji +2,000 | Logo +5,000) ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf0 \strokec4  \cf8 \strokec8 calculate_item_price\cf0 \strokec4 (\cf9 \strokec9 item\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     price = \cf10 \strokec10 25000\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  item[\cf5 \strokec5 'f_emoji'\cf0 \strokec4 ] != \cf5 \strokec5 "None"\cf0 \strokec4 : price += \cf10 \strokec10 2000\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  item[\cf5 \strokec5 'f_img'\cf0 \strokec4 ] \cf7 \strokec7 is\cf0 \strokec4  \cf7 \strokec7 not\cf0 \strokec4  \cf7 \strokec7 None\cf0 \strokec4 : price += \cf10 \strokec10 5000\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  item[\cf5 \strokec5 'b_emoji'\cf0 \strokec4 ] != \cf5 \strokec5 "None"\cf0 \strokec4 : price += \cf10 \strokec10 2000\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  item[\cf5 \strokec5 'b_img'\cf0 \strokec4 ] \cf7 \strokec7 is\cf0 \strokec4  \cf7 \strokec7 not\cf0 \strokec4  \cf7 \strokec7 None\cf0 \strokec4 : price += \cf10 \strokec10 5000\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  price\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # --- Receipt Engine Updated to matching plm. studio color tones ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf0 \strokec4  \cf8 \strokec8 generate_jpeg_receipt\cf0 \strokec4 (\cf9 \strokec9 cart\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     total_qty = \cf8 \strokec8 len\cf0 \strokec4 (cart)\cb1 \
\cb3     shipping_fee = \cf10 \strokec10 0\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  total_qty >= \cf10 \strokec10 2\cf0 \strokec4  \cf2 \strokec2 else\cf0 \strokec4  \cf10 \strokec10 5000\cf0 \cb1 \strokec4 \
\
\cb3     receipt_height = \cf10 \strokec10 700\cf0 \strokec4  + (total_qty * \cf10 \strokec10 160\cf0 \strokec4 )\cb1 \
\cb3     receipt = Image.new(\cf5 \strokec5 'RGB'\cf0 \strokec4 , (\cf10 \strokec10 1000\cf0 \strokec4 , receipt_height), (\cf10 \strokec10 250\cf0 \strokec4 , \cf10 \strokec10 249\cf0 \strokec4 , \cf10 \strokec10 246\cf0 \strokec4 )) \cf6 \strokec6 # Off-white aesthetic cream\cf0 \cb1 \strokec4 \
\cb3     draw = ImageDraw.Draw(receipt)\cb1 \
\
\cb3     korea_tz = pytz.timezone(\cf5 \strokec5 'Asia/Seoul'\cf0 \strokec4 )\cb1 \
\cb3     now = datetime.now(korea_tz)\cb1 \
\cb3     \cb1 \
\cb3     order_date = now.strftime(\cf5 \strokec5 "%Y-%m-%d"\cf0 \strokec4 )\cb1 \
\cb3     order_time = now.strftime(\cf5 \strokec5 "%H:%M:%S"\cf0 \strokec4 )\cb1 \
\
\cb3     \cf6 \strokec6 # Outer Border with Brand Color #2F3E2B (Dark Olive Green)\cf0 \cb1 \strokec4 \
\cb3     draw.rectangle([\cf10 \strokec10 40\cf0 \strokec4 , \cf10 \strokec10 40\cf0 \strokec4 , \cf10 \strokec10 960\cf0 \strokec4 , receipt_height - \cf10 \strokec10 40\cf0 \strokec4 ], outline=(\cf10 \strokec10 47\cf0 \strokec4 , \cf10 \strokec10 62\cf0 \strokec4 , \cf10 \strokec10 43\cf0 \strokec4 ), width=\cf10 \strokec10 3\cf0 \strokec4 )\cb1 \
\
\cb3     \cf6 \strokec6 # Header Branding Text\cf0 \cb1 \strokec4 \
\cb3     draw.text((\cf10 \strokec10 500\cf0 \strokec4 , \cf10 \strokec10 110\cf0 \strokec4 ), \cf5 \strokec5 "BEJIN.studio"\cf0 \strokec4 , fill=(\cf10 \strokec10 47\cf0 \strokec4 , \cf10 \strokec10 62\cf0 \strokec4 , \cf10 \strokec10 43\cf0 \strokec4 ), anchor=\cf5 \strokec5 "mm"\cf0 \strokec4 , font_size=\cf10 \strokec10 46\cf0 \strokec4 )\cb1 \
\cb3     draw.text((\cf10 \strokec10 500\cf0 \strokec4 , \cf10 \strokec10 165\cf0 \strokec4 ), \cf5 \strokec5 "Design your own clothing, your own way."\cf0 \strokec4 , fill=(\cf10 \strokec10 120\cf0 \strokec4 , \cf10 \strokec10 130\cf0 \strokec4 , \cf10 \strokec10 115\cf0 \strokec4 ), anchor=\cf5 \strokec5 "mm"\cf0 \strokec4 , font_size=\cf10 \strokec10 20\cf0 \strokec4 )\cb1 \
\cb3     draw.text((\cf10 \strokec10 500\cf0 \strokec4 , \cf10 \strokec10 110\cf0 \strokec4 ), \cf5 \strokec5 "BEJIN.studio"\cf0 \strokec4 , fill=(\cf10 \strokec10 47\cf0 \strokec4 , \cf10 \strokec10 62\cf0 \strokec4 , \cf10 \strokec10 43\cf0 \strokec4 ), anchor=\cf5 \strokec5 "mm"\cf0 \strokec4 , font_size=\cf10 \strokec10 46\cf0 \strokec4 )\cb1 \
\cb3     draw.text((\cf10 \strokec10 500\cf0 \strokec4 , \cf10 \strokec10 200\cf0 \strokec4 ), \cf7 \strokec7 f\cf5 \strokec5 "Order Date: \cf0 \strokec4 \{order_date\}\cf5 \strokec5   \cf0 \strokec4 |\cf5 \strokec5   Time: \cf0 \strokec4 \{order_time\}\cf5 \strokec5 "\cf0 \strokec4 , fill=(\cf10 \strokec10 120\cf0 \strokec4 , \cf10 \strokec10 130\cf0 \strokec4 , \cf10 \strokec10 115\cf0 \strokec4 ), anchor=\cf5 \strokec5 "mm"\cf0 \strokec4 , font_size=\cf10 \strokec10 18\cf0 \strokec4 )\cb1 \
\
\cb3     y_pos = \cf10 \strokec10 240\cf0 \cb1 \strokec4 \
\cb3     subtotal_accum = \cf10 \strokec10 0\cf0 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 for\cf0 \strokec4  i, item \cf7 \strokec7 in\cf0 \strokec4  \cf8 \strokec8 enumerate\cf0 \strokec4 (cart):\cb1 \
\cb3         draw.line([(\cf10 \strokec10 80\cf0 \strokec4 , y_pos), (\cf10 \strokec10 920\cf0 \strokec4 , y_pos)], fill=(\cf10 \strokec10 225\cf0 \strokec4 , \cf10 \strokec10 230\cf0 \strokec4 , \cf10 \strokec10 220\cf0 \strokec4 ), width=\cf10 \strokec10 1\cf0 \strokec4 )\cb1 \
\cb3         y_pos += \cf10 \strokec10 20\cf0 \cb1 \strokec4 \
\
\cb3         thumb = create_shirt_mockup(item[\cf5 \strokec5 'color'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_txt'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_txt_size'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_img'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_img_size'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_emoji'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_pos'\cf0 \strokec4 ]).resize((\cf10 \strokec10 110\cf0 \strokec4 , \cf10 \strokec10 110\cf0 \strokec4 ))\cb1 \
\cb3         draw.rectangle([\cf10 \strokec10 89\cf0 \strokec4 , y_pos - \cf10 \strokec10 1\cf0 \strokec4 , \cf10 \strokec10 201\cf0 \strokec4 , y_pos + \cf10 \strokec10 111\cf0 \strokec4 ], outline=(\cf10 \strokec10 210\cf0 \strokec4 , \cf10 \strokec10 215\cf0 \strokec4 , \cf10 \strokec10 205\cf0 \strokec4 ), width=\cf10 \strokec10 1\cf0 \strokec4 )\cb1 \
\cb3         receipt.paste(thumb, (\cf10 \strokec10 90\cf0 \strokec4 , y_pos))\cb1 \
\
\cb3         item_price = calculate_item_price(item)\cb1 \
\cb3         subtotal_accum += item_price\cb1 \
\cb3         clean_color = item[\cf5 \strokec5 'color'\cf0 \strokec4 ].split()[\cf10 \strokec10 0\cf0 \strokec4 ]\cb1 \
\
\cb3         draw.text((\cf10 \strokec10 230\cf0 \strokec4 , y_pos + \cf10 \strokec10 10\cf0 \strokec4 ), \cf7 \strokec7 f\cf5 \strokec5 "BEJIN Custom Shirt Order // #0\cf0 \strokec4 \{i+\cf10 \strokec10 1\cf0 \strokec4 \}\cf5 \strokec5 "\cf0 \strokec4 , fill=(\cf10 \strokec10 47\cf0 \strokec4 , \cf10 \strokec10 62\cf0 \strokec4 , \cf10 \strokec10 43\cf0 \strokec4 ), font_size=\cf10 \strokec10 26\cf0 \strokec4 )\cb1 \
\cb3         draw.text((\cf10 \strokec10 230\cf0 \strokec4 , y_pos + \cf10 \strokec10 45\cf0 \strokec4 ), \cf7 \strokec7 f\cf5 \strokec5 "Size: \cf0 \strokec4 \{item[\cf5 \strokec5 'size'\cf0 \strokec4 ]\}\cf5 \strokec5   \cf0 \strokec4 |\cf5 \strokec5   Color: \cf0 \strokec4 \{clean_color\}\cf5 \strokec5   \cf0 \strokec4 |\cf5 \strokec5   Front Size: \cf0 \strokec4 \{item[\cf5 \strokec5 'f_txt_size'\cf0 \strokec4 ]\}\cf5 \strokec5 pt"\cf0 \strokec4 , fill=(\cf10 \strokec10 120\cf0 \strokec4 , \cf10 \strokec10 130\cf0 \strokec4 , \cf10 \strokec10 115\cf0 \strokec4 ), font_size=\cf10 \strokec10 20\cf0 \strokec4 )\cb1 \
\cb3         draw.text((\cf10 \strokec10 230\cf0 \strokec4 , y_pos + \cf10 \strokec10 75\cf0 \strokec4 ), \cf7 \strokec7 f\cf5 \strokec5 "Logo: \cf0 \strokec4 \{\cf5 \strokec5 'Yes (+5k)'\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  item[\cf5 \strokec5 'f_img'\cf0 \strokec4 ] \cf2 \strokec2 else\cf0 \strokec4  \cf5 \strokec5 'No'\cf0 \strokec4 \}\cf5 \strokec5   \cf0 \strokec4 |\cf5 \strokec5   Emoji: \cf0 \strokec4 \{\cf5 \strokec5 'Yes (+2k)'\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  item[\cf5 \strokec5 'f_emoji'\cf0 \strokec4 ]\cf12 \strokec12 !\cf0 \strokec4 =\cf5 \strokec5 'None'\cf0 \strokec4  \cf2 \strokec2 else\cf0 \strokec4  \cf5 \strokec5 'No'\cf0 \strokec4 \}\cf5 \strokec5 "\cf0 \strokec4 , fill=(\cf10 \strokec10 120\cf0 \strokec4 , \cf10 \strokec10 130\cf0 \strokec4 , \cf10 \strokec10 115\cf0 \strokec4 ), font_size=\cf10 \strokec10 20\cf0 \strokec4 )\cb1 \
\
\cb3         draw.text((\cf10 \strokec10 910\cf0 \strokec4 , y_pos + \cf10 \strokec10 40\cf0 \strokec4 ), \cf7 \strokec7 f\cf5 \strokec5 "\cf0 \strokec4 \{item_price\cf10 \strokec10 :,\cf0 \strokec4 \}\cf5 \strokec5  KRW"\cf0 \strokec4 , fill=(\cf10 \strokec10 47\cf0 \strokec4 , \cf10 \strokec10 62\cf0 \strokec4 , \cf10 \strokec10 43\cf0 \strokec4 ), anchor=\cf5 \strokec5 "ra"\cf0 \strokec4 , font_size=\cf10 \strokec10 26\cf0 \strokec4 )\cb1 \
\cb3         y_pos += \cf10 \strokec10 140\cf0 \cb1 \strokec4 \
\
\cb3     y_pos += \cf10 \strokec10 20\cf0 \cb1 \strokec4 \
\cb3     draw.line([(\cf10 \strokec10 80\cf0 \strokec4 , y_pos), (\cf10 \strokec10 920\cf0 \strokec4 , y_pos)], fill=(\cf10 \strokec10 47\cf0 \strokec4 , \cf10 \strokec10 62\cf0 \strokec4 , \cf10 \strokec10 43\cf0 \strokec4 ), width=\cf10 \strokec10 2\cf0 \strokec4 )\cb1 \
\cb3     y_pos += \cf10 \strokec10 40\cf0 \cb1 \strokec4 \
\
\cb3     draw.text((\cf10 \strokec10 100\cf0 \strokec4 , y_pos), \cf5 \strokec5 "Subtotal Amount"\cf0 \strokec4 , fill=(\cf10 \strokec10 120\cf0 \strokec4 , \cf10 \strokec10 130\cf0 \strokec4 , \cf10 \strokec10 115\cf0 \strokec4 ), font_size=\cf10 \strokec10 24\cf0 \strokec4 )\cb1 \
\cb3     draw.text((\cf10 \strokec10 900\cf0 \strokec4 , y_pos), \cf7 \strokec7 f\cf5 \strokec5 "\cf0 \strokec4 \{subtotal_accum\cf10 \strokec10 :,\cf0 \strokec4 \}\cf5 \strokec5  KRW"\cf0 \strokec4 , fill=(\cf10 \strokec10 47\cf0 \strokec4 , \cf10 \strokec10 62\cf0 \strokec4 , \cf10 \strokec10 43\cf0 \strokec4 ), anchor=\cf5 \strokec5 "ra"\cf0 \strokec4 , font_size=\cf10 \strokec10 24\cf0 \strokec4 )\cb1 \
\
\cb3     y_pos += \cf10 \strokec10 50\cf0 \cb1 \strokec4 \
\cb3     draw.text((\cf10 \strokec10 100\cf0 \strokec4 , y_pos), \cf5 \strokec5 "Shipping Fee"\cf0 \strokec4 , fill=(\cf10 \strokec10 120\cf0 \strokec4 , \cf10 \strokec10 130\cf0 \strokec4 , \cf10 \strokec10 115\cf0 \strokec4 ), font_size=\cf10 \strokec10 24\cf0 \strokec4 )\cb1 \
\cb3     draw.text((\cf10 \strokec10 900\cf0 \strokec4 , y_pos), \cf5 \strokec5 "Complimentary"\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  shipping_fee == \cf10 \strokec10 0\cf0 \strokec4  \cf2 \strokec2 else\cf0 \strokec4  \cf7 \strokec7 f\cf5 \strokec5 "\cf0 \strokec4 \{shipping_fee\cf10 \strokec10 :,\cf0 \strokec4 \}\cf5 \strokec5  KRW"\cf0 \strokec4 , fill=(\cf10 \strokec10 47\cf0 \strokec4 , \cf10 \strokec10 62\cf0 \strokec4 , \cf10 \strokec10 43\cf0 \strokec4 ), anchor=\cf5 \strokec5 "ra"\cf0 \strokec4 , font_size=\cf10 \strokec10 24\cf0 \strokec4 )\cb1 \
\
\cb3     y_pos += \cf10 \strokec10 70\cf0 \cb1 \strokec4 \
\cb3     grand_total = subtotal_accum + shipping_fee\cb1 \
\
\cb3     \cf6 \strokec6 # Total Box matching bottom band style\cf0 \cb1 \strokec4 \
\cb3     draw.rectangle([\cf10 \strokec10 80\cf0 \strokec4 , y_pos, \cf10 \strokec10 920\cf0 \strokec4 , y_pos + \cf10 \strokec10 75\cf0 \strokec4 ], fill=(\cf10 \strokec10 47\cf0 \strokec4 , \cf10 \strokec10 62\cf0 \strokec4 , \cf10 \strokec10 43\cf0 \strokec4 ))\cb1 \
\cb3     draw.text((\cf10 \strokec10 110\cf0 \strokec4 , y_pos + \cf10 \strokec10 38\cf0 \strokec4 ), \cf5 \strokec5 "TOTAL PAYMENT"\cf0 \strokec4 , fill=(\cf10 \strokec10 250\cf0 \strokec4 , \cf10 \strokec10 249\cf0 \strokec4 , \cf10 \strokec10 246\cf0 \strokec4 ), anchor=\cf5 \strokec5 "lm"\cf0 \strokec4 , font_size=\cf10 \strokec10 24\cf0 \strokec4 )\cb1 \
\cb3     draw.text((\cf10 \strokec10 890\cf0 \strokec4 , y_pos + \cf10 \strokec10 38\cf0 \strokec4 ), \cf7 \strokec7 f\cf5 \strokec5 "\cf0 \strokec4 \{grand_total\cf10 \strokec10 :,\cf0 \strokec4 \}\cf5 \strokec5  KRW"\cf0 \strokec4 , fill=(\cf10 \strokec10 255\cf0 \strokec4 , \cf10 \strokec10 255\cf0 \strokec4 , \cf10 \strokec10 255\cf0 \strokec4 ), anchor=\cf5 \strokec5 "rm"\cf0 \strokec4 , font_size=\cf10 \strokec10 28\cf0 \strokec4 )\cb1 \
\
\cb3     \cf2 \strokec2 return\cf0 \strokec4  receipt\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf0 \strokec4  \cf8 \strokec8 go_to_step\cf0 \strokec4 (\cf9 \strokec9 step_name\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.session_state[\cf5 \strokec5 'current_step'\cf0 \strokec4 ] = step_name\cb1 \
\cb3     st.rerun()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # --- SIDEBAR ROUTING ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 options = [\cf5 \strokec5 "Welcome Studio \uc0\u10024 "\cf0 \strokec4 , \cf5 \strokec5 "Step 1: Design Workshop"\cf0 \strokec4 , \cf5 \strokec5 "Step 2: Finalize Order"\cf0 \strokec4 ]\cb1 \
\cb3 sidebar_selection = st.sidebar.radio(\cf5 \strokec5 "Navigation"\cf0 \strokec4 , options, index=options.index(st.session_state[\cf5 \strokec5 'current_step'\cf0 \strokec4 ]))\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  sidebar_selection != st.session_state[\cf5 \strokec5 'current_step'\cf0 \strokec4 ]:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     go_to_step(sidebar_selection)\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # --- WELCOME PAGE (WITH DYNAMIC PREVIEW GALLERY) ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  st.session_state[\cf5 \strokec5 'current_step'\cf0 \strokec4 ] == \cf5 \strokec5 "Welcome Studio \uc0\u10024 "\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf6 \strokec6 # Header Banner Block matching BEJIN studio layout\cf0 \cb1 \strokec4 \
\cb3     st.markdown(\cf5 \strokec5 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5         <div style="background-color: #FFFFFF; padding: 40px; border-radius: 20px; border: 1px solid #D1DCB2; margin-bottom: 30px;">\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5             <h1 style="margin: 0; font-size: 38px; color: #2F3E2B;">[BEJIN] Your style. Your rules. Fully customized.</h1>\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5             <p style="color: #6B7A64; font-size: 18px; margin-top: 10px;">Design your own clothing, your own way.\uc0\u55357 \u56558 </p>\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5         </div>\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5     """\cf0 \strokec4 , unsafe_allow_html=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     col_info, col_action = st.columns([\cf10 \strokec10 1.2\cf0 \strokec4 , \cf10 \strokec10 1\cf0 \strokec4 ])\cb1 \
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col_info:\cb1 \
\cb3         st.markdown(\cf5 \strokec5 "### \uc0\u10024  STUDIO PROCESS"\cf0 \strokec4 )\cb1 \
\cb3         st.write(\cf5 \strokec5 "1. **Design a shirt** with unique color, text size, logo, and tiny emoji motifs."\cf0 \strokec4 )\cb1 \
\cb3         st.write(\cf5 \strokec5 "2. Click **'\uc0\u55357 \u57042  Add This Design to Cart'** to lock your creation."\cf0 \strokec4 )\cb1 \
\cb3         st.write(\cf5 \strokec5 "3. Instantly change parameters to design your **second or third shirt** completely from scratch."\cf0 \strokec4 )\cb1 \
\cb3         st.write(\cf5 \strokec5 "4. Finalize to get a receipt."\cf0 \strokec4 )\cb1 \
\
\cb3         st.markdown(\cf5 \strokec5 "### \uc0\u55357 \u56496  ADD ON PRICING"\cf0 \strokec4 )\cb1 \
\cb3         st.table(\{\cb1 \
\cb3             \cf5 \strokec5 "Component Selection"\cf0 \strokec4 : [\cf5 \strokec5 "Plain Shirt / Pure Text Base"\cf0 \strokec4 , \cf5 \strokec5 "Emoji Graphic Accent"\cf0 \strokec4 , \cf5 \strokec5 "Custom Logo Upload Image"\cf0 \strokec4 ],\cb1 \
\cb3             \cf5 \strokec5 "Price Rule (KRW)"\cf0 \strokec4 : [\cf5 \strokec5 "25,000 KRW"\cf0 \strokec4 , \cf5 \strokec5 "+ 2,000 KRW"\cf0 \strokec4 , \cf5 \strokec5 "+ 5,000 KRW"\cf0 \strokec4 ]\cb1 \
\cb3         \})\cb1 \
\cb3         st.info(\cf5 \strokec5 "\uc0\u55357 \u56613  **PROMO:** Buy 2 shirts or more to unlock **FREE SHIPPING**!"\cf0 \strokec4 )\cb1 \
\
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col_action:\cb1 \
\cb3         st.markdown(\cf5 \strokec5 "### \uc0\u55357 \u57042  LIVE CART PREVIEW"\cf0 \strokec4 )\cb1 \
\
\cb3         \cf2 \strokec2 if\cf0 \strokec4  \cf7 \strokec7 not\cf0 \strokec4  st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ]:\cb1 \
\cb3             st.info(\cf5 \strokec5 "Your cart is empty. Rendering minimalist default template as inspiration:"\cf0 \strokec4 )\cb1 \
\cb3             sample_shirt = create_shirt_mockup(\cf5 \strokec5 "Classic White \uc0\u9898 "\cf0 \strokec4 , \cf5 \strokec5 "studio."\cf0 \strokec4 , \cf10 \strokec10 20\cf0 \strokec4 , \cf7 \strokec7 None\cf0 \strokec4 , \cf10 \strokec10 45\cf0 \strokec4 , \cf5 \strokec5 "None"\cf0 \strokec4 , \cf5 \strokec5 "Center"\cf0 \strokec4 )\cb1 \
\cb3             st.image(sample_shirt, width=\cf10 \strokec10 280\cf0 \strokec4 , caption=\cf5 \strokec5 "Sample: Plain White Studio Shirt"\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             st.success(\cf7 \strokec7 f\cf5 \strokec5 "You have \cf0 \strokec4 \{\cf8 \strokec8 len\cf0 \strokec4 (st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ])\}\cf5 \strokec5  custom shirt(s) ready in your cart!"\cf0 \strokec4 )\cb1 \
\
\cb3             \cf2 \strokec2 for\cf0 \strokec4  idx, item \cf7 \strokec7 in\cf0 \strokec4  \cf8 \strokec8 enumerate\cf0 \strokec4 (st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ]):\cb1 \
\cb3                 \cf2 \strokec2 with\cf0 \strokec4  st.expander(\cf7 \strokec7 f\cf5 \strokec5 "\uc0\u55357 \u56405  Shirt #\cf0 \strokec4 \{idx+\cf10 \strokec10 1\cf0 \strokec4 \}\cf5 \strokec5  Preview - \cf0 \strokec4 \{item[\cf5 \strokec5 'color'\cf0 \strokec4 ].split()[\cf10 \strokec10 0\cf0 \strokec4 ]\}\cf5 \strokec5  (\cf0 \strokec4 \{item[\cf5 \strokec5 'size'\cf0 \strokec4 ]\}\cf5 \strokec5 )"\cf0 \strokec4 , expanded=\cf7 \strokec7 True\cf0 \strokec4 ):\cb1 \
\cb3                     col_p1, col_p2 = st.columns(\cf10 \strokec10 2\cf0 \strokec4 )\cb1 \
\cb3                     \cf2 \strokec2 with\cf0 \strokec4  col_p1:\cb1 \
\cb3                         f_img_thumb = create_shirt_mockup(item[\cf5 \strokec5 'color'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_txt'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_txt_size'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_img'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_img_size'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_emoji'\cf0 \strokec4 ], item[\cf5 \strokec5 'f_pos'\cf0 \strokec4 ])\cb1 \
\cb3                         st.image(f_img_thumb, caption=\cf7 \strokec7 f\cf5 \strokec5 "Front Look (Text: \cf0 \strokec4 \{item[\cf5 \strokec5 'f_txt_size'\cf0 \strokec4 ]\}\cf5 \strokec5 pt)"\cf0 \strokec4 , use_container_width=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\cb3                     \cf2 \strokec2 with\cf0 \strokec4  col_p2:\cb1 \
\cb3                         b_img_thumb = create_shirt_mockup(item[\cf5 \strokec5 'color'\cf0 \strokec4 ], item[\cf5 \strokec5 'b_txt'\cf0 \strokec4 ], item[\cf5 \strokec5 'b_txt_size'\cf0 \strokec4 ], item[\cf5 \strokec5 'b_img'\cf0 \strokec4 ], item[\cf5 \strokec5 'b_img_size'\cf0 \strokec4 ], item[\cf5 \strokec5 'b_emoji'\cf0 \strokec4 ], item[\cf5 \strokec5 'b_pos'\cf0 \strokec4 ])\cb1 \
\cb3                         st.image(b_img_thumb, caption=\cf7 \strokec7 f\cf5 \strokec5 "Back Look (Text: \cf0 \strokec4 \{item[\cf5 \strokec5 'b_txt_size'\cf0 \strokec4 ]\}\cf5 \strokec5 pt)"\cf0 \strokec4 , use_container_width=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\cb3                     st.write(\cf7 \strokec7 f\cf5 \strokec5 "**Value:** \cf0 \strokec4 \{calculate_item_price(item)\cf10 \strokec10 :,\cf0 \strokec4 \}\cf5 \strokec5  KRW"\cf0 \strokec4 )\cb1 \
\
\cb3             \cf2 \strokec2 if\cf0 \strokec4  st.button(\cf5 \strokec5 "Clear Cart & Reset Previews"\cf0 \strokec4 ):\cb1 \
\cb3                 st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ] = []\cb1 \
\cb3                 st.rerun()\cb1 \
\
\cb3         st.markdown(\cf5 \strokec5 "<br>"\cf0 \strokec4 , unsafe_allow_html=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  st.button(\cf5 \strokec5 "\uc0\u55357 \u57037 \u65039  START DESIGNING \u10132 "\cf0 \strokec4 , \cf11 \strokec11 type\cf0 \strokec4 =\cf5 \strokec5 "primary"\cf0 \strokec4 , use_container_width=\cf7 \strokec7 True\cf0 \strokec4 ):\cb1 \
\cb3             go_to_step(\cf5 \strokec5 "Step 1: Design Workshop"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # --- DESIGN WORKSHOP (WITH NEW FONT SIZE SLIDERS) ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 elif\cf0 \strokec4  st.session_state[\cf5 \strokec5 'current_step'\cf0 \strokec4 ] == \cf5 \strokec5 "Step 1: Design Workshop"\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.header(\cf7 \strokec7 f\cf5 \strokec5 "\uc0\u55356 \u57256  Step 1: Creative Canvas (Current Cart: \cf0 \strokec4 \{\cf8 \strokec8 len\cf0 \strokec4 (st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ])\}\cf5 \strokec5  Items)"\cf0 \strokec4 )\cb1 \
\
\cb3     col_basic, col_custom, col_preview = st.columns([\cf10 \strokec10 1\cf0 \strokec4 , \cf10 \strokec10 1.2\cf0 \strokec4 , \cf10 \strokec10 1.5\cf0 \strokec4 ])\cb1 \
\
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col_basic:\cb1 \
\cb3         st.markdown(\cf5 \strokec5 "### 1. Apparel Base"\cf0 \strokec4 )\cb1 \
\cb3         color = st.selectbox(\cf5 \strokec5 "Shirt Color"\cf0 \strokec4 , [\cf5 \strokec5 "Classic White \uc0\u9898 "\cf0 \strokec4 , \cf5 \strokec5 "Pitch Black \uc0\u9899 "\cf0 \strokec4 , \cf5 \strokec5 "Navy Blue \uc0\u55357 \u56629 "\cf0 \strokec4 , \cf5 \strokec5 "Deep Green \uc0\u55357 \u57314 "\cf0 \strokec4 ])\cb1 \
\cb3         size = st.select_slider(\cf5 \strokec5 "Size Config"\cf0 \strokec4 , [\cf5 \strokec5 "S"\cf0 \strokec4 , \cf5 \strokec5 "M"\cf0 \strokec4 , \cf5 \strokec5 "L"\cf0 \strokec4 , \cf5 \strokec5 "XL"\cf0 \strokec4 ])\cb1 \
\
\cb3         st.markdown(\cf5 \strokec5 "---"\cf0 \strokec4 )\cb1 \
\cb3         st.markdown(\cf5 \strokec5 "### \uc0\u55357 \u57042  Cart Dashboard"\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  \cf7 \strokec7 not\cf0 \strokec4  st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ]:\cb1 \
\cb3             st.caption(\cf5 \strokec5 "No shirts added yet."\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 for\cf0 \strokec4  idx, c_item \cf7 \strokec7 in\cf0 \strokec4  \cf8 \strokec8 enumerate\cf0 \strokec4 (st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ]):\cb1 \
\cb3                 st.caption(\cf7 \strokec7 f\cf5 \strokec5 "#\cf0 \strokec4 \{idx+\cf10 \strokec10 1\cf0 \strokec4 \}\cf5 \strokec5 : \cf0 \strokec4 \{c_item[\cf5 \strokec5 'color'\cf0 \strokec4 ].split()[\cf10 \strokec10 0\cf0 \strokec4 ]\}\cf5 \strokec5  (\cf0 \strokec4 \{c_item[\cf5 \strokec5 'size'\cf0 \strokec4 ]\}\cf5 \strokec5 ) - \cf0 \strokec4 \{calculate_item_price(c_item)\cf10 \strokec10 :,\cf0 \strokec4 \}\cf5 \strokec5  KRW"\cf0 \strokec4 )\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  st.button(\cf5 \strokec5 "Reset All items"\cf0 \strokec4 , key=\cf5 \strokec5 "reset_workshop"\cf0 \strokec4 ):\cb1 \
\cb3                 st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ] = []\cb1 \
\cb3                 st.rerun()\cb1 \
\
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col_custom:\cb1 \
\cb3         emojis = [\cf5 \strokec5 "None"\cf0 \strokec4 , \cf5 \strokec5 "Cute Bear \uc0\u55358 \u56824 "\cf0 \strokec4 , \cf5 \strokec5 "Pink Bow \uc0\u55356 \u57216 "\cf0 \strokec4 , \cf5 \strokec5 "Red Heart \uc0\u10084 \u65039 "\cf0 \strokec4 , \cf5 \strokec5 "Retro Star \uc0\u55356 \u57119 "\cf0 \strokec4 , \cf5 \strokec5 "Fresh Clover \uc0\u55356 \u57152 "\cf0 \strokec4 , \cf5 \strokec5 "Cherries \uc0\u55356 \u57170 "\cf0 \strokec4 , \cf5 \strokec5 "Sparkles \uc0\u10024 "\cf0 \strokec4 ]\cb1 \
\
\cb3         \cf6 \strokec6 # --- FRONT APP DESIGN CONTROLS ---\cf0 \cb1 \strokec4 \
\cb3         st.markdown(\cf5 \strokec5 "### 2. Front Parameters"\cf0 \strokec4 )\cb1 \
\cb3         f_pos = st.radio(\cf5 \strokec5 "Alignment"\cf0 \strokec4 , [\cf5 \strokec5 "Left"\cf0 \strokec4 , \cf5 \strokec5 "Center"\cf0 \strokec4 , \cf5 \strokec5 "Right"\cf0 \strokec4 ], horizontal=\cf7 \strokec7 True\cf0 \strokec4 , key=\cf5 \strokec5 'fp'\cf0 \strokec4 )\cb1 \
\cb3         f_emoji = st.selectbox(\cf5 \strokec5 "Mini Emoji Accent (+2k)"\cf0 \strokec4 , emojis, key=\cf5 \strokec5 'fe'\cf0 \strokec4 )\cb1 \
\cb3         f_txt = st.text_input(\cf5 \strokec5 "Mini Text Graphic (Base)"\cf0 \strokec4 , placeholder=\cf5 \strokec5 "Type minimalist tags..."\cf0 \strokec4 , key=\cf5 \strokec5 'ft'\cf0 \strokec4 )\cb1 \
\cb3         f_txt_size = st.slider(\cf5 \strokec5 "Front Text Size (pt)"\cf0 \strokec4 , min_value=\cf10 \strokec10 12\cf0 \strokec4 , max_value=\cf10 \strokec10 36\cf0 \strokec4 , value=\cf10 \strokec10 20\cf0 \strokec4 , step=\cf10 \strokec10 2\cf0 \strokec4 , key=\cf5 \strokec5 'fts'\cf0 \strokec4 )\cb1 \
\cb3         f_img = st.file_uploader(\cf5 \strokec5 "Logo Upload (+5k)"\cf0 \strokec4 , \cf11 \strokec11 type\cf0 \strokec4 =[\cf5 \strokec5 'png'\cf0 \strokec4 ,\cf5 \strokec5 'jpg'\cf0 \strokec4 ], key=\cf5 \strokec5 'f'\cf0 \strokec4 )\cb1 \
\cb3         f_img_size = st.slider(\cf5 \strokec5 "Front Logo Size (px)"\cf0 \strokec4 , min_value=\cf10 \strokec10 20\cf0 \strokec4 , max_value=\cf10 \strokec10 100\cf0 \strokec4 , value=\cf10 \strokec10 45\cf0 \strokec4 , step=\cf10 \strokec10 5\cf0 \strokec4 , key=\cf5 \strokec5 'fis'\cf0 \strokec4 ) \cf6 \strokec6 # New Image Size Slider\cf0 \cb1 \strokec4 \
\
\cb3         st.markdown(\cf5 \strokec5 "---"\cf0 \strokec4 )\cb1 \
\
\cb3         \cf6 \strokec6 # --- BACK APP DESIGN CONTROLS ---\cf0 \cb1 \strokec4 \
\cb3         st.markdown(\cf5 \strokec5 "### 3. Back Parameters"\cf0 \strokec4 )\cb1 \
\cb3         b_pos = st.radio(\cf5 \strokec5 "Alignment "\cf0 \strokec4 , [\cf5 \strokec5 "Left"\cf0 \strokec4 , \cf5 \strokec5 "Center"\cf0 \strokec4 , \cf5 \strokec5 "Right"\cf0 \strokec4 ], horizontal=\cf7 \strokec7 True\cf0 \strokec4 , key=\cf5 \strokec5 'bp'\cf0 \strokec4 )\cb1 \
\cb3         b_emoji = st.selectbox(\cf5 \strokec5 "Mini Emoji Accent (+2k) "\cf0 \strokec4 , emojis, key=\cf5 \strokec5 'be'\cf0 \strokec4 )\cb1 \
\cb3         b_txt = st.text_input(\cf5 \strokec5 "Mini Text Graphic (Base) "\cf0 \strokec4 , placeholder=\cf5 \strokec5 "Type custom tags..."\cf0 \strokec4 , key=\cf5 \strokec5 'bt'\cf0 \strokec4 )\cb1 \
\cb3         b_txt_size = st.slider(\cf5 \strokec5 "Back Text Size (pt)"\cf0 \strokec4 , min_value=\cf10 \strokec10 12\cf0 \strokec4 , max_value=\cf10 \strokec10 36\cf0 \strokec4 , value=\cf10 \strokec10 20\cf0 \strokec4 , step=\cf10 \strokec10 2\cf0 \strokec4 , key=\cf5 \strokec5 'bts'\cf0 \strokec4 )\cb1 \
\cb3         b_img = st.file_uploader(\cf5 \strokec5 "Logo Upload (+5k) "\cf0 \strokec4 , \cf11 \strokec11 type\cf0 \strokec4 =[\cf5 \strokec5 'png'\cf0 \strokec4 ,\cf5 \strokec5 'jpg'\cf0 \strokec4 ], key=\cf5 \strokec5 'b'\cf0 \strokec4 )\cb1 \
\cb3         b_img_size = st.slider(\cf5 \strokec5 "Back Logo Size (px)"\cf0 \strokec4 , min_value=\cf10 \strokec10 20\cf0 \strokec4 , max_value=\cf10 \strokec10 100\cf0 \strokec4 , value=\cf10 \strokec10 45\cf0 \strokec4 , step=\cf10 \strokec10 5\cf0 \strokec4 , key=\cf5 \strokec5 'bis'\cf0 \strokec4 ) \cf6 \strokec6 # New Image Size Slider\cf0 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col_preview:\cb1 \
\cb3         \cf6 \strokec6 # --- REAL-TIME PREVIEW COLUMN (Stacked vertically in the right column) ---\cf0 \cb1 \strokec4 \
\cb3         st.markdown(\cf5 \strokec5 "### \uc0\u55357 \u56764 \u65039  Front Real-Time Preview"\cf0 \strokec4 )\cb1 \
\cb3         st.image(create_shirt_mockup(color, f_txt, f_txt_size, f_img, f_img_size, f_emoji, f_pos), use_container_width=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\
\cb3         st.markdown(\cf5 \strokec5 "### \uc0\u55357 \u56764 \u65039  Back Real-Time Preview"\cf0 \strokec4 )\cb1 \
\cb3         st.image(create_shirt_mockup(color, b_txt, b_txt_size, b_img, b_img_size, b_emoji, b_pos), use_container_width=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\
\cb3         current_item_temp = \{\cb1 \
\cb3             \cf5 \strokec5 "color"\cf0 \strokec4 : color, \cf5 \strokec5 "size"\cf0 \strokec4 : size,\cb1 \
\cb3             \cf5 \strokec5 "f_txt"\cf0 \strokec4 : f_txt, \cf5 \strokec5 "f_txt_size"\cf0 \strokec4 : f_txt_size, \cf5 \strokec5 "f_img"\cf0 \strokec4 : f_img.getvalue() \cf2 \strokec2 if\cf0 \strokec4  f_img \cf2 \strokec2 else\cf0 \strokec4  \cf7 \strokec7 None\cf0 \strokec4 , \cf5 \strokec5 "f_img_size"\cf0 \strokec4 : f_img_size, \cf5 \strokec5 "f_pos"\cf0 \strokec4 : f_pos, \cf5 \strokec5 "f_emoji"\cf0 \strokec4 : f_emoji,\cb1 \
\cb3             \cf5 \strokec5 "b_txt"\cf0 \strokec4 : b_txt, \cf5 \strokec5 "b_txt_size"\cf0 \strokec4 : b_txt_size, \cf5 \strokec5 "b_img"\cf0 \strokec4 : b_img.getvalue() \cf2 \strokec2 if\cf0 \strokec4  b_img \cf2 \strokec2 else\cf0 \strokec4  \cf7 \strokec7 None\cf0 \strokec4 , \cf5 \strokec5 "b_img_size"\cf0 \strokec4 : b_img_size, \cf5 \strokec5 "b_pos"\cf0 \strokec4 : b_pos, \cf5 \strokec5 "b_emoji"\cf0 \strokec4 : b_emoji\cb1 \
\cb3         \}\cb1 \
\
\cb3         this_price = calculate_item_price(current_item_temp)\cb1 \
\cb3         st.metric(\cf5 \strokec5 "Current Design Value"\cf0 \strokec4 , \cf7 \strokec7 f\cf5 \strokec5 "\cf0 \strokec4 \{this_price\cf10 \strokec10 :,\cf0 \strokec4 \}\cf5 \strokec5  KRW"\cf0 \strokec4 )\cb1 \
\
\cb3         col_btn1, col_btn2 = st.columns(\cf10 \strokec10 2\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 with\cf0 \strokec4  col_btn1:\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  st.button(\cf5 \strokec5 "\uc0\u55357 \u57042  Add This Design to Cart"\cf0 \strokec4 , \cf11 \strokec11 type\cf0 \strokec4 =\cf5 \strokec5 "secondary"\cf0 \strokec4 , use_container_width=\cf7 \strokec7 True\cf0 \strokec4 ):\cb1 \
\cb3                 st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ].append(current_item_temp)\cb1 \
\cb3                 st.success(\cf7 \strokec7 f\cf5 \strokec5 "Success! Shirt #\cf0 \strokec4 \{\cf8 \strokec8 len\cf0 \strokec4 (st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ])\}\cf5 \strokec5  added with size specifications."\cf0 \strokec4 )\cb1 \
\cb3                 st.rerun()\cb1 \
\
\cb3         \cf2 \strokec2 with\cf0 \strokec4  col_btn2:\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  st.button(\cf5 \strokec5 "\uc0\u9989  Checkout All Items \u10132 "\cf0 \strokec4 , \cf11 \strokec11 type\cf0 \strokec4 =\cf5 \strokec5 "primary"\cf0 \strokec4 , use_container_width=\cf7 \strokec7 True\cf0 \strokec4 ):\cb1 \
\cb3                 \cf2 \strokec2 if\cf0 \strokec4  \cf7 \strokec7 not\cf0 \strokec4  st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ] \cf7 \strokec7 and\cf0 \strokec4  (f_txt \cf7 \strokec7 or\cf0 \strokec4  f_img \cf7 \strokec7 or\cf0 \strokec4  f_emoji != \cf5 \strokec5 "None"\cf0 \strokec4  \cf7 \strokec7 or\cf0 \strokec4  b_txt \cf7 \strokec7 or\cf0 \strokec4  b_img \cf7 \strokec7 or\cf0 \strokec4  b_emoji != \cf5 \strokec5 "None"\cf0 \strokec4 ):\cb1 \
\cb3                     st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ].append(current_item_temp)\cb1 \
\
\cb3                 \cf2 \strokec2 if\cf0 \strokec4  \cf7 \strokec7 not\cf0 \strokec4  st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ]:\cb1 \
\cb3                     st.error(\cf5 \strokec5 "Your cart is empty. Please add at least one design before checkout."\cf0 \strokec4 )\cb1 \
\cb3                 \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3                     go_to_step(\cf5 \strokec5 "Step 2: Finalize Order"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 # --- MULTI-ITEM DIGITAL RECEIPT ---\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 elif\cf0 \strokec4  st.session_state[\cf5 \strokec5 'current_step'\cf0 \strokec4 ] == \cf5 \strokec5 "Step 2: Finalize Order"\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.header(\cf5 \strokec5 "\uc0\u55358 \u56830  Step 2: Finalize Order"\cf0 \strokec4 )\cb1 \
\
\cb3     \cf2 \strokec2 if\cf0 \strokec4  \cf7 \strokec7 not\cf0 \strokec4  st.session_state.get(\cf5 \strokec5 'cart'\cf0 \strokec4 ):\cb1 \
\cb3         st.error(\cf5 \strokec5 "No active cart found. Please return to the Workshop."\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  st.button(\cf5 \strokec5 "Back to Workshop"\cf0 \strokec4 ): go_to_step(\cf5 \strokec5 "Step 1: Design Workshop"\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         st.balloons()\cb1 \
\cb3         cart_data = st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ]\cb1 \
\
\cb3         col_receipt_view, col_receipt_meta = st.columns([\cf10 \strokec10 1\cf0 \strokec4 , \cf10 \strokec10 1\cf0 \strokec4 ])\cb1 \
\
\cb3         \cf2 \strokec2 with\cf0 \strokec4  col_receipt_view:\cb1 \
\cb3             final_receipt = generate_jpeg_receipt(cart_data)\cb1 \
\cb3             st.image(final_receipt, width=\cf10 \strokec10 450\cf0 \strokec4 )\cb1 \
\
\cb3         \cf2 \strokec2 with\cf0 \strokec4  col_receipt_meta:\cb1 \
\cb3             st.markdown(\cf5 \strokec5 "### \uc0\u55356 \u57225  Purchase Complete!"\cf0 \strokec4 )\cb1 \
\cb3             st.write(\cf7 \strokec7 f\cf5 \strokec5 "Thank you for your order. We have successfully rendered a single receipt for all **\cf0 \strokec4 \{\cf8 \strokec8 len\cf0 \strokec4 (cart_data)\}\cf5 \strokec5  customized items** in your session."\cf0 \strokec4 )\cb1 \
\
\cb3             img_buffer = io.BytesIO()\cb1 \
\cb3             final_receipt.save(img_buffer, format=\cf5 \strokec5 'JPEG'\cf0 \strokec4 , quality=\cf10 \strokec10 95\cf0 \strokec4 )\cb1 \
\
\cb3             st.markdown(\cf5 \strokec5 "<br>"\cf0 \strokec4 , unsafe_allow_html=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\cb3             st.download_button(\cf5 \strokec5 "\uc0\u55357 \u56549  DOWNLOAD RECEIPT (.jpeg)"\cf0 \strokec4 , data=img_buffer.getvalue(), file_name=\cf5 \strokec5 "BEJIN_studio_receipt.jpg"\cf0 \strokec4 , mime=\cf5 \strokec5 "image/jpeg"\cf0 \strokec4 , use_container_width=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\
\cb3             \cf2 \strokec2 if\cf0 \strokec4  st.button(\cf5 \strokec5 "\uc0\u55357 \u56580  Design More Shirts (New Session)"\cf0 \strokec4 , use_container_width=\cf7 \strokec7 True\cf0 \strokec4 ):\cb1 \
\cb3                 st.session_state[\cf5 \strokec5 'cart'\cf0 \strokec4 ] = []\cb1 \
\cb3                 go_to_step(\cf5 \strokec5 "Step 1: Design Workshop"\cf0 \strokec4 )\cb1 \
}