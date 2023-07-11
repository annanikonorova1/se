names = ['Анна', 'Елена', 'Алексей', 'Василий']
zarplata = [25000, 20000, 18000, 50000]
prem = ['10.25%', '15.00%', '18.50%', '12.05%']


def zarplata_gen(names: list[str], zarplata: list[int], prem: list[str]) -> dict[str: float]:
    return {name: sale / 100 * bon for name, sale, bon in zip(names, zarplata, (float(i[:-1]) for i in prem))}.items()
print(*(zarplata_gen(names, zarplata, prem)))