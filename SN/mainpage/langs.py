class EN:
    class BASE:
        LogOut = "Logout"
        Friends = "Friends"
        NAME = "SN"
        choose_lang = "English"
        login = "Login"
        photos = "Photos"
        groups = "Groups"

    class Login(BASE):
        incorrect_username_or_password = 'Incorrect username or password!'
        title = "Login"
        no_account = "Don't you have an account?"
        login = "Login"

    class Account(BASE):
        username = "Username"
        email = "Email"
        name = "Name"
        surname = "Surname"
        error = "User not found!"
        permissions = "User restricted access"
        country = "Country"
        city = "City"
        sex = "Sex"
        age = "Birthday"
        sex_names = {
            'male': 'male',
            'female': 'female',
            'none': 'none',
        }
        add_friend = "Add to friends"
        edit = "Edit profile"
        sex_is_not_defined = "Sex is not defined"
        male = "Male"
        female = "Female"
        choose_sex = "Choose sex"
        post_save = "Save"
        post_error = "Some fields were not filled in!"
        remove_photo = "Remove the photo"
        choose_photo = "Choose the photo"

    class Friends(BASE):
        title = "Friends"
        your_friends = "Your friends"
        outgoing_requests = "Outgoing requests"
        friend_requests = "Friend requests"
        incoming_requests = "Incoming requests"
        accept_the_request = "Accept the request"
        user_del = "User deleted"
        remove_friend = "Remove a friend"
        remove_request = "Remove a request"
        all_users = "All users"
        add_request = "Add to friends"

    class Reg(BASE):
        title = "Registration"
        error_passwords = "Passwords don't match!"
        error_fields = "Some fields were not filled in!"
        name = "Your name"
        surname = "Your surname"
        email = "Your email"
        username = "Username"
        password1 = "Password"
        password2 = "Repeat password"
        error_email = "User with this email already exist!"
        error_username = "User with this username already exist!"
        register = "Register"
        birthday = "Birthday"
        country = "Country"
        city = "City"
        sex = "Sex"
        sex_is_not_defined = "Sex is not defined"
        male = "Male"
        female = "Female"
        choose_sex = "Choose sex"
        error_group = "Group with this username already exisst!"

    class Error404(BASE):
        title = "Page not found!"
        error_user_and_group_is_not_found = "Groups or user is not found!"

    class YourPhotos(BASE):
        title = "Photos"
        your_photos = "Your photos"
        redirect_to_all_photos = "Go to all photos"
        date = "Date"
        add_photo = "Add a photo"

    class AllPhotos(BASE):
        title = "All photos"
        all_photos = "All photos"
        user = "User"
        date = "Date"

    class AddPhoto(BASE):
        title = "Add a photo"
        add_photo = "Add a photo"
        error = "Dont't choose a photo!"

    class YourGroups(BASE):
        title = "Your groups"
        your_groups = "Your groups"
        create_group = "Create a group"
        all_groups = "All groups"

    class AllGroups(YourGroups):
        title = "All groups"

    class Group(BASE):
        followers = "Followers"
        admin = "Admin"
        editors = "Editors"

    class CreateGroup(BASE):
        title = "Create a group"
        name = "Name"
        description = "Description"
        groupname = "Groupname"
        create = "Create"


# #######################################################################################################################################

class RU(EN):
    class BASE(EN.BASE):
        LogOut = "Выйти"
        Friends = "Друзья"
        choose_lang = "Русский"
        login = "Войти"
        photos = "Фотографии"
        groups = "Группы"

    class Login(EN.Login, BASE):
        incorrect_username_or_password = 'Неправильное имя пользователя или пароль!'
        title = "Войти"
        no_account = "Нет аккаунта?"
        login = "Войти"

    class Account(EN.Account, BASE):
        username = "Имя пользователя"
        email = "Эл. почта"
        name = "Имя"
        surname = "Фамилия"
        error = "Пользователь не найден!"
        permissions = "Пользователь ограничил доступ"
        country = "Страна"
        city = "Город"
        sex = "Пол"
        age = "День рождения"
        sex_names = {
            'male': 'мужской',
            'female': 'женский',
            'none': 'не определён',
        }
        add_friend = "Добавить в друзья"
        edit = "Редактировать профиль"
        sex_is_not_defined = "Пол не определён"
        male = "Мужской"
        female = "Женский"
        choose_sex = "Выбрать пол"
        post_save = "Сохранить"
        remove_photo = "Убрать фотографию"
        choose_photo = "Выбрать фотографию"

    class Friends(EN.Friends, BASE):
        title = "Друзья"
        your_friends = "Ваши друзья"
        outgoing_requests = "Исходящие запросы"
        friend_requests = "Заявки в друзья"
        incoming_requests = "Входящие запросы"
        accept_the_request = "Принять запрос"
        user_del = "Пользователь удалён"
        remove_friend = "Убрать из друзей"
        remove_request = "Убрать запрос"
        all_users = "Все пользователи"
        add_request = "Добавить в друзья"

    class Reg(EN.Reg, BASE):
        title = "Регистрация"
        error_passwords = "Пароли не совпадают!"
        error_fields = "Некоторые поля не было заполнены!"
        name = "Ваше имя"
        surname = "Ваша фамилия"
        email = "Ваша почта"
        username = "Имя пользователя"
        password1 = "Пароль"
        password2 = "Повторить пароль"
        error_email = "Пользователь с данной почтой уже существует!"
        error_username = "Пользователь с данным именем пользователя уже существует!"
        register = "Зарегистрироваться"
        birthday = "День рождения"
        country = "Страна"
        city = "Город"
        sex = "Пол"
        sex_is_not_defined = "Пол не определён"
        male = "Мужской"
        female = "Женский"
        choose_sex = "Выбрать пол"
        error_group = "Группа с этим именем пользователя уже существует!"

    class Error404(EN.Error404, BASE):
        title = "Страница не найдена!"
        error_user_and_group_is_not_found = "Группа или пользователь не найден!"

    class YourPhotos(EN.YourPhotos, BASE):
        title = "Фотографии"
        your_photos = "Ваши фотографии"
        date = "Дата"
        redirect_to_all_photos = "Перейти ко всем фотографиям"
        add_photo = "Добавить фотографию"

    class AllPhotos(EN.AllPhotos, BASE):
        title = "Все фотографии"
        all_photos = "Все фотографии"
        user = "Пользователь"
        date = "Дата"

    class AddPhoto(EN.AddPhoto, BASE):
        title = "Добавить фотографию"
        add_photo = "Добавить фотографию"
        error = "Не выбрана фотография"

    class YourGroups(EN.YourGroups, BASE):
        title = "Ваши группы"
        your_groups = "Ваши группы"
        create_group = "Создать группу"
        all_groups = "Все группы"

    class AllGroups(EN.AllGroups, YourGroups):
        title = "Все группы"

    class Group(EN.Group, BASE):
        followers = "Подписчики"
        admin = "Админ"
        editors = "Редакторы"

    class CreateGroup(EN.CreateGroup, BASE):
        title = "Создать группу"
        name = "Название группы"
        description = "Описание группы"
        groupname = "Уникальное имя группы"
        create = "Создать"