import random

def generate_address_variations(dong_number: str, floor_number: str, house_number: str):
    if dong_number == "-":
        variations = [
            f"{house_number}",
            f"{house_number}호",
            f"{house_number} 호",
            f"제{house_number}호",
            f"제 {house_number}호",
            f"제{house_number} 호",
            f"제 {house_number} 호",
            f"{floor_number}층{house_number}",
            f"{floor_number}층 {house_number}",
            f"{floor_number}층,{house_number}",
            f"{floor_number}층, {house_number}",
            f"{floor_number}층 ,{house_number}",
            f"{floor_number}층 , {house_number}",
            f"{floor_number}층{house_number}호",
            f"{floor_number}층{house_number} 호",
            f"{floor_number}층,{house_number}호",
            f"{floor_number}층,{house_number} 호",
            f"{floor_number}층 {house_number}호",
            f"{floor_number}층 {house_number} 호",
            f"{floor_number}층, {house_number}호",
            f"{floor_number}층, {house_number} 호",
            f"{floor_number}층 ,{house_number}호",
            f"{floor_number}층 ,{house_number} 호",
            f"{floor_number}층 , {house_number}호",
            f"{floor_number}층 , {house_number} 호",
            f"{floor_number}층제{house_number}호",
            f"{floor_number}층제{house_number} 호",
            f"{floor_number}층제 {house_number}호",
            f"{floor_number}층제 {house_number} 호",
            f"{floor_number}층 제{house_number}호",
            f"{floor_number}층 제{house_number} 호",
            f"{floor_number}층 제 {house_number}호",
            f"{floor_number}층 제 {house_number} 호",
            f"{floor_number}층, 제{house_number}",
            f"{floor_number}층, 제 {house_number}",
            f"{floor_number}층, 제{house_number}호",
            f"{floor_number}층, 제 {house_number}호",
            f"{floor_number}층, 제{house_number} 호",
            f"{floor_number}층, 제 {house_number} 호",
            f"{floor_number}층,제{house_number}호",
            f"{floor_number}층,제 {house_number}호",
            f"{floor_number}층,제{house_number} 호",
            f"{floor_number}층,제 {house_number} 호",
            f"제{floor_number}층{house_number}",
            f"제{floor_number}층 {house_number}",
            f"제{floor_number}층,{house_number}",
            f"제{floor_number}층, {house_number}",
            f"제{floor_number}층 ,{house_number}",
            f"제{floor_number}층 , {house_number}",
            f"제{floor_number}층{house_number}호",
            f"제{floor_number}층{house_number} 호",
            f"제{floor_number}층,{house_number}호",
            f"제{floor_number}층,{house_number} 호",
            f"제{floor_number}층, {house_number}호",
            f"제{floor_number}층 {house_number}호",
            f"제{floor_number}층 {house_number} 호",
            f"제{floor_number}층제{house_number}호",
            f"제{floor_number}층제{house_number} 호",
            f"제{floor_number}층,제{house_number}호",
        ]
    else:
        variations = [
            f"{dong_number}동{house_number}",
            f"{dong_number}동 {house_number}",
            f"{dong_number}동{house_number}호",
            f"{dong_number}동 {house_number}호",
            f"{dong_number}동{house_number} 호",
            f"{dong_number}동 제{house_number}호",
            f"{dong_number}동 제 {house_number}호",
            f"{dong_number}동 제{house_number} 호",
            f"{dong_number}동 제 {house_number} 호",

            f"{dong_number}동{floor_number}층{house_number}",
            f"{dong_number}동 {floor_number}층{house_number}",
            f"{dong_number}동{floor_number}층 {house_number}",
            f"{dong_number}동 {floor_number}층 {house_number}",
            f"{dong_number}동{floor_number}층,{house_number}",
            f"{dong_number}동 {floor_number}층,{house_number}",
            f"{dong_number}동{floor_number}층, {house_number}",
            f"{dong_number}동 {floor_number}층, {house_number}",

            f"{dong_number}동{floor_number}층{house_number}호",
            f"{dong_number}동 {floor_number}층{house_number}호",
            f"{dong_number}동{floor_number}층 {house_number}호",
            f"{dong_number}동 {floor_number}층 {house_number}호",
            f"{dong_number}동{floor_number}층{house_number} 호",
            f"{dong_number}동 {floor_number}층{house_number} 호",
            f"{dong_number}동{floor_number}층 {house_number} 호",
            f"{dong_number}동 {floor_number}층 {house_number} 호",

            f"{dong_number}동{floor_number}층,{house_number}호",
            f"{dong_number}동 {floor_number}층,{house_number}호",
            f"{dong_number}동{floor_number}층, {house_number}호",
            f"{dong_number}동 {floor_number}층, {house_number}호",
            f"{dong_number}동{floor_number}층,{house_number} 호",
            f"{dong_number}동 {floor_number}층,{house_number} 호",
            f"{dong_number}동{floor_number}층, {house_number} 호",
            f"{dong_number}동 {floor_number}층, {house_number} 호",

            f"{dong_number}동{floor_number}층제{house_number}호",
            f"{dong_number}동 {floor_number}층제{house_number}호",
            f"{dong_number}동{floor_number}층 제{house_number}호",
            f"{dong_number}동 {floor_number}층 제{house_number}호",
            f"{dong_number}동{floor_number}층제 {house_number}호",
            f"{dong_number}동 {floor_number}층제 {house_number}호",
            f"{dong_number}동{floor_number}층 제 {house_number}호",
            f"{dong_number}동 {floor_number}층 제 {house_number}호",

            f"{dong_number}동{floor_number}층제{house_number} 호",
            f"{dong_number}동 {floor_number}층제{house_number} 호",
            f"{dong_number}동{floor_number}층 제{house_number} 호",
            f"{dong_number}동 {floor_number}층 제{house_number} 호",
            f"{dong_number}동{floor_number}층제 {house_number} 호",
            f"{dong_number}동 {floor_number}층제 {house_number} 호",
            f"{dong_number}동{floor_number}층 제 {house_number} 호",
            f"{dong_number}동 {floor_number}층 제 {house_number} 호",

            f"{dong_number}동{floor_number}층,제{house_number}호",
            f"{dong_number}동 {floor_number}층,제{house_number}호",
            f"{dong_number}동{floor_number}층, 제{house_number}호",
            f"{dong_number}동 {floor_number}층, 제{house_number}호",
            f"{dong_number}동{floor_number}층,제 {house_number}호",
            f"{dong_number}동 {floor_number}층,제 {house_number}호",
            f"{dong_number}동{floor_number}층, 제 {house_number}호",
            f"{dong_number}동 {floor_number}층, 제 {house_number}호",

            f"{dong_number}동{floor_number}층,제{house_number} 호",
            f"{dong_number}동 {floor_number}층,제{house_number} 호",
            f"{dong_number}동{floor_number}층, 제{house_number} 호",
            f"{dong_number}동 {floor_number}층, 제{house_number} 호",
            f"{dong_number}동{floor_number}층,제 {house_number} 호",
            f"{dong_number}동 {floor_number}층,제 {house_number} 호",
            f"{dong_number}동{floor_number}층, 제 {house_number} 호",
            f"{dong_number}동 {floor_number}층, 제 {house_number} 호",

            f"{dong_number}동제{floor_number}층{house_number}",
            f"{dong_number}동 제{floor_number}층{house_number}",
            f"{dong_number}동제{floor_number}층 {house_number}",
            f"{dong_number}동 제{floor_number}층 {house_number}",
            f"{dong_number}동제{floor_number}층,{house_number}",
            f"{dong_number}동 제{floor_number}층,{house_number}",
            f"{dong_number}동제{floor_number}층, {house_number}",
            f"{dong_number}동 제{floor_number}층, {house_number}",

            f"{dong_number}동제{floor_number}층{house_number}호",
            f"{dong_number}동 제{floor_number}층{house_number}호",
            f"{dong_number}동제{floor_number}층 {house_number}호",
            f"{dong_number}동 제{floor_number}층 {house_number}호",
            f"{dong_number}동제{floor_number}층{house_number} 호",
            f"{dong_number}동 제{floor_number}층{house_number} 호",
            f"{dong_number}동제{floor_number}층 {house_number} 호",
            f"{dong_number}동 제{floor_number}층 {house_number} 호",

            f"{dong_number}동제{floor_number}층,{house_number}호",
            f"{dong_number}동 제{floor_number}층,{house_number}호",
            f"{dong_number}동제{floor_number}층, {house_number}호",
            f"{dong_number}동 제{floor_number}층, {house_number}호",
            f"{dong_number}동제{floor_number}층,{house_number} 호",
            f"{dong_number}동 제{floor_number}층,{house_number} 호",
            f"{dong_number}동제{floor_number}층, {house_number} 호",
            f"{dong_number}동 제{floor_number}층, {house_number} 호",

            f"{dong_number}동제{floor_number}층제{house_number}호",
            f"{dong_number}동 제{floor_number}층제{house_number}호",
            f"{dong_number}동제{floor_number}층 제{house_number}호",
            f"{dong_number}동 제{floor_number}층 제{house_number}호",
            f"{dong_number}동제{floor_number}층제 {house_number}호",
            f"{dong_number}동 제{floor_number}층제 {house_number}호",
            f"{dong_number}동제{floor_number}층 제 {house_number}호",
            f"{dong_number}동 제{floor_number}층 제 {house_number}호",

            f"{dong_number}동제{floor_number}층,제{house_number}호",
            f"{dong_number}동 제{floor_number}층,제{house_number}호",
            f"{dong_number}동제{floor_number}층, 제{house_number}호",
            f"{dong_number}동 제{floor_number}층, 제{house_number}호",
            f"{dong_number}동제{floor_number}층,제 {house_number}호",
            f"{dong_number}동 제{floor_number}층,제 {house_number}호",
            f"{dong_number}동제{floor_number}층, 제 {house_number}호",
            f"{dong_number}동 제{floor_number}층, 제 {house_number}호",

            f"{dong_number}동제{floor_number}층{house_number}",
            f"{dong_number}동 제{floor_number}층{house_number}",
            f"{dong_number}동제{floor_number}층 {house_number}",
            f"{dong_number}동 제{floor_number}층 {house_number}",
            f"{dong_number}동제{floor_number}층,{house_number}",
            f"{dong_number}동 제{floor_number}층,{house_number}",
            f"{dong_number}동제{floor_number}층, {house_number}",
            f"{dong_number}동 제{floor_number}층, {house_number}",
        ]

    random.shuffle(variations)
    return variations

def split_address_number(address_number: str):
    parts = address_number.split("-")

    if len(parts) == 1:
        return parts[0], ""

    return parts[0], parts[1]

def split_phone_number(phone_number: str):
    phone_number = phone_number[3:]
    first_part = phone_number[:4]
    second_part = phone_number[4:]
    return first_part, second_part

def generate_full_address(city_name: str, district_name: str, dong_name: str):
    return f"{city_name} {district_name} {dong_name}"