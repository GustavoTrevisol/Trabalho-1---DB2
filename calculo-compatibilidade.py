def compatibilidade(pet, adotante):
    pontos = 0

    # Espécie
    if pet["especie"] == adotante["caracteristicas_desejadas"]["especie"]:
        pontos += 20
    else:
        pontos -= 20

    # Porte
    if pet.get("porte") == adotante["caracteristicas_desejadas"]["porte"]:
        pontos += 10
    else:
        pontos -= 10

    # Sexo
    if pet.get("sexo") == adotante["caracteristicas_desejadas"]["sexo"]:
        pontos += 5
    else:
        pontos -= 5

    # Saúde
    p_needs = pet.get("necessidades", {})
    a_needs = adotante["caracteristicas_desejadas"]

    if p_needs.get("tratamento_continuo") or p_needs.get("necessidades_especiais"):
        if a_needs.get("aceita_necessidades"):
            pontos += 10
    else:
        if a_needs.get("aceita_necessidades"):
            pontos += 5
        elif not a_needs.get("aceita_necessidades"):
            pontos += 10

    if not p_needs.get("doenca_cronica", False):
        if not a_needs.get("aceita_doenca_cronica", True):
            pontos += 5
    else:
        if a_needs.get("aceita_doenca_cronica", False):
            pontos += 10

    # Social (fatores impeditivos)
    social = pet.get("social", {})
    if social.get("com_outros_animais") is False and adotante["caracteristicas_desejadas"].get("possui_outros_animais"):
        return -9999  # Fator impeditivo
    if social.get("exige_cuidados_constantes") and not adotante["caracteristicas_desejadas"].get("tempo_disponivel", False):
        return -9999  # Fator impeditivo

    # Caso passe, dar pontos extras por adaptação social.
    if social.get("com_outros_animais") and adotante["caracteristicas_desejadas"].get("possui_outros_animais"):
        pontos += 5
    if social.get("exige_cuidados_constantes") and adotante["caracteristicas_desejadas"].get("tempo_disponivel"):
        pontos += 5

    return pontos