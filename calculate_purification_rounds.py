


def purification_rounds(F_initial, F_threshold):
    """
    Belirli bir F_initial ile başlayarak F_threshold'a ulaşmak için gereken purification round sayısını hesaplar.

    Parametreler:
    - F_initial (float): Başlangıç fidelitesi (0 < F < 1)
    - F_threshold (float): Hedef fidelite (0 < F < 1)

    Dönüş:
    - L (int): Gerekli minimum purification round sayısı
    - F_current (float): Son elde edilen fidelite
    """
    if not (0 < F_initial < 1 and 0 < F_threshold < 1):
        raise ValueError("Fidelity values must be between 0 and 1 (exclusive).")

    F_current = F_initial
    L = 0

    while F_current < F_threshold:
        F_current = F_current**2 / (F_current**2 + (1 - F_current)**2)
        L += 1
        # Eğer aynı değerde takılıyorsa (yaklaşamıyorsa), döngüyü kır
        if abs(1 - F_current) < 1e-10:
            break

    return L, F_current