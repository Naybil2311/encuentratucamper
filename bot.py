import os
import requests

SUPABASE_URL = "https://ecidgvwrog9savmdzj1z.supabase.co"
SUPABASE_KEY = "sb_publishable_eCIDgVWRog9savmDZJ1Z-Q_RRYIHMj4"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

# Anuncios adaptados a las columnas básicas de tu tabla
anuncios_antiguos = [
    {
        "title": "Volkswagen T3 Westfalia",
        "price": 14500,
        "location": "Girona",
        "year": 1988,
        "km": 210000,
        "sleeps": 4,
        "type": "Gran Volumen",
        "image": "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clásicos"
    },
    {
        "title": "Mercedes MB100 Camperizada",
        "price": 8900,
        "location": "Asturias",
        "year": 1995,
        "km": 185000,
        "sleeps": 2,
        "type": "Furgoneta Camper
	
	
		
	
	
		Activar hasta 5,60% cashback
	
",
        "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Comunidad",
        "source": "Agregador Clásicos"
    }
]

print("🚀 Conectando con Supabase...")

for anuncio in anuncios_antiguos:
    try:
        url = f"{SUPABASE_URL}/rest/v1/anuncios"
        response = requests.post(url, json=anuncio, headers=headers)
        print(f"Respuesta HTTP {response.status_code}: {response.text}")
    except Exception as err:
        print(f"Error en la petición: {err}")

print("🎉 Proceso finalizado con éxito.")
