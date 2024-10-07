# This is the synthetic datasets generated using mistral.ai, meta.ai
# Below command have been used to generate the data. 
"""
# Can you generate me a JSON of 20 image captions with the fields "text", "labels" and the image captions should be a mixture of captions about "label": "food" and "label" : "not_food".  

# For example:
 
# Food caption: "My favourite food is ice cream"
# Not food caption: "A yellow tractor driving over the hill"

"""
pizza_captions = [
    "A slice of pepperoni pizza with a layer of melted cheese",
    "Margherita pizza topped with fresh basil leaves and juicy tomatoes",
    "Pizza with a variety of toppings including mushrooms, olives, and bell peppers",
    "A close-up shot of a cheesy pizza slice being pulled away from the pie",
    "A whole pizza pie with a thin and crispy crust",
    "Pizza with a unique topping combination of pineapple and ham",
    "A slice of veggie pizza loaded with colorful and nutritious vegetables",
    "Pizza with a stuffed crust, oozing with cheese",
    "A pair of slices from a barbecue chicken pizza",
    "Pizza with a white sauce base, topped with spinach and artichokes",
    "A square slice of Sicilian-style pizza with a thick and fluffy crust",
    "Pizza with a gluten-free crust, suitable for those with dietary restrictions",
    "A slice of pizza with a spicy kick, featuring jalapeno peppers",
    "Pizza with a meat lover's theme, including sausage, bacon, and pepperoni",
    "A gourmet pizza with a pesto base, topped with grilled chicken and sun-dried tomatoes",
    "Pizza with a unique, round-shaped crust hole in the middle",
    "A slice of pizza with a generous amount of shredded parmesan cheese on top",
    "Pizza with a seasonal theme, featuring toppings like butternut squash and kale",
    "A slice of pizza from a Detroit-style pie, with a thick, rectangular crust",
    "Pizza with a dessert twist, featuring a sweet Nutella base and fresh strawberries on top",
    "Pizza with a Mediterranean twist, featuring toppings like feta cheese, kalamata olives, and roasted red peppers",
    "A slice of pizza with a pesto base, topped with grilled vegetables and a balsamic glaze",
    "Pizza with a unique crust, such as cauliflower or zucchini, for a healthier option",
    "A slice of pizza with a spicy buffalo chicken topping and a drizzle of ranch dressing",
    "Pizza with a seafood theme, featuring toppings like shrimp, clams, and calamari"
]

sushi_captions = [
    "Assorted sushi rolls on a plate, featuring California rolls and spicy tuna rolls.",
    "Nigiri sushi topped with fresh salmon and tuna slices on vinegared rice.",
    "Sushi platter showcasing a variety of colorful rolls and garnishes.",
    "Close-up of a sushi roll with avocado, cucumber, and salmon.",
    "Bowl of sashimi with thin slices of raw fish.",
    "Sushi with unique toppings like seared tuna or eel sauce.",
    "Vegetarian sushi roll with avocado and pickled radish filling.",
    "Plate of sushi served with pickled ginger and wasabi.",
    "Sushi with a spicy kick, featuring jalapeno peppers or spicy mayo.",
    "Crunchy sushi roll with tempura flakes or panko breadcrumbs.",
    "Sushi platter featuring a rainbow of colors with salmon, tuna, and avocado.",
    "Sweet and savory sushi roll with ingredients like mango and shrimp.",
    "Uniquely shaped sushi roll, such as a heart or flower.",
    "Gluten-free sushi roll using tamari sauce instead of soy sauce.",
    "Low-carb sushi roll with cucumber or seaweed wraps instead of rice.",
    "Fusion sushi roll with ingredients like cream cheese or teriyaki sauce.",
    "Seasonal sushi roll with ingredients like persimmon or pumpkin.",
    "Smoky flavored sushi roll with smoked salmon or grilled eel.",
    "Vegan sushi roll with ingredients like tofu or grilled vegetables.",
    "Spicy tuna sushi roll with a crispy tempura coating.",
    "Sweet and spicy sushi roll with ingredients like mango and jalapeno.",
    "Crunchy sushi roll with a creamy filling, featuring shrimp tempura and avocado.",
    "Uniquely presented sushi roll, such as a hand roll or sushi burrito.",
    "Sushi roll with premium ingredients like uni or wagyu beef.",
    "Traditional Japanese flavored sushi roll with pickled plum or fermented soybeans."
]

curry_captions = [
    "A steaming bowl of fiery chicken curry, infused with a blend of aromatic spices and topped with fresh cilantro leaves.",
    "Luxurious coconut shrimp curry on a generous plate, featuring succulent shrimp in a rich coconut milk sauce, served with jasmine rice.",
    "Robust beef curry in a hearty bowl, simmered with a medley of spices, tomatoes, and onions, garnished with chopped green onions.",
    "Colorful vegetable curry plate, showcasing a vibrant mix of carrots, peas, and potatoes in a spiced sauce, perfect for a healthy meal.",
    "Comforting lamb curry bowl, featuring tender lamb slow-cooked in a flavorful sauce with cumin and coriander, garnished with toasted cumin seeds.",
    "Creamy mild korma curry, featuring tender chicken chunks in a rich sauce made with yogurt and cream, sprinkled with sliced almonds.",
    "Tangy fish curry bowl, featuring delicate fish pieces in a zesty sauce made with tamarind and curry leaves, ideal for a light meal.",
    "Mouthwatering paneer tikka masala, featuring juicy paneer in a rich tomato-based sauce, garnished with fresh coriander leaves.",
    "Spicy chickpea curry bowl, featuring nutty chickpeas in a flavorful sauce with onions and tomatoes, finished with a wedge of lemon.",
    "Fragrant Thai green curry, featuring vegetables and chicken or tofu in a rich coconut milk sauce with lemongrass, served with jasmine rice.",
    "Vibrant red curry with tofu and bell peppers, featuring tofu and sweet bell peppers in a rich coconut milk sauce.",
    "Decadent butter chicken curry, featuring tender chicken in a velvety sauce made with butter and tomatoes, served with warm naan bread.",
    "Comforting lentil dal curry, featuring nutty lentils in a spiced sauce with onions and tomatoes, garnished with fresh cilantro leaves.",
    "Spicy vindaloo curry with tender pork pieces, featuring a fiery sauce made with vinegar and chili peppers, perfect for bold flavor lovers.",
    "Fragrant vegetable curry with coconut milk and spices, featuring a mix of tender vegetables in a rich, aromatic sauce.",
    "Sweet and savory mango curry with chicken and bell peppers, featuring a flavorful sauce made with ripe mangoes and coconut milk.",
    "Spicy eggplant curry with fresh basil, featuring tender eggplant in a rich sauce with onions and tomatoes, finished with basil leaves.",
    "Aromatic goat curry, featuring tender goat pieces in a flavorful sauce with spices, served with steamed basmati rice.",
    "Creamy spinach and potato curry, featuring fluffy potatoes and nutritious spinach in a rich sauce with cream and garam masala.",
    "Mouthwatering mushroom curry, featuring shiitake and button mushrooms in a rich coconut milk sauce with spices and herbs.",
    "Tangy tomato curry with chicken, featuring tender chicken pieces in a zesty tomato-based sauce with onions and spices.",
    "Spicy prawn curry with fresh mint garnish, featuring juicy prawns in a fiery sauce with onions and tomatoes, finished with mint leaves.",
    "Hearty pumpkin curry with toasted pumpkin seeds, featuring sweet pumpkin pieces in a creamy coconut milk sauce, finished with toasted seeds.",
    "Creamy cauliflower curry with garlic naan, featuring tender cauliflower in a rich sauce with cream and spices, served with garlic naan bread.",
    "Rich and spicy lamb rogan josh with yogurt garnish, featuring tender lamb pieces in a bold sauce with spices, finished with creamy yogurt."
]

fruit_captions = [
    "A basket of fresh strawberries with a sprinkle of powdered sugar",
    "A slice of juicy watermelon with a sprinkle of chili powder and lime juice",
    "A bowl of mixed berries, including blueberries, raspberries, and blackberries",
    "A close-up shot of a ripe and juicy peach with a sprinkle of cinnamon",
    "A plate of sliced pineapple with a side of whipped cream and a cherry on top",
    "A bowl of cherries with a sprig of mint for garnish",
    "A fruit platter with a variety of exotic fruits, such as dragon fruit, mangosteen, and durian",
    "A bowl of sliced mango with a drizzle of honey and a sprinkle of Tajin seasoning",
    "A fruit kabob with a variety of fruits, such as grapes, melon, and berries",
    "A bowl of pomegranate seeds with a sprinkle of lime zest and a drizzle of agave nectar",
    "A whole papaya on a white plate with two apples on the side",
    "A bowl of sliced dragon fruit with a sprinkle of coconut flakes and a drizzle of lime juice",
    "A bowl of sliced kiwi with a sprinkle of sugar and a side of yogurt",
    "A bowl of sliced cantaloupe with a sprinkle of cinnamon and a side of cottage cheese",
    "A bowl of sliced honeydew with a sprinkle of salt and a side of prosciutto",
    "Grapefruit slides on top of yoghurt in a green bowl with a metal spoon in the side",
    "A bowl of sliced oranges with a sprinkle of cinnamon and a side of cloves",
    "Three apples and two oranges next to each other on a kitchen table",
    "A bowl of sliced pears with a sprinkle of ginger and a side of honey",
    "A bowl of sliced bananas with a sprinkle of cocoa powder and a side of peanut butter",
    "Two handfuls of bananas in a fruit bowl with grapes on the side, the fruit bowl is blue",
    "A bowl of sliced tomatoes with a sprinkle of basil and a side of mozzarella cheese",
    "A bowl of sliced cucumbers with a sprinkle of dill and a side of sour cream",
    "A bowl of sliced bell peppers with a sprinkle of paprika and a side of hummus",
    "Boxes of apples, pears, pineapple, manadrins and oranges at a fruit market"
]

vegetable_captions = [
    "Fresh cherry tomatoes in a basket, sprinkled with sea salt for a savory snack.",
    "Cucumbers on a plate, served with a side of tangy tzatziki sauce.",
    "A colorful bowl of mixed carrots, including orange and purple.",
    "A close-up shot of a big orange pumpkin with a face cut out of the side for Halloween.",
    "Carrots on a plate, served with a side of creamy hummus and a sprinkle of paprika.",
    "Cherry tomatoes and mozzarella balls in a bowl, drizzled with balsamic glaze for a tasty appetizer.",
    "A platter of raw vegetables, including broccoli, cauliflower, and snap peas, perfect for a healthy snack.",
    "Radishes in a bowl, sprinkled with salt and served with a side of butter.",
    "A kabob of grilled vegetables, including zucchini, squash, and onion, perfect for a summer barbecue.",
    "Jicama in a bowl, sprinkled with chili powder and served with a side of lime wedges for a refreshing snack.",
    "Celery in a bowl, served with a side of peanut butter and a sprinkle of raisins for a classic, tasty snack.",
    "Beets in a bowl, sprinkled with goat cheese and served with a side of arugula for a sophisticated, flavorful dish.",
    "Fennel in a bowl, sprinkled with lemon zest and served with a side of olive oil for a light, refreshing dish.",
    "Kohlrabi in a bowl, sprinkled with salt and served with a side of yogurt dip for a tasty, unique snack.",
    "Turnips in a bowl, sprinkled with pepper and served with a side of mustard sauce for a hearty, flavorful dish.",
    "Rutabaga in a bowl, sprinkled with nutmeg and served with a side of brown sugar for a sweet, comforting dish.",
    "Parsnips in a bowl, sprinkled with thyme and served with a side of honey for a tasty, unique snack.",
    "Brussels sprouts in a bowl, sprinkled with bacon bits and served with a side of maple syrup for a savory, sweet dish.",
    "Artichokes in a bowl, sprinkled with garlic and served with a side of lemon aioli for a tasty, sophisticated dish.",
    "Asparagus in a bowl, sprinkled with Parmesan cheese and served with a side of hollandaise sauce for a classic, flavorful dish.",
    "Green beans in a bowl, sprinkled with almonds and served with a side of lemon vinaigrette for a healthy, tasty dish.",
    "Eggplant in a bowl, sprinkled with feta cheese and served with a side of tomato sauce for a tasty, Mediterranean-inspired dish.",
    "Zucchini in a bowl, sprinkled with basil and served with a side of marinara sauce for a classic, Italian-inspired dish.",
    "Yellow squash in a bowl, sprinkled with oregano and served with a side of pesto sauce for a tasty, flavorful dish.",
    "Potatoes, onions, garlic, cauliflower, and broccolini in boxes at the market, ready for a tasty, healthy meal."
]

food_captions = pizza_captions + sushi_captions + fruit_captions + vegetable_captions + curry_captions
print(len(food_captions))