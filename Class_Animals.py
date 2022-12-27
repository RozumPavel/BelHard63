class Animals:
    sounds = ("rrr", "auu", "mew", "gav")

    def __init__(self, kind: str, weight: int, color: str, speed: int):
        self.kind = kind
        self.weight = weight
        self.color = color
        self.speed = speed

    @classmethod
    def get_sound(cls, sound: str):
        cls.sound = sound
        if len(sound) >= 4 or len(sound) <= 2:
            raise ValueError("Звук должен быть написан 3 символами")
        elif sound not in cls.sounds:
            raise ValueError("У животного нет доступного звука")
        else:
            print(sound)


bear = Animals(kind="bear", weight=350, color="brown", speed=35)
bear.get_sound('rrr')

cat = Animals(kind="cat", weight=5, color="black", speed=25)
cat.get_sound('mew')

cow = Animals(kind="cow", weight=220, color="white", speed=20)
cow.get_sound('muu')  # данного звука нет, поэтому выдаст ошибку
