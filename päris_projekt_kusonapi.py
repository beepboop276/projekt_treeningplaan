import requests
import json

eesmark = input("Mis on sinu treeningu eesmärk? (nt kaalulangetus, lihaskasv, vastupidavus): ")
paevad_nadalas = input("Mitu päeva nädalas soovid treenida?: ")
treeningu_kestus = input("Kui pikad peaksid treeningud olema? (minutites): ")
muud_soovid = input("Kas on muid erisoove või piiranguid? (nt vigastused, treeningvarustus, kodus/saalis): ")

api_voti = "SIIA!!!!!"  
url = "https://openrouter.ai/api/v1/chat/completions"  

headers = {
    "Authorization": f"Bearer {api_voti}",
    "Content-Type": "application/json",
}

data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": (
                "Sa oled personaaltreener ja koostad treeningkava inimloetavas ja ilusas formaadis, mitte JSON-is. "
                "Struktuur peab olema selline:\n"
                "Eesmärk: ...\n"
                "Päevad Nädalas: ...\n"
                "Treeningu Kestus: ...\n"
                "Treeninguplaan:\n"
                "- Esmaspäev – Jalatreening:\n"
                "  - Harjutus 1 – Kordused\n"
                "  - Harjutus 2 – Kordused\n"
                "- Kolmapäev – Ülakehatreening:\n"
                "  - Harjutus 1 – Kordused\n"
                "  - jne.\n"
                "Muud Soovid: ...\n"
                "Iga treeningpäeva alla pane ka konkreetsed harjutused ja mitu korda/kordust teha."
            )
        },
        {
            "role": "user",
            "content": (
                f"Soovin treeningkava järgmiste tingimustega:\n"
                f"Eesmärk: {eesmark}\n"
                f"Treeningupäevad nädalas: {paevad_nadalas}\n"
                f"Treeningu kestus: {treeningu_kestus} minutit\n"
                f"Muud soovid/piirangud: {muud_soovid}\n"
                "Palun tee iga päeva treening põhjalikuks ja kirjuta iga harjutuse juurde mitu seeriat ja kordust."
            )
        }
    ]
}


response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    vastus_json = response.json()
    raw_content = vastus_json['choices'][0]['message']['content']

    with open("treeningkava.txt", "w", encoding="utf-8") as f:
        f.write(raw_content.strip())

    print("Teie isiklik treeningkava on salvestatud faili 'treeningkava.txt'.")
else:
    print(f"Tekkis viga: {response.status_code}")
    print(response.text)


#jap jap
