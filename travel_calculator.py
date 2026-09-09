distance_mi = 0.4
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print('False')
elif distance_mi <= 1.0 and is_raining:
       print('False')
elif distance_mi <= 1.0 and not is_raining:
       print('True')
elif distance_mi <= 6.0 and is_raining:
        print('False')
#elif distance_mi > 6.0 and has_ride_share_app:
#        print('False')
elif distance_mi > 1.0 and distance_mi <= 6.0 and (not is_raining and has_bike):
    print('True')
elif distance_mi > 1.0 and distance_mi <= 6.0 and (not is_raining and not has_bike):
    print('False')
elif distance_mi > 6.0 and has_ride_share_app:
    print('True')
elif distance_mi > 6.0 and has_car:
    print('True')
elif distance_mi > 6.0 and (not has_car and not has_ride_share_app):
    print('False')
