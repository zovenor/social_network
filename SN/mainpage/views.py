from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import langs
from .models import Friend, Follower, UserDetail


def page_not_found_view(request, exception):
    content = {
        'list': get_wordlist(request).Error404
    }
    return render(request, 'mainpage/404.html', content, status=404)


def get_sex(request, sex):
    if sex == 'male':
        return get_wordlist(request).Account.sex_names['male']
    elif sex == 'female':
        return get_wordlist(request).Account.sex_names['female']
    else:
        return get_wordlist(request).Account.sex_names['none']


def hehe(request):
    content = {
        'list': get_wordlist(request).BASE,
    }

    return render(request, 'mainpage/hehe.html', content)


# Decorator for authentication
def user_is_authenticated(func):
    def redir(self, request):
        return redirect('/login')

    def wrapper(self, request, **kwargs):
        if request.user.is_authenticated:
            return func(self, request, **kwargs)
        else:
            return redir(self, request)

    return wrapper


def get_wordlist(request):
    langs_list = {
        'en': langs.EN,
        'ru': langs.RU,
    }
    if 'lang' in request.COOKIES:
        lang = request.COOKIES['lang']
        try:
            return langs_list[lang]
        except:
            return langs_list['en']
    else:
        return langs_list['en']


class IndexView(View):

    @user_is_authenticated
    def get(self, request):
        return redirect('/account')

    def post(self, request):
        return redirect('/')


class LogInView(View):
    def get(self, request, error=''):
        content = {
            'error': error,
            'list': get_wordlist(request).Login
        }

        if not request.user.is_authenticated:
            return render(request, 'mainpage/login.html', content)
        else:
            return redirect("/")

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return self.get(request, error=get_wordlist(request).Login.incorrect_username_or_password)
        else:
            login(request, user)
            return redirect('/')


class AccountIDView(View):

    def get(self, request, id=None, username=None, user_view=None):
        try:
            if username != None:
                id = User.objects.get(username=username).id
            if id == 1:
                return redirect('/admin/')
            content = {
                'permissions': 'opened',
                'user_view': UserDetail.objects.get(user=id),
                'list': get_wordlist(request).Account,
                'get_sex': get_sex(request, UserDetail.objects.get(user=id).sex),
            }
            if request.user.id == id and user_view == None:
                return redirect('/account')
            else:
                if user_view != None:
                    content['user_view'] = UserDetail.objects.get(user=request.user.id)
                else:
                    if content['user_view'].permissions == 'private':
                        if not Friend.objects.filter(user1=id, user2=request.user.id) and not Friend.objects.filter(
                                user1=request.user.id, user2=id):
                            content['permissions'] = 'closed'
                return render(request, 'mainpage/account.html', content)
        except:
            content = {
                'list': get_wordlist(request).Account
            }
            return render(request, 'mainpage/error.html', content)


class AccountView(View):
    def get(self, request, username):
        return AccountIDView.get(self, request, username=username)


class YourAccountView(View):
    @user_is_authenticated
    def get(self, request):
        return AccountIDView.get(self, request, id=request.user.id,
                                 user_view=UserDetail.objects.get(user=request.user.id))


class LogOutView(View):

    @user_is_authenticated
    def get(self, request):
        logout(request)
        return redirect(request.GET['url'])


class FriendsView(View):
    @user_is_authenticated
    def get(self, request):
        user_id = request.user.id
        f1 = Friend.objects.filter(user1=user_id)
        f2 = Friend.objects.filter(user2=user_id)

        content = {
            'list': get_wordlist(request).Friends,
            'friends': f1.union(f2),
            'incoming_requests': Follower.objects.filter(user2=user_id),
            'outgoing_requests': Follower.objects.filter(user1=user_id),
            'all_users': User.objects.all(),
        }

        id_list = {
            'friends': [],
            'incoming_requests': [],
            'outgoing_requests': [],
        }

        for el in content['friends']:
            if user_id == el.user1:
                id_list['friends'] += [el.user2]
            else:
                id_list['friends'] += [el.user1]

        for el in content['incoming_requests']:
            id_list['incoming_requests'] += [el.user1]

        for el in content['outgoing_requests']:
            id_list['outgoing_requests'] += [el.user2]

        content['id_list'] = id_list

        # Accept request
        try:
            add_id = int(request.GET['add'][2:])
            if Follower.objects.filter(user1=add_id, user2=user_id):
                Friend.objects.create(user1=user_id, user2=add_id)
                Follower.objects.filter(user1=add_id, user2=user_id).delete()
            return redirect(request.path)
        except:
            pass

        # Remove friend
        try:
            rm_id = int(request.GET['rm'][2:])
            if Friend.objects.filter(user1=rm_id, user2=user_id):
                Follower.objects.create(user1=rm_id, user2=user_id)
                Friend.objects.filter(user1=rm_id, user2=user_id).delete()
            elif Friend.objects.filter(user1=user_id, user2=rm_id):
                Follower.objects.create(user1=rm_id, user2=user_id)
                Friend.objects.filter(user1=user_id, user2=rm_id).delete()
            return redirect(request.path)
        except:
            pass

        # Remove request
        try:
            rm_request_id = int(request.GET['rm_request'][2:])
            if Follower.objects.filter(user1=user_id, user2=rm_request_id):
                Follower.objects.filter(user1=user_id, user2=rm_request_id).delete()
            return redirect(request.path)
        except:
            pass

        # Add request
        try:
            add_request_id = int(request.GET['add_request'][2:])
            if not Follower.objects.filter(user1=user_id, user2=add_request_id) and user_id != add_request_id:
                Follower.objects.create(user1=user_id, user2=add_request_id)
            return redirect(request.path)
        except:
            pass

        return render(request, 'mainpage/friends.html', content)


class RegView(View):
    def get(self, request, error="", post_list={}):
        if not request.user.is_authenticated:
            content = {
                'list': get_wordlist(request).Reg,
                'error': error,
                'pl': post_list,
            }
            return render(request, 'mainpage/reg.html', content)
        else:
            return redirect('/')

    def post(self, request):

        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        error = ""
        post_list = {
            'name': name,
            'surname': surname,
            'email': email,
            'username': username,
            'password1': password1,
            'password2': password2,
        }

        if name != "" and surname != "" and email != "" and username != "" and password1 != "" and password2 != "":
            if password1 == password2:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        User.objects.create_user(first_name=name, last_name=surname, email=email, username=username,
                                                 password=password1)
                        user = authenticate(username=username, password=password1)
                        login(request, user)
                        return redirect("/")
                    else:
                        error = get_wordlist(request).Reg.error_email  # User with this email already exist!
                else:
                    error = get_wordlist(request).Reg.error_username  # User with this username already exist!
            else:
                error = get_wordlist(request).Reg.error_passwords  # Password don't match!
        else:
            error = get_wordlist(request).Reg.error_fields  # Some fields were not filled in!

        return self.get(request, error=error, post_list=post_list)
