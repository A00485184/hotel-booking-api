from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReservationSerializer

@api_view(['GET'])
def get_list_of_hotels(request):
    checkin = request.query_params.get('checkin')
    checkout = request.query_params.get('checkout')
    
    hotel_list_a = [
        {"hotel_name": "Ocean View Resort", "price_per_night": 150, "location": "Miami"},
        {"hotel_name": "Mountain Retreat", "price_per_night": 200, "location": "Denver"}
    ]
    hotel_list_b = [
        {"hotel_name": "City Center Inn", "price_per_night": 100, "location": "New York"},
        {"hotel_name": "Airport Tracker Hotel", "price_per_night": 80, "location": "Chicago"}
    ]

    # Change list based on presence or value of checkin dates
    if checkin and checkout:
        # Simulated logic: if checkin is in december or a specific string logic
        if "-12-" in checkin:
            return Response({"hotels": hotel_list_b}, status=status.HTTP_200_OK)
        return Response({"hotels": hotel_list_a}, status=status.HTTP_200_OK)
    
    # Default return when no date is supplied
    return Response({"hotels": hotel_list_a + hotel_list_b}, status=status.HTTP_200_OK)

@api_view(['POST'])
def reservation_confirmation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        reservation = serializer.save()
        return Response(
            {"confirmation_number": reservation.confirmation_number},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
