cpu_price = float(input())
video_card_price = float(input())
price_for_one_ram_block = float(input())
number_of_ram_blocks = int(input())
percentage_discount = float(input())

cpu_price -= ((cpu_price / 100) * (percentage_discount * 100))
video_card_price -= ((video_card_price / 100) * (percentage_discount * 100))

final_price = cpu_price + video_card_price + price_for_one_ram_block * number_of_ram_blocks
final_price *= 1.57

print(f'Money needed - {final_price:.2f} leva.')
