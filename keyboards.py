from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_language_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Русский 🇷🇺", callback_data="lang_ru")],
        [InlineKeyboardButton(text="Հայերեն 🇦🇲", callback_data="lang_hy")]
    ])

def get_main_menu_keyboard():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🔍 Смотреть анкеты")],
        [KeyboardButton(text="❤️ Мои совпадения"), KeyboardButton(text="👤 Мой профиль")],
        [KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="ℹ️ Помощь")]
    ], resize_keyboard=True)

def get_gender_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👨 Мужской", callback_data="gender_male")],
        [InlineKeyboardButton(text="👩 Женский", callback_data="gender_female")],
        [InlineKeyboardButton(text="🏳️‍⚧️ Другое", callback_data="gender_other")]
    ])

def get_goal_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💕 Серьезные отношения", callback_data="goal_serious")],
        [InlineKeyboardButton(text="😊 Легкие отношения", callback_data="goal_casual")],
        [InlineKeyboardButton(text="👥 Дружба", callback_data="goal_friendship")],
        [InlineKeyboardButton(text="🤷 Просто посмотреть", callback_data="goal_looking")]
    ])

def get_skip_bio_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⏭️ Пропустить", callback_data="skip_bio")]
    ])

def get_profile_action_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="❤️ Лайк", callback_data="like"),
            InlineKeyboardButton(text="👎 Пропустить", callback_data="pass")
        ]
    ])

def get_match_keyboard(user_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать сообщение", url=f"tg://user?id={user_id}")],
        [InlineKeyboardButton(text="❤️ Посмотреть совпадения", callback_data="view_matches")],
        [InlineKeyboardButton(text="🔙 В меню", callback_data="back_to_menu")]
    ])

def get_profile_menu_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✏️ Редактировать профиль", callback_data="edit_profile")],
        [InlineKeyboardButton(text="🔙 В меню", callback_data="back_to_menu")]
    ])
