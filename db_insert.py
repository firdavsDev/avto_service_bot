from utils.db_api.db import Database

# Avto servislar ma'lumotlari
avto_servislar = {
    "Avto_elektrik": [
        {"location": (41.311081, 69.279386), "phone": "+998901234568",
         "service_name": "Avto elektrik"},
        {"location": (41.345678, 69.345678), "phone": "+998923456789",
         "service_name": "Avto elektrik"},
        {"location": (41.123456, 69.123456), "phone": "+998901234567",
         "service_name": "Avto_elektrik"},
        {"location": (41.234567, 69.234567), "phone": "+998912345678",
         "service_name": "Avto elektrik"}
    ],

    "Moy_almashtirish": [
        {"location": (41.315812, 69.279629), "phone": "+998912345678",
         "service_name": "Moy almashtirish"}
    ],

    "Avto_yurish_qismini_tamirlash": [
        {"location": (41.309821, 69.279308), "phone": "+998923456789",
         "service_name": "Avto yurish qismini tamirlash"}
    ],

    "Kuzovchi": [
        {"location": (41.314052, 69.278798),
         "phone": "+998934567890", "service_name": "Kuzovchi"}
    ],

    "Avto_diagnostika": [
        {"location": (41.311450, 69.280196), "phone": "+998945678901",
         "service_name": "Avto diagnostika"}
    ],

    "Avto_detailing": [
        {"location": (41.310587, 69.279923), "phone": "+998956789012",
         "service_name": "Avto detailing"}
    ]
}

# DB ni yaratish
db = Database(path_to_db="data.db")

# services jadvalini yaratish
db.create_table("Avto_elektrik", ["service_name", "location", "phone_number"])
db.create_table("Moy_almashtirish", [
                "service_name", "location", "phone_number"])
db.create_table("Avto_yurish_qismini_tamirlash", [
                "service_name", "location", "phone_number"])
db.create_table("Kuzovchi", ["service_name", "location", "phone_number"])
db.create_table("Avto_diagnostika", [
                "service_name", "location", "phone_number"])
db.create_table("Avto_detailing", ["service_name", "location", "phone_number"])

# services jadvaliga ma'lumotlarni qo'shish
for service_name, services in avto_servislar.items():
    for service in services:
        db.insert_data(
            service_name,
            ["service_name", "location", "phone_number"],
            [service["service_name"], service["location"], service["phone"]]
        )

db.close()
