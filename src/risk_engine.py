def calculate_risk(probability):

    if probability > 0.8:
        return "HIGH RISK"

    elif probability > 0.5:
        return "MEDIUM RISK"

    else:
        return "LOW RISK"