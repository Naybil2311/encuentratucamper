import requests

SUPABASE_URL = "https://agazyoihnkienkywbpxe.supabase.co"
SUPABASE_KEY = "sb_publishable_eCIDgVWRog9savmDZJ1Z-Q_RRYIHMj4"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

# Categorías
cat_camper = "Camper"
cat_gran_volumen = "Gran Volumen"
cat_autocaravana = "Autocaravana"

anuncios = [
    # --- AUTOCARAVANAS MULTIMARCA ---
    {
        "title": "Benimar Tessoro 463 UP (2021)",
        "price": 54900,
        "location": "Madrid",
        "year": 2021,
        "km": 42000,
        "sleeps": 5,
        "type": cat_autocaravana,
        "image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Multimarca"
    },
    {
        "title": "McLouis Glamys 22 Capuchina (2018)",
        "price": 43500,
        "location": "Sevilla",
        "year": 2018,
        "km": 68000,
        "sleeps": 7,
        "type": cat_autocaravana,
        "image": "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Multimarca"
    },
    {
        "title": "Chausson Titanium 640 Perfilada (2020)",
        "price": 51200,
        "location": "Barcelona",
        "year": 2020,
        "km": 35000,
        "sleeps": 4,
        "type": cat_autocaravana,
        "image": "https://images.unsplash.com/photo-1527786356703-4b100091cd2c?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Comunidad",
        "source": "Agregador Multimarca"
    },
    {
        "title": "Hymer Mobil B544 Clásica (1990)",
        "price": 13900,
        "location": "Alicante",
        "year": 1990,
        "km": 178000,
        "sleeps": 5,
        "type": cat_autocaravana,
        "image": "https://images.unsplash.com/photo-1513311068348-19c8fbdc0bb6?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Clasicos"
    },
    {
        "title": "Burstner Ixeo Time IT 710 (2015)",
        "price": 41900,
        "location": "Valencia",
        "year": 2015,
        "km": 89000,
        "sleeps": 4,
        "type": cat_autocaravana,
        "image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Multimarca"
    },
    {
        "title": "Rimor Seal 5 Capuchina (2019)",
        "price": 46000,
        "location": "Zaragoza",
        "year": 2019,
        "km": 54000,
        "sleeps": 6,
        "type": cat_autocaravana,
        "image": "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=800&q=80",
        "seller_type": "Particular",
        "source": "Agregador Multimarca"
    },

    # --- CAMPERS Y GRAN VOLUMEN ---
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
        "title": "Mercedes MB100 Camperizada (1995)",
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
        "title": "Ford Transit Mk3 Vintage (1992)",
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

print("Iniciando insercion multimarca en Supabase...")

for a in anuncios:
    try:
        r = requests.post(f"{SUPABASE_URL}/rest/v1/anuncios", json=a, headers=headers)
        print(f"Respuesta Supabase [{r.status_code}] -> {a['title']}")
    except Exception as e:
        print(f"Error enviando {a['title']}: {e}")

print("Proceso completado con exito.")
