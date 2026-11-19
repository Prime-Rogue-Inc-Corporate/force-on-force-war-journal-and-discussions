"""Draw the Case 1 memes as images.

The captions were written by AI agents (see cases/001). The pictures are drawn here, in code, from each agent's
one-line description of its image. Writes memes/001/<nn>-<slug>.png.

    python tools/make_memes.py        # needs playwright and a Chrome; fonts.css (the site's Archivo) is optional
"""
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "memes" / "001"
INK, US, CA = "#16212a", "#1f5fa8", "#c8322b"
W, SH = 1200, 800          # scene is 1200 x 800; the caption band sits under it


def svg(body, bg="#dfe6d4"):
    return f'<svg viewBox="0 0 {W} {SH}" width="{W}" height="{SH}" xmlns="http://www.w3.org/2000/svg"><rect width="{W}" height="{SH}" fill="{bg}"/>{body}</svg>'


def box(x, y, w, h, html, style=""):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}">{html}</div>'


LEAF = "M0-26l6 11 9-4-3 16 10-7 2 7 11 0-7 9 5 4-17 11 2 9-14-3v14h-8v-14l-14 3 2-9-17-11 5-4-7-9 11 0 2-7 10 7-3-16 9 4z"


def flag(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect width="120" height="64" fill="#fff"/><rect width="30" height="64" fill="{CA}"/>'
            f'<rect x="90" width="30" height="64" fill="{CA}"/><path d="{LEAF}" transform="translate(60 33) scale(.82)" fill="{CA}"/></g>')


def cork(body):
    dots = "".join(f'<circle cx="{(i * 97) % 1200}" cy="{(i * 61) % 800}" r="2" fill="#a67f4a" opacity=".5"/>' for i in range(160))
    return svg(dots + body, "#c9a26b")


def paper(x, y, w, h, rot=0, fill="#fffdf6", pin=True):
    p = f'<circle cx="{x + w / 2}" cy="{y + 12}" r="8" fill="{CA}" stroke="#7f1d18" stroke-width="2"/>' if pin else ""
    return f'<g transform="rotate({rot} {x + w / 2} {y + h / 2})"><rect x="{x + 5}" y="{y + 6}" width="{w}" height="{h}" fill="#000" opacity=".18"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>{p}</g>'


def truck(x, y, s=1.0, c="#5d6b4f"):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="0" y="-52" width="110" height="52" fill="{c}"/><rect x="112" y="-38" width="38" height="38" fill="{c}"/>'
            f'<rect x="120" y="-32" width="22" height="14" fill="#cfe0ea"/><circle cx="28" cy="2" r="13" fill="{INK}"/><circle cx="84" cy="2" r="13" fill="{INK}"/><circle cx="130" cy="2" r="13" fill="{INK}"/></g>')


def person(x, y, s=1.0, c=INK, cap=False, helmet=False):
    hat = '<path d="M-22-96h44l12 6h-30z M-22-96a22 20 0 0 1 44 0z" fill="#3d6f8f"/>' if cap else ""
    hel = '<path d="M-26-88a26 26 0 0 1 52 0z" fill="#5d6b4f"/>' if helmet else ""
    return (f'<g transform="translate({x} {y}) scale({s})"><circle cx="0" cy="-80" r="20" fill="#e2b48c"/>{hat}{hel}'
            f'<path d="M-34 0c0-40 14-56 34-56s34 16 34 56z" fill="{c}"/></g>')


def scene_sequel():
    left = (f'<rect x="40" y="60" width="520" height="680" fill="#b8892f"/><rect x="62" y="82" width="476" height="636" fill="#131a33"/>'
            '<rect x="150" y="430" width="300" height="170" fill="#f4f1e6"/><path d="M130 430h340l-170-80z" fill="#f4f1e6"/>'
            + "".join(f'<rect x="{168 + i * 46}" y="450" width="18" height="150" fill="#d9d3c0"/>' for i in range(6))
            + '<rect x="62" y="600" width="476" height="118" fill="#0d1226"/>'
            + "".join(f'<path d="M{170 + i * 55} 440c-30-60 20-90 0-150 50 40 60 90 30 150z" fill="#f08a1c"/><path d="M{182 + i * 55} 440c-14-34 10-52 2-86 26 24 30 52 14 86z" fill="#ffd34d"/>' for i in range(5)))
    right = ('<defs><linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3b3f6b"/><stop offset=".6" stop-color="#e58a5b"/><stop offset="1" stop-color="#f6c98a"/></linearGradient>'
             '<filter id="blur"><feGaussianBlur stdDeviation="2.2"/></filter></defs>'
             '<g filter="url(#blur)"><rect x="640" y="60" width="520" height="680" fill="url(#dusk)"/><rect x="640" y="600" width="520" height="140" fill="#3a3a3a"/>'
             '<rect x="690" y="380" width="330" height="26" fill="#e8e8e8"/><rect x="710" y="406" width="14" height="194" fill="#bbb"/><rect x="986" y="406" width="14" height="194" fill="#bbb"/>'
             '<rect x="790" y="520" width="46" height="80" fill="#c8322b"/><rect x="880" y="520" width="46" height="80" fill="#c8322b"/>'
             '<rect x="1070" y="250" width="12" height="350" fill="#888"/><rect x="1030" y="250" width="92" height="120" fill="#16212a"/>'
             '<text x="1076" y="300" font-size="30" fill="#ffd34d" text-anchor="middle" font-weight="800">3.89</text><text x="1076" y="344" font-size="30" fill="#ffd34d" text-anchor="middle" font-weight="800">4.19</text>'
             + flag(1016, 176, 1.0) + '</g>')
    return svg(left + right, INK)


def scene_plaque():
    siding = "".join(f'<path d="M0 {y}H1200" stroke="#cdbf9f" stroke-width="3"/>' for y in range(40, 800, 46))
    vend = ('<rect x="900" y="190" width="240" height="560" rx="10" fill="#27445e"/><rect x="924" y="220" width="150" height="330" fill="#9fc3da"/>'
            + "".join(f'<rect x="{936 + c * 46}" y="{240 + r * 76}" width="32" height="52" rx="5" fill="{col}"/>' for r in range(4) for c, col in enumerate(["#e8b23a", CA, "#5aa469"]))
            + '<rect x="1090" y="240" width="30" height="120" fill="#16212a"/><rect x="924" y="600" width="150" height="60" fill="#16212a"/>')
    return (svg(siding + vend + '<rect x="110" y="170" width="700" height="430" rx="16" fill="#6b4a1e"/><rect x="128" y="188" width="664" height="394" rx="10" fill="#b07a34"/>'
                + "".join(f'<circle cx="{cx}" cy="{cy}" r="9" fill="#5a3c14"/>' for cx, cy in ((150, 210), (770, 210), (150, 560), (770, 560))), "#e6dcc3")
            + box(160, 225, 600, 330, 'ON THIS SITE<br>NOTHING WAS BURNED<div style="font-size:26px;letter-spacing:.06em;margin-top:22px;font-weight:600">SWEET GRASS PORT OF ENTRY</div>',
                  "font:800 52px/1.15 var(--f);color:#3d2a0d;text-align:center;letter-spacing:.03em;display:flex;flex-direction:column;justify-content:center"))


def scene_corkboard():
    cards = [(60, 60, 250, 170, -4), (360, 40, 220, 150, 3), (900, 60, 240, 180, 5), (70, 330, 230, 170, 4), (920, 340, 220, 170, -5), (380, 560, 200, 130, -3), (700, 540, 230, 150, 4)]
    body = "".join(paper(*c, fill=f) for c, f in zip(cards, ["#dbe7d0", "#fffdf6", "#cfe0ea", "#fffdf6", "#dbe7d0", "#f3e3a8", "#fffdf6"]))
    body += "".join(f'<path d="M{x + w / 2} {y + 12}L600 330" stroke="{CA}" stroke-width="4"/>' for x, y, w, h, r in cards)
    body += paper(480, 270, 240, 140, 0, "#fff") + '<text x="600" y="368" text-anchor="middle" font-size="84" font-weight="800" fill="#16212a">1814</text>'
    body += "".join(f'<path d="M{x + 30} {y + 60}h{w - 60}M{x + 30} {y + 90}h{w - 90}" stroke="#9aa5ad" stroke-width="6"/>' for x, y, w, h, r in cards)
    return cork(body + '<rect x="0" y="720" width="1200" height="80" fill="#6b4a1e"/>' + person(170, 800, 1.9, "#2f3f52"))


def scene_booth():
    convoy = "".join(truck(560 + i * 118, 610 - i * 34, 1.0 - i * .13) for i in range(5))
    return svg('<rect y="560" width="1200" height="240" fill="#8d8d8d"/><path d="M0 660H1200" stroke="#f4f1e6" stroke-width="6" stroke-dasharray="40 30"/>' + convoy
               + '<rect x="70" y="250" width="330" height="420" fill="#f4f1e6" stroke="#16212a" stroke-width="5"/><rect x="40" y="215" width="390" height="46" fill="#1f5fa8"/>'
               '<rect x="130" y="320" width="210" height="170" fill="#bfd8e6" stroke="#16212a" stroke-width="5"/>' + person(235, 490, 1.25, "#5d6b4f", helmet=True)
               + '<rect x="300" y="430" width="90" height="60" fill="#fff" stroke="#16212a" stroke-width="3" transform="rotate(-12 345 460)"/><path d="M312 446h60M312 462h60M312 478h40" stroke="#9aa5ad" stroke-width="4" transform="rotate(-12 345 460)"/>'
               '<rect x="455" y="535" width="16" height="130" fill="#16212a"/><rect x="455" y="535" width="330" height="16" fill="#c8322b"/>', "#bcd6e8")


def scene_form():
    rows = [("GOODS ACQUIRED ABROAD / MARCHANDISES ACQUISES", "1 HAMLET, 1 CUSTOMS POST, 1 TRUCK STOP, 1 INTERSTATE (PARTIAL)"),
            ("LENGTH OF ABSENCE / DURÉE DE L'ABSENCE", "UNDER 24 HOURS"), ("PERSONAL EXEMPTION / EXEMPTION PERSONNELLE", "NONE"), ("DUTY OWING / DROITS À PAYER", "ON THE FULL AMOUNT")]
    f = "".join(f'<div style="border-top:2px solid #16212a;padding:10px 0 12px"><div style="font:700 15px var(--f);color:#44535d">{e(a)}</div>'
                f'<div style="font:700 27px/1.2 ui-monospace,Menlo,monospace;color:#1c3f8f;margin-top:6px">{e(b)}</div></div>' for a, b in rows)
    return (svg('<rect x="120" y="50" width="900" height="720" fill="#000" opacity=".2" transform="rotate(-2.500 570 410)"/>', "#8a6a44")
            + box(110, 40, 900, 720, f'<div style="font:800 34px var(--f);margin-bottom:14px">DECLARATION CARD / CARTE DE DÉCLARATION</div>{f}',
                  "background:#fffdf6;padding:34px 44px;box-sizing:border-box;transform:rotate(-2.500deg)")
            + box(820, 40, 190, 190, "", "border:14px solid #7a4a1c;border-radius:50%;opacity:.45;box-sizing:border-box"))


def scene_notice():
    cat = ('<circle cx="170" cy="330" r="46" fill="#16212a"/><path d="M132 300l8-44 28 30zM208 300l-8-44-28 30z" fill="#16212a"/><ellipse cx="170" cy="420" rx="60" ry="50" fill="#16212a"/>'
           '<text x="170" y="250" text-anchor="middle" font-size="36" font-weight="800" fill="#c8322b">LOST CAT</text>')
    tire = ('<circle cx="1030" cy="360" r="78" fill="#16212a"/><circle cx="1030" cy="360" r="40" fill="#bbb"/><text x="1030" y="250" text-anchor="middle" font-size="27" font-weight="800" fill="#16212a">TIRE ROTATION</text>'
            '<text x="1030" y="500" text-anchor="middle" font-size="40" font-weight="800" fill="#c8322b">$29.99</text>')
    body = paper(60, 190, 220, 330, -4) + cat + paper(910, 190, 240, 350, 3, "#f3e3a8") + tire + paper(330, 90, 540, 600, 0, "#fff") + '<path d="M330 90l150 0-150 220z" fill="#fff" opacity=".0"/>'
    return (cork(body) + box(360, 130, 480, 540, 'NOTICE TO ALL 65 RESIDENTS<div style="font:600 25px/1.35 var(--f);margin-top:18px;text-align:left">Service is available in the official language of your choice.<br><br>Interstate 15 is closed pending review.<br><br>Processing time: 6 to 8 weeks.<br><br>Do not call to ask about your file.</div>',
                             "font:800 34px/1.15 var(--f);color:#16212a;text-align:center"))


def scene_map():
    grid = "".join(f'<path d="M{x} 0V800" stroke="#cfd8c0" stroke-width="2"/>' for x in range(0, 1200, 80)) + "".join(f'<path d="M0 {y}H1200" stroke="#cfd8c0" stroke-width="2"/>' for y in range(0, 800, 80))
    city = "".join(f'<rect x="{760 + c * 44}" y="{130 + r * 44}" width="34" height="34" fill="#b9b2a3"/>' for r in range(4) for c in range(5))
    return svg(grid + '<path d="M0 560H1200" stroke="#16212a" stroke-width="4" stroke-dasharray="18 10"/>' + city
               + f'<path d="M560 760V400L500 400 870 200 760 380 700 380V760z" fill="{CA}" transform="rotate(8 700 500)"/>'
               '<text x="850" y="520" font-size="40" font-weight="800" fill="#c8322b">MAIN EFFORT</text>'
               '<text x="980" y="110" font-size="30" font-weight="800" fill="#16212a" text-anchor="middle">LETHBRIDGE</text>'
               f'<path d="M430 470C330 500 300 600 330 690" stroke="{US}" stroke-width="9" fill="none"/><path d="M312 672l22 34 18-36z" fill="{US}"/>'
               '<circle cx="336" cy="722" r="11" fill="#16212a"/><text x="360" y="734" font-size="28" font-weight="700" fill="#16212a">truck stop</text>', "#eef0e2")


def scene_highway():
    grass = "".join(f'<path d="M{(i * 53) % 1200} {560 + (i * 37) % 230}q14-8 26-26" stroke="#8a9a4a" stroke-width="4" fill="none"/>' for i in range(70))
    return svg('<rect y="380" width="1200" height="420" fill="#c7b458"/>' + grass + '<path d="M470 800L590 380h20L730 800z" fill="#5a5a5a"/><path d="M600 800V380" stroke="#f4f1e6" stroke-width="6" stroke-dasharray="46 40"/>'
               '<rect x="860" y="250" width="70" height="130" fill="#b5523a"/><path d="M850 250h90l-45-46z" fill="#8f3f2c"/><rect x="930" y="300" width="46" height="80" fill="#9c4631"/>'
               + truck(585, 470, .5) + truck(592, 428, .3) + truck(596, 404, .18) + '<circle cx="230" cy="150" r="60" fill="#fff3c4"/>', "#a9cfe6")


def scene_whiteboard():
    col = lambda t, items: f'<div style="flex:1;padding:0 26px"><div style="font:800 46px var(--f);border-bottom:6px solid {INK};padding-bottom:8px;margin-bottom:16px">{t}</div>' + "".join(f'<div style="margin:9px 0">{e(i)}</div>' for i in items) + "</div>"
    them = col("THEM", ["1 city", "1 university", "1 very long bridge", "all of the wind", "Grade: C-minus"])
    us_ = col("US", ["65 residents", "1 customs booth", "1 diesel island", "hot showers", "Grade: A"])
    return (svg('<rect x="150" y="50" width="900" height="560" rx="10" fill="#fff" stroke="#9aa5ad" stroke-width="14"/><rect x="150" y="610" width="900" height="16" fill="#9aa5ad"/><path d="M600 80V590" stroke="#16212a" stroke-width="5"/>'
                + person(1090, 800, 2.1, "#3b5d3a", cap=True) + '<path d="M1040 610L930 470" stroke="#e2b48c" stroke-width="26" stroke-linecap="round"/>', "#d9d2c3")
            + box(170, 76, 860, 510, them + us_, "display:flex;font:600 36px/1.2 var(--f);color:#1c3f8f"))


def scene_pump4():
    clouds = "".join(f'<ellipse cx="{180 + i * 190}" cy="{170 + (i % 2) * 40}" rx="170" ry="70" fill="#4a5568"/>' for i in range(6))
    roller = ('<rect x="760" y="480" width="300" height="200" rx="10" fill="#c9c9c9" stroke="#16212a" stroke-width="5"/><rect x="780" y="500" width="260" height="110" fill="#fbe3a1"/>'
              + "".join(f'<rect x="792" y="{512 + i * 24}" width="236" height="15" rx="7" fill="#b5523a"/>' for i in range(4)) + '<rect x="820" y="630" width="180" height="26" fill="#16212a"/>')
    men = person(330, 700, 1.7, "#3d4a34", helmet=True) + person(450, 700, 1.9, "#3d4a34", helmet=True) + person(570, 700, 1.7, "#3d4a34", helmet=True)
    return svg('<rect x="30" y="30" width="1140" height="740" fill="#b8892f"/><rect x="60" y="60" width="1080" height="680" fill="#2a3246"/>' + clouds + '<rect x="60" y="640" width="1080" height="100" fill="#4c4534"/>'
               '<path d="M470 640V200" stroke="#d9d3c0" stroke-width="12"/>' + flag(476, 200, 1.9) + men + roller, INK)


def scene_scale():
    city = "".join(f'<rect x="{90 + c * 42}" y="{190 + r * 42}" width="32" height="32" fill="#a9a294"/>' for r in range(10) for c in range(10))
    lot = "".join(f'<path d="M{680 + i * 70} 190V610" stroke="#f4f1e6" stroke-width="10"/>' for i in range(7))
    return svg('<rect x="60" y="160" width="480" height="480" fill="#dfe6d4" stroke="#16212a" stroke-width="5"/>' + city + '<path d="M60 520C200 470 330 600 540 540" stroke="#7fa9c9" stroke-width="22" fill="none"/>'
               '<rect x="660" y="160" width="480" height="480" fill="#8d8d8d" stroke="#16212a" stroke-width="5"/>' + lot
               + '<rect x="1000" y="470" width="110" height="130" fill="#16212a"/><text x="1055" y="525" text-anchor="middle" font-size="26" font-weight="800" fill="#ffd34d">DIESEL</text><text x="1055" y="575" text-anchor="middle" font-size="40" font-weight="800" fill="#ffd34d">4.19</text>'
               '<text x="300" y="120" text-anchor="middle" font-size="40" font-weight="800" fill="#16212a">WHAT WE TOOK</text><text x="900" y="120" text-anchor="middle" font-size="40" font-weight="800" fill="#16212a">WHAT THEY TOOK</text>'
               '<text x="600" y="720" text-anchor="middle" font-size="34" font-weight="700" fill="#44535d">same scale*</text>', "#f3f6f7")


def scene_podium():
    return svg('<rect y="640" width="1200" height="160" fill="#8d8d8d"/><rect x="740" y="250" width="360" height="400" rx="8" fill="#eef4f8" stroke="#16212a" stroke-width="6"/>'
               '<text x="920" y="390" text-anchor="middle" font-size="110" font-weight="800" fill="#1f5fa8">ICE</text><rect x="770" y="440" width="140" height="180" fill="#bfd8e6" stroke="#16212a" stroke-width="4"/><rect x="930" y="440" width="140" height="180" fill="#bfd8e6" stroke="#16212a" stroke-width="4"/>'
               f'<rect x="80" y="70" width="1040" height="130" fill="{CA}"/><text x="600" y="158" text-anchor="middle" font-size="66" font-weight="800" fill="#fff">HISTORIC BREAKTHROUGH</text>'
               '<path d="M300 760l40-330h180l40 330z" fill="#6b4a1e"/><rect x="320" y="400" width="220" height="36" fill="#4d3413"/><path d="M430 400V330" stroke="#16212a" stroke-width="8"/><circle cx="430" cy="322" r="14" fill="#16212a"/>', "#cfc8b8")


def scene_slide():
    return svg('<rect x="60" y="50" width="1080" height="700" fill="#fff" stroke="#16212a" stroke-width="5"/><rect x="60" y="50" width="1080" height="96" fill="#16212a"/><text x="100" y="118" font-size="54" font-weight="800" fill="#fff">UPDATE</text>'
               f'<path d="M560 700V330h-70L620 190 750 330h-70V700z" fill="{US}"/><path d="M620 160l12 36h38l-31 22 12 36-31-22-31 22 12-36-31-22h38z" fill="#ffd34d" stroke="#16212a" stroke-width="3" transform="translate(0 -30)"/>'
               '<text x="800" y="200" font-size="40" font-weight="800" fill="#16212a">LETHBRIDGE</text>'
               f'<path d="M620 706c-34-44-34-76 0-76s34 32 0 76z" fill="{CA}" transform="translate(0 6) scale(1 1)"/><circle cx="620" cy="664" r="26" fill="{CA}"/><circle cx="620" cy="664" r="10" fill="#fff"/>'
               '<text x="680" y="680" font-size="34" font-weight="700" fill="#c8322b">them</text><text x="400" y="480" font-size="34" font-weight="700" fill="#1f5fa8">us</text>', "#3a4654")


def scene_receipt():
    items = [("AIRCRAFT CARRIERS x11", "$$$$$$$$"), ("SATELLITES", "$$$$$$$"), ("STEALTH AIRCRAFT", "$$$$$$$$$"), ("MISC. DRONES", "$$$$"), ("INVASION, ALBERTA", "$$$$$$"), ("1 x GUY TO WATCH MONTANA", "ITEM NOT PURCHASED")]
    rows = "".join(f'<div style="display:flex;justify-content:space-between;gap:18px;margin:14px 0;{"font-weight:800;border-top:3px dashed #16212a;padding-top:16px;color:#c8322b" if "GUY" in a else ""}"><span>{e(a)}</span><span>{e(b)}</span></div>' for a, b in items)
    return (svg("", "#6f7f8c") + box(330, -20, 540, 860, f'<div style="text-align:center;font-weight:800;font-size:34px;margin-bottom:20px">*** RECEIPT ***</div>{rows}<div style="text-align:center;margin-top:30px">THANK YOU. NO RETURNS.</div>',
                                    "background:#fffdf6;padding:60px 40px;box-sizing:border-box;font:600 26px/1.25 ui-monospace,Menlo,monospace;color:#16212a;box-shadow:10px 10px 0 rgba(0,0,0,.25)"))


def scene_sign():
    return (svg('<rect y="560" width="1200" height="240" fill="#5a5a5a"/><path d="M0 680H1200" stroke="#f4f1e6" stroke-width="7" stroke-dasharray="50 40"/><rect x="330" y="560" width="18" height="170" fill="#16212a"/><rect x="852" y="560" width="18" height="170" fill="#16212a"/>'
                '<rect x="250" y="110" width="700" height="460" rx="14" fill="#f08a1c" stroke="#16212a" stroke-width="10"/>', "#e7a56c")
            + box(270, 140, 660, 180, "I-15 NORTH<br>CLOSED", "font:800 78px/1.05 var(--f);text-align:center;color:#16212a")
            + box(300, 340, 600, 200, "DETOUR:<br>go back three weeks<br>and don't", "background:#fff;font:700 44px/1.15 var(--f);text-align:center;color:#16212a;padding:16px;box-sizing:border-box;transform:rotate(-2deg);box-shadow:4px 5px 0 rgba(0,0,0,.25)"))


def scene_marker():
    grass = "".join(f'<path d="M{(i * 41) % 1200} 800q10-50 30-90" stroke="#6f8a3a" stroke-width="7" fill="none"/>' for i in range(60))
    return (svg('<rect y="600" width="1200" height="200" fill="#93a54e"/><rect x="580" y="430" width="40" height="330" fill="#4d3413"/>' + grass
                + '<rect x="250" y="80" width="700" height="260" rx="14" fill="#5a4a36"/><rect x="290" y="370" width="620" height="170" rx="10" fill="#e9c46a" stroke="#fff3c4" stroke-width="8"/>', "#a9cfe6")
            + box(270, 110, 660, 200, "1890<br>RAILROAD ARRIVES", "font:800 64px/1.15 var(--f);text-align:center;color:#e6dcc3")
            + box(300, 388, 600, 140, "THIS WEEK<br>SECOND THING", "font:800 50px/1.15 var(--f);text-align:center;color:#3d2a0d"))


def scene_bulletin():
    cat = '<circle cx="170" cy="330" r="46" fill="#16212a"/><path d="M132 300l8-44 28 30zM208 300l-8-44-28 30z" fill="#16212a"/><ellipse cx="170" cy="420" rx="60" ry="50" fill="#16212a"/><text x="170" y="250" text-anchor="middle" font-size="36" font-weight="800" fill="#c8322b">LOST CAT</text>'
    body = paper(60, 190, 220, 330, -4) + cat + paper(920, 230, 230, 240, 4, "#f3e3a8") + paper(330, 90, 540, 600, 0, "#fff")
    return (cork(body) + box(940, 290, 190, 160, "HAY<br>for sale<br>call Dale", "font:italic 700 34px/1.2 Georgia,serif;color:#1c3f8f;text-align:center;transform:rotate(4deg)")
            + box(370, 140, 460, 520, 'TOWN MEETING<br>TUESDAY<div style="font:500 28px/1.4 ui-monospace,Menlo,monospace;margin-top:26px;text-align:left">Item 1: the occupation.<br><br>Item 2: who is plowing the frontage road now.<br><br>Please budget most of the evening for Item 2.</div>',
                  "font:800 40px/1.15 ui-monospace,Menlo,monospace;color:#16212a;text-align:center"))


def scene_phone():
    msgs = ["u ok??", "are you ok", "saw the news. you alive?", "call your mother", "ARE THE CANADIANS AT YOUR HOUSE", "u ok", "hello???", "is the highway open"]
    bub = "".join(f'<div style="background:#e6e9ee;border-radius:22px;padding:10px 18px;margin:9px 0;width:fit-content;max-width:330px">{e(m)}</div>' for m in msgs)
    return (svg('<rect y="520" width="1200" height="280" fill="#c7b458"/><path d="M620 800L820 520h60L1200 760v40z" fill="#5a5a5a"/><rect x="60" y="540" width="420" height="150" fill="#27445e"/><rect x="60" y="690" width="420" height="30" fill="#16212a"/>'
                + person(250, 560, 1.6, "#7a4a1c", cap=True), "#a9cfe6")
            + box(700, 40, 420, 720, f'<div style="font:800 24px var(--f);text-align:center;margin-bottom:8px">Messages (11)</div>{bub}',
                  "background:#fff;border:14px solid #16212a;border-radius:44px;padding:26px 24px;box-sizing:border-box;font:500 23px/1.2 var(--f);color:#16212a;overflow:hidden"))


MEMES = [
    ("sequel", "ca", "The history nerd", scene_sequel, "1814 / THE SEQUEL. Smaller budget. Same creative vision."),
    ("plaque", "ca", "The history nerd", scene_plaque, "It is a customs post. There are forms in there we might need. Progress since 1814: measurable."),
    ("corkboard", "ca", "The history nerd", scene_corkboard, "Me, three weeks into explaining that closing one interstate exit is a direct continuation of British amphibious doctrine."),
    ("purpose-of-trip", "ca", "The bureaucrat", scene_booth, "\"Purpose of your trip?\" \"Invasion.\" \"Is that business or pleasure, sir. / Affaires ou agrément, monsieur.\""),
    ("declaration", "ca", "The bureaucrat", scene_form, "Goods acquired abroad: one interstate (partial). Duty owing on the full amount."),
    ("notice", "ca", "The bureaucrat", scene_notice, "Effective today you are entitled to service in the official language of your choice."),
    ("main-effort", "ca", "The southern Albertan", scene_map, "They took the city the trucks were driving to. We took the road the trucks were driving on. Enjoy Lethbridge. Hope you packed a lunch."),
    ("flanking-doctrine", "ca", "The southern Albertan", scene_highway, "Southern Alberta flanking doctrine: get on the highway, point south, do not turn for two hours. They never saw it coming, which is impressive, because out here you can see everything coming."),
    ("trade-grades", "ca", "The southern Albertan", scene_whiteboard, "Them, C-minus: they have to keep the wind. Us, A, and we are not giving the showers back."),
    ("pump-4", "us", "The war supporter", scene_pump4, "Historians will call it the Battle of Pump 4."),
    ("same-scale", "us", "The war supporter", scene_scale, "Today's territorial exchange. *We had to enlarge theirs until the diesel price was legible."),
    ("ice-machine", "us", "The war supporter", scene_podium, "Enemy announces the capture of one strategic ice machine and closes I-15, delaying a guy hauling drywall to Great Falls. Meanwhile, we have a city."),
    ("mixed-day", "us", "The war opponent", scene_slide, "We have taken Lethbridge. They have taken the road to Lethbridge. Staff is describing this as \"a mixed day.\""),
    ("receipt", "us", "The war opponent", scene_receipt, "Who is guarding Montana? We were offered the add-on at checkout and said \"no thanks, we're good.\""),
    ("detour", "us", "The war opponent", scene_sign, "Detour: go back three weeks and don't."),
    ("second-thing", "us", "The Montana local", scene_marker, "1890: Railroad arrives. THIS WEEK: Second thing."),
    ("town-meeting", "us", "The Montana local", scene_bulletin, "Please budget most of the evening for Item 2."),
    ("thoughts-and-prayers", "us", "The Montana local", scene_phone, "Eleven people have texted to ask if I'm okay. I'm fine. The interstate is not. Thoughts and prayers for the interstate."),
]


def page(slug, side, who, scene, cap, fonts):
    n = len(cap)
    size = 62 if n < 50 else 50 if n < 95 else 40 if n < 150 else 33
    return f"""<!doctype html><meta charset="utf-8"><style>{fonts}
:root{{--f:Archivo,"Arial Narrow",Arial,sans-serif}} body{{margin:0}} text{{font-family:var(--f)}}
#m{{width:{W}px;background:{INK};position:relative;font-family:var(--f)}}
.s{{position:relative;width:{W}px;height:{SH}px;overflow:hidden}}
.c{{padding:30px 46px 22px;color:#fff;font:800 {size}px/1.14 var(--f);text-align:center;text-wrap:balance}}
.f{{display:flex;justify-content:space-between;padding:0 46px 22px;color:#9fb0bb;font:600 19px/1 var(--f)}}
.f b{{color:{'#ff8f88' if side == 'ca' else '#8fbdf2'}}}</style>
<div id="m"><div class="s">{scene()}</div><div class="c">{e(cap)}</div>
<div class="f"><span><b>{e(who)}</b>, {'Canada' if side == 'ca' else 'United States'}</span><span>Force on Force war journal · Case 1 · caption by an AI agent · fiction</span></div></div>"""


def main():
    from playwright.sync_api import sync_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    fonts = (ROOT / "tools" / "fonts.css").read_text() if (ROOT / "tools" / "fonts.css").exists() else ""
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": W, "height": 1300})
        for i, (slug, side, who, scene, cap) in enumerate(MEMES, 1):
            pg.set_content(page(slug, side, who, scene, cap, fonts))
            pg.wait_for_timeout(120)
            pg.locator("#m").screenshot(path=str(OUT / f"{i:02d}-{slug}.png"))
        b.close()
    print(len(MEMES), "memes ->", OUT)


if __name__ == "__main__":
    main()
