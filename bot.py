import requests

SUPABASE_URL = "https://ecidgvwrog9savmdzj1z.supabase.co"
SUPABASE_KEY = "sb_publishable_eCIDgVWRog9savmDZJ1Z-Q_RRYIHMj4"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

anuncios = [
    {
        "title": "Volkswagen T3 Westfalia",
        "price": 14500,
        "location": "Girona",
        "year": 1988,
        "km": 210000,
        "sleeps": 4,
        "type": "Camper"
	
	
		
	
	
		Activar hasta 5,60% cashback
	
",
        "image": "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador"
    },
    {
        "title": "Mercedes MB100 Camper
	
	
		
	
	
		Activar hasta 5,60% cashback
	
",
        "price": 8900,
        "location": "Asturias",
        "year": 1995,
        "km": 185000,
        "sleeps": 2,
        "type": "Camper
	
	
		
	
	
		Activar hasta 5,60% cashback
	
",
        "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Comunidad",
        "source": "Agregador"
    }
]

print("Iniciando envio a Supabase...")

for item in anuncios:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=item, headers=headers)
        print(f"Estado HTTP {r.status_code} para {item['title']}")
    except Exception as e:
        print(f"Error: {e}")

print("Proceso finalizado con exito.")
