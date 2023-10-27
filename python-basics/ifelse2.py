_points = int(input())
_bonus_points = 0

if _points < 100:
    _bonus_points = 5
elif 100 <= _points < 200:
    _bonus_points = 6
elif _points >= 200:
    _bonus_points = 7

print(f'BONUS POINTS: {_bonus_points} ')
print(f'TOTAL POINTS: {_points}')
