import os
import requests

SUPABASE_URL = "https://agazyoihnkienkywbpxe.supabase.co"
# Reemplaza esta clave por la 'service_role' de Supabase (Settings -> API) si RLS está activo
SUPABASE_KEY = "sb_publishable_eCIDgVWRog9savmDZJ1Z-Q_RRYIHMj4" 
APIFY_TOKEN = os.getenv("APIFY_TOKEN")

headers_supabase = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

def clasificar_vehiculo(titulo):
    t = titulo.lower()
    if any(k in t for k in ["hymer", "benimar", "mclouis", "chausson", "burstner", "rimor", "capuchina", "perfilada"]):
        return "Autocaravana"
    elif any(k in t for k in ["ducato", "boxer", "jumper", "sprinter", "crafter", "master", "gran volumen"]):
        return "Gran Volumen"
    return "Furgoneta Camper"

# Anuncios directos de prueba garantizados
anuncios_prueba = [
    {
        "title": "Volkswagen California T6.1 Ocean DSG 150CV",
        "price": 58900,
        "location": "Barcelona",
        "year": 2021,
        "km": 42000,
        "sleeps": 4,
        "type": "Furgoneta Camper",
        "image": "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=800&q=80",
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
        "image": "https://images.unsplash.com/photo-1527786356703-4b100091cd2c?auto=format&fit=crop&w=800&q=80",
        "url": "https://www.milanuncios.com/autocaravanas-de-segunda-mano/fiat-ducato-camper.htm",
        "seller_type": "Profesional",
        "source": "Milanuncios"
    }
]

print("Iniciando prueba de conexión con Supabase...")
insertados = 0

for a in anuncios_prueba:
    endpoint = f"{SUPABASE_URL}/rest/v1/anuncios"
    r = requests.post(endpoint, json=a, headers=headers_supabase)
    print(f"Respuesta HTTP Supabase: {r.status_code}")
    
    if r.status_code in [200, 201]:
        insertados += 1
        print(f"✓ Éxito al insertar: {a['title']}")
    else:
        print(f"× FALLO AL INSERTAR [{r.status_code}]: {r.text}")

print(f"Proceso finalizado. Total insertados: {insertados}")
