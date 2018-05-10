import apps.main.constants as const
import apps.main.db_layer as db
import apps.main.keys as keys
import apps.main.mock as mock
import bcrypt
import json

from django.http import JsonResponse
from django.shortcuts import redirect, render

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
    context['all_stay_types'] = const.STAY_TYPE
    context['all_prop_types'] = const.PROP_TYPE
    context['all_uniq_types'] = const.UNIQ_TYPE
    context['all_amenities'] = const.AMENITIES
    context['all_facilities'] = const.FACILITIES
    return render(request, 'main/index.html', context)

def criteria_ajax(request):
    if request.method != 'POST':
        return JsonResponse({ 'url': redirect('main:index').url }, status=405)
    filtered_listing_ids_dict = db.get_filtered_listing_ids_dict(request.POST)
    response_data = {}
    response_data['filtered_listing_ids_dict_str'] = json.dumps(filtered_listing_ids_dict)
    return JsonResponse(response_data)

def listing(request, id):
    context = {}
    db.get_listing(id, context)
    context['gmap_api_key'] = keys.GMAP_API_KEY
    return render(request, 'main/listing.html', context)

