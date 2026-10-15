import requests

SUPABASE_URL = "https://agazyoihnkienkywbpxe.supabase.co"
SUPABASE_KEY = "https://agazyoihnkienkywbpxe.supabase.co/rest/v1/"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

# Categorías en variables para proteger la sintaxis
c_camper = "Camper"
c_gran_volumen = "Gran Volumen"
c_autocaravana = "Autocaravana"

# Lote amplio de campers vintage y clásicas
anuncios = [
    {
        "title": "Volkswagen T3 Westfalia (1988)",
        "price": 14500,
        "location": "Girona",
        "year": 1988,
        "km": 210000,
        "sleeps": 4,
        "type": c_gran_volumen,
        "image": "https://images.unsplash.com/photo-1523987355523-c7b5b0dd90a7?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Mercedes MB100 Camperizada (1995)",
        "price": 8900,
        "location": "Asturias",
        "year": 1995,
        "km": 185000,
        "sleeps": 2,
        "type": c_camper,
        "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Comunidad",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Ford Transit Mk3 Vintage (1992)",
        "price": 6500,
        "location": "Granada",
        "year": 1992,
        "km": 160000,
        "sleeps": 3,
        "type": c_camper,
        "image": "https://images.unsplash.com/photo-1516939884455-1445c8652f83?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Volkswagen T2 Bay Window (1976)",
        "price": 24000,
        "location": "Málaga",
        "year": 1976,
        "km": 120000,
        "sleeps": 2,
        "type": c_camper,
        "image": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Fiat Ducato Maxi Camper (1990)",
        "price": 9500,
        "location": "Valencia",
        "year": 1990,
        "km": 195000,
        "sleeps": 4,
        "type": c_gran_volumen,
        "image": "https://images.unsplash.com/photo-1527786356703-4b100091cd2c?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Peugeot J5 Camper Homologada (1991)",
        "price": 7800,
        "location": "León",
        "year": 1991,
        "km": 175000,
        "sleeps": 3,
        "type": c_camper,
        "image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Mercedes 207D Camper Clásica (1984)",
        "price": 11200,
        "location": "Tarragona",
        "year": 1984,
        "km": 230000,
        "sleeps": 4,
        "type": c_gran_volumen,
        "image": "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Comunidad",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Volkswagen T4 California Syncro (1998)",
        "price": 16800,
        "location": "Pamplona",
        "year": 1998,
        "km": 260000,
        "sleeps": 4,
        "type": c_camper,
        "image": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Mitsubishi L300 4x4 Camper (1994)",
        "price": 13500,
        "location": "Huesca",
        "year": 1994,
        "km": 205000,
        "sleeps": 2,
        "type": c_camper,
        "image": "https://images.unsplash.com/photo-1506015391300-4802dc74de2e?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Hymer Mobile Clásica Fiat (1989)",
        "price": 12900,
        "location": "Alicante",
        "year": 1989,
        "km": 170000,
        "sleeps": 5,
        "type": c_autocaravana,
        "image": "https://images.unsplash.com/photo-1513311068348-19c8fbdc0bb6?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    }
]

print("🚀 Iniciando insercion masiva en Supabase...")

for a in anuncios:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers)
        print(f"Respuesta Supabase [{r.status_code}] -> {a['title']}")
    except Exception as e:
        print(f"Error enviando {a['title']}: {e}")

print("🎉 Insercion completada con exito.")
