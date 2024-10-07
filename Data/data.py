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


not_food_captions = [
    "Sleek silver laptop resting on a wooden desk",
    "Remote control placed on a couch cushion",
    "Stainless steel refrigerator with a convenient water dispenser",
    "Red ceramic mug sitting next to a coffee maker",
    "Flat screen TV neatly mounted on a wall",
    "Pair of reading glasses left open on a book",
    "Black leather couch adding elegance to a living room",
    "White porcelain sink with a shiny chrome faucet",
    "Wooden cutting board with a chef's knife ready for use",
    "Vintage record player spinning a vinyl record",
    "Set of stainless steel utensils arranged on a kitchen table",
    "Colorful area rug brightening up a living room",
    "Standing floor lamp providing light next to an armchair",
    "Silver toaster oven sitting on a kitchen counter",
    "Set of keys hanging on a hook by the door",
    "Potted plant adding greenery to a windowsill",
    "Stack of books waiting to be read on a bookshelf",
    "Red brick fireplace with a mantel serving as a centerpiece",
    "King-size bed with a white comforter inviting a good night's sleep",
    "Round wooden dining table with chairs gathered around",
    "White ceramic vase holding fresh flowers",
    "Black and white checkered kitchen floor adding a classic touch",
    "Microwave oven ready for use on a kitchen counter",
    "Washing machine and dryer side by side in a laundry room",
    "Set of wine glasses hanging on a rack",
    "Vintage telephone sitting on a desk",
    "Wooden hanger holding clothes on a rack",
    "Ceiling fan with lights illuminating a bedroom",
    "Set of pots and pans hanging from a kitchen rack",
    "White bathtub with a shower curtain ready for a soak",
    "Coffee table cluttered with magazines",
    "Silverware organizer keeping cutlery tidy in a kitchen drawer",
    "Wall clock ticking away in a living room",
    "Set of headphones resting on a desk",
    "Vacuum cleaner stored in a closet",
    "Wooden dresser with a mirror reflecting the room",
    "Set of curtains draped over a window",
    "Chandelier casting light in a dining room",
    "Garage door with a remote control ready for use",
    "Set of speakers perched on a shelf",
    "Dishwasher installed in a kitchen",
    "Set of candles arranged on a mantel",
    "Garden hose rolled up and ready in a yard",
    "Set of tools organized in a garage",
    "Bicycle leaning casually against a wall",
    "Lawn mower stored in a shed",
    "Barbecue grill waiting on a patio",
    "Swimming pool sparkling in a backyard",
    "Hammock swaying between two trees",
    "Mailbox standing by a front door",
    "Birdhouse hanging from a tree",
    "Set of golf clubs stored in a bag",
    "Basketball hoop set up in a driveway",
    "Skateboard leaning against a bench",
    "Set of dumbbells stacked in a gym",
    "Yoga mat rolled up and ready in a corner",
    "Treadmill available in a home gym",
    "Set of skis leaning against a wall",
    "Surfboard leaning against a fence",
    "Fishing rod propped against a dock",
    "Camping tent pitched in a backyard",
    "Set of binoculars placed on a table",
    "Drone resting on a desk",
    "Set of paintbrushes stored in a jar",
    "Guitar leaning casually against a couch",
    "Set of board games stacked on a shelf",
    "Sewing machine ready for use on a table",
    "Set of knitting needles with yarn waiting to be knitted",
    "Camera mounted on a tripod",
    "Set of books stacked on a desk",
    "Telescope positioned on a balcony",
    "Microscope set up on a table",
    "Set of test tubes arranged in a rack",
    "Set of headphones placed on a desk",
    "Set of candles lit on a table",
    "Set of plates stacked in a cupboard",
    "Set of pillows arranged on a couch",
    "Set of glasses gleaming in a cabinet",
    "Set of bowls stacked on a shelf",
    "Set of mugs hanging on a hook",
    "Set of spoons stored in a drawer",
    "Set of forks kept in a holder",
    "Set of napkins arranged in a ring",
    "Set of tea towels folded in a kitchen",
    "Set of potholders stored in a drawer",
    "Set of oven mitts hanging on a hook",
    "Set of measuring cups nested in a drawer",
    "Set of measuring spoons hung on a rack",
    "Set of mixing bowls perched on a shelf",
    "Set of baking sheets stacked in a cabinet",
    "Set of muffin tins stacked together",
    "Set of cake pans tucked in a drawer",
    "Set of cookie cutters collected in a jar",
    "Set of spatulas kept in a holder",
    "Set of tongs stored in a drawer",
    "Set of napkins dispensed from a dispenser",
    "Set of straws held in a holder",
    "A girl feeding her rabbit in the garden",
    "Cuddling with a cat on her lap, a woman enjoys her morning coffee",
    "Walking in the park, a man jogs with his energetic dog",
    "Watching TV together, a family has their dog stretched out on the floor",
    "A boy building a fort in the living room with his curious cat watching",
    "A close-up of a woman practicing yoga in the living room while her dog mimics her poses",
    "A couple enjoying a movie night on the couch with their pets snuggled close",
    "A close-up of a girl feeding her rabbit in the garden",
    "A close-up of a cat lounging on a windowsill with a child reading nearby",
    "A close-up of a man and his dog sharing a quiet moment on the porch",
    "A boy giving his dog a bath in the backyard",
    "A close-up of a family playing a board game with their pets watching intently",
    "A child playing with a golden retriever in the backyard",
    "Reading a book on the couch, a woman has a cat curled up beside her",
    "Cooking dinner in the kitchen, a man has a dog eagerly watching",
    "Family gathered around a dining table, laughing and eating",
    "Relaxing on the porch, a couple enjoys the company of their two dogs by their feet",
    "Brushing her cat's fur in her bedroom, a young girl concentrates",
    "Playing video games in the living room, a boy has a dog lying next to him",
    "Working from home at her desk, a woman deals with a cat sitting on the keyboard",
    "Taking a nap on a hammock, a man has his dog snuggled up next to him",
    "Friends having a barbecue in the backyard while pets play nearby"
    "A collection of cleaning products under the sink",
    "Computer desk with laptop and computer monitor on it with a mousepad and keyboard",
    "Two dogs laying on a rug",
    "A cat and a dog sitting on a couch",
    "Three black dogs laying on the garage floor with a blue car in the background",
    "A white car parked in a driveway with a wooden fence behind it",
    "Two people sitting at a dining room table with a newspaper on it"
]

len(not_food_captions)


food_items = [{"text": caption, "label": "food"} for caption in food_captions]
not_food_items = [{"text": caption, "label": "not_food"} for caption in not_food_captions]
print(len(food_items))
print(len(not_food_items))

# Merge the two lists
all_items = food_items + not_food_items
len(all_items)

# Make them into a DataFrame
import pandas as pd

df = pd.DataFrame(all_items)

# Shuffle the DataFrame
df = df.sample(frac=1).reset_index(drop=True)

df.sample(6)


# Inspecting the datasets:
random_indexes = random.sample(range(len(dataset["train"])), 5)
print(random_indexes)

random_samples = dataset["train"][random_indexes]

print(f"[INFO] Random samples from dataset: \n")
for text, label in zip(random_samples["text"], random_samples["label"]):
    print(f"Text: {text} | Label: {label}")

# # Get Unique label values
dataset["train"].unique("label")