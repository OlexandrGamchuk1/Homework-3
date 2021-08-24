a = int(input('Enter apartment numbers '))
if 0 < a <= 144:
    print(f'On the {int((a - 1) % 36 / 4 + 1)}th floor.')
    print(f'{int((a - 1) / 36 + 1)} entrance.')
else:
    print('No apartment')