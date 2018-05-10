import apps.main.db_layer as db
import apps.main.mock as mock
import bcrypt

from django.http import JsonResponse
from django.shortcuts import redirect, render
from pprint import pprint

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
    mock.create_users()
    mock.create_listings()
    context = {}
    context['listings'] = db.get_all_listings()
    return render(request, 'main/index.html', context)

def filter_ajax(request):
    if request.method != 'POST':
        return JsonResponse({ 'url': redirect('main:index').url }, status=405)
    response_data = {}
    from_date = request.POST.get('from_date')
    to_date = request.POST.get('to_date')
    if from_date and to_date:
        bookable_listing_ids_qs = db.get_bookable_listings_ids(from_date, to_date)
        dict_str = '{'
        for listing_id in bookable_listing_ids_qs:
            dict_str += ' "{}" : {}, '.format(listing_id, 1)
        if len(dict_str) > 3:
            dict_str = dict_str[:-2]
        dict_str += ' }'
        response_data['bookable_listing_ids_dict_str'] = dict_str;
    return JsonResponse(response_data)

def listing(request, id):
    context = {}
    db.get_listing(id, context)
    return render(request, 'main/listing.html', context)

