

def minimumHealth(damage, armor):
    total = sum(damage)
    maxDamage = max(damage)

    return 1 + total - min(armor, maxDamage)
