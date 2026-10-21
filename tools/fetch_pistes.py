"""Fetch ski piste + aerialway data from OpenStreetMap (Overpass) for the resorts
used on the site, and save simplified JSON to data/pistes-<key>.json.
Runs on GitHub Actions (see .github/workflows/pistes.yml)."""
import json, re, time, urllib.parse, urllib.request, os, sys

EPS = ['https://overpass-api.de/api/interpreter',
       'https://overpass.kumi.systems/api/interpreter',
       'https://maps.mail.ru/osm/tools/overpass/api/interpreter']
BROAD = (36.75, 138.65, 37.10, 139.00)   # Yuzawa / Minamiuonuma area
TARGETS = {
    'kagura':   {'re': r'かぐら|神楽|Kagura|みつまた|三俣|田代|Tashiro', 'fallback': (36.80, 138.70, 36.90, 138.83)},
    'ishiuchi': {'re': r'石打丸山|Ishiuchi Maruyama', 'fallback': (36.94, 138.78, 37.02, 138.88)},
    'kandatsu': {'re': r'神立|Kandatsu', 'fallback': (36.92, 138.80, 37.00, 138.92)},
}
PAD = 0.004

def overpass(q):
    last = None
    for attempt in range(3):
        for ep in EPS:
            try:
                data = urllib.parse.urlencode({'data': q}).encode()
                req = urllib.request.Request(ep, data=data, headers={'User-Agent': 'ski-trip-site/1.0 (github.com/Jerry-6969/ski-trip)'})
                with urllib.request.urlopen(req, timeout=120) as r:
                    return json.loads(r.read().decode())
            except Exception as e:
                last = e; print('  overpass fail', ep, e, file=sys.stderr)
        time.sleep(10)
    raise last

def bb(b): return f'{b[0]},{b[1]},{b[2]},{b[3]}'

def main():
    os.makedirs('data', exist_ok=True)
    log = []
    q = f'[out:json][timeout:90];(way["landuse"="winter_sports"]({bb(BROAD)});relation["landuse"="winter_sports"]({bb(BROAD)}););out tags bb;'
    areas = overpass(q).get('elements', [])
    log.append('## winter_sports areas in Yuzawa region')
    for a in areas:
        t = a.get('tags', {}); b = a.get('bounds') or {}
        log.append(f"- {a['type']}/{a['id']} name={t.get('name','')} name:en={t.get('name:en','')} bounds={b}")
    for key, cfg in TARGETS.items():
        hits = [a for a in areas if a.get('bounds') and re.search(cfg['re'], ' '.join([a.get('tags', {}).get(k, '') for k in ('name', 'name:en', 'name:ja', 'alt_name')]))]
        if hits:
            s = min(h['bounds']['minlat'] for h in hits) - PAD; w = min(h['bounds']['minlon'] for h in hits) - PAD
            n = max(h['bounds']['maxlat'] for h in hits) + PAD; e = max(h['bounds']['maxlon'] for h in hits) + PAD
            box = (round(s, 4), round(w, 4), round(n, 4), round(e, 4)); src = 'osm-area: ' + ', '.join(h.get('tags', {}).get('name', '') for h in hits)
        else:
            box = cfg['fallback']; src = 'fallback bbox'
        q = (f'[out:json][timeout:90];(way["piste:type"="downhill"]({bb(box)});relation["piste:type"="downhill"]({bb(box)});'
             f'way["aerialway"]["aerialway"!="station"]["aerialway"!="pylon"]({bb(box)}););out tags geom;')
        js = overpass(q)
        r5 = lambda x: round(x, 5)
        P, A = [], []
        for el in js.get('elements', []):
            t = el.get('tags', {})
            nm = t.get('piste:name') or t.get('name') or t.get('piste:ref') or t.get('ref') or ''
            g = lambda geom: [[r5(c['lat']), r5(c['lon'])] for c in (geom or []) if c]
            if el['type'] == 'way' and t.get('aerialway'):
                A.append({'n': nm, 'k': t['aerialway'], 'g': g(el.get('geometry'))}); continue
            if el['type'] == 'way':
                P.append({'n': nm, 'd': t.get('piste:difficulty', ''), 'g': g(el.get('geometry'))})
            if el['type'] == 'relation':
                for m in el.get('members', []):
                    if m.get('type') == 'way' and m.get('geometry'):
                        P.append({'n': nm, 'd': t.get('piste:difficulty', ''), 'g': g(m['geometry'])})
        P = [x for x in P if len(x['g']) > 1]; A = [x for x in A if len(x['g']) > 1]
        out = {'t': int(time.time() * 1000), 'bbox': box, 'src': src, 'p': P, 'a': A}
        with open(f'data/pistes-{key}.json', 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, separators=(',', ':'))
        log.append(f'\n## {key}: {len(P)} piste segments, {len(A)} aerialways, bbox={box} ({src})')
        names = {}
        for x in P: names.setdefault((x['n'], x['d']), 0); names[(x['n'], x['d'])] += 1
        for (nm, d), c in sorted(names.items(), key=lambda z: (z[0][1], z[0][0])): log.append(f'- piste [{d or "-"}] {nm or "(no name)"} x{c}')
        for x in A: log.append(f"- lift [{x['k']}] {x['n'] or '(no name)'}")
        time.sleep(5)
    with open('data/pistes-summary.md', 'w', encoding='utf-8') as f: f.write('\n'.join(log) + '\n')
    print('\n'.join(log))

if __name__ == '__main__':
    main()
