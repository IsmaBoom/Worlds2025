import json
import os

# Ruta base para los archivos de texto
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(SCRIPT_DIR, "..", "src", "txts")

def reiniciar_campeones():
    """Reinicia los archivos de campeones a 0"""
    champions = {
        "Aatrox": 0, "Ahri": 0, "Akali": 0, "Akshan": 0, "Alistar": 0, "Ambessa": 0,
        "Amumu": 0, "Anivia": 0, "Annie": 0, "Aphelios": 0, "Ashe": 0, "Aurelion Sol": 0,
        "Aurora": 0, "Azir": 0, "Bard": 0, "Bel'Veth": 0, "Briar": 0, "Blitzcrank": 0,
        "Brand": 0, "Braum": 0, "Caitlyn": 0, "Camille": 0, "Cassiopeia": 0, "Cho'Gath": 0,
        "Corki": 0, "Darius": 0, "Diana": 0, "Dr. Mundo": 0, "Draven": 0, "Ekko": 0,
        "Elise": 0, "Evelynn": 0, "Ezreal": 0, "Fiddlesticks": 0, "Fiora": 0, "Fizz": 0,
        "Galio": 0, "Gangplank": 0, "Garen": 0, "Gnar": 0, "Gragas": 0, "Graves": 0,
        "Gwen": 0, "Hecarim": 0, "Heimerdinger": 0, "Hwei": 0, "Illaoi": 0, "Irelia": 0,
        "Ivern": 0, "Janna": 0, "Jarvan IV": 0, "Jax": 0, "Jayce": 0, "Jhin": 0,
        "Jinx": 0, "Kai'Sa": 0, "Kalista": 0, "Karma": 0, "Karthus": 0, "Kassadin": 0,
        "Katarina": 0, "Kayle": 0, "Kayn": 0, "Kennen": 0, "Kha'Zix": 0, "Kindred": 0,
        "Kled": 0, "Kog'Maw": 0, "K'Sante": 0, "LeBlanc": 0, "Lee Sin": 0, "Leona": 0,
        "Lillia": 0, "Lissandra": 0, "Lucian": 0, "Lulu": 0, "Lux": 0, "Malphite": 0,
        "Malzahar": 0, "Maokai": 0, "Master Yi": 0, "Mel": 0, "Milio": 0, "Miss Fortune": 0,
        "Mordekaiser": 0, "Morgana": 0, "Naafiri": 0, "Nami": 0, "Nasus": 0, "Nautilus": 0,
        "Neeko": 0, "Nidalee": 0, "Nilah": 0, "Nocturne": 0, "Nunu & Willump": 0, "Olaf": 0,
        "Orianna": 0, "Ornn": 0, "Pantheon": 0, "Poppy": 0, "Pyke": 0, "Qiyana": 0,
        "Quinn": 0, "Renata Glasc": 0, "Rakan": 0, "Rammus": 0, "Rek'Sai": 0, "Rell": 0,
        "Renekton": 0, "Rengar": 0, "Riven": 0, "Rumble": 0, "Ryze": 0, "Samira": 0,
        "Sejuani": 0, "Senna": 0, "Seraphine": 0, "Sett": 0, "Shaco": 0, "Shen": 0,
        "Shyvana": 0, "Singed": 0, "Sion": 0, "Sivir": 0, "Skarner": 0, "Sona": 0,
        "Soraka": 0, "Smolder": 0, "Swain": 0, "Sylas": 0, "Syndra": 0, "Tahm Kench": 0,
        "Taliyah": 0, "Talon": 0, "Taric": 0, "Teemo": 0, "Thresh": 0, "Tristana": 0,
        "Trundle": 0, "Tryndamere": 0, "Twisted Fate": 0, "Twitch": 0, "Udyr": 0,
        "Urgot": 0, "Varus": 0, "Vayne": 0, "Veigar": 0, "Vel'Koz": 0, "Vex": 0,
        "Vi": 0, "Viego": 0, "Viktor": 0, "Vladimir": 0, "Volibear": 0, "Warwick": 0,
        "Wukong": 0, "Xayah": 0, "Xerath": 0, "Xin Zhao": 0, "Yasuo": 0, "Yone": 0,
        "Yorick": 0, "Yunara": 0, "Yuumi": 0, "Zac": 0, "Zed": 0, "Zeri": 0,
        "Ziggs": 0, "Zilean": 0, "Zoe": 0, "Zyra": 0,
    }
    
    archivos_campeones = [
        "campeones_picks.txt",
        "campeones_bans.txt",
        "campeones_victorias.txt",
        "campeones_kills.txt",
        "campeones_muertes.txt"
    ]
    
    for archivo in archivos_campeones:
        with open(os.path.join(BASE_PATH, archivo), "w", encoding="utf8") as f:
            json.dump(champions, f, indent=4)
        print(f"✓ {archivo} reiniciado")

def reiniciar_jugadores():
    """Reinicia los archivos de jugadores a 0"""
    players = {
        "369": 0, "Alvaro": 0, "Azhi": 0, "Bdd": 0, "Beichuan": 0, "Betty": 0, "Bin": 0, "Boal": 0,
        "BrokenBlade": 0, "Busio": 0, "Bwipo": 0, "Canyon": 0, "Caps": 0, "Chovy": 0, "Creme": 0,
        "Cuzz": 0, "Delight": 0, "deokdam": 0, "Dhokla": 0, "Dire": 0, "Disamis": 0,
        "Doggo": 0, "Doran": 0, "Driver": 0, "Duro": 0, "Eddie": 0, "Elk": 0,
        "Elyoya": 0, "Eyla": 0, "Faker": 0, "FBI": 0, "Flandre": 0, "GALA": 0,
        "Gumayusi": 0, "Hang": 0, "Hans Sama": 0, "Hiro02": 0, "Hizto": 0, "HongQ": 0,
        "Hope": 0, "Inspired": 0, "JackeyLove": 0, "Jojopyun": 0, "JunJia": 0, "Kael": 0,
        "Kaiwing": 0, "Kanavi": 0, "Karsa": 0, "Keria": 0, "Kiin": 0, "knight": 0,
        "Labrov": 0, "Maple": 0, "Massu": 0, "Meiko": 0, "Mikyx": 0, "Mireu": 0,
        "Morttheus": 0, "Myrwn": 0, "Oner": 0, "ON": 0, "Oscarinin": 0, "Peanut": 0,
        "PerfecT": 0, "Peter": 0, "Poby": 0, "Quad": 0, "Quid": 0, "Razork": 0, "Rest": 0,
        "River": 0, "Rookie": 0, "Ruler": 0, "shad0w": 0, "Shanks": 0,
        "SkewMond": 0, "Supa": 0, "Taki": 0, "Tarzan": 0, "TheShy": 0, "Trymbi": 0,
        "Upset": 0, "Viper": 0, "Wei": 0, "Woody": 0, "Zeka": 0, "Zeus": 0,
    }
    
    archivos_jugadores = [
        "jugadores_kills.txt",
        "jugadores_muertes.txt",
        "jugadores_asistencias.txt",
        "jugadores_asesinatos.txt",
    ]
    
    for archivo in archivos_jugadores:
        with open(os.path.join(BASE_PATH, archivo), "w", encoding="utf8") as f:
            json.dump(players, f, indent=4)
        print(f"✓ {archivo} reiniciado")

def reiniciar_jugadores_distintos():
    """Reinicia el archivo de jugadores distintos a listas vacías"""
    players = {
        "369": [], "Alvaro": [], "Azhi": [], "Bdd": [], "Beichuan": [], "Betty": [], "Bin": [], "Boal": [],
        "BrokenBlade": [], "Busio": [], "Bwipo": [], "Canyon": [], "Caps": [], "Chovy": [], "Creme": [],
        "Cuzz": [], "Delight": [], "deokdam": [], "Dhokla": [], "Dire": [], "Disamis": [],
        "Doggo": [], "Doran": [], "Driver": [], "Duro": [], "Eddie": [], "Elk": [],
        "Elyoya": [], "Eyla": [], "Faker": [], "FBI": [], "Flandre": [], "GALA": [],
        "Gumayusi": [], "Hang": [], "Hans Sama": [], "Hiro02": [], "Hizto": [], "HongQ": [],
        "Hope": [], "Inspired": [], "JackeyLove": [], "Jojopyun": [], "JunJia": [], "Kael": [],
        "Kaiwing": [], "Kanavi": [], "Karsa": [], "Keria": [], "Kiin": [], "knight": [],
        "Labrov": [], "Maple": [], "Massu": [], "Meiko": [], "Mikyx": [], "Mireu": [],
        "Morttheus": [], "Myrwn": [], "Oner": [], "ON": [], "Oscarinin": [], "Peanut": [],
        "PerfecT": [], "Peter": [], "Poby": [], "Quad": [], "Quid": [], "Razork": [], "Rest": [],
        "River": [], "Rookie": [], "Ruler": [], "shad0w": [], "Shanks": [],
        "SkewMond": [], "Supa": [], "Taki": [], "Tarzan": [], "TheShy": [], "Trymbi": [],
        "Upset": [], "Viper": [], "Wei": [], "Woody": [], "Zeka": [], "Zeus": [],
    }
    
    with open(os.path.join(BASE_PATH, "jugadores_distintos.txt"), "w", encoding="utf8") as f:
        json.dump(players, f, indent=4)
    print(f"✓ jugadores_distintos.txt reiniciado")

def reiniciar_equipos():
    """Reinicia los archivos de equipos"""
    teams_tiempo = {
        "100 Thieves": "60:00", "Anyone's Legend": "60:00", "Bilibili Gaming": "60:00",
        "CTBC Flying Oyster": "60:00", "FlyQuest": "60:00", "Fnatic": "60:00",
        "G2 Esports": "60:00", "Gen.G Esports": "60:00", "Hanwha Life Esports": "60:00",
        "Invictus Gaming": "60:00", "Keyd Stars": "60:00", "KOI": "60:00",
        "KT Rolster": "60:00", "PSG Talon": "60:00", "Secret Whales": "60:00",
        "T1": "60:00", "Top Esports": "60:00",
    }
    
    teams_kills = {
        "100 Thieves": 0, "Anyone's Legend": 0, "Bilibili Gaming": 0,
        "CTBC Flying Oyster": 0, "FlyQuest": 0, "Fnatic": 0,
        "G2 Esports": 0, "Gen.G Esports": 0, "Hanwha Life Esports": 0,
        "Invictus Gaming": 0, "Keyd Stars": 0, "KOI": 0,
        "KT Rolster": 0, "PSG Talon": 0, "Secret Whales": 0,
        "T1": 0, "Top Esports": 0,
    }
    
    teams_distintos = {
        "100 Thieves": [], "Anyone's Legend": [], "Bilibili Gaming": [],
        "CTBC Flying Oyster": [], "FlyQuest": [], "Fnatic": [],
        "G2 Esports": [], "Gen.G Esports": [], "Hanwha Life Esports": [],
        "Invictus Gaming": [], "Keyd Stars": [], "KOI": [],
        "KT Rolster": [], "PSG Talon": [], "Secret Whales": [],
        "T1": [], "Top Esports": [],
    }
    
    with open(os.path.join(BASE_PATH, "equipos_corta.txt"), "w", encoding="utf8") as f:
        json.dump(teams_tiempo, f, indent=4)
    print(f"✓ equipos_corta.txt reiniciado")
    
    with open(os.path.join(BASE_PATH, "equipos_kills.txt"), "w", encoding="utf8") as f:
        json.dump(teams_kills, f, indent=4)
    print(f"✓ equipos_kills.txt reiniciado")
    
    with open(os.path.join(BASE_PATH, "equipos_distintos.txt"), "w", encoding="utf8") as f:
        json.dump(teams_distintos, f, indent=4)
    print(f"✓ equipos_distintos.txt reiniciado")


    
    

def reiniciar_links():
    """Reinicia el archivo de links"""
    with open(os.path.join(BASE_PATH, "links.txt"), "w", encoding="utf8") as f:
        json.dump([], f, indent=4)
    print(f"✓ links.txt reiniciado")

def reiniciar_ultimos_equipos():
    """Reinicia el archivo de últimos equipos"""
    with open(os.path.join(BASE_PATH, "ultimos_equipos.txt"), "w", encoding="utf8") as f:
        json.dump([], f, indent=4)
    print(f"✓ ultimos_equipos.txt reiniciado")

def main():
    print("=" * 60)
    print("🔄 REINICIANDO TODOS LOS ARCHIVOS DE ESTADÍSTICAS")
    print("=" * 60)
    print()
    
    confirmacion = input("⚠️  ¿Estás seguro de que quieres reiniciar todos los archivos? (escribe 'SI' para confirmar): ")
    
    if confirmacion.upper() != "SI":
        print("\n❌ Operación cancelada")
        return
    
    print("\n🚀 Comenzando reinicio...\n")
    
    reiniciar_campeones()
    print()
    
    reiniciar_jugadores()
    print()
    
    reiniciar_jugadores_distintos()
    print()
    
    reiniciar_equipos()
    print()
    
    
    reiniciar_links()
    print()
    
    reiniciar_ultimos_equipos()
    
    print()
    print("=" * 60)
    print("✅ REINICIO COMPLETADO EXITOSAMENTE")
    print("=" * 60)
    print()
    print("Todos los archivos han sido reiniciados a sus valores iniciales.")
    print("Puedes comenzar a procesar nuevas partidas.")

if __name__ == "__main__":
    main()
