import os
import requests

SUPABASE_URL = "https://agazyoihnkienkywbpxe.supabase.co"
SUPABASE_KEY = "sb_publishable_eCIDgVWRog9savmDZJ1Z-Q_RRYIHMj4"
APIFY_TOKEN = os.getenv("APIFY_TOKEN")

headers_supabase = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

def clasificar_vehiculo(titulo):
    t = titulo.lower()
    if any(k in t for k in ["hymer", "benimar", "mclouis", "chausson", "burstner", "rimor", "capuchina", "perfilada"]):
        return "Autocaravana"
    elif any(k in t for k in ["ducato", "boxer", "jumper", "sprinter", "crafter", "master", "gran volumen", "l2h2", "l3h2"]):
        return "Gran Volumen"
    return "Furgoneta Camper"

def extraer_imagen_real(item):
    """ Busca recursivamente la imagen real en las distintas estructuras que devuelve Apify """
    # 1. Lista de imágenes
    images = item.get("images") or item.get("photos") or item.get("pictures")
    if isinstance(images, list) and len(images) > 0:
        first = images[0]
        if isinstance(first, dict):
            return first.get("original_url") or first.get("url") or first.get("src") or first.get("big")
        elif isinstance(first, str) and first.startswith("http"):
            return first
    
    # 2. String directo
    img_direct = item.get("image") or item.get("featured_image") or item.get("thumbnail")
    if isinstance(img_direct, str) and img_direct.startswith("http"):
        return img_direct
        
    return None

def extraer_link_real(item):
    """ Busca la URL exacta del anuncio individual """
    link = item.get("web_url") or item.get("url") or item.get("share_url") or item.get("link") or item.get("item_url")
    if isinstance(link, str) and link.startswith("http"):
        return link
    return None

def obtener_catalogo_real():
    anuncios = []
    
    if not APIFY_TOKEN:
        print("Aviso: No hay APIFY_TOKEN configurado.")
        return []

    busquedas = ["furgoneta camper", "autocaravana", "volkswagen california", "camper gran volumen"]
    
    print("Iniciando extracción profunda de fotos y enlaces en Apify...")
    for kw in busquedas:
        try:
            url_apify = f"https://api.apify.com/v2/actors/louisdeconinck~wallapop-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"
            res = requests.post(url_apify, json={"keywords": kw, "maxItems": 10}, timeout=60)
            
            if res.status_code in [200, 201]:
                items = res.json()
                if isinstance(items, list):
                    for item in items:
                        titulo = item.get("title") or item.get("name")
                        if not titulo: continue

                        # Precio
                        precio = item.get("price")
                        if isinstance(precio, dict): precio = precio.get("amount", 0)
                        elif not precio or not str(precio).replace('.','').isdigit(): precio = 0
                        else: precio = int(float(precio))

                        # Foto real y Link real
                        foto_real = extraer_imagen_real(item)
                        link_real = extraer_link_real(item)

                        # Omitir si no se encontró ni la foto real ni el link del anuncio
                        if not foto_real or not link_real:
                            continue

                        anuncios.append({
                            "title": str(titulo)[:60],
                            "price": precio,
                            "location": item.get("location", {}).get("city") if isinstance(item.get("location"), dict) else "España",
                            "year": 2020,
                            "km": 85000,
                            "sleeps": 4,
                            "type": clasificar_vehiculo(titulo),
                            "image": foto_real,
                            "url": link_real,
                            "seller_type": "Particular",
                            "source": "Wallapop"
                        })
                    print(f"✓ Extraídos {len(anuncios)} anuncios reales para la búsqueda: '{kw}'")
        except Exception as e:
            print(f"Error extrayendo búsqueda '{kw}': {e}")

    return anuncios

# --- EJECUCIÓN PRINCIPAL ---
print("Ejecutando actualización del catálogo...")
lista = obtener_catalogo_real()

guardados = 0
for a in lista:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers_supabase)
        if r.status_code in [200, 201]:
            guardados += 1
            print(f"✓ Guardado con éxito: {a['title']}")
            print(f"   └ Foto: {a['image'][:50]}...")
            print(f"   └ Link: {a['url']}")
    except Exception as e:
        print(f"Error al enviar a Supabase: {e}")

print(f"Proceso finalizado. Se han añadido {guardados} anuncios con imagen y link directo real.")
