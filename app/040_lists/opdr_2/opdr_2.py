# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# 1e rivier, 2e land 
print("De rivier", rivieren[0].capitalize(), "stroomt onder andere door", rivier_info[rivieren[0]][1].capitalize())

# 2e rivier, 1e land
print("De rivier", rivieren[1].capitalize(), "stroomt onder andere door", rivier_info[rivieren[1]][0].capitalize())

# 3e rivier, 3e land
print("De rivier", rivieren[2].capitalize(), "stroomt onder andere door", rivier_info[rivieren[2]][2].capitalize())

