from django.utils import timezone
import random

from tours.models import Tour

tour_names = [
    'Праздник огурца',
    'Фестиваль корюшки',
    'Рускеалa',
    'Крым',
    'Октоберфест'
]

levels = ['Normal', 'Gold', 'VIP', 'Platinum', 'Abramovich']

for name in tour_names:
    for level in levels:
        Tour.objects.create(tour_date=timezone.localdate() + timezone.timedelta(random.randint(10, 150)),
                            tour_name=f"{name} {level}",
                            tour_tickets=random.randint(20, 75),
                            tour_distance=random.randrange(200, 3000, 50))
