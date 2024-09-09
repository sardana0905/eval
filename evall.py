# Movie Rental Service Simulation

# Sample data
movies = [
    {'id': 1, 'title': 'The Matrix', 'available': True},
    {'id': 2, 'title': 'Inception', 'available': True},
    {'id': 3, 'title': 'The Godfather', 'available': True},
    {'id': 4, 'title': 'Pulp Fiction', 'available': True}
]

customers = {
    'cust1': {'name': 'Madhav', 'rented_movies': []},
    'cust2': {'name': 'Simran', 'rented_movies': []},
}

rentals = []

def list_available_movies():
    print("\nAvailable Movies:")
    for movie in movies:
        if movie['available']:
            print(f"ID: {movie['id']}, Title: {movie['title']}")

def rent_movie(customer_id, movie_id):
    customer = customers.get(customer_id)
    if not customer:
        print("Customer not found!")
        return

    movie = next((m for m in movies if m['id'] == movie_id), None)
    if not movie:
        print("Movie not found!")
        return

    if not movie['available']:
        print("Movie is not available for rent!")
        return

    movie['available'] = False
    customer['rented_movies'].append(movie_id)
    rentals.append({'customer_id': customer_id, 'movie_id': movie_id})
    print(f"Movie '{movie['title']}' rented to customer '{customer['name']}'.")

def return_movie(customer_id, movie_id):
    customer = customers.get(customer_id)
    if not customer:
        print("Customer not found!")
        return

    if movie_id not in customer['rented_movies']:
        print("Movie not rented by this customer!")
        return

    movie = next((m for m in movies if m['id'] == movie_id), None)
    if not movie:
        print("Movie not found!")
        return

    movie['available'] = True
    customer['rented_movies'].remove(movie_id)
    rentals.append({'customer_id': customer_id, 'movie_id': movie_id, 'return': True})
    print(f"Movie '{movie['title']}' returned by customer '{customer['name']}'.")

def generate_rental_report():
    print("\nRental Report:")
    for rental in rentals:
        customer = customers.get(rental['customer_id'])
        movie = next((m for m in movies if m['id'] == rental['movie_id']), None)
        if rental.get('return'):
            print(f"Movie '{movie['title']}' returned by customer '{customer['name']}'.")
        else:
            print(f"Movie '{movie['title']}' rented to customer '{customer['name']}'.")

# Example usage
if __name__ == "__main__":
    while True:
        print("\nMovie Rental Service")
        print("1. List Available Movies")
        print("2. Rent Movie")
        print("3. Return Movie")
        print("4. Generate Rental Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_available_movies()
        elif choice == '2':
            customer_id = input("Enter customer ID: ")
            movie_id = int(input("Enter movie ID to rent: "))
            rent_movie(customer_id, movie_id)
        elif choice == '3':
            customer_id = input("Enter customer ID: ")
            movie_id = int(input("Enter movie ID to return: "))
            return_movie(customer_id, movie_id)
        elif choice == '4':
            generate_rental_report()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
