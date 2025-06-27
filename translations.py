TRANSLATIONS = {
    'ru': {
        'welcome': "🇦🇲 Добро пожаловать в ISrte Dating! 💕\n\nПервый локальный анонимный проект знакомств в Армении!\n\n🔒 Полная конфиденциальность\n💬 Безопасные знакомства\n🎯 Только люди из Армении\n\nВыберите язык / Ընտրեք լեզուն:",
    },
    'hy': {
        'welcome': "🇦🇲 Բարի գալուստ ISrte Dating! 💕\n\nՀայաստանի առաջին տեղական անանուն ծանոթությունների նախագիծ!\n\n🔒 Լրիվ գաղտնիություն\n💬 Անվտանգ ծանոթություններ\n🎯 Միայն Հայաստանի բնակիչներ\n\nԱռաջին հերթին ընտրեք լեզուն:",
    }
}

def get_text(key: str, lang: str = 'ru', **kwargs) -> str:
    text = TRANSLATIONS.get(lang, TRANSLATIONS['ru']).get(key, key)
    return text.format(**kwargs) if kwargs else text
