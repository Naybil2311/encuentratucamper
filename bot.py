import requests

SUPABASE_URL = "https://ecidgvwrog9savmdzj1z.supabase.co"
SUPABASE_KEY = "sb_publishable_eCIDgVWRog9savmDZJ1Z-Q_RRYIHMj4"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

cat_camper = "Camper"
cat_gran_volumen = "Gran Volumen"

anuncios = [
    {
        "title": "Volkswagen T3 Westfalia (1988)",
        "price": 14500,
        "location": "Girona",
        "year": 1988,
        "km": 210000,
        "sleeps": 4,
        "type": cat_gran_volumen,
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
        "type": cat_camper,
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
        "type": cat_camper,
        "image": "https://images.unsplash.com/photo-1516939884455-1445c8652f83?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    }
]

print("Iniciando insercion en Supabase...")

for a in anuncios:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers)
        print(f"Respuesta Supabase [{r.status_code}] -> {a['title']}")
    except Exception as e:
        print(f"Error enviando {a['title']}: {e}")

print("Proceso completado.")
