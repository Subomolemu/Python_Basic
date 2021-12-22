players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

new_players = []
for man, points in players.items():
    new_players.append(sum((man, points), ()))
print(new_players)
