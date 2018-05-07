import apps.main.db_layer as db
import bcrypt

from django.http import JsonResponse
from django.shortcuts import redirect, render

from pprint import pprint

def create_mock_data():
    db.create_static_data()
    db.create_user('jon@email.com', 'Jon L', 'xxx', 'M')
    db.create_user('peter@email.com', 'Peter S', 'xxx', 'M')

    db.create_listing('2018-07-28', '2018-08-05', 'miami', 'addr', None, 100, 1, 1, 1, 1, [])
    db.create_listing('2018-01-01', '2018-12-31', 'bangkok', 'addr', None, 100, 1, 1, 1, 1, [])
    db.create_listing('2018-06-01', '2018-10-31', 'tokyo', 'addr', None, 100, 1, 1, 1, 1, [])
    db.create_listing('2018-03-25', '2018-04-26', 'singapore', 'addr', None, 100, 1, 1, 1, 1, [])
    db.create_listing('2018-03-01', '2018-08-07', 'houston', 'addr', None, 100, 1, 1, 1, 1, [])
    return None

def get_logged_in_user(request):
    if 'user_id' not in request.session:
        return None
    try:
        return m.User.objects.get(id=request.session['user_id'])
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
    request.session.clear()
    return None, ex

def index(request):
    # create_mock_data()
    # db.create_booking('2018-03-24', '2018-04-04', 'bangkok1', 1000, 2, 2)
    # db.cancel_booking(2)
    # listing_ids = db.get_bookable_listings('2018-03-25', '2018-03-30', db.get_all_listing_ids())
    return render(request, 'main/index.html')

def signup_ajax(request):
    user = get_logged_in_user(request)
    if user:
        return JsonResponse({ 'url': redirect('main:index') })
    if request.method != 'POST':
        return JsonResponse({ 'url': redirect('main:index') }, status=405)
    email = request.POST.get('email')
    fullname = request.POST.get('fullname')
    hashed_pwd = request.POST.get('hashed_pwd')
    if (not email or not fullname or not hashed_pwd):
        return JsonResponse({ 'msg': 'one or more signup fields empty!' }, status=400)
    try:
        encrypted_bytes = bcrypt.hashpw(hashed_pwd.encode('utf-8'), bcrypt.gensalt())
        encrypted_str = encrypted_bytes.decode('utf-8')
        User.objects.create(email=email, encrypted_hashed_pwd=encrypted_str)
        return JsonResponse({ 'success': True })
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return JsonResponse({ 'url': redirect('main:index') }, status=500)

