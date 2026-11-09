def media(*notas):
    media = sum(notas) / len(notas)
    return media

print(media(9, 8, 5, 8))
print(media(10, 6))


