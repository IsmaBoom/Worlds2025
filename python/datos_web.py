from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import json

def dragones():
    dragones_totales = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "dragones","r+",encoding="utf8")
    dragones_L = dragones_totales.read()
    dragones_totales.close()
    #Dragones en cada partida a mano:
    Tecnoquimica = 0
    Nube = 0
    Hextech = 0
    Infernal = 0
    Montaña = 0
    Oceano = 0
    #Añadir los dragones a los totales:
    mi_diccionario = json.loads(dragones_L)
    dragones_totales = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "dragones","w",encoding="utf8")
    mi_diccionario['Tecnoquimica'] += Tecnoquimica
    mi_diccionario['Nube'] += Nube
    mi_diccionario['Hextech'] += Hextech
    mi_diccionario['Infernal'] += Infernal
    mi_diccionario['Montaña'] += Montaña
    mi_diccionario['Oceano'] += Oceano 

    json.dump(mi_diccionario, dragones_totales,indent=4)
    dragones_totales.close()
    
def campeones():
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
    return champions

def jugadores():
    players = {
    "369": 0, "Alvaro": 0, "Azhi": 0, "Bdd": 0, "Betty": 0, "Bin": 0, "Boal": 0,
    "BrokenBlade": 0, "Busio": 0, "Canyon": 0, "Caps": 0, "Chovy": 0, "Creme": 0,
    "Cuzz": 0, "Delight": 0, "deokdam": 0, "Dhokla": 0, "Dire": 0, "Disamis": 0,
    "Doggo": 0, "Doran": 0, "Driver": 0, "Duro": 0, "Eddie": 0, "Elk": 0,
    "Elyoya": 0, "Eyla": 0, "Faker": 0, "FBI": 0, "Flandre": 0, "GALA": 0,
    "Gumayusi": 0, "Hang": 0, "Hans Sama": 0, "Hiro02": 0, "Hitzo": 0, "HongQ": 0,
    "Hope": 0, "Inspired": 0, "JackeyLove": 0, "Jojopyun": 0, "JunJia": 0, "Kael": 0,
    "Kaiwing": 0, "Kanavi": 0, "Karsa": 0, "Keria": 0, "Kiin": 0, "knight": 0,
    "Labrov": 0, "Maple": 0, "Massu": 0, "Meiko": 0, "Mikyx": 0, "Mireu": 0,
    "Morttheus": 0, "Myrwn": 0, "Oner": 0, "ON": 0, "Oscarinin": 0, "Peanut": 0,
    "PerfecT": 0, "Peter": 0, "Poby": 0, "Quad": 0, "Quid": 0, "Razork": 0,
    "Rest": 0, "River": 0, "Rookie": 0, "Ruler": 0, "shad0w": 0, "Shanks": 0,
    "SkewMond": 0, "Supa": 0, "Taki": 0, "Tarzan": 0, "TheShy": 0, "Trymbi": 0,
    "Upset": 0, "Viper": 0, "Wei": 0, "Woody": 0, "Zeka": 0, "Zeus": 0,
}
    return players

def jugadores_distintos():
    return jugadores()

def equipos():
    teams = {
    "100 Thieves": "60:00", "Anyone's Legend": "60:00", "Bilibili Gaming": "60:00",
    "CBTC Flying Oyster": "60:00", "FlyQuest": "60:00", "Fnatic": "60:00",
    "G2 Esports": "60:00", "Gen.G Esports": "60:00", "Hanwha Life Esports": "60:00",
    "Invictus Gaming": "60:00", "Keyd Stars": "60:00", "KOI": "60:00",
    "KT Rolster": "60:00", "PSG Talon": "60:00", "Secret Whales": "60:00",
    "T1": "60:00", "Top Esports": "60:00",
}
    return teams

def equipos_distintos():
    teams = {
        "100 Thieves": [], "Anyone's Legend": [], "Bilibili Gaming": [],
        "CBTC Flying Oyster": [], "FlyQuest": [], "Fnatic": [],
        "G2 Esports": [], "Gen.G Esports": [], "Hanwha Life Esports": [],
        "Invictus Gaming": [], "Keyd Stars": [], "KOI": [],
        "KT Rolster": [], "PSG Talon": [], "Secret Whales": [],
        "T1": [], "Top Esports": [],
    }
    return teams

def campeones_pickeados(lista_campeones,gana):
     campeones_picks = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "campeones_picks","r+",encoding="utf8")
     picks = json.loads(campeones_picks.read())
     campeones_picks.close()
     for i in lista_campeones:
          picks[i] += 1
     campeones_picks = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "campeones_picks","w",encoding="utf8")
     json.dump(picks,campeones_picks,indent=4)
     campeones_picks.close()
     if gana:
        victorias = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "campeones_victorias","r+",encoding="utf8")
        victorias_L = json.loads(victorias.read())
        victorias.close()
        for i in lista_campeones:
            victorias_L[i] += 1
        victorias = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "campeones_victorias","w",encoding="utf8")
        json.dump(victorias_L,victorias,indent=4)
        victorias.close()
     
def campeones_baneados(lista_campeones):
     campeones_bans = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "campeones_bans","r+",encoding="utf8")
     bans = json.loads(campeones_bans.read())
     campeones_bans.close()
     for i in lista_campeones:
          bans[i] += 1
     campeones_bans = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "campeones_bans","w",encoding="utf8")
     json.dump(bans,campeones_bans,indent=4)
     campeones_bans.close()

def picks_bans(soup,equipos_partida,ganador):
    gana = False
    #t = soup.find("div",class_="match-bm-lol-game-veto-overview")
    #picks_bans= t.find_all("ul")
    equipos = soup.select('div.match-bm-lol-game-veto-overview-team')
    picks = []
    bans = []

    for equipo in equipos:
        # === PICKS ===
        fila_picks = equipo.select_one('[aria-labelledby="picks"]')
        if fila_picks:
            for a in fila_picks.select('a[title]'):
                campeon = a['title'].strip()
                if campeon not in picks:  # evitar duplicados por doble imagen
                    picks.append(campeon)

        # === BANS ===
        fila_bans = equipo.select_one('[aria-labelledby="bans"]')
        if fila_bans:
            for a in fila_bans.select('a[title]'):
                campeon = a['title'].strip()
                if campeon not in bans:
                    bans.append(campeon)

    picks_equipo0 = picks[0:5]
    picks_equipo1 = picks[5:10]
    bans_equipo0 = bans[0:5]
    bans_equipo1 = bans[5:10]
    # for j in picks_bans[0].find_all("a"):
    #         picks_equipo0.append(re.search(r'title="([^"]+)"', str(j)).group(1))
    print(f"Picks de {equipos_partida[0]}: {picks_equipo0}")
    if equipos_partida[0] == ganador:
        gana = True
    campeones_pickeados(picks_equipo0,gana)
    
    # for j in picks_bans[1].find_all("a"):
    #         bans_equipo0.append(re.search(r'title="([^"]+)"', str(j)).group(1))
    print(f"Bans de {equipos_partida[0]}: {bans_equipo0}")
    campeones_baneados(bans_equipo0)

    gana = False
    # for j in picks_bans[2].find_all("a"):
    #         picks_equipo1.append(re.search(r'title="([^"]+)"', str(j)).group(1))
    print(f"Picks de {equipos_partida[1]}: {picks_equipo1}")
    if equipos_partida[1] == ganador:
        gana = True
    campeones_pickeados(picks_equipo1,gana)
    
    # for j in picks_bans[3].find_all("a"):
    #         bans_equipo1.append(re.search(r'title="([^"]+)"', str(j)).group(1))
    print(f"Bans de {equipos_partida[1]}: {bans_equipo1}")                
    campeones_baneados(bans_equipo1)

def duracion_partida(ganador,duracion_nueva):
     equipos_corta = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "equipos_corta","r+",encoding="utf8")
     duraciones = json.loads(equipos_corta.read())
     equipos_corta.close()
     if str(duraciones[ganador]) > duracion_nueva:
        duraciones[ganador] = duracion_nueva
     equipos_corta = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "equipos_corta","w",encoding="utf8")
     json.dump(duraciones, equipos_corta,indent=4)
     equipos_corta.close()

def kda(t,jugadores_partida,campeones_partida):
    player_stats = t.find_all("div", class_="match-bm-players-player-stats")

    kdas = []

    for player in player_stats:
        # Buscar el bloque de estadísticas individuales
        stats = player.find_all("div", class_="match-bm-players-player-stat")
        for stat in stats:
            title = stat.find("div", class_="match-bm-players-player-stat-title")
            if title and "KDA" in title.text:
                data = stat.find("div", class_="match-bm-players-player-stat-data")
                if data:
                    kda = data.get_text(strip=True)
                    kdas.append(kda)
    #print(kdas)
    c = 0
    #print(kda_info)
    for info in kdas:
         kills, deaths, assists = info.split('/')
         jugadores_kills(int(kills),jugadores_partida[c])
         jugadores_muertes(int(deaths),jugadores_partida[c])
         jugadores_asistencias(int(assists),jugadores_partida[c])
         campeones_muertes(int(deaths),campeones_partida[c])
         top_kills(int(kills),jugadores_partida[c])
         c += 1
            
def jugadores_kills(kills,jugador):
     jugadores_kills_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "jugadores_kills","r+",encoding="utf8")
     kills_L = json.loads(jugadores_kills_.read())
     jugadores_kills_.close()
     kills_L[jugador] += kills
     jugadores_kills_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "jugadores_kills","w",encoding="utf8")
     json.dump(kills_L,jugadores_kills_,indent = 4)
     jugadores_kills_.close()

def jugadores_muertes(muertes,jugador):
     jugadores_muertes_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "jugadores_muertes","r+",encoding="utf8")
     muertes_L = json.loads(jugadores_muertes_.read())
     jugadores_muertes_.close()
     muertes_L[jugador] += muertes
     jugadores_muertes_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "jugadores_muertes","w",encoding="utf8")
     json.dump(muertes_L,jugadores_muertes_,indent = 4)
     jugadores_muertes_.close()

def campeones_muertes(muertes,campeon):
     campeones_muertes_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "campeones_muertes","r+",encoding="utf8")
     muertes_L = json.loads(campeones_muertes_.read())
     campeones_muertes_.close()
     muertes_L[campeon] += muertes
     campeones_muertes_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "campeones_muertes","w",encoding="utf8")
     json.dump(muertes_L,campeones_muertes_,indent = 4)
     campeones_muertes_.close()

def jugadores_asistencias(asistencias,jugador):
     jugadores_asistencias_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "jugadores_asistencias","r+",encoding="utf8")
     asistencias_L = json.loads(jugadores_asistencias_.read())
     jugadores_asistencias_.close()
     asistencias_L[jugador] += asistencias
     jugadores_asistencias_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "jugadores_asistencias","w",encoding="utf8")
     json.dump(asistencias_L,jugadores_asistencias_,indent = 4)
     jugadores_asistencias_.close()

def partida_mas_larga(duracion):
     larga = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "partida_mas_larga","r+",encoding="utf8")
     larga_L = larga.read().replace('"','')
     larga.close()
     if duracion > larga_L:
          larga = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "partida_mas_larga","w",encoding="utf8")
          json.dump(duracion,larga,indent=4)
          larga.close()

def jugadores_distintos_2(jugadors,campeons):
    jugdores_distintos_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "jugadores_distintos","r+",encoding="utf8")
    distintos_L = json.loads(jugdores_distintos_.read())
    jugdores_distintos_.close()

    for jugador in distintos_L:
        if distintos_L[jugador] == 0:
            distintos_L[jugador] = []

    for jugador, campeon in zip(jugadors, campeons):
        if campeon not in distintos_L[jugador]:
            distintos_L[jugador].append(campeon)
    
    #  for i in range(0,len(jugadors)):
    #     if distintos_L[jugadors[i]] == 0:
    #         distintos_L[jugadors[i]] = []
    #         distintos_L[jugadors[i]].append(campeons[i])
    #     if campeons[i] not in distintos_L[jugadors[i]]:
    #         distintos_L[jugadors[i]].append(campeons[i])
    jugdores_distintos_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "jugadores_distintos","w",encoding="utf8")
    json.dump(distintos_L,jugdores_distintos_,indent=4)
    jugdores_distintos_.close()

def equipos_distintos_2(equips,campeons):
     equipos_distintos_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "equipos_distintos","r+",encoding="utf8")
     distintos_L = json.loads(equipos_distintos_.read())
     equipos_distintos_.close()
     for i in range(0,len(campeons)):
        if i < 5:
            if campeons[i] not in distintos_L[equips[0]]:
                distintos_L[equips[0]].append(campeons[i])
        else:
            if campeons[i] not in distintos_L[equips[1]]:
                distintos_L[equips[1]].append(campeons[i])
     equipos_distintos_ = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "equipos_distintos","w",encoding="utf8")
     json.dump(distintos_L,equipos_distintos_,indent=4)
     equipos_distintos_.close()

def top_kills(kills,jugador):
     record = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "jugadores_asesinatos","r+",encoding="utf8")
     record_L = json.loads(record.read())
     record.close()
     if record_L[jugador] < kills:
          record_L[jugador] = kills
          record = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "jugadores_asesinatos","w",encoding="utf8")
          json.dump(record_L,record,indent = 4)

def winrate():
    victorias = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "campeones_victorias","r+",encoding="utf8")
    victorias_L = json.loads(victorias.read())
    victorias.close()
    picks = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\%s.txt" % "campeones_picks","r+",encoding="utf8")
    picks_L = json.loads(picks.read())
    picks.close()
    winrate = {
    clave: (victorias_L[clave] / picks_L[clave]) if picks_L[clave] > 4 else 0
    for clave in picks_L
}
    print(winrate)
    print("******************************************************")
    return winrate
    
def exportar_datos_web():
    """Exporta todos los datos en formato JSON para la web"""
    
    # Top Picks
    with open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\campeones_picks.txt", "r", encoding="utf8") as f:
        picks = json.load(f)
    top_picks = sorted(picks.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Top Bans
    with open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\campeones_bans.txt", "r", encoding="utf8") as f:
        bans = json.load(f)
    top_bans = sorted(bans.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Top Kills
    with open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\jugadores_asesinatos.txt", "r", encoding="utf8") as f:
        kills_record = json.load(f)
    top_kills_record = sorted(kills_record.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Victorias más cortas
    with open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\equipos_corta.txt", "r", encoding="utf8") as f:
        victorias_cortas = json.load(f)
    top_victorias_cortas = sorted(victorias_cortas.items(), key=lambda x: x[1])[:10]
    
    # KDA
    with open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\jugadores_kills.txt", "r", encoding="utf8") as f:
        kills = json.load(f)
    with open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\jugadores_muertes.txt", "r", encoding="utf8") as f:
        deaths = json.load(f)
    with open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\jugadores_asistencias.txt", "r", encoding="utf8") as f:
        assists = json.load(f)
    
    kda = {}
    for player in kills:
        if deaths[player] != 0:
            kda[player] = (kills[player] + assists[player]) / deaths[player]
        else:
            kda[player] = kills[player] + assists[player]
    top_kda = sorted(kda.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Winrate
    win = winrate()
    top_winrate = sorted(win.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Exportar todo
    datos_web = {
        "top_picks": [{"campeon": k, "cantidad": v} for k, v in top_picks],
        "top_bans": [{"campeon": k, "cantidad": v} for k, v in top_bans],
        "top_kills": [{"jugador": k, "kills": v} for k, v in top_kills_record],
        "top_victorias_cortas": [{"equipo": k, "tiempo": v} for k, v in top_victorias_cortas],
        "top_kda": [{"jugador": k, "kda": round(v, 2)} for k, v in top_kda],
        "top_winrate": [{"campeon": k, "winrate": round(v * 100, 2)} for k, v in top_winrate],
    }
    
    # Guardar en archivo JSON para la web
    with open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\WorldsAstro\Aqui\datos_web.json", "w", encoding="utf8") as f:
        json.dump(datos_web, f, indent=4, ensure_ascii=False)
    
    print("Datos exportados correctamente a datos_web.json")
    return datos_web

def main(links, link):
    #links.append(link)
    with open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\links.txt","w") as fichero:
        json.dump(links, fichero)
    
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")

    equipos_partida = []
    visto = set()

    for span in soup.find_all("span", class_="team-template-team-icon"):
        nombre = span.get("data-highlighting-class")
        if nombre and nombre not in visto:
            visto.add(nombre)
            equipos_partida.append(nombre.strip())
    
    print(equipos_partida)
    r = soup.find_all("li",class_=lambda class_name: class_name and class_name.startswith('tab'))

    if len(r) != 0:
        for partida in range(2,len(r)+1):
            t = soup.find("div",class_=f"content{partida}")
            duracion = t.find("div",class_="match-bm-lol-game-summary-length").text
            gana = t.find("div",class_="match-bm-lol-game-summary-score").text[0]
            jugadores_info = t.find_all("div",class_="match-bm-players-player-name")
            print(jugadores_info)
            print("Nº Partida:",partida-1)
            print("Duración:",duracion)
            if gana == "W":
                ganador = equipos_partida[0]
                print("Gana",ganador)
            else:
                ganador = equipos_partida[1]
                print("Gana",ganador)
            jugadores_partida = []
            campeones_partida = []
            for info in jugadores_info:
                jugador = info.find("a").text
                personaje = info.find("i").text
                if jugador == "Shogun (Vietnamese player)":
                    jugador = "Shogun"
                if jugador == "River (Korean player)":
                    jugador = "River"
                if jugador == "Light (Wang Guang-Yu)":
                    jugador = "Light"
                if jugador == "Viper (Korean player)":
                    jugador = "Viper" 
                if jugador == "Weiwei":
                    jugador = "WeiWei"  
                jugadores_partida.append(jugador)
                campeones_partida.append(personaje)
                #print(jugador, personaje)
            #print(ganador)
            picks_bans(t,equipos_partida,ganador)
            duracion_partida(ganador,duracion)
            #print(jugadores_partida)
            #print(campeones_partida)
            kda(t,jugadores_partida,campeones_partida)
            #partida_mas_larga(duracion)
            jugadores_distintos_2(jugadores_partida,campeones_partida)
            equipos_distintos_2(equipos_partida,campeones_partida)
            winrate()
            print("---------------------------------------------")
        ultimos_equipos = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\ultimos_equipos.txt","w",encoding="utf8")
        json.dump(equipos_partida,ultimos_equipos,indent=4)
        ultimos_equipos.close()
    else:
        duracion = soup.find("div",class_="match-bm-lol-game-summary-length").text
        jugadores_info = soup.find_all("div",class_="match-bm-lol-players-player-name")
        print("Duración:",duracion)
        team_div = soup.find('div', class_='match-bm-lol-match-header-team')
        w_div = team_div.find_all('div')[-1]
        gana = w_div.get_text(strip=True)
        if gana == "W":
            ganador = equipos_partida[0]
            print("Gana",ganador)
        else:
            ganador = equipos_partida[1]
            print("Gana",ganador)
        jugadores_partida = []
        campeones_partida = []
        for info in jugadores_info:
            jugador = info.find("a").text
            personaje = info.find("i").text
            if jugador == "Shogun (Vietnamese player)":
                jugador = "Shogun"
            if jugador == "River (Korean player)":
                jugador = "River"
            if jugador == "Light (Wang Guang-Yu)":
                jugador = "Light"
            if jugador == "Viper (Korean player)":
                jugador = "Viper"
            if jugador == "Weiwei":
                jugador = "WeiWei"
            jugadores_partida.append(jugador)
            campeones_partida.append(personaje)
            #print(jugador, personaje)
        picks_bans(soup,equipos_partida,ganador)
        duracion_partida(ganador,duracion)
        #print(jugadores_partida)
        kda(soup,jugadores_partida,campeones_partida)
        partida_mas_larga(duracion)
        jugadores_distintos_2(jugadores_partida,campeones_partida)
        equipos_distintos_2(equipos_partida,campeones_partida)
        winrate()
        print("---------------------------------------------")
        ultimos_equipos = open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\ultimos_equipos.txt","w",encoding="utf8")
        json.dump(equipos_partida,ultimos_equipos,indent=4)
        ultimos_equipos.close()
    
    # Exportar datos para la web
    exportar_datos_web()
    print(f"Datos actualizados después del partido entre {equipos_partida[0]} y {equipos_partida[1]}")

if __name__ == "__main__":
    # Inicializar archivos si es necesario
    link = "https://liquipedia.net/leagueoflegends/Match:ID_Wrd25PlyIn_R01-M001"
    try:
        with open(r"C:\Users\ismae\OneDrive\Documentos\Entretenimiento\Worlds2025\links.txt","r") as fichero:
            links = json.load(fichero)
    except FileNotFoundError:
        links = []
    
    if link not in links:
        print("Procesando nueva partida...")
        main(links, link)
    else:
        print("Partida ya procesada. Exportando datos...")
        exportar_datos_web()