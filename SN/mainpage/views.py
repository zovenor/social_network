from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import langs
from .models import Friend, Follower, UserDetail, Photo


def user_to_user(self, request, user_view, url=""):
    id1 = request.user.id
    id2 = user_view.user.id
    response = {
        'url': request.path,
    }
    if Friend.objects.filter(user1=id1, user2=id2) or Friend.objects.filter(user1=id2, user2=id1):
        response.update({
            'text': get_wordlist(request).Friends.remove_friend,
            'link': f'/friends?rm=id{id2}',
            'class': "remove_friend",
        })
    elif Follower.objects.filter(user1=id2, user2=id1):
        response.update({
            'text': get_wordlist(request).Friends.accept_the_request,
            'link': f'/friends?add=id{id2}',
            'class': "accept_request",
        })
    elif Follower.objects.filter(user1=id1, user2=id2):
        response.update({
            'text': get_wordlist(request).Friends.remove_request,
            'link': f'/friends?rm_request=id{id2}',
            'class': "remove_request",
        })
    else:
        response.update({
            'text': get_wordlist(request).Friends.add_request,
            'link': f'/friends?add_request=id{id2}',
            'class': "add_request",
        })
    return f'<a class="{response["class"]}" href="{response["link"]}&url={response["url"]}">{response["text"]}</a>'


def base(func):
    def wrapper(self, request, content={}, *args, **kwargs):
        if request.user.is_authenticated:
            content.update({'your_user': UserDetail.objects.get(user=request.user)})
        return func(self, request, content=content, **kwargs)

    return wrapper


def page_not_found_view(request, exception):
    content = {
        'list': get_wordlist(request).Error404
    }
    return render(request, 'mainpage/404.html', content, status=404)


def url_redirect_or_not(request):
    if 'url' in request.GET:
        return redirect(request.GET['url'])
    else:
        return redirect(request.path)


def get_sex(request, sex):
    if sex == 'male':
        return get_wordlist(request).Account.sex_names['male']
    elif sex == 'female':
        return get_wordlist(request).Account.sex_names['female']
    else:
        return get_wordlist(request).Account.sex_names['none']


class HeheView(View):

    @base
    def get(self, request, content={}):
        content.update({
            'list': get_wordlist(request).BASE,
        })

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
    @base
    @user_is_authenticated
    def get(self, request, content={}):
        return redirect('/account')

    def post(self, request):
        return redirect('/')


class LogInView(View):
    @base
    def get(self, request, error='', content={}):
        content.update({
            'error': error,
            'list': get_wordlist(request).Login
        })

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

    @base
    def get(self, request, id=None, username=None, user_view=None, content={}):
        try:
            # if request receive username
            if username != None:
                id = User.objects.get(username=username).id
            # if user is admin
            if id == 1:
                return redirect('/admin/')
            content.update({
                'edit': False,
                'permissions': 'opened',
                'user_view': UserDetail.objects.get(user=id),
                'list': get_wordlist(request).Account,
                'get_sex': get_sex(request, UserDetail.objects.get(user=id).sex),
                'user_to_user': user_to_user(self, request, UserDetail.objects.get(user=id)),
                'edit_permissions': False,
                'choose_photo': False,
            })
            # if user is you
            if request.user.id == id and user_view == None:
                return redirect('/account')
            else:
                # if user is not transmitted (if path = "/account" you redirect to this func with the specific user)
                if user_view != None:
                    # if user wanna edit profile
                    if 'edit' in request.GET:
                        if request.GET['edit'] == 'True':
                            content['edit_permissions'] = True
                        else:
                            return redirect(request.path)
                    # if user remove account's photo
                    elif 'rm_photo' in request.GET:
                        if request.GET['rm_photo'] == 'True':
                             user_photo = UserDetail.objects.get(user=id)
                             user_photo.photo = None
                             user_photo.save()
                             return redirect("/account")
                    elif 'choose_photo' in request.GET:
                        if request.GET['choose_photo'] == 'True':
                            content['choose_photo'] = True
                            content['photos_library'] = Photo.objects.filter(user=id)
                    elif 'choose_photo_by_id' in request.GET:
                        try:
                            choose_photo_by_id = int(request.GET['choose_photo_by_id'])
                            user_photo = UserDetail.objects.get(user=id)
                            user_photo.photo = Photo.objects.get(id=choose_photo_by_id)
                            user_photo.save()
                            return redirect('/account')
                        except:
                            content['error'] = "Incorrect id!"
                    content['user_view'] = UserDetail.objects.get(user=request.user.id)
                    content['edit'] = True
                else:
                    if 'edit' in request.GET:
                        return redirect(request.path)
                    # check permissions
                    if content['user_view'].permissions == 'private':
                        # if you are not user's friend
                        if not Friend.objects.filter(user1=id, user2=request.user.id) and not Friend.objects.filter(
                                user1=request.user.id, user2=id):
                            content['permissions'] = 'closed'
                content['friends'] = Friend.objects.filter(user1=request.user.id, user2=content['user_view'].id).union(
                    Friend.objects.filter(user1=content['user_view'].id, user2=request.user.id))
                return render(request, 'mainpage/account.html', content)
        # If user is not found
        except:
            content.update({
                'list': get_wordlist(request).Account
            })
            return render(request, 'mainpage/error.html', content)


class AccountView(View):
    def get(self, request, username):
        return AccountIDView.get(self, request, username=username)


class YourAccountView(View):
    @user_is_authenticated
    def get(self, request, **kwargs):
        return AccountIDView.get(self, request, id=request.user.id,
                                 user_view=UserDetail.objects.get(user=request.user.id))

    def post(self, request):
        photo = UserDetail.objects.get(user=request.user).photo
        if 'photo' in request.FILES:
            photo = Photo.objects.create(user=request.user, photo=request.FILES['photo'])
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        sex = request.POST['sex']
        birthday = request.POST['date']
        country = request.POST['country']
        city = request.POST['city']

        user = UserDetail.objects.get(user=request.user)
        if name != "" and surname != "" and email != "" and sex != "" and birthday != "" and country != "" and city != "":
            user_main = User.objects.get(id=user.user.id)
            user_main.email = email
            user_main.first_name = name
            user_main.last_name = surname
            user.sex = sex
            user.age = birthday
            user.photo = photo
            user.country = country
            user.city = city
            user.save()
            user_main.save()
        else:
            return AccountIDView(self, request, id=request.user.id,
                                 content={'post_error': get_wordlist(request).Account.post_error})
        return redirect("/account")


class LogOutView(View):

    @user_is_authenticated
    def get(self, request, url="", **kwargs):
        logout(request)
        return redirect(request.GET['url'])


class FriendsView(View):
    @base
    @user_is_authenticated
    def get(self, request, content={}, **kwargs):
        user_id = request.user.id
        f1 = Friend.objects.filter(user1=user_id)
        f2 = Friend.objects.filter(user2=user_id)

        content.update({
            'list': get_wordlist(request).Friends,
            'friends': f1.union(f2),
            'incoming_requests': Follower.objects.filter(user2=user_id),
            'outgoing_requests': Follower.objects.filter(user1=user_id),
            'all_users': UserDetail.objects.all(),
        })

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
            return url_redirect_or_not(request)
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
            return url_redirect_or_not(request)
        except:
            pass

        # Remove request
        try:
            rm_request_id = int(request.GET['rm_request'][2:])
            if Follower.objects.filter(user1=user_id, user2=rm_request_id):
                Follower.objects.filter(user1=user_id, user2=rm_request_id).delete()
            return url_redirect_or_not(request)
        except:
            pass

        # Add request
        try:
            add_request_id = int(request.GET['add_request'][2:])
            if not Follower.objects.filter(user1=user_id, user2=add_request_id) and user_id != add_request_id:
                Follower.objects.create(user1=user_id, user2=add_request_id)
            return url_redirect_or_not(request)
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
        birthday = request.POST['date']
        country = request.POST['country']
        city = request.POST['city']
        sex = request.POST['sex']

        error = ""
        post_list = {
            'name': name,
            'surname': surname,
            'email': email,
            'username': username,
            'password1': password1,
            'password2': password2,
            'birthday': birthday,
            'country': country,
            'city': city,
            'sex': sex,
        }

        if name != "" and surname != "" and email != "" and username != "" and password1 != "" and password2 != "" and birthday != "" and country != "" and city != "" and sex != "":
            if password1 == password2:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        User.objects.create_user(first_name=name, last_name=surname, email=email, username=username,
                                                 password=password1)
                        UserDetail.objects.create(user=User.objects.get(username=username), age=birthday,
                                                  country=country, city=city, sex=sex)
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


class PhotosView(View):
    @base
    @user_is_authenticated
    def get(self, request, content={}, **kwargs):
        content.update({
            'list': get_wordlist(request).YourPhotos,
            'photos': Photo.objects.filter(user=request.user),
            'all_photos': None,
        })

        if 'all' in request.GET:
            if request.GET['all'] == 'True':
                content['all_photos'] = Photo.objects.filter(permissions="public")
                content['photos'] = None
                content['list'] = get_wordlist(request).AllPhotos
        elif 'add_photo' in request.GET:
            if request.GET['add_photo'] == "True":
                content['list'] = get_wordlist(request).AddPhoto

        return render(request, 'mainpage/photos.html', content)

    def post(self, request):
        if 'photo' in request.FILES:
            Photo.objects.create(user=request.user, photo=request.FILES['photo'])
            return redirect('/')
        else:
            return self.get(request, content={'error': get_wordlist(request).AddPhoto.error})
