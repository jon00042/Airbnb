import json

##
## ORDER MATTERS: CANNOT BE CHANGED AFTER PROD DATA EXISTS
## THESE ARRAYS SERVE AS BITMASKS AND CANNOT HAVE MORE THAN 32 ITEMS
##

STAY_TYPE = ['Entire place','Private room','Shared room']
PROP_TYPE = ['House','Apartment','Bed and breakfast','Boutique hotel','Bungalow', 'Cabin','Chalet','Cottage','Guest suite','Guesthouse','Hostel','Hotel','Loft','Resort','Townhouse', 'Villa']
AMENITIES = ['Kitchen','Shampoo','Heating','A/C','Washer','Dryer','Wifi','Breakfast','Fireplace','Intercom','Doorman','Hangers','Iron','Hair dryer','Workspace','TV','Crib','High chair','Self check-in','Smoke detector']
FACILITIES = ['Free parking','Gym','Hot tub','Pool']
UNIQ_TYPE = ['Barn','Boat','Camper/RV','Campsite','Casa particular','Castle','Cave','Cycladic house','Dammuso','Dome house','Earth house','Farm stay','Houseboat','Hut','Igloo','Island','Lighthouse','Minsu','Nature lodge','Pension (South Korea)','Plane','Ryokan','Shepherds hut','Tent','Tiny house','Tipi','Train','Treehouse','Trullo','Windmill','Yurt']
#RULES = [('Not suitable for events','Suitable for events'),('No pets allowed','Pets allowed'),('Smoking not permitted','Smoking allowed')]

DICTS = {}

def mask_to_list(const_list, mask):
    if type(const_list) != list or type(mask) != int:
        return None
    out_list = []
    for i in range(len(const_list)):
        if mask & (1 << i):
            out_list.append(const_list[i])
    return out_list

def list_to_mask(const_list, in_list):
    if type(in_list) == str:
        in_list = json.loads(in_list)
    if type(const_list) != list or type(in_list) != list:
        return 0
    const_id_str = str(id(const_list))
    const_dict = DICTS.get(const_id_str)
    if not const_dict:
        const_dict = {}
        for i in range(len(const_list)):
            const_dict[const_list[i]] = 1 << i
        DICTS[const_id_str] = const_dict
    mask = 0
    for elem in in_list:
        if elem in const_dict:
            mask |= const_dict[elem]
    return mask

