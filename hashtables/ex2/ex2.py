#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Understanding:

    We can create a dictionary that serves as a hash table
    containing the list of flights to and from each destination.
    We're given "NONE" at the start, so by using that destination
    as the key for the next source, we find our next source-destination
    pair. We then append each of these cities as we hit them,
    doing this process once for each ticket we have.
    """
    trip_dict = {}

    for ticket in tickets:
        trip_dict[ticket.source] = ticket.destination

    print(trip_dict)
    route = []
    route.append(trip_dict["NONE"])

    for i in range(1, len(tickets)):
        route.append(trip_dict[route[i-1]])

    return route
