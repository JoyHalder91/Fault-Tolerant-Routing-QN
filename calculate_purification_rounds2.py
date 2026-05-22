


def calculate_purification_rounds(F_initial, required_threshold):
    F_current = F_initial
    rounds = 0

    while F_current < required_threshold:
        F_current = (F_current ** 2) / (F_current ** 2 + (1 - F_current) ** 2)
        rounds += 1
        # Sonsuz döngüye karşı önlem (örneğin threshold ulaşılmazsa)
        if rounds > 100:
            print("Warning: Too many rounds, purification may not converge.")
            break

    return rounds , F_current