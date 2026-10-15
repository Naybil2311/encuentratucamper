import requests

SUPABASE_URL = "https://ecidgvwrog9savmdzj1z.supabase.co"
SUPABASE_KEY = "sb_publishable_eCIDgVWRog9savmDZJ1Z-Q_RRYIHMj4"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

anuncios_antiguos = [
    {
        "title": "Volkswagen T3 Joker Westfalia (1988)",
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
        "title": "Mercedes MB100 Camperizada Homologada",
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
    },
    {
        "title": "Ford Transit Mk3 Camper
	
	
		
	
	
		Activar hasta 5,60% cashback
	
 Vintage",
        "price": 6500,
        "location": "Granada",
        "year": 1992,
        "km": 160000,
        "sleeps": 3,
        "type": "Furgoneta Camper
	
	
		
	
	
		Activar hasta 5,60% cashback
	
",
        "image": "https://images.unsplash.com/photo-1516939884455-1445c8652f83?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clásicos"
    }
]

print("🚀 Conectando con Supabase e insertando anuncios...")

for anuncio in anuncios_antiguos:
    try:
        url = f"{SUPABASE_URL}/rest/v1/anuncios"
        res = requests.post(url, json=anuncio, headers=headers)
        print(f"Respuesta HTTP {res.status_code} para '{anuncio['title']}'")
    except Exception as e:
        print(f"Error: {e}")

print("🎉 Proceso finalizado.")
