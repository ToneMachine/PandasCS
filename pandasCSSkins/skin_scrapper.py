from bs4 import BeautifulSoup
import requests
import csv

item_type = 'skin'

weapon_types = {
    'pistols': ['cz75-auto', 'desert-eagle', 'dual-berettas', 'five-seven', 'glock-18', 'p2000', 'p250', 'r8-revolver', 'tec-9', 'usp-s'],
    'smgs': ['mac-10', 'mp5-sd', 'mp7', 'mp9', 'p90', 'pp-bizon', 'ump-45'],
    'heavy': ['m249', 'mag-7', 'negev', 'nova', 'sawed-off', 'xm1014'],
    'rifles': ['ak-47', 'aug', 'awp', 'famas', 'g3sg1', 'galil-ar', 'm4a1-s', 'm4a4', 'scar-20', 'sg-553', 'ssg-08'],
    #'knives': ['bayonet', 'bowie knife', 'butterfly knife', 'classic knife', 'falchion', 'flip knife', 'gut knife', 'huntsman knife', 'karambit', 'kukri knife', 'm9 bayonet', 'navaja knife', 'nomad knife', 'paracord knife', 'shadow daggers', 'skeleton knife', 'stiletto knife', 'survival knife', 'talon knife', 'urus knife'],
    #'gloves': ['bloodhound gloves', 'broken fang gloves', 'driver gloves', 'hand wraps', 'hydra gloves', 'moto gloves', 'specialist gloves', 'sport gloves']
}

# recursive func
def check_weapon(weapon, pattern_name, types_list):
    if not types_list:
        return

    # creates url
    weapon_type, weapon_list = types_list[0]
    if weapon in weapon_list:
        URL = f"https://cs2skins.gg/items/{item_type}/{weapon_type}/{weapon}/{pattern_name}"
        print("Scraping:", URL)

        # get request
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")
        item = soup.find("div", class_="skin-properties mt-6")

        # data value
        property_list = item.find_all("div", class_="attribute-row")

        rarity = item.find("a", class_="attribute-link").text
        weapon_category = property_list[0].text.replace("Name","")
        style_description = property_list[1].text
        weapon_Name = property_list[2].text.replace("Name","")
        sticker_slots = property_list[3].text
        pattern_Name = property_list[4].text.replace("Name","")
        float_range = property_list[5].text
        is_stattrak = property_list[6].text.strip("StatTrak Available o es")
        is_souvenir = property_list[7].text.strip("Souvenir Available es")
        team = property_list[9].text.replace("Name","").replace("Counter-Terrorist", "CT").replace("Terrorist", "T").replace("Both Teams", "Both")

        if pattern_name == 'howl':
            collection = None
        else:
            collection = item.find("div", class_="collection-info").text

        # writes to skin table csv file
        writer.writerow([weapon_category, weapon_Name, pattern_Name, rarity, is_stattrak, is_souvenir, team, collection])

    # continues with rest of the list
    else:
        check_weapon(weapon, pattern_name, types_list[1:])

# opens skin table csv file
with open("pandasCSSkins/skin_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "category", "weapon", "pattern",
        "rarity", "stat trak", "souvenir", "team", "collection"
    ])

    # read listing csv file
    with open("pandasCSSkins/listing.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                continue

            # creates weapon and weapon pattern name var
            name = row[1].lower().split('|')
            weapon = name[0].rstrip().replace(" ","-")
            pattern = (
                name[1].lstrip().replace("ö","").replace("ā","")
                .replace("'","").replace("!","").replace(".","").replace("&","")
                .replace(" 壱","").replace("弐","2").replace("龍王 ","")
                .replace(" ","-").replace("---","-").replace("--","-").replace("♥","") 
                if len(name) > 1 else None
                )

            # calls check weapon func
            check_weapon(weapon, pattern, list(weapon_types.items()))