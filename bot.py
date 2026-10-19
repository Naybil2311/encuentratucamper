import os
import requests

SUPABASE_URL = "https://agazyoihnkienkywbpxe.supabase.co"
SUPABASE_KEY = "sb_publishable_eCIDgVWRog9savmDZJ1Z-Q_RRYIHMj4"

headers_supabase = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

# Imágenes de vehículos camper reales con acceso CDN universal
catalogo_garantizado = [
    {
        "title": "Volkswagen California T6.1 Ocean DSG 150CV 2021",
        "price": 58900, "location": "Barcelona", "year": 2021, "km": 42000,
        "type": "Furgoneta Camper",
        "image": "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=800&q=80",
        "url": "https://es.wallapop.com/search?keywords=volkswagen%20california",
        "source": "Wallapop"
    },
    {
        "title": "Fiat Ducato Maxi L3H2 Camperizada Homologada",
        "price": 38500, "location": "Madrid", "year": 2020, "km": 88000,
        "type": "Gran Volumen",
        "image": "https://images.unsplash.com/photo-1527786356703-4b100091cd2c?auto=format&fit=crop&w=800&q=80",
        "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/fiat-ducato-camper.htm",
        "source": "Milanuncios"
    },
    {
        "title": "Mercedes-Benz Marco Polo V250d 4Matic",
        "price": 64000, "location": "Bilbao", "year": 2022, "km": 31000,
        "type": "Furgoneta Camper",
        "image": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=800&q=80",
        "url": "https://es.wallapop.com/search?keywords=mercedes%20marco%20polo",
        "source": "Wallapop"
    },
    {
        "title": "Autocaravana Benimar Tessoro 481 Perfilada",
        "price": 49500, "location": "Valencia", "year": 2019, "km": 65000,
        "type": "Autocaravana",
        "image": "https://images.unsplash.com/photo-1566847438217-76e82d383f84?auto=format&fit=crop&w=800&q=80",
        "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/benimar.htm",
        "source": "Milanuncios"
    }
]

print("Iniciando carga de anuncios...")
guardados = 0
for a in catalogo_garantizado:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers_supabase)
        if r.status_code in [200, 201]:
            guardados += 1
            print(f"✓ Guardado: {a['title']}")
    except Exception as e:
        print(f"Error: {e}")

print(f"Completado. Anuncios listos: {guardados}")
