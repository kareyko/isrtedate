from aiogram.fsm.state import StatesGroup, State

class RegistrationStates(StatesGroup):
    choosing_language = State()
    waiting_for_name = State()
    waiting_for_age = State()
    waiting_for_gender = State()
    waiting_for_goal = State()
    waiting_for_photo = State()
    waiting_for_bio = State()

class BrowsingStates(StatesGroup):
    browsing_profiles = State()

class EditProfileStates(StatesGroup):
    editing_profile = State()
