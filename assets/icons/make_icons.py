"""Icons for the libraries table, in the style of assets/banner-dark.svg: slate tile, ambient glow, gradient glyph.
Run in assets/icons: python make_icons.py  (writes <lib>.svg and <lib>.png; PNG needs playwright)."""
import asyncio, pathlib, sys

CYAN = ("#38BDF8", "#818CF8"); MINT = ("#34D399", "#38BDF8"); VIOLET = ("#818CF8", "#C084FC"); SUN = ("#FBBF24", "#F43F5E")
W = 'stroke="url(#g)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none"'
F = 'fill="url(#g)"'
T = 'font-family="-apple-system, Segoe UI, Roboto, DejaVu Sans, sans-serif" font-weight="800" text-anchor="middle"'
HOLE = 'fill="#0F172A"'
icons = {
 "scrapladder": (CYAN, f'''<path d="M88 52V204 M168 52V204" {W}/><path d="M88 76H168 M88 112H168 M88 148H168 M88 184H168" {W} stroke-width="8"/>
<circle cx="168" cy="76" r="14" fill="#FBBF24" stroke="#0F172A" stroke-width="5"/>'''),
 "transcriptladder": (SUN, f'''<path d="M48 98V118 M70 82V134 M92 66V150 M114 88V128" {W}/><path d="M140 76H208 M140 108H208 M140 140H190" {W}/>
<path d="M56 186H200" {W} stroke-width="7" opacity=".55"/>'''),
 "DedupKit": (MINT, f'''<rect x="44" y="60" width="96" height="120" rx="14" {W}/><rect x="116" y="76" width="96" height="120" rx="14" {W} {HOLE.replace('fill','fill')}/>
<rect x="116" y="76" width="96" height="120" rx="14" {W}/><path d="M140 140l18 18 34-36" {W}/>'''),
 "llm-cost-kit": (CYAN, f'''<circle cx="100" cy="116" r="56" {W}/><text x="100" y="142" {T} font-size="70" {F}>$</text>
<path d="M178 200V170 M200 200V146 M222 200V118" {W} stroke-width="12"/>'''),
 "llm-batch-kit": (VIOLET, f'''<rect x="40" y="152" width="96" height="30" rx="8" {W}/><rect x="40" y="110" width="96" height="30" rx="8" {W}/>
<rect x="40" y="68" width="96" height="30" rx="8" {W}/><text x="186" y="125" {T} font-size="52" {F}>1</text>
<path d="M160 138H212" {W} stroke-width="8"/><text x="186" y="192" {T} font-size="52" {F}>2</text>'''),
 "SimilarImageFinder": (MINT, f'''<rect x="24" y="88" width="80" height="80" rx="12" {W}/><path d="M32 156l22-26 18 18 12-12 16 20" {W} stroke-width="7"/>
<rect x="152" y="88" width="80" height="80" rx="12" {W}/><path d="M160 156l22-26 18 18 12-12 16 20" {W} stroke-width="7"/>
<path d="M114 122q7-8 14 0t14 0 M114 140q7-8 14 0t14 0" {W} stroke-width="6"/>'''),
 "BrCommerceKit": (SUN, f'''<path d="M40 64H68L90 160H196L214 92H80" {W}/><circle cx="102" cy="190" r="12" {F}/><circle cx="182" cy="190" r="12" {F}/>
<text x="148" y="142" {T} font-size="34" {F}>R$</text>'''),
 "PtBr.Text": (VIOLET, f'''<text x="128" y="148" {T} font-size="96" {F}>Ãç</text><path d="M60 186H196" {W} stroke-width="8"/>'''),
 "pros-e-contras-ptbr": (MINT, f'''<circle cx="172" cy="128" r="46" {W} opacity=".5"/><path d="M150 128H194" {W} opacity=".5"/>
<circle cx="88" cy="128" r="46" {W} {HOLE}/><circle cx="88" cy="128" r="46" {W}/><path d="M88 106V150 M66 128H110" {W}/>'''),
 "DomainCheck": (CYAN, f'''<circle cx="116" cy="120" r="66" {W} stroke-width="8"/><ellipse cx="116" cy="120" rx="28" ry="66" {W} stroke-width="7"/>
<path d="M50 120H182 M62 86H170 M62 154H170" {W} stroke-width="7"/>
<circle cx="184" cy="184" r="34" fill="#0F172A" stroke="#34D399" stroke-width="7"/><path d="M168 184l11 11 21-22" stroke="#34D399" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'''),
 "ibge-nomes": (SUN, f'''<circle cx="96" cy="96" r="30" {W}/><path d="M44 196c4-38 26-58 52-58s48 20 52 58" {W}/>
<text x="188" y="128" {T} font-size="54" {F}>Aa</text><path d="M162 156H212 M162 180H200" {W} stroke-width="8"/>'''),
 "search-pattern-miner": (VIOLET, f'''<path d="M36 74H104 M36 116H96 M36 158H104" {W} stroke-width="8" opacity=".7"/>
<path d="M112 80l26 36-26 36" {W} stroke-width="8"/>
<path d="M172 60H154V172H172 M206 60H224V172H206" {W}/><circle cx="189" cy="116" r="9" {F}/>
<path d="M60 206H196" {W} stroke-width="7" opacity=".55"/>'''),
}


def svg(name: str) -> str:
    (a, b), body = icons[name]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256" role="img" aria-label="{name}">
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B1120"/><stop offset=".5" stop-color="#0F172A"/><stop offset="1" stop-color="#020617"/></linearGradient>
 <linearGradient id="g" gradientUnits="userSpaceOnUse" x1="40" y1="40" x2="216" y2="216"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>
 <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="34"/></filter>
 <filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="7"/></filter>
 <clipPath id="tile"><rect width="256" height="256" rx="44"/></clipPath>
</defs>
<rect width="256" height="256" rx="44" fill="url(#bg)"/>
<g clip-path="url(#tile)">
 <circle cx="40" cy="30" r="90" fill="{a}" opacity=".28" filter="url(#blur)"/>
 <circle cx="230" cy="236" r="90" fill="{b}" opacity=".24" filter="url(#blur)"/>
</g>
<rect x="1" y="1" width="254" height="254" rx="43" fill="none" stroke="#334155" stroke-width="2"/>
<g transform="translate(128 128) scale(.78) translate(-128 -128)">
 <g filter="url(#soft)" opacity=".55">{body}</g>
 {body}
</g>
</svg>
'''


async def png(names, out):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(); pg = await br.new_page(viewport={"width": 256, "height": 256}, device_scale_factor=2)
        for n in names:
            await pg.set_content(f'<html><body style="margin:0;background:transparent">{svg(n)}</body></html>')
            await pg.screenshot(path=str(out / f"{n}.png"), omit_background=True, clip={"x": 0, "y": 0, "width": 256, "height": 256})
        await br.close()


if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out.mkdir(exist_ok=True)
    for n in icons:
        (out / f"{n}.svg").write_text(svg(n), encoding="utf-8")
    asyncio.run(png(list(icons), out))
