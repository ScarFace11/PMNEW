"""
Нумерация в лабиринте:
    1 - Стенки лабиринта (через них нельзя пройти)
    2 - Пакмен - под управлением игрока
    4 - Ловушка(Лазер) - при косании игрок спавнится в стартовой точке, и теряет 1 хп
    5 - Монетка - в будущем нужна для покупки в магазине
    6 - бонус - находится на всех дорожках, нужно для набора счёта, в дальнейшем для рекордной таблицы
    9 - пустота 
"""

Tile_size = 50 # 50 почемуто?
color_way = (155, 205, 255)
#color_way = (255, 205, 255)
color_wall = (60, 60, 60)
color_bonus = (0, 255, 0)

#Width,Height = 1300,900  #основа
Width,Height = 1920,1080
#Width,Height = 620,840

fps = 60
