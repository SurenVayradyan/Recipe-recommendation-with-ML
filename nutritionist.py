# -----------------------------------------
# Program by Vayradyan.S.
#
# Hello everyone!
# -----------------------------------------
import recipes

ingredients = ['almond', 'amaretto', 'anchovy', 'anise','apple', 'apple juice', 'apricot','artichoke', 'arugula', 'asian pear', 'asparagus','avocado','bacon','banana', 'barley','bean', 'beef', 'beef rib', 'beef shank', 'beef tenderloin', 'beer', 'beet', 'bell pepper', 'berry','biscuit','blackberry','blue cheese' 'blueberry','bourbon','bran', 'brandy', 'bread', 'breadcrumbs','brie', 'brine', 'brisket', 'broccoli', 'broccoli rabe','brown rice', 'brownie','brussel sprout', 'buffalo','bulgur', 'burrito', 'butter', 'buttermilk', 'butternut squash', 'butterscotch/caramel', 'cabbage', 'cake','calvados','campari','cantaloupe', 'capers', 'caraway', 'cardamom', 'carrot', 'cashew', 'cauliflower', 'caviar', 'celery','champagne', 'chard','cheddar', 'cheese', 'cherry', 'chestnut','chicken', 'chickpea','chile pepper','chill', 'chive', 'chocolate','cilantro','cinnamon','clam', 'clove','coconut', 'cod', 'coffee', 'cognac/armagnac', 'collard greens', 'condiment', 'condiment/spread','cookie', 'cookies', 'coriander', 'corn', 'cornmeal', 'cottage cheese', 'couscous', 'crab', 'cranberry', 'cranberry sauce', 'cream cheese', 'créme de cacao','cucumber', 'cumin', 'cupcake', 'currant', 'curry', 'custard','diwali','dried fruit','duck','egg', 'egg nog', 'eggplant','fennel', 'feta', 'fig', 'fish','fortified wine','fruit', 'fruit juice','garlic','gin', 'ginger', 'goat cheese', 'goose', 'gouda','grains', 'granola', 'grape', 'grapefruit', 'grappa', 'green bean', 'green onion/scallion','ground beef', 'ground lamb','halibut','ham','hazelnut','herb','hominy/cornmeal/masa', 'honey', 'honeydew', 'horseradish', 'hot pepper','hummus', 'ice cream','jam or jelly','jerusalem artichoke','jícama','kale','kirsch','kiwi','kumquat','lamb','lamb shank','leek', 'legume', 'lemon', 'lemon juice', 'lemongrass', 'lentil', 'lettuce', 'lima bean', 'lime', 'lime juice', 'lingonberry', 'liqueur', 'lobster','lychee', 'macadamia nut','mango', 'maple syrup','marinade','marscarpone', 'marshmallow', 'martini','mayonnaise', 'meat','melon','milk/cream','mint','mozzarella','mussel', 'mustard','nectarine','noodle', 'nut', 'nutmeg', 'oat', 'oatmeal', 'octopus','olive','onion', 'orange', 'orange juice', 'oregano','orzo','oyster','papaya', 'paprika','parmesan', 'parsley', 'parsnip','passion fruit','pasta','pea', 'peach', 'peanut', 'peanut butter','pear', 'pecan','pepper','persimmon','phyllo/puff pastry dough', 'pickles','pine nut', 'pineapple', 'pistachio','plum','pomegranate', 'pomegranate juice', 'poppy', 'pork','pork rib', 'pork tenderloin','potato','poultry','prosciutto','prune', 'pumpkin','quail','rabbit','radish', 'raisin','raspberry','red wine','rhubarb', 'rice', 'ricotta','root vegetable', 'rosemary','rum', 'rutabaga', 'rye', 'saffron','sake', 'salad', 'salad dressing', 'salmon', 'salsa','sangria','sausage', 'scallop', 'scotch', 'seafood','self', 'semolina', 'sesame', 'sesame oil', 'shallot','shellfish','shrimp','sorbet', 'soufflé/meringue','sour cream', 'sourdough','soy','soy sauce','sparkling wine','squash','steak','strawberry','sweet potato/yam', 'swiss cheese','swordfish','tangerine','tarragon','tea','tequila','thyme', 'tilapia','tofu','tomato', 'tortillas','tropical fruit', 'trout', 'tuna','turnip','vanilla', 'veal','vegetable','venison', 'vermont', 'vermouth', 'vinegar','vodka', 'waffle', 'walnut', 'wasabi','watercress', 'watermelon','whiskey', 'white wine','wild rice','wine','yogurt','zucchini']

print(f'Список ингредиентов для ваших блюд: {ingredients}', '\n')
l_ingredients = input('Введите название ингредиентов из списка: ').split(sep=',')
l_ingredients = [ingredient.strip() for ingredient in l_ingredients]

print('I. НАШ ПРОГНОЗ')
rating = recipes.Forecast(l_ingredients).predict_rating_category()

print(rating, '\n')

recipes.NutritionFacts(l_ingredients).filter([], 4)

print('III. ТОП-3 ПОХОЖИХ РЕЦЕПТА: ')
recipes.SimilarRecipes(l_ingredients).top_similar(3)
