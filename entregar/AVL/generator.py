import random
with open("ejA.txt", "a") as txt:
    for _ in range(1800):
        name = random.choice(("C", "Rust", "Python", "Rust", "C++", "SQL", "PHP"))
        duration = random.randint(10, 240)
        n = random.randint(1, 25)
        lv = random.choice(("A", "B", "C", "D"))
        lang = random.choice(("Cas", "Gal", "Eng", "Ger", "Fre"))
        pr = round(random.uniform(5, 50), 2)
        txt.write(f"\n{name},{duration},{n},{lv},{lang},{pr}")