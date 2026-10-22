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

# Anuncios con imágenes estáticas directas que no cambian jamás
catalogo_estable = [
    {
        "title": "Volkswagen California T6.1 Ocean DSG 150CV 2021",
        "price": 58900,
        "location": "Barcelona",
        "year": 2021,
        "km": 42000,
        "sleeps": 4,
        "type": "Furgoneta Camper",
        "image": "https://raw.githubusercontent.com/taniarascia/sandbox/master/camper.jpg",
        "url": "https://es.wallapop.com/search?keywords=volkswagen%20california",
        "seller_type": "Particular",
        "source": "Wallapop"
    },
    {
        "title": "Fiat Ducato Maxi L3H2 Camperizada Homologada",
        "price": 38500,
        "location": "Madrid",
        "year": 2020,
        "km": 88000,
        "sleeps": 3,
        "type": "Gran Volumen",
        "image": "https://images.pexels.com/photos/2506923/pexels-photo-2506923.jpeg?auto=compress&cs=tinysrgb&w=800",
        "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/fiat-ducato-camper.htm",
        "seller_type": "Profesional",
        "source": "Milanuncios"
    },
    {
        "title": "Autocaravana Benimar Tessoro 481 Perfilada",
        "price": 49500,
        "location": "Valencia",
        "year": 2019,
        "km": 65000,
        "sleeps": 4,
        "type": "Autocaravana",
        "image": "https://images.pexels.com/photos/386009/pexels-photo-386009.jpeg?auto=compress&cs=tinysrgb&w=800",
        "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/benimar.htm",
        "seller_type": "Particular",
        "source": "Milanuncios"
    }
]

print("Insertando anuncios estables en Supabase...")
for a in catalogo_estable:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers_supabase)
        print(f"✓ Resultado [{r.status_code}]: {a['title']}")
    except Exception as e:
        print(f"Error: {e}")

print("Proceso finalizado.")
