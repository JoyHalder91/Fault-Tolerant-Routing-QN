def compute_required_bell_pairs(demand, purification_rounds):
    """
    Her bir request için toplam gerekli Bell pair sayısını hesaplar.

    Args:
        demand (int or float): Request için gerekli qubit sayısı.
        purification_rounds (int): Gerekli purification round sayısı.

    Returns:
        float: Toplam gerekli Bell pair sayısı.
    """
    if purification_rounds is None:
        return None  # purification yapılamıyorsa

    if purification_rounds == 0:
        return demand  # sadece qubit kadar Bell pair gerekir

    required_bell_pairs_for_purification = 2 * purification_rounds
    required_bell_pairs_total = demand * required_bell_pairs_for_purification
    return required_bell_pairs_total