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

def obtener_imagen_item(item):
    """ Extrae la foto real del objeto devolviendo una URL válida """
    # 1. Campos directos o listas de imágenes
    images = item.get("images") or item.get("photos") or item.get("pictures")
    if isinstance(images, list) and len(images) > 0:
        first = images[0]
        if isinstance(first, dict):
            url = first.get("original_url") or first.get("url") or first.get("src") or first.get("big")
            if url: return url
        elif isinstance(first, str):
            return first if first.startswith("http") else f"https://{first}"

    # 2. Atributos directos de tipo string
    img_direct = item.get("image") or item.get("featured_image") or item.get("thumbnail") or item.get("picture")
    if isinstance(img_direct, str) and len(img_direct) > 5:
        return img_direct if img_direct.startswith("http") else f"https://{img_direct}"

    # Foto por defecto en caso de no venir especificada en la API
    return "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80"

def obtener_url_item(item):
    """ Extrae el enlace exacto a la publicación de Wallapop """
    link = item.get("web_url") or item.get("url") or item.get("share_url") or item.get("link") or item.get("item_url")
    if isinstance(link, str) and len(link) > 5:
        return link if link.startswith("http") else f"https://es.wallapop.com/item/{link}"
    
    # Si viene el ID del ítem, construimos la URL directa
    item_id = item.get("id") or item.get("item_id")
    if item_id:
        return f"https://es.wallapop.com/item/{item_id}"
        
    return "https://es.wallapop.com"

def obtener_catalogo():
    anuncios = []
    
    if not APIFY_TOKEN:
        print("Aviso: APIFY_TOKEN no configurado en Secrets.")
        return []

    busquedas = ["furgoneta camper", "autocaravana", "volkswagen california"]
    
    print("Iniciando extracción en Apify...")
    for kw in busquedas:
        try:
            url_apify = f"https://api.apify.com/v2/actors/louisdeconinck~wallapop-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"
            res = requests.post(url_apify, json={"keywords": kw, "maxItems": 10}, timeout=60)
            
            if res.status_code in [200, 201]:
                items = res.json()
                if isinstance(items, list) and len(items) > 0:
                    for item in items:
                        titulo = item.get("title") or item.get("name") or item.get("subject")
                        if not titulo: 
                            continue

                        # Extracción de Precio
                        precio = item.get("price")
                        if isinstance(precio, dict): 
                            precio = precio.get("amount", 20000)
                        elif not precio or not str(precio).replace('.','').isdigit(): 
                            precio = 20000
                        else: 
                            precio = int(float(precio))

                        # Extracción flexible de Imagen y Enlace
                        foto_url = obtener_imagen_item(item)
                        link_url = obtener_url_item(item)

                        anuncios.append({
                            "title": str(titulo)[:60],
                            "price": precio,
                            "location": item.get("location", {}).get("city") if isinstance(item.get("location"), dict) else "España",
                            "year": 2020,
                            "km": 85000,
                            "sleeps": 4,
                            "type": clasificar_vehiculo(str(titulo)),
                            "image": foto_url,
                            "url": link_url,
                            "seller_type": "Particular",
                            "source": "Wallapop"
                        })
                    print(f"✓ Extraídos {len(items)} anuncios para: '{kw}'")
                else:
                    print(f"Búsqueda '{kw}' no devolvió elementos.")
            else:
                print(f"Error HTTP {res.status_code} en Apify para '{kw}'.")
        except Exception as e:
            print(f"Excepción en búsqueda '{kw}': {e}")

    return anuncios

# --- EJECUCIÓN PRINCIPAL ---
print("Ejecutando bot de sincronización de anuncios...")
lista_anuncios = obtener_catalogo()

guardados = 0
for a in lista_anuncios:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers_supabase)
        if r.status_code in [200, 201]:
            guardados += 1
            print(f"✓ [{r.status_code}] Guardado: {a['title']} | Enlace: {a['url']}")
        else:
            print(f"× Error [{r.status_code}] al guardar en Supabase: {r.text}")
    except Exception as e:
        print(f"Error conectando a Supabase: {e}")

print(f"Proceso finalizado. Se han insertado {guardados} anuncios en Supabase.")
