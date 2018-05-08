import apps.main.db_layer as db
import bcrypt

from django.http import JsonResponse
from django.shortcuts import redirect, render
from pprint import pprint

def create_mock_data():
    db.create_static_data()
    db.create_user('jon@email.com', 'Jon L', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('peter@email.com', 'Peter S', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('rick@email.com', 'Rick L', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('fiaz@email.com', 'Fiaz S', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('etienne@email.com', 'Etienne D', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_listing(1, '2018-01-01', '2018-12-31', 'Playboy Mansion', 'Party with models!', '10236 Charing Cross Road', '90024', 'USA', '1', 20, 10, 5.5, 10000, [ db.lookup_attr_id('stay_type','Entire place'), db.lookup_attr_id('prop_type','House'), db.lookup_attr_id('facilities','Free parking on premises'), db.lookup_attr_id('facilities','Gym'), db.lookup_attr_id('facilities','Hot tub'), db.lookup_attr_id('facilities','Pool'), db.lookup_attr_id('amenities','Kitchen'), db.lookup_attr_id('amenities','Heating'), db.lookup_attr_id('amenities','Air conditioning'), db.lookup_attr_id('amenities','Washer'), db.lookup_attr_id('amenities','Dryer'), db.lookup_attr_id('amenities','Wifi') ])
    return None

def get_logged_in_user(request):
    if 'user_id' not in request.session:
        return None
    try:
        return m.User.objects.get(id=request.session['user_id'])
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
    request.session.clear()
    return None, str(ex)

def logout(request):
    request.session.clear()
    return redirect('main:index')

def login_ajax(request):
    user = get_logged_in_user(request)
    if user:
        return JsonResponse({ 'url': redirect('main:index').url })
    if request.method != 'POST':
        return JsonResponse({ 'url': redirect('main:index').url }, status=405)
    email = request.POST.get('email')
    hashed_b64_pwd = request.POST.get('hashed_b64_pwd')
    if not email or not hashed_b64_pwd:
        return JsonResponse({ 'msg': 'All fields must be filled in!' }, status=400)
    user, error = db.get_user(email)
    if not user:
        if not error:
            error = 'internal server error!'
        return JsonResponse({ 'msg': error }, status=400)
    if not bcrypt.checkpw(hashed_b64_pwd.encode('utf-8'), user.encrypted_hashed_pwd.encode('utf-8')):
        return JsonResponse({ 'msg': 'Login attempt failed!' }, status=400)
    request.session['user_id'] = user.id
    return JsonResponse({ 'url': redirect('main:index').url })

def signup_ajax(request):
    user = get_logged_in_user(request)
    if user:
        return JsonResponse({ 'url': redirect('main:index').url })
    if request.method != 'POST':
        return JsonResponse({ 'url': redirect('main:index').url }, status=405)
    email = request.POST.get('email')
    fullname = request.POST.get('fullname')
    hashed_b64_pwd = request.POST.get('hashed_b64_pwd')
    if not email or not fullname or not hashed_b64_pwd:
        return JsonResponse({ 'msg': 'All fields must be filled in!' }, status=400)
    encrypted_bytes = bcrypt.hashpw(hashed_b64_pwd.encode('utf-8'), bcrypt.gensalt())
    encrypted_str = encrypted_bytes.decode('utf-8')
    user, error = db.create_user(email, fullname, encrypted_str)
    if not user and not error:
        error = 'internal server error!'
    if error:
        return JsonResponse({ 'msg': error }, status=400)
    request.session['user_id'] = user.id
    return JsonResponse({ 'url': redirect('main:index').url })

def index(request):
    create_mock_data()
    # db.create_booking('2018-03-24', '2018-04-04', 'bangkok1', 1000, 2, 2)
    # db.cancel_booking(2)
    # listing_ids = db.get_bookable_listings('2018-03-25', '2018-03-30', db.get_all_listing_ids())
    context = {}
    context['listings'] = db.get_all_listings()
    return render(request, 'main/index.html', context)

def listing(request, id):
    context = {}
    db.get_listing(id, context)
    return render(request, 'main/listing.html', context)

