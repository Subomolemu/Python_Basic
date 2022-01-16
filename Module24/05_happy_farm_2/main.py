import gardener


gardener_1 = gardener.PotatoGardener('Федя', 5)
gardener_1.garden_care()
potato_bucket = gardener_1.harvest()
for potato in potato_bucket:
    print(potato)
