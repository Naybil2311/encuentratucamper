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
        print("Error: No se encontró la variable APIFY_TOKEN en los Secrets de GitHub.")
        return []

    url_apify = f"https://api.apify.com/v2/acts/apify~wallapop-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"
    
    payload = {
        "searchKeywords": "camper autocaravana",
        "maxItems": 10
    }
    
    anuncios = []
    try:
        print("Llamando a Apify para extraer ofertas de la red...")
        res = requests.post(url_apify, json=payload, timeout=90)
        if res.status_code in [200, 201]:
            items = res.json()
            for item in items:
                titulo = item.get("title", "Camper Segunda Mano")
                precio = item.get("price", 25000)
                if isinstance(precio, dict):
                    precio = precio.get("amount", 25000)
                
                anuncios.append({
                    "title": str(titulo)[:60],
                    "price": int(precio) if str(precio).isdigit() else 25000,
                    "location": item.get("location", {}).get("city", "España") if isinstance(item.get("location"), dict) else "España",
                    "year": 2020,
                    "km": 80000,
                    "sleeps": 4,
                    "type": clasificar_vehiculo(titulo),
                    "image": item.get("images", [{}])[0].get("original_url", "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80") if isinstance(item.get("images"), list) and len(item.get("images")) > 0 else "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80",
                    "seller_type": "Particular",
                    "source": "Wallapop (Apify)"
                })
            print(f"Obtenidos {len(anuncios)} anuncios desde Apify.")
        else:
            print(f"Respuesta Apify status: {res.status_code}")
    except Exception as e:
        print(f"Error consultando Apify: {e}")
        
    return anuncios

# --- EJECUCIÓN PRINCIPAL ---
print("Iniciando Bot Integrado Apify + Supabase...")

anuncios_nuevos = obtener_anuncios_apify()

if anuncios_nuevos:
    for a in anuncios_nuevos:
        try:
            r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers_supabase)
            print(f"✓ [{r.status_code}] Insertado: {a['title']}")
        except Exception as e:
            print(f"Error enviando a Supabase: {e}")
else:
    print("No se obtuvieron anuncios nuevos en esta ejecución.")

print("Proceso completado.")
