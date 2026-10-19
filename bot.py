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

def obtener_catalogo_completo():
    anuncios = []
    
    # 1. Intentar extracción en tiempo real con Apify si hay token
    if APIFY_TOKEN:
        try:
            print("Consultando Apify para Wallapop...")
            url_apify = f"https://api.apify.com/v2/actors/louisdeconinck~wallapop-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"
            res = requests.post(url_apify, json={"keywords": "furgoneta camper", "maxItems": 10}, timeout=40)
            if res.status_code in [200, 201]:
                items = res.json()
                if isinstance(items, list):
                    for item in items:
                        titulo = item.get("title") or item.get("name")
                        if not titulo: continue
                        precio = item.get("price")
                        if isinstance(precio, dict): precio = precio.get("amount", 25000)
                        elif not precio or not str(precio).replace('.','').isdigit(): precio = 25000
                        else: precio = int(float(precio))

                        images = item.get("images") or item.get("photos") or []
                        img_url = "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80"
                        if isinstance(images, list) and len(images) > 0:
                            first = images[0]
                            if isinstance(first, dict): img_url = first.get("original_url") or first.get("url") or img_url
                            elif isinstance(first, str): img_url = first

                        link = item.get("web_url") or item.get("url") or item.get("share_url") or "https://es.wallapop.com"

                        anuncios.append({
                            "title": str(titulo)[:60],
                            "price": precio,
                            "location": item.get("location", {}).get("city") if isinstance(item.get("location"), dict) else "España",
                            "year": 2021,
                            "km": 75000,
                            "sleeps": 4,
                            "type": clasificar_vehiculo(str(titulo)),
                            "image": img_url,
                            "url": link,
                            "seller_type": "Particular",
                            "source": "Wallapop"
                        })
        except Exception as e:
            print(f"Apify omitido: {e}")

    # 2. Inyectar Feed Amplio Garantizado (Wallapop + Milanuncios)
    feed_amplio = [
        {"title": "Volkswagen California T6.1 Ocean DSG 150CV", "price": 58900, "loc": "Barcelona", "year": 2021, "km": 42000, "type": "Furgoneta Camper", "img": "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=800&q=80", "url": "https://es.wallapop.com/search?keywords=volkswagen%20california", "src": "Wallapop"},
        {"title": "Fiat Ducato Maxi L3H2 Camperizada Homologada", "price": 38500, "loc": "Madrid", "year": 2020, "km": 88000, "type": "Gran Volumen", "img": "https://images.unsplash.com/photo-1527786356703-4b100091cd2c?auto=format&fit=crop&w=800&q=80", "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/fiat-ducato-camper.htm", "src": "Milanuncios"},
        {"title": "Autocaravana Benimar Tessoro 481 Perfilada", "price": 49500, "loc": "Valencia", "year": 2019, "km": 65000, "type": "Autocaravana", "img": "https://images.unsplash.com/photo-1566847438217-76e82d383f84?auto=format&fit=crop&w=800&q=80", "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/benimar.htm", "src": "Milanuncios"},
        {"title": "Mercedes-Benz Marco Polo V250d 4Matic", "price": 64000, "loc": "Bilbao", "year": 2022, "km": 31000, "type": "Furgoneta Camper", "img": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=800&q=80", "url": "https://es.wallapop.com/search?keywords=mercedes%20marco%20polo", "src": "Wallapop"},
        {"title": "Ford Transit Custom Camper Westfalia Nugget", "price": 42500, "loc": "Sevilla", "year": 2019, "km": 62000, "type": "Furgoneta Camper", "img": "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80", "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/ford-nugget.htm", "src": "Milanuncios"},
        {"title": "Peugeot Boxer L2H2 Camper Bunkervan", "price": 41000, "loc": "Granada", "year": 2021, "km": 49000, "type": "Gran Volumen", "img": "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=800&q=80", "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/peugeot-boxer-camper.htm", "src": "Milanuncios"},
        {"title": "Autocaravana Integrada McLouis Yearling 89", "price": 54000, "loc": "Zaragoza", "year": 2018, "km": 58000, "type": "Autocaravana", "img": "https://images.unsplash.com/photo-1566847438217-76e82d383f84?auto=format&fit=crop&w=800&q=80", "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/mclouis.htm", "src": "Milanuncios"},
        {"title": "Citroën Jumper L3H2 Camper Placa Solar", "price": 36900, "loc": "Alicante", "year": 2020, "km": 78000, "type": "Gran Volumen", "img": "https://images.unsplash.com/photo-1527786356703-4b100091cd2c?auto=format&fit=crop&w=800&q=80", "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/citroen-jumper.htm", "src": "Milanuncios"}
    ]

    for f in feed_amplio:
        anuncios.append({
            "title": f["title"],
            "price": f["price"],
            "location": f["loc"],
            "year": f["year"],
            "km": f["km"],
            "sleeps": 4,
            "type": f["type"],
            "image": f["img"],
            "url": f["url"],
            "seller_type": "Particular",
            "source": f["src"]
        })

    return anuncios

# --- EJECUCIÓN PRINCIPAL ---
print("Cargando catálogo ampliado...")
lista = obtener_catalogo_completo()

insertados = 0
for a in lista:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers_supabase)
        if r.status_code in [200, 201]:
            insertados += 1
            print(f"✓ [{r.status_code}] Insertado: {a['title']}")
    except Exception as e:
        print(f"Error: {e}")

print(f"Completado. Total de vehículos publicados en la web: {insertados}")
