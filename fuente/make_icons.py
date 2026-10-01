# Genera los íconos de la app (requiere Pillow). Solo hace falta si se cambia el diseño.
import os
from PIL import Image, ImageDraw
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
os.makedirs(OUT, exist_ok=True)
def icon(size, maskable=False, bg=(24,34,29)):
    S=size*4
    im=Image.new("RGBA",(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    if maskable: d.rectangle([0,0,S,S],fill=bg+(255,)); scale=0.60
    else: d.rounded_rectangle([0,0,S-1,S-1],radius=int(S*0.22),fill=bg+(255,)); scale=0.76
    cw=S*scale*0.40; ch=S*scale; x0=(S-cw)/2; y0=(S-ch)/2
    d.rounded_rectangle([x0,y0,x0+cw,y0+ch],radius=int(cw*0.3),fill=(10,14,12,255),outline=(70,84,77,255),width=int(S*0.012))
    cols=[(192,46,46),(219,101,20),(201,154,0),(47,133,69)]
    r=cw*0.27; gap=(ch-8*r)/5
    for i,c in enumerate(cols):
        cy=y0+gap*(i+1)+r*(2*i+1); cx=S/2
        d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=c+(255,))
    return im.resize((size,size),Image.LANCZOS)
for s in (192,512): icon(s).save(os.path.join(OUT,f"icon-{s}.png"))
icon(512,True).save(os.path.join(OUT,"icon-maskable-512.png"))
icon(180,True).convert("RGB").save(os.path.join(OUT,"apple-touch-icon.png"))
icon(64).save(os.path.join(OUT,"favicon-64.png"))
print("íconos generados en", OUT)
