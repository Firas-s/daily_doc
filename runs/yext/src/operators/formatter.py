import json
from src.operators.date import get_timedelta
from src.operators.date import add_hours
from src.operators.date import get_hours

def parser():
    return None

def get_value(store, key):
    if "." in key:
        s = key.split(".")
        for i in s:
            store = store.get(i, {})
            if not store:
                return store == None     
        return store
    else:
        return store.get(key)
    
def get_openings(store):
    """ retrieve opening and closing times of stores for weekdays and Holidays 
    Parameters 
    ----------
    store : index of value in JSON file
    Returns
    -------
    dataframe : Dictionary which contains openings and closing times, time range 
    of stores for weekdays and Holidays 
    """     
    dataframe = dict()
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    dataframe["total_hours"] = get_timedelta("00:00")
    for day in days:
        item = dict()
        try:
            delta = get_timedelta("00:00")
            item["openings"] = store.get("hours", {}).get(day, {}).get("openIntervals", [])
            for time in store.get("hours", {}).get(day, {}).get("openIntervals"):
                if time["start"] < time["end"]:
                    time1 = get_timedelta(time["start"])
                    time2 = get_timedelta(time["end"])
                    hours = get_hours(time2 - time1)
                    delta = get_timedelta(hours) + delta
            item["hours"] = get_hours(delta)
            dataframe["total_hours"] = dataframe["total_hours"] + delta

        except Exception as e:
            item["hours"] = None
        item["is_closed"] = store.get("hours", {}).get(day, {}).get("isClosed", False)

        dataframe[day] = item
    dataframe["total_hours"] = get_hours(dataframe["total_hours"])

    dataframe["holidays"] = []
    if store.get("hours", {}).get("holidayHours") is not None:
        dataframe["total_hours_Holidays"] = get_timedelta("00:00")
        for holiday in store.get("hours", {}).get("holidayHours"):
            if holiday.get("date") is not None:
                item = dict()
                delta = get_timedelta("00:00")
                item["date"] = holiday.get("date")
                item["openings"] = holiday.get("openIntervals", [])
                if holiday.get("openIntervals") is not None:
                    for time in holiday.get("openIntervals", []):
                        if time["start"] < time["end"]:
                            time1 = get_timedelta(time["start"])
                            time2 = get_timedelta(time["end"])
                            hours = get_hours(time2 - time1)
                            delta = get_timedelta(hours) + delta
                    item["hours"] = get_hours(delta)
                    dataframe["total_hours_Holidays"] = dataframe["total_hours_Holidays"] + delta
            
            item["is_closed"] = holiday.get("isClosed", False)
            dataframe["holidays"].append(item)
        dataframe["total_hours_Holidays"] = get_hours(dataframe["total_hours_Holidays"])
        
    return dataframe

def str_bool(store, index):
    """ Convert string to Bool 
    
    Parameters 
    ----------
    store : index of value in JSON file
    index : Dictionary value 

    Returns
    -------
    True/False : conversion of string ("true" or "false") to boolean (True or False)
    """     
    value = store.get("googleAttributes", {}).get(index, [None])[0]
    return True if value == "true" else False

def coord(store, index):
    """ Convert Bool to None 
    
    Parameters 
    ----------
    store : index of value in JSON file
    index : Dictionary value 

    Returns
    -------
    None : conversion of Bool ("false") to None
    """     
    value = get_value(store,index)
    return None if value == False else value

def get_image(store):
    """ Retrieve multiple images of the brands  
    
    Parameters 
    ----------
    store : index of value in JSON file 

    Returns
    -------
    dataframe : Dictionary which contains "googleProfilePhoto" and "images" of each store
    """     
    dataframe = dict()
    try:
        dataframe["googleProfilePhoto"] = store.get("googleProfilePhoto", {}).get("url", None)
        dataframe["image"] = store.get("photoGallery", [None])[0].get("image", {}).get("url", None)
        dataframe["image2"] = store.get("photoGallery", [None])[1].get("image", {}).get("url", None)
    except Exception as e:
        dataframe["googleProfilePhoto"] = None
        dataframe["image"] = None
        dataframe["image2"] = None
    return dataframe
 
def oneStock(store):
    """ Retrieve 'OneStock' informations  
    
    Parameters 
    ----------
    store : index of value in JSON file 

    Returns
    -------
    dataframe : Dictionary which contains all "oneStock" informations of stores 
    """
    dataframe = dict()
    for index in store.keys():
        if index == "c_email_directeur_region_darj_onestock" or index == "c_cLFLOneStockRegional_diretor_email":
            dataframe["c_email_directeur_region_onestock"] = store.get(index, None)
        elif index == "c_centre_ville_darj_onestock" or index == "c_cLFLOneStockDowntown":
            dataframe["c_centre_ville_onestock"] = store.get(index, None)
        elif index == "c_darjOneStockAdyen_merchant_account" or index == "c_cLFLOneStockAdyen_merchant_account":
            dataframe["c_OneStockAdyen_merchant_account"] = store.get(index, None)
        elif index == "c_cLFLOneStockCfs_active": 
            dataframe["c_OneStockCfs_active"] = store.get(index,None)
        elif index == "c_cfs_actif_darj_onestock":
            dataframe["c_OneStockCfs_active"] = True if store.get(index, None) == "True" else False 
        elif index == "c_cLFLOneStockOis_active":
            dataframe["c_OneStockOis_active"] = store.get(index, None)
        elif index == "c_ois_actif_darj_onestock":
            dataframe["c_OneStockOis_active"] = True if store.get(index, None) == "True" else False
        elif index == "c_cLFLOneStockRc_active":
            dataframe["c_OneStockRc_active"] = store.get(index, None)
        elif index == "c_rc_actif_darj_onestock":
            dataframe["c_OneStockRc_active"] = True if store.get(index, None) == "True" else False
        elif index == "c_priorite_magasin_darj_onestock" or index == "c_cLFLOneStockStore_priority":
            dataframe["c_OneStockStore_priority"] = store.get(index, None)
        elif index == "c_carrier_pickup_darj_onestock" or index == "c_cLFLOneStockCarrier_pickup":
            dataframe["c_OneStockCarrier_pickup"] = store.get(index, None)
        elif index == "c_cLFLOneStockSfs_active":
            dataframe["c_OneStockSfs_active"] = store.get(index, None)
        elif index == "c_sfs_actif_darj_onestock":
            dataframe["c_OneStockSfs_active"] = True if store.get(index, None) == "True" else False
        elif index == "c_succursale_darj_onestock" or index == "c_cLFLOneStockBranch":
            dataframe["c_succursale_onestock"] = store.get(index, None)
        elif index == "c_type_darj_onestock" or index == "c_cLFLOneStockEndpoint_type":
            dataframe["c_type_onestock"] = store.get(index, None)
        elif index == "c_usine_darj_onestock":
            dataframe["c_usine_onestock"] = store.get(index, None)
        elif index == "c_pays_magasin_darj_onestock":
            dataframe["c_pays_magasin_onestock"] = store.get(index, None)   

        if (index == "c_carrier_pickup_darj_onestock" and not(isinstance(store[index], list))) or (index == "c_cLFLOneStockCarrier_pickup" and not(isinstance(store[index], list))):
            dataframe["c_OneStockCarrier_pickup"] = list(dataframe["c_OneStockCarrier_pickup"])    
 
    return dataframe

     

def format(store, schema):
    dataframe = dict()
    level1_keys = schema.keys()
    for level1_key in level1_keys:
        level1_value = schema[level1_key]
        if type(level1_value) is dict:
            sub_dataframe = dict()
            for level2_key in level1_value.keys():
                level2_value = level1_value[level2_key]
                if "str_bool()" in level2_value:
                    sub_dataframe[level2_key] = str_bool(store, level2_value.split("-")[1])
                elif "coord()" in level2_value:
                    sub_dataframe[level2_key] = coord(store, level2_value.split("-")[1]) 
                else:
                    sub_dataframe[level2_key] = get_value(store, level2_value)
            dataframe[level1_key] = sub_dataframe
        elif level1_value == "oneStock()":
            dataframe[level1_key] = oneStock(store)
        elif level1_value == "get_image()":
            dataframe[level1_key] = get_image(store)
        else:
            if level1_value == "get_openings()":
                dataframe[level1_key] = get_openings(store)
            else:    
                dataframe[level1_key] = get_value(store, level1_value)
    return dataframe

