import emoji
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks: :party_popper: ' * 3))
print('BUM! BUM! POOOW!\033[1;35m')
print('HAPPY NEW YEAR!\033[m')
print(emoji.emojize(':fireworks: :party_popper: ' * 3))
