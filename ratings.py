"""Restaurant rating lister."""

def process_data(file_name):
    """Read data file line by line and return dictionary of {restaurant_name : score}"""

    content = open(file_name)
    restaurant_info = {}
    
    for line in content:
        line = line.rstrip()
        line = line.split(":")        
        restaurant_info[line[0]] = int(line[1])
        # restaurant, score = line.split(":")
        # scores[restaurant] = int(score)
    content.close()

    return restaurant_info


def add_restaurant(restaurant_info):
    """Add a restaurant and rating."""
    
    restaurant = input('What restaurant would you like to rate? ')
    score = input('How would you rate that restaurant from 1 to 5? ')
    restaurant_info[restaurant] = int(score)
    

def print_sorted_scores(scores):
    """Print sorted restaurant names and scores."""

    for restaurant, score in sorted(restaurant_info.items()):
        print(f"{restaurant} is rated at {score}.")


# Proceesing data from file
restaurant_info = process_data('scores.txt')

# Prompt user for new restaurant name and rating
add_restaurant(restaurant_info)

# Print in alphabetical order the list or restaurants and ratings
print_sorted_scores(restaurant_info)