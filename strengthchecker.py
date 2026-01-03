import re

def check_password_strength(password):
    # handling empty input
    if not password:
        return ""  

    score = 0
    suggestions = []
    length = len(password)

    # length points
    if length >= 12:
        score += 30
    elif length >= 8:
        score += 20
    else:
        score += max(0, length * 2)
        suggestions.append("Use at least 8–12 characters")

    # bonus for extra long passwords
    if length > 12:
        score += min((length - 12) * 2, 10) 

    #uppercase & lowercase
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    if has_upper and has_lower:
        score += 20
    elif has_upper or has_lower:
        score += 10
        suggestions.append("Add both uppercase and lowercase letters")
    else:
        suggestions.append("Add both uppercase and lowercase letters")

    #digits
    digits = len(re.findall(r"\d", password))
    if digits >= 1:
        score += min(digits * 3, 20)  
    else:
        suggestions.append("Add numbers")

    #special characters
    specials = len(re.findall(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password))
    if specials >= 1:
        score += min(specials * 3, 20)  
    else:
        suggestions.append("Add special characters")

    #repeated patterns penalty
    if re.search(r"(.)\1{2,}", password):
        score -= 10
        suggestions.append("Avoid repeating the same characters 3+ times in a row")

    #simple brute-force penalty
    if re.fullmatch(r"\d+", password):
        score = min(score, 5) 
    elif re.fullmatch(r"[a-z]+", password, re.I):
        score = min(score, 10)  

    #cap score at 100 
    score = min(score, 100)

    #determine strength level 
    if score >= 75:
        level = "STRONG"
    elif score >= 50:
        level = "MEDIUM"
    else:
        level = "WEAK"

    #format result for flask
    result = f"Score: {score}/100\nStrength Level: {level}"
    if suggestions:
        result += "\nSuggestions:\n" + "\n".join(suggestions)

    return result
