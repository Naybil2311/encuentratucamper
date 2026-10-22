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

# Imágenes distintas y específicas para cada tipo de vehículo
catalogo_real = [
    {
        "title": "Volkswagen California T6.1 Ocean DSG 150CV 2021",
        "price": 58900, "location": "Barcelona", "year": 2021, "km": 42000, "sleeps": 4,
        "type": "Furgoneta Camper",
        "image": "https://images.pexels.com/photos/2506923/pexels-photo-2506923.jpeg?auto=compress&cs=tinysrgb&w=800",
        "url": "https://es.wallapop.com/search?keywords=volkswagen%20california",
        "seller_type": "Particular", "source": "Wallapop"
    },
    {
        "title": "Fiat Ducato Maxi L3H2 Camperizada Homologada",
        "price": 38500, "location": "Madrid", "year": 2020, "km": 88000, "sleeps": 3,
        "type": "Gran Volumen",
        "image": "https://images.pexels.com/photos/1252399/pexels-photo-1252399.jpeg?auto=compress&cs=tinysrgb&w=800",
        "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/fiat-ducato-camper.htm",
        "seller_type": "Profesional", "source": "Milanuncios"
    },
    {
        "title": "Mercedes-Benz Marco Polo V250d 4Matic",
        "price": 64000, "location": "Bilbao", "year": 2022, "km": 31000, "sleeps": 4,
        "type": "Furgoneta Camper",
        "image": "https://images.pexels.com/photos/221433/pexels-photo-221433.jpeg?auto=compress&cs=tinysrgb&w=800",
        "url": "https://es.wallapop.com/search?keywords=mercedes%20marco%20polo",
        "seller_type": "Particular", "source": "Wallapop"
    },
    {
        "title": "Autocaravana Benimar Tessoro 481 Perfilada",
        "price": 49500, "location": "Valencia", "year": 2019, "km": 65000, "sleeps": 4,
        "type": "Autocaravana",
        "image": "https://images.pexels.com/photos/386009/pexels-photo-386009.jpeg?auto=compress&cs=tinysrgb&w=800",
        "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/benimar.htm",
        "seller_type": "Particular", "source": "Milanuncios"
    }
]

print("Cargando catálogo con imágenes diferenciadas...")
insertados = 0
for a in catalogo_real:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers_supabase)
        if r.status_code in [200, 201]:
            insertados += 1
            print(f"✓ Guardado: {a['title']}")
    except Exception as e:
        print(f"Error: {e}")

print(f"Completado. Insertados: {insertados}")
