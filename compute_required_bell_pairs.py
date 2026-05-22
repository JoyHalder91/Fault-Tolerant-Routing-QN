def compute_required_bell_pairs(demand, purification_rounds):
    """
    Her bir request için toplam gerekli Bell pair sayısını hesaplar.

    Args:
        demand (int or float): Request için gerekli qubit sayısı.
        purification_rounds (int): Gerekli purification round sayısı.

    Returns:
        int: Toplam gerekli Bell pair sayısı.
    """
    if purification_rounds == 0:
        required_bell_pairs_for_purification = 1
    else:
        required_bell_pairs_for_purification = 2 * purification_rounds

    required_bell_pairs_total = demand * required_bell_pairs_for_purification
    return required_bell_pairs_total