from bs4 import BeautifulSoup
import requests
import csv

item_type = 'skin'
weapon_type_list = ['pistols', 'smgs', 'heavy', 'rifles', 'knives', 'gloves']
pistols_list = ['cz75-auto', 'desert-eagle', 'dual-berettas', 'five-seven', 'glock-18', 'p2000', 'p250', 'r8-revolver', 'tec-9', 'usp-s']
smgs_list = ['mac-10', 'mp5-sd', 'mp7', 'mp9', 'p90', 'pp-bizon', 'ump-45']
heavy_list = ['m249', 'mag-7', 'negev', 'nova', 'sawed-off', 'xm1014']
rifles_list = ['ak-47', 'aug', 'awp', 'famas', 'g3sg1', 'galil ar', 'm4a1-s', 'm4a4', 'scar-20', 'sg 553', 'ssg 08']
knifes_list = ['bayonet', 'bowie knife', 'butterfly knife', 'classic knife', 'falchion', 'flip knife', 'gut knife', 'huntsman knife', 'karambit', 'kukri knife', 'm9 bayonet', 'navaja knife', 'nomad knife', 'paracord knife', 'shadow daggers', 'skeleton knife', 'stiletto knife', 'survival knife', 'talon knife', 'urus knife']
gloves_list = ['bloodhound gloves', 'broken fang gloves', 'driver gloves', 'hand wraps', 'hydra gloves', 'moto gloves', 'specialist gloves', 'sport gloves']


#URL = f"https://cs2skins.gg/items/{item_type}/{weapon_type}/{weapon}/{weapon_name}"

with open("pandasCSSkins/listing.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 2:
            continue

        name = row[1].lower().split('|')
        weapon = name[0].rstrip()
        weapon_name = name[1].lstrip() if len(name) > 1 else None

        for weapon_type in weapon_type_list:

            if weapon_type == 'pistols':
                if weapon in pistols_list:
                    print(item_type, weapon_type, weapon, weapon_name)

            elif weapon_type == 'smgs':
                if weapon in smgs_list:
                    print(item_type, weapon_type, weapon, weapon_name)

            elif weapon_type == 'heavy':
                if weapon in heavy_list:
                    print(item_type, weapon_type, weapon, weapon_name)

            elif weapon_type == 'rifles':
                if weapon in rifles_list:
                    print(item_type, weapon_type, weapon, weapon_name)

            elif weapon_type == 'knifes':
                if weapon in knifes_list:
                    print(item_type, weapon_type, weapon, weapon_name)

            elif weapon_type == 'gloves':
                if weapon in gloves_list:
                    print(item_type, weapon_type, weapon, weapon_name)