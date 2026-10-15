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

def obtener_anuncios():
    anuncios = []
    
    # 1. Intentar Apify si hay Token
    if APIFY_TOKEN:
        url_apify = f"https://api.apify.com/v2/actors/louisdeconinck~wallapop-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"
        payload = {"keywords": "furgoneta camper", "maxItems": 5}
        try:
            res = requests.post(url_apify, json=payload, timeout=90)
            if res.status_code in [200, 201]:
                items = res.json()
                if isinstance(items, list):
                    for item in items:
                        titulo = item.get("title") or item.get("name") or "Camper Segunda Mano"
                        precio = item.get("price")
                        if isinstance(precio, dict):
                            precio = precio.get("amount", 25000)
                        elif not precio or not str(precio).replace('.','').isdigit():
                            precio = 25000
                        else:
                            precio = int(float(precio))

                        link_web = item.get("url") or item.get("web_url") or item.get("share_url") or item.get("link") or "https://wallapop.com"

                        anuncios.append({
                            "title": str(titulo)[:60],
                            "price": precio,
                            "location": "España",
                            "year": 2021,
                            "km": 65000,
                            "sleeps": 4,
                            "type": clasificar_vehiculo(titulo),
                            "image": "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80",
                            "url": link_web,
                            "seller_type": "Particular",
                            "source": "Wallapop"
                        })
        except Exception as e:
            print(f"Error Apify: {e}")

    # 2. Si Apify falla o no hay Token, usar datos de prueba CON URL
    if not anuncios:
        print("Añadiendo anuncios de prueba con URL rellena...")
        anuncios = [
            {
                "title": "Volkswagen California T6 Ocean (Prueba Link)",
                "price": 49000,
                "location": "Madrid",
                "year": 2020,
                "km": 50000,
                "sleeps": 4,
                "type": "Furgoneta Camper",
                "image": "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=800&q=80",
                "url": "https://wallapop.com",
                "seller_type": "Particular",
                "source": "Wallapop Test"
            }
        ]
        
    return anuncios

# --- EJECUCIÓN ---
print("Iniciando Bot...")
lista = obtener_anuncios()

for a in lista:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers_supabase)
        print(f"✓ [{r.status_code}] Guardado: {a['title']} | URL: {a['url']}")
    except Exception as e:
        print(f"Error: {e}")

print("Finalizado.")
