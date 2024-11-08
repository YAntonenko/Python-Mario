#08.11.2024 Yuna Antonenko
#Ülesane 11

def pikim_sona(*sonad):
    pikim = 0
    for i in sonad:
        if len(i)>pikim:
            pikim=len(i)
    print(f"Pikkim sõna on {pikim} märki!")


pikim_sona("üks","kaks","kolmkümmend", "kaheksa", "vjfgdlfökvlkjnpoegrvlkös")