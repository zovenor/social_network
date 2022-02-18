class EN:
    class BASE:
        LogOut = "Logout"
        Friends = "Friends"
        NAME = "SN"
        choose_lang = "English"

    class Login(BASE):
        incorrect_username_or_password = 'Incorrect username or password!'
        title = "Login"
        no_account = "Don't you have an account?"

    class Account(BASE):
        username = "Username"
        email = "Email"
        name = "Name"
        surname = "Surname"

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
        add_request = "Add friend"

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


class RU(EN):
    class BASE(EN.BASE):
        LogOut = "Выйти"
        Friends = "Друзья"
        choose_lang = "Русский"

    class Login(EN.Login, BASE):
        incorrect_username_or_password = 'Неправильное имя пользователя или пароль!'
        title = "Вход"
        no_account = "Нет аккаунта?"

    class Account(EN.Account, BASE):
        username = "Имя пользователя"
        email = "Эл. почта"
        name = "Имя"
        surname = "Фамилия"

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
