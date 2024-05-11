from geopy.distance import geodesic

def find_nearest_services(user_location, services, count=3):
    nearest_services = []
    # convert 'location': '(41.345678, 69.345678)', to tuple in every service
    for service in services:
        service['location'] = tuple(map(float,
                                        service['location'].strip('()').split(', ')))

    sorted_services = sorted(services, key=lambda x: geodesic(
        user_location, x['location']).kilometers)
    for i in range(min(count, len(sorted_services))):
        service_info = sorted_services[i]
        distance = geodesic(user_location, service_info['location']).kilometers
        nearest_services.append((service_info, distance))
    return nearest_services
