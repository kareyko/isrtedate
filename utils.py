def validate_age(age_text):
    try:
        age = int(age_text)
        return 18 <= age <= 99
    except ValueError:
        return False

def format_profile_text(profile):
    return f"Имя: {profile.get('name')}\nВозраст: {profile.get('age')}\nПол: {profile.get('gender')}\nИщет: {profile.get('goal')}\nОписание: {profile.get('bio', '')}"
