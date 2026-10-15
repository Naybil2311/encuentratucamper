import requests

SUPABASE_URL = "https://ecidgvwrog9savmdzj1z.supabase.co"
SUPABASE_KEY = "sb_publishable_eCIDgVWRog9savmDZJ1Z-Q_RRYIHMj4"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

# Construimos los tipos concatenando variables para evitar la inyección de la extensión de cashback
t1 = "Furgoneta" + " " + "Camper"
t2 = "Gran" + " " + "Volumen"

anuncios = [
    {
        "title": "Volkswagen T3 Westfalia (1988)",
        "price": 14500,
        "location": "Girona",
        "year": 1988,
        "km": 210000,
        "sleeps": 4,
        "type": t2,
        "image": "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Mercedes MB100 Camperizada",
        "price": 8900,
        "location": "Asturias",
        "year": 1995,
        "km": 185000,
        "sleeps": 2,
        "type": t1,
        "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Comunidad",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Ford Transit Mk3 Vintage",
        "price": 6500,
        "location": "Granada",
        "year": 1992,
        "km": 160000,
        "sleeps": 3,
        "type": t1,
        "image": "https://images.unsplash.com/photo-1516939884455-1445c8652f83?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    }
]

print("Iniciando envio a Supabase...")

for a in anuncios:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers)
        print(f"Resultado: {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")

print("Proceso completado.")
