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
    elif any(k in t for k in ["ducato", "boxer", "jumper", "sprinter", "crafter", "master", "gran volumen"]):
        return "Gran Volumen"
    return "Furgoneta Camper"

def obtener_anuncios_apify():
    if not APIFY_TOKEN:
        print("Aviso: No se encontro APIFY_TOKEN. Se omitira Apify.")
        return []

    url_apify = f"https://api.apify.com/v2/actors/louisdeconinck~wallapop-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"
    payload = {"keywords": "furgoneta camper", "maxItems": 10}
    
    anuncios = []
    try:
        res = requests.post(url_apify, json=payload, timeout=120)
        if res.status_code in [200, 201]:
            items = res.json()
            if isinstance(items, list):
                for item in items:
                    titulo = item.get("title") or item.get("name") or "Camper Segunda Mano"
                    
                    # Precio
                    precio = item.get("price")
                    if isinstance(precio, dict):
                        precio = precio.get("amount", 25000)
                    elif not precio or not str(precio).replace('.','').isdigit():
                        precio = 25000
                    else:
                        precio = int(float(precio))

                    # Imagen
                    imagen = "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80"
                    images_field = item.get("images") or item.get("photos")
                    if isinstance(images_field, list) and len(images_field) > 0:
                        first_img = images_field[0]
                        if isinstance(first_img, dict):
                            imagen = first_img.get("original_url") or first_img.get("url") or imagen
                        elif isinstance(first_img, str):
                            imagen = first_img

                    # Enlace real a Wallapop
                    link_web = item.get("web_url") or item.get("share_url") or item.get("url") or "https://wallapop.com"

                    anuncios.append({
                        "title": str(titulo)[:60],
                        "price": precio,
                        "location": "España",
                        "year": 2020,
                        "km": 85000,
                        "sleeps": 4,
                        "type": clasificar_vehiculo(titulo),
                        "image": imagen,
                        "url": link_web,  # <--- Guarda el enlace original aquí
                        "seller_type": "Particular",
                        "source": "Wallapop"
                    })
    except Exception as e:
        print(f"Error consultando Apify: {e}")
        
    return anuncios

# --- EJECUCIÓN ---
print("Iniciando Bot de Inserción...")
anuncios_totales = obtener_anuncios_apify()

for a in anuncios_totales:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers_supabase)
        print(f"✓ [{r.status_code}] Guardado: {a['title']} | URL: {a['url']}")
    except Exception as e:
        print(f"Error: {e}")

print("Proceso completado.")
