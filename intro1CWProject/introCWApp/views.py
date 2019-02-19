from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# response to if you have not chosen a specific route
def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")
# response to when to enter the music route
def music(request):
    return HttpResponse("There are 3 routes in this route: "
                        "/wutang, \n"
                        "/fleetwoodmac/, \n"
                        "/shing02, \n"
                        "Could you be more specific.")
# response to when you type and enter the wutang route
def wutang(request):
    return HttpResponse("'Wu Tang Clan ain't nuthin' to **** with.'\n"
                        "The official ranks of the Wu-Tang Clan number nine:\n "
                        "RZA, GZA, Ghostface, Raekwon, U-God, Masta Killa, Inspectah Deck, Method Man and\n"
                        "the now departed Ol’ Dirty Bastard.\n"
                        "Cappadonna became something of a semi-member but never secured water-tight Wu status.")
# response to when you type and enter the fleetwoodmac route
def fleetwoodmac(request):
    return HttpResponse("'Don't tell me that you love me.'\n"
                        "Fleetwood Mac are a British-American rock band, formed in London in 1967.")
# the response you get when you type and enter the shing02 route
def shing02(request):
    return HttpResponse("'I talk weird,\nMy flow is awkward,\nIt's artwork.'\n"
                        "Due in part to growing up in Western cities,\n"
                        "Shing02 stands as one of the few multilingual rappers from Japan able to compose songs\n"
                        "entirely in either English or Japanese.")
