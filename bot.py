from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup ,InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery 
import random
import time
import asyncio
import logging
import threading
api_id = 28635232
api_hash = "02a51a96b8428d0b8489f5caa629bca2"


# Initialize the main bot client
app = Client("fun_area_bot", api_id=api_id, api_hash=api_hash)




# Define the /start command handler
@app.on_message(filters.command("start"))
def start_command(client: Client, message: Message):
    # Description of the bot
    bot_description = (
        "🌟 Welcome to the Ultimate Who Am I Game! 🌟\n\n"
        "Think you've got what it takes to guess the right person, place, or thing from just a few tricky clues? 🤔\n"
        "Get ready to dive into a world of fun, challenge your friends, and unlock your inner detective! 🕵️‍♀️🕵️‍♂️\n\n"
        "💥 How It Works:\n"
        "In each round, you’ll be given clever hints. Your task is to figure out 'Who' or 'What' is being described! Every second counts ⏳, so make sure to think fast. The quicker you guess the right answer, the higher your score! 📈 But be careful, the clues get tougher as you advance! 😎\n\n"
        "🎮 Game Modes:\n"
        "- Solo Play: Enjoy unlimited brain-teasing rounds at your own pace. 🧠\n"
        "- Challenge Friends: Invite friends or group members for a showdown! 🥇\n"
        "- Timed Rounds: Can you solve the mystery before time runs out? 🕐\n\n"
        "🏆 Leaderboard and Scores:\n"
        "Track your progress, rankings, and compare scores with others! 💪\n"
        "✨ Fun topics include famous personalities, historical events, and everyday objects! 🎁\n\n"
        "Ready to play? Let the guessing begin! 🎉"
    )

    # Inline buttons for Help, Feedback, Invite Friends
    keyboard = [
        [InlineKeyboardButton("Help", callback_data="help")],
        [InlineKeyboardButton("Feedback", callback_data="feedback")],
        [InlineKeyboardButton("Game", callback_data="game")],
        [InlineKeyboardButton("Invite Friends", callback_data="invite")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the image with caption
    photo_url = "https://tse3.mm.bing.net/th?id=OIP.NWRP-o8PwDCmc_Vx_kyaCgHaE4&pid=Api&P=0&h=180"  # URL to the image
    message.reply_photo(photo=photo_url, caption=bot_description, reply_markup=reply_markup)


@app.on_callback_query(filters.regex("back_to_start"))
def handle_back_to_start(client: Client, callback_query: CallbackQuery):
    # Same bot description
    bot_description = (
        "🌟 Welcome to the Ultimate Who Am I Game! 🌟\n\n"
        "Think you've got what it takes to guess the right person, place, or thing from just a few tricky clues? 🤔\n"
        "Get ready to dive into a world of fun, challenge your friends, and unlock your inner detective! 🕵️‍♀️🕵️‍♂️\n\n"
        "💥 How It Works:\n"
        "In each round, you’ll be given clever hints. Your task is to figure out 'Who' or 'What' is being described! Every second counts ⏳, so make sure to think fast. The quicker you guess the right answer, the higher your score! 📈\n\n"
        "🎮 Game Modes: Play solo, challenge friends, and enjoy fun-filled rounds! 🧠\n"
        "🏆 Leaderboard and Rewards: Track your scores and challenge friends! 🏅\n\n"
        "Let's get started now! 🎉"
    )
    
    # Acknowledge the callback
    callback_query.answer()  
    
    # Edit the message to show the original bot description
    callback_query.edit_message_text(bot_description)
    
    # Inline buttons
    keyboard = [
        [InlineKeyboardButton("Help", callback_data="help")],
        [InlineKeyboardButton("Feedback", callback_data="feedback")],
        [InlineKeyboardButton("Game", callback_data="game")],
        [InlineKeyboardButton("Invite Friends", callback_data="invite")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Update the message with the new reply markup
    callback_query.edit_message_reply_markup(reply_markup=reply_markup)

@app.on_callback_query(filters.regex("game"))
def handle_game_callback(client: Client, callback_query: CallbackQuery):
    # Create the feedback message
    game_message = (
    "🎉 **Welcome to 'Who Am I'!** 🎉\n\n"
    "Get ready for an exciting guessing game where you will unravel clues about famous personalities from various fields! 🤔✨\n\n"
    
    "🔥 **How to Play:** 🔥\n"
    "1. **Start the Game:** Type **/play** to jump into the fun! 🚀\n"
    "2. **Guess the Personality:** You'll receive clues—use them to guess who it is before time runs out! ⏳💡\n"
    "3. **Pause Anytime:** If you want to take a break, just type **/stop** to end the game! ✋\n\n"
    
    "💌 **Why You’ll Love It:**\n"
    "- Challenge yourself with interesting clues! 💭\n"
    "- Discover new icons and historical figures! 📚\n"
    "- Play solo or compete with friends for the ultimate guessing showdown! 🏆\n\n"
    
    "Are you ready to test your knowledge? Type **/play** now and let the guessing begin! 🎊"
)

    # Acknowledge the callback
    callback_query.answer()

    # Edit the message to show the feedback message
    callback_query.edit_message_text(game_message)

    # Optionally, you can include a button to go back or continue playing
    keyboard = [
        [InlineKeyboardButton("Back to Start", callback_data="back_to_start")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    callback_query.edit_message_reply_markup(reply_markup=reply_markup)


@app.on_callback_query(filters.regex("feedback"))
def handle_feedback_callback(client: Client, callback_query: CallbackQuery):
    # Create the feedback message
    feedback_message = (
        "📝 **We Value Your Feedback!** 📝\n\n"
        "Your experience with the 'Who Am I' bot matters to us! Whether you have suggestions, questions, or just want to share what you love about the game, we’re all ears! 👂💬\n\n"
        "🌟 **What Can You Share?**\n"
        "- **Suggestions:** Got an idea to make the game even better? We’d love to hear it! 💡\n"
        "- **Bug Reports:** Noticed something off? Let us know so we can fix it pronto! 🛠️\n"
        "- **Shoutouts:** Enjoying the game? Give us a shout and let us know what’s working well! 🎉\n\n"
        "🔗 **How to Provide Feedback:**\n"
        "Simply type your message and send it our way. Your feedback helps us improve and bring more fun features to the game! 📲\n\n"
        "Thank you for helping us make 'Who Am I' even more awesome! 🙏"
    )

    # Acknowledge the callback
    callback_query.answer()

    # Edit the message to show the feedback message
    callback_query.edit_message_text(feedback_message)

    # Optionally, you can include a button to go back or continue playing
    keyboard = [
        [InlineKeyboardButton("Back to Start", callback_data="back_to_start")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    callback_query.edit_message_reply_markup(reply_markup=reply_markup)



@app.on_callback_query(filters.regex("invite"))
def handle_invite_callback(client: Client, callback_query: CallbackQuery):
    # Invite message content
    invite_message = (
        "🎉 **Invite Your Friends for More Fun!** 🎉\n\n"
        "What's better than playing Who Am I? Playing it with your friends! 👫👬\n"
        "The fun multiplies when you challenge others to guess faster and smarter! 💡\n\n"
        "💥 **How to Invite:**\n"
        "Just send an invite to your friends or group members and let the fun begin!\n"
        "👾 **Challenge Each Other:** See who's the fastest guesser! 🏆\n"
        "📊 **Climb the Leaderboard Together:** Compete or team up for higher scores! 🎮\n"
        "🎁 **Bonus Rewards:** Earn rewards when friends join and play! 🎉\n\n"
        "🚀 Ready? Invite your friends now and get guessing! 🥇"
    )
    
    # Acknowledge the callback
    callback_query.answer()  
    
    # Edit the message to show the invite message
    callback_query.edit_message_text(invite_message)

    # Button to go back
    keyboard = [
        [InlineKeyboardButton("Back to Start", callback_data="back_to_start")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    callback_query.edit_message_reply_markup(reply_markup=reply_markup)


@app.on_callback_query(filters.regex("help"))
def handle_help_callback(client: Client, callback_query: CallbackQuery):
    help_content = (
        "🛠️ **Help Command:** How to Use This Bot 🛠️\n\n"
        "1.🤖 **Add Me to Your Group for Endless Fun!** 🎉\n\n"
        "👥 **Step 1:** Add me to your group! The more friends you have, the more fun the game becomes! 👫👬\n\n"
        "💡 **Step 2:** Type `/start` to begin the game. I'll send a clue describing a person, place, or thing. 🕵️‍♂️ Can you guess it before time runs out? ⏳\n\n"
        "📝 **How to Play:**\n"
        "- I'll give you a hint, and you just type your guess in the chat! 🖊️\n"
        "- The faster you answer, the more points you get! ⏩\n"
        "- Play solo or challenge your friends to see who’s the ultimate guesser! 🥇\n\n"
        "🎯 **Game Modes:** Solo and Multiplayer! Invite friends for maximum fun! 🎮\n"
        "🏆 **Pro Tip:** Be quick! Speed and accuracy will help you climb the leaderboard! 💨"
    )
    
    # Acknowledge the callback
    callback_query.answer()  
    
    # Edit the message to show the help content
    callback_query.edit_message_text(help_content)

    # Button to go back
    keyboard = [
        [InlineKeyboardButton("Back to Start", callback_data="back_to_start")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    callback_query.edit_message_reply_markup(reply_markup=reply_markup)



scores = {}

# Example questions for each difficulty level
questions_easy = [
    {"question": "I am the largest planet in our solar system. Who am I?", "answer": "Jupiter"},
    {"question": "I am the first man to walk on the moon. Who am I?", "answer": "Neil Armstrong"},
    {"question": "I am known as the 'father of computers'. Who am I?", "answer": "Charles Babbage"},
    {"question": "I am a yellow fruit often associated with monkeys. Who am I?", "answer": "Banana"},
    {"question": "I am the tallest animal in the world. Who am I?", "answer": "Giraffe"},
    {"question": "I am the planet closest to the sun. Who am I?", "answer": "Mercury"},
    {"question": "I am the primary author of the Declaration of Independence. Who am I?", "answer": "Thomas Jefferson"},
    {"question": "I am the animal known for building dams. Who am I?", "answer": "Beaver"},
    {"question": "I am the capital city of France. Who am I?", "answer": "Paris"},
    {"question": "I am the sport where players use a racket to hit a shuttlecock. Who am I?", "answer": "Badminton"},
    {"question": "I am the largest mammal on Earth. Who am I?", "answer": "Blue Whale"},
    {"question": "I am a large, striped cat native to Asia. Who am I?", "answer": "Tiger"},
    {"question": "I am the author of 'Harry Potter'. Who am I?", "answer": "J.K. Rowling"},
    {"question": "I am a machine used to wash clothes. Who am I?", "answer": "Washing machine"},
    {"question": "I am the process by which plants make food using sunlight. Who am I?", "answer": "Photosynthesis"},
    {"question": "I am a famous Italian dish made with dough, sauce, and cheese. Who am I?", "answer": "Pizza"},
    {"question": "I am a shape with three sides. Who am I?", "answer": "Triangle"},
    {"question": "I am the first U.S. President. Who am I?", "answer": "George Washington"},
    {"question": "I am the chemical element with the symbol 'O'. Who am I?", "answer": "Oxygen"},
    {"question": "I am the organ in your body that pumps blood. Who am I?", "answer": "Heart"},
    {"question": "I am an insect that makes honey. Who am I?", "answer": "Bee"},
    {"question": "I am a popular social media platform known for sharing pictures. Who am I?", "answer": "Instagram"},
    {"question": "I am the outermost layer of the Earth. Who am I?", "answer": "Crust"},
    {"question": "I am the person who discovered gravity by watching an apple fall. Who am I?", "answer": "Isaac Newton"},
    {"question": "I am the largest desert in the world. Who am I?", "answer": "Sahara Desert"},
    {"question": "I am a season characterized by falling leaves and cooler weather. Who am I?", "answer": "Autumn"},
    {"question": "I am the author of 'Romeo and Juliet'. Who am I?", "answer": "William Shakespeare"},
    {"question": "I am the famous Egyptian monument with the body of a lion and the head of a man. Who am I?", "answer": "The Sphinx"},
    {"question": "I am a day of the week that comes after Friday. Who am I?", "answer": "Saturday"},
    {"question": "I am the color of the sky on a clear day. Who am I?", "answer": "Blue"},
    {"question": "I am a beverage made from beans that helps people wake up. Who am I?", "answer": "Coffee"},
    {"question": "I am a red fruit that can also be used as a vegetable in cooking. Who am I?", "answer": "Tomato"},
    {"question": "I am the type of tree that produces acorns. Who am I?", "answer": "Oak tree"},
    {"question": "I am the main ingredient in a traditional omelette. Who am I?", "answer": "Egg"},
    {"question": "I am the famous clock tower in London. Who am I?", "answer": "Big Ben"},
    {"question": "I am a constellation named after a hunter in Greek mythology. Who am I?", "answer": "Orion"},
    {"question": "I am the person who invented the telephone. Who am I?", "answer": "Alexander Graham Bell"},
    {"question": "I am a small, flying mammal that uses echolocation. Who am I?", "answer": "Bat"},
    {"question": "I am a green gemstone associated with the month of May. Who am I?", "answer": "Emerald"},
    {"question": "I am a giant panda's favorite food. Who am I?", "answer": "Bamboo"},
    {"question": "I am the tallest mountain in the world. Who am I?", "answer": "Mount Everest"},
    {"question": "I am the part of a plant that absorbs water and nutrients. Who am I?", "answer": "Root"},
    {"question": "I am the country that is home to the Great Wall. Who am I?", "answer": "China"},
    {"question": "I am a yellow Pokémon known for my electrical powers. Who am I?", "answer": "Pikachu"},
    {"question": "I am a primary color, often associated with strawberries. Who am I?", "answer": "Red"},
    {"question": "I am a sea creature with eight arms. Who am I?", "answer": "Octopus"},
    {"question": "I am the author of 'Alice's Adventures in Wonderland'. Who am I?", "answer": "Lewis Carroll"},
    {"question": "I am the primary ingredient in guacamole. Who am I?", "answer": "Avocado"},
    {"question": "I am the city known as 'The Big Apple'. Who am I?", "answer": "New York City"},
    {"question": "I am the smallest unit of matter. Who am I?", "answer": "Atom"},
    {"question": "I am the closest star to Earth. Who am I?", "answer": "The Sun"},
    {"question": "I am a four-legged pet that purrs when happy. Who am I?", "answer": "Cat"},
    {"question": "I am the process that allows plants to grow from seeds. Who am I?", "answer": "Germination"},
    {"question": "I am a famous artist known for painting the Mona Lisa. Who am I?", "answer": "Leonardo da Vinci"},
    {"question": "I am a salty liquid found in the oceans. Who am I?", "answer": "Seawater"},
    {"question": "I am the largest organ in the human body. Who am I?", "answer": "Skin"},
    {"question": "I am a bird that cannot fly but is known for running fast. Who am I?", "answer": "Ostrich"},
    {"question": "I am a holiday celebrated on December 25th. Who am I?", "answer": "Christmas"},
    {"question": "I am the shape of a ball. Who am I?", "answer": "Sphere"},
    {"question": "I am the instrument you use to measure temperature. Who am I?", "answer": "Thermometer"},
    {"question": "I am a place where wild animals are kept for people to see. Who am I?", "answer": "Zoo"},
    {"question": "I am the country where pizza and pasta originated. Who am I?", "answer": "Italy"},
    {"question": "I am the painter who cut off part of his ear. Who am I?", "answer": "Vincent van Gogh"},
    {"question": "I am a famous toy building block that snaps together. Who am I?", "answer": "LEGO"},
    {"question": "I am a round object that you kick in a soccer game. Who am I?", "answer": "Soccer ball"},
    {"question": "I am a star constellation shaped like a big dipper. Who am I?", "answer": "Ursa Major"},
    {"question": "I am the last book of the New Testament. Who am I?", "answer": "Revelation"},
    {"question": "I am a puzzle made of small interlocking pieces. Who am I?", "answer": "Jigsaw puzzle"},
    {"question": "I am a cold dessert made from cream and sugar. Who am I?", "answer": "Ice cream"},
    {"question": "I am a fish that can inflate itself when threatened. Who am I?", "answer": "Pufferfish"},
    {"question": "I am the branch of mathematics dealing with shapes and space. Who am I?", "answer": "Geometry"},
    {"question": "I am a tool used to cut paper or fabric. Who am I?", "answer": "Scissors"},
    {"question": "I am a small, furry animal that hops and has long ears. Who am I?", "answer": "Rabbit"},
    {"question": "I am the tallest land animal. Who am I?", "answer": "Giraffe"},
    {"question": "I am the metal used in making coins and jewelry, symbolized as 'Au'. Who am I?", "answer": "Gold"},
    {"question": "I am the fastest land animal. Who am I?", "answer": "Cheetah"},
    {"question": "I am the famous ship that sank on its maiden voyage in 1912. Who am I?", "answer": "Titanic"},
    {"question": "I am a large body of saltwater. Who am I?", "answer": "Ocean"},
    {"question": "I am the land where kangaroos are commonly found. Who am I?", "answer": "Australia"},
    {"question": "I am the gas that humans need to breathe. Who am I?", "answer": "Oxygen"},
    {"question": "I am a natural satellite of the Earth. Who am I?", "answer": "The Moon"},
    {"question": "I am the Greek god of the sea. Who am I?", "answer": "Poseidon"},
    {"question": "I am a sweet, sticky substance made by bees. Who am I?", "answer": "Honey"},
    {"question": "I am a person who leads an orchestra or choir. Who am I?", "answer": "Conductor"},
    {"question": "I am the famous wizard in 'Harry Potter'. Who am I?", "answer": "Harry Potter"},
    {"question": "I am a fruit that is red, round, and often used to make sauce. Who am I?", "answer": "Tomato"},
    {"question": "I am the layer of gases surrounding the Earth. Who am I?", "answer": "Atmosphere"},
    {"question": "I am a tool used to write or draw, made of wood and graphite. Who am I?", "answer": "Pencil"},
    {"question": "I am a famous scientist who developed the theory of relativity. Who am I?", "answer": "Albert Einstein"},
    {"question": "I am the day of the week that comes after Monday. Who am I?", "answer": "Tuesday"},
    {"question": "I am the closest planet to the Sun. Who am I?", "answer": "Mercury"},
    {"question": "I am the famous ship captain who searched for Neverland. Who am I?", "answer": "Captain Hook"},
    {"question": "I am the liquid metal used in thermometers. Who am I?", "answer": "Mercury"},
    {"question": "I am a country famous for the Eiffel Tower. Who am I?", "answer": "France"},
    {"question": "I am a fruit that shares my name with a color. Who am I?", "answer": "Orange"},
    {"question": "I am a device used to take pictures. Who am I?", "answer": "Camera"},
    {"question": "I am the famous Roman emperor stabbed by Brutus. Who am I?", "answer": "Julius Caesar"},
    {"question": "I am the smallest planet in our solar system. Who am I?", "answer": "Mercury"},
    {"question": "I am a famous painting of a woman with a mysterious smile. Who am I?", "answer": "Mona Lisa"},
    {"question": "I am the substance used to power cars, also known as petrol. Who am I?", "answer": "Gasoline"},
    {"question": "I am the structure that protects your brain. Who am I?", "answer": "Skull"},
    {"question": "I am the yellow part of an egg. Who am I?", "answer": "Yolk"},
    {"question": "I am a large bird that cannot fly, native to Australia. Who am I?", "answer": "Emu"},
    {"question": "I am a landmass surrounded by water on all sides. Who am I?", "answer": "Island"},
    {"question": "I am the famous tower in Pisa that leans. Who am I?", "answer": "Leaning Tower of Pisa"},
    {"question": "I am the person who wrote 'Romeo and Juliet'. Who am I?", "answer": "William Shakespeare"},
    {"question": "I am a famous painter who cut off his ear. Who am I?", "answer": "Vincent van Gogh"},
    {"question": "I am a small insect that makes honey. Who am I?", "answer": "Bee"},
    {"question": "I am the sound a dog makes. Who am I?", "answer": "Bark"},
    {"question": "I am a piece of land higher than the surrounding land. Who am I?", "answer": "Hill"},
    {"question": "I am a material made from trees, used for writing. Who am I?", "answer": "Paper"},
    {"question": "I am the famous mountain range between Nepal and Tibet. Who am I?", "answer": "Himalayas"},
    {"question": "I am a green vegetable that looks like a small tree. Who am I?", "answer": "Broccoli"},
    {"question": "I am the famous British ship that fought the Spanish Armada. Who am I?", "answer": "The Golden Hind"},
    {"question": "I am a big cat known for my beautiful stripes. Who am I?", "answer": "Tiger"},
    {"question": "I am the planet famous for my rings. Who am I?", "answer": "Saturn"},
    {"question": "I am the place where you can see many stars at night. Who am I?", "answer": "Sky"},
    {"question": "I am a large reptile that lives both in water and on land. Who am I?", "answer": "Crocodile"},
    {"question": "I am the famous scientist who developed the theory of evolution. Who am I?", "answer": "Charles Darwin"},
    {"question": "I am a drink made from grapes, often used in celebrations. Who am I?", "answer": "Wine"},
    {"question": "I am a long, thin, flying insect that is known for hovering over water. Who am I?", "answer": "Dragonfly"},
    {"question": "I am a farm animal known for giving wool. Who am I?", "answer": "Sheep"},
    {"question": "I am a large structure built to hold back water. Who am I?", "answer": "Dam"},
    {"question": "I am the small, red fruit often used in desserts and jams. Who am I?", "answer": "Strawberry"},
    {"question": "I am the green part of the plant that uses sunlight for food. Who am I?", "answer": "Leaf"},
    {"question": "I am a famous landmark in Egypt, known for my triangular shape. Who am I?", "answer": "Pyramid"},
    {"question": "I am a structure built over water to connect two places. Who am I?", "answer": "Bridge"},
    {"question": "I am a small, nocturnal mammal that can fly. Who am I?", "answer": "Bat"},
    {"question": "I am the Italian city famous for my canals and gondolas. Who am I?", "answer": "Venice"},
    {"question": "I am a famous wizard with a lightning-shaped scar on my forehead. Who am I?", "answer": "Harry Potter"},
    {"question": "I am the organ that pumps blood through your body. Who am I?", "answer": "Heart"},
    {"question": "I am a type of pasta shaped like little tubes. Who am I?", "answer": "Macaroni"},
    {"question": "I am a tool used to write or draw, and I have an eraser on one end. Who am I?", "answer": "Pencil"},
    {"question": "I am a large mammal known for my tusks and trunk. Who am I?", "answer": "Elephant"},
    {"question": "I am a color you get when you mix blue and red. Who am I?", "answer": "Purple"},
    {"question": "I am the famous painter of 'Starry Night'. Who am I?", "answer": "Vincent van Gogh"},
    {"question": "I am the animal that is known for building dams. Who am I?", "answer": "Beaver"},
    {"question": "I am a reptile known for shedding my skin and slithering. Who am I?", "answer": "Snake"},
    {"question": "I am the largest ocean on Earth. Who am I?", "answer": "Pacific Ocean"},
    {"question": "I am a musical instrument with black and white keys. Who am I?", "answer": "Piano"},
    {"question": "I am a fruit that is also the name of a tech company. Who am I?", "answer": "Apple"},
    {"question": "I am a superhero known for my shield and being from America. Who am I?", "answer": "Captain America"},
    {"question": "I am the body of water separating the UK and France. Who am I?", "answer": "English Channel"},
    {"question": "I am a cold place where you might see penguins and polar bears. Who am I?", "answer": "Arctic"},
    {"question": "I am the city known for the Golden Gate Bridge. Who am I?", "answer": "San Francisco"},
    {"question": "I am the popular building toy with bricks that snap together. Who am I?", "answer": "Lego"},
    {"question": "I am a large, slow animal with a shell on my back. Who am I?", "answer": "Turtle"},
    {"question": "I am a famous superhero from Gotham City. Who am I?", "answer": "Batman"},
    {"question": "I am a large bird often cooked and eaten during Thanksgiving. Who am I?", "answer": "Turkey"},
    {"question": "I am a large, hot desert in northern Africa. Who am I?", "answer": "Sahara Desert"},
    {"question": "I am the country known for sushi and samurai. Who am I?", "answer": "Japan"},
    {"question": "I am a small, furry animal often kept as a pet, with long ears. Who am I?", "answer": "Rabbit"},
    {"question": "I am the part of the eye that controls how much light enters. Who am I?", "answer": "Pupil"},
    {"question": "I am a two-wheeled vehicle powered by pedals. Who am I?", "answer": "Bicycle"},
    {"question": "I am the large island country known for kangaroos and the Great Barrier Reef. Who am I?", "answer": "Australia"},
    {"question": "I am a flying mammal that sleeps upside down. Who am I?", "answer": "Bat"},
    {"question": "I am a huge river that flows through Brazil. Who am I?", "answer": "Amazon River"},
    {"question": "I am a famous detective created by Sir Arthur Conan Doyle. Who am I?", "answer": "Sherlock Holmes"},
    {"question": "I am a bird that cannot fly and is known for living in Antarctica. Who am I?", "answer": "Penguin"},
    {"question": "I am a famous space telescope launched by NASA. Who am I?", "answer": "Hubble Space Telescope"},
    {"question": "I am a holiday celebrated with fireworks in the USA on July 4th. Who am I?", "answer": "Independence Day"},
    {"question": "I am a small red fruit with seeds on the outside. Who am I?", "answer": "Strawberry"},
    {"question": "I am a large, furry primate found in Africa. Who am I?", "answer": "Gorilla"},
    {"question": "I am a big cat known for my spots. Who am I?", "answer": "Leopard"},
    {"question": "I am the structure inside your mouth used for chewing food. Who am I?", "answer": "Teeth"},
    {"question": "I am a sport where players hit a ball over a net using rackets. Who am I?", "answer": "Tennis"},
    {"question": "I am the fastest land animal. Who am I?", "answer": "Cheetah"},
    {"question": "I am the instrument used by doctors to listen to your heartbeat. Who am I?", "answer": "Stethoscope"},
    {"question": "I am a bird known for my colorful feathers and ability to mimic sounds. Who am I?", "answer": "Parrot"},
    {"question": "I am a famous structure in France known for its iron lattice design. Who am I?", "answer": "Eiffel Tower"},
    {"question": "I am the fourth planet from the Sun and known for my red appearance. Who am I?", "answer": "Mars"},
    {"question": "I am a large cat that is the national animal of India. Who am I?", "answer": "Bengal Tiger"},
    {"question": "I am a famous Disney princess who lost her glass slipper. Who am I?", "answer": "Cinderella"},
    {"question": "I am a large, green vegetable that is used in salads. Who am I?", "answer": "Lettuce"},
    {"question": "I am the most populous country in the world. Who am I?", "answer": "China"},
    {"question": "I am a sea creature with eight arms. Who am I?", "answer": "Octopus"},
    {"question": "I am a sport where players aim to shoot a ball into a hoop. Who am I?", "answer": "Basketball"},
    {"question": "I am the shape with three sides. Who am I?", "answer": "Triangle"},
    {"question": "I am a fruit that keeps doctors away if you eat one every day. Who am I?", "answer": "Apple"},
    {"question": "I am the famous spacecraft that took astronauts to the moon. Who am I?", "answer": "Apollo 11"},
    {"question": "I am a city known for Bollywood. Who am I?", "answer": "Mumbai"},
    {"question": "I am the soft white part of bread. Who am I?", "answer": "Crumb"},
    {"question": "I am a flying mammal that lives in caves. Who am I?", "answer": "Bat"},
    {"question": "I am the process by which plants make their own food using sunlight. Who am I?", "answer": "Photosynthesis"}
]


    


questions_medium = [
    {"question": "I am a famous physicist known for my theory of relativity. Who am I?", "answer": "Albert Einstein"},
    {"question": "I am a fruit that is often confused with a vegetable and is a key ingredient in guacamole. Who am I?", "answer": "Avocado"},
    {"question": "I am the author of the Harry Potter series. Who am I?", "answer": "J.K. Rowling"},
    {"question": "I am a country that is known for its pyramids and the Nile River. Who am I?", "answer": "Egypt"},
    {"question": "I am the capital of Japan. Who am I?", "answer": "Tokyo"},
    {"question": "I am a famous artist known for painting the Mona Lisa. Who am I?", "answer": "Leonardo da Vinci"},
    {"question": "I am the largest planet in our solar system. Who am I?", "answer": "Jupiter"},
    {"question": "I am a beverage made by steeping tea leaves in hot water. Who am I?", "answer": "Tea"},
    {"question": "I am the main character in the novel 'Moby Dick'. Who am I?", "answer": "Ishmael"},
    {"question": "I am the metal that is liquid at room temperature and is used in thermometers. Who am I?", "answer": "Mercury"},
    {"question": "I am an animal known for my ability to change color and can be found in tropical forests. Who am I?", "answer": "Chameleon"},
    {"question": "I am a fictional character who lives in a pineapple under the sea. Who am I?", "answer": "SpongeBob SquarePants"},
    {"question": "I am a small, flightless bird native to New Zealand. Who am I?", "answer": "Kiwi"},
    {"question": "I am a well-known Italian dish made with cheese and tomato. Who am I?", "answer": "Pizza"},
    {"question": "I am a famous monument located in India, built by Mughal Emperor Shah Jahan. Who am I?", "answer": "Taj Mahal"},
    {"question": "I am a large mammal known for my intelligence and strong social bonds, often found in the ocean. Who am I?", "answer": "Dolphin"},
    {"question": "I am a type of large, carnivorous reptile often found in rivers and swamps. Who am I?", "answer": "Crocodile"},
    {"question": "I am the first woman to fly solo across the Atlantic Ocean. Who am I?", "answer": "Amelia Earhart"},
    {"question": "I am a large, spotted cat native to the Americas, often found in rainforests. Who am I?", "answer": "Jaguar"},
    {"question": "I am the process by which plants absorb sunlight to create energy. Who am I?", "answer": "Photosynthesis"},
    {"question": "I am a historic trade route that connected the East and West. Who am I?", "answer": "Silk Road"},
    {"question": "I am a famous comic book hero known for my web-slinging abilities. Who am I?", "answer": "Spider-Man"},
    {"question": "I am the author of 'Pride and Prejudice'. Who am I?", "answer": "Jane Austen"},
    {"question": "I am the currency used in Japan. Who am I?", "answer": "Yen"},
    {"question": "I am a device used to measure temperature. Who am I?", "answer": "Thermometer"},
    {"question": "I am a popular game involving strategy, played on a board with 64 squares. Who am I?", "answer": "Chess"},
    {"question": "I am a type of tree known for producing acorns. Who am I?", "answer": "Oak"},
    {"question": "I am the longest river in the world. Who am I?", "answer": "Nile"},
    {"question": "I am a popular social media platform known for photo sharing. Who am I?", "answer": "Instagram"},
    {"question": "I am a large land mammal known for my trunk and tusks. Who am I?", "answer": "Elephant"},
    {"question": "I am a popular dessert made with layers of cream and cake. Who am I?", "answer": "Tiramisu"},
    {"question": "I am a famous painter known for my works during the Renaissance period. Who am I?", "answer": "Raphael"},
    {"question": "I am a small, colorful bird known for my ability to hover. Who am I?", "answer": "Hummingbird"},
    {"question": "I am a classic children's story about a girl who visits a magical land. Who am I?", "answer": "Alice in Wonderland"},
    {"question": "I am a large desert located in Northern Africa. Who am I?", "answer": "Sahara"},
    {"question": "I am a mythical creature that is half-human and half-horse. Who am I?", "answer": "Centaur"},
    {"question": "I am the national flower of the USA, often associated with Thanksgiving. Who am I?", "answer": "Rose"},
    {"question": "I am a protein-rich food that is a staple in many diets worldwide. Who am I?", "answer": "Egg"},
    {"question": "I am a legendary figure known for my incredible strength and adventures. Who am I?", "answer": "Hercules"},
    {"question": "I am a large bird known for my long neck and legs. Who am I?", "answer": "Flamingo"},
    {"question": "I am a small, fruit-flavored candy, often shaped like a bear. Who am I?", "answer": "Gummy Bear"},
    {"question": "I am the capital city of France. Who am I?", "answer": "Paris"},
    {"question": "I am a device used to take photographs. Who am I?", "answer": "Camera"},
    {"question": "I am a popular board game where players buy and trade properties. Who am I?", "answer": "Monopoly"},
    {"question": "I am a famous fictional detective created by Arthur Conan Doyle. Who am I?", "answer": "Sherlock Holmes"},
    {"question": "I am a large, slow-moving reptile often found in warm climates. Who am I?", "answer": "Tortoise"},
    {"question": "I am a popular fruit known for its high vitamin C content and is often used in beverages. Who am I?", "answer": "Orange"},
    {"question": "I am a classic fairytale character known for my glass slipper. Who am I?", "answer": "Cinderella"},
    {"question": "I am a famous American president who delivered the Gettysburg Address. Who am I?", "answer": "Abraham Lincoln"},
    {"question": "I am the largest organ in the human body. Who am I?", "answer": "Skin"},
    {"question": "I am a popular type of music known for its use of strong rhythms and improvisation. Who am I?", "answer": "Jazz"},
    {"question": "I am the main character in the film 'The Lion King'. Who am I?", "answer": "Simba"},
    {"question": "I am a popular animated character created by Walt Disney who is also a mouse. Who am I?", "answer": "Mickey Mouse"},
    {"question": "I am a large, fluffy mammal known for my wool. Who am I?", "answer": "Sheep"},
    {"question": "I am a type of pasta that is shaped like little ears. Who am I?", "answer": "Orecchiette"},
    {"question": "I am a large, flightless bird that is native to Australia. Who am I?", "answer": "Emu"},
    {"question": "I am a chemical element with the symbol 'O' and is essential for life. Who am I?", "answer": "Oxygen"},
    {"question": "I am a popular American holiday celebrated with fireworks on the Fourth of July. Who am I?", "answer": "Independence Day"},
    {"question": "I am the author of the 'Lord of the Rings' series. Who am I?", "answer": "J.R.R. Tolkien"},
    {"question": "I am a natural satellite that orbits the Earth. Who am I?", "answer": "Moon"},
    {"question": "I am a popular video game character known for jumping and collecting coins. Who am I?", "answer": "Mario"},
    {"question": "I am a color often associated with royalty. Who am I?", "answer": "Purple"},
    {"question": "I am a popular TV show about a group of friends living in New York City. Who am I?", "answer": "Friends"},
    {"question": "I am a famous explorer known for discovering America. Who am I?", "answer": "Christopher Columbus"},
    {"question": "I am a large body of salt water that covers most of the Earth. Who am I?", "answer": "Ocean"},
    {"question": "I am a popular type of dance that originated in the Caribbean. Who am I?", "answer": "Salsa"},
    {"question": "I am a popular social media platform known for short videos. Who am I?", "answer": "TikTok"},
    {"question": "I am a large, powerful carnivore often referred to as the 'King of the Jungle'. Who am I?", "answer": "Lion"},
     {"question": "I am a type of pasta shaped like little tubes and often used in baked dishes. Who am I?", "answer": "Ziti"},
    {"question": "I am a famous Greek philosopher known for my teachings on ethics and politics. Who am I?", "answer": "Plato"},
    {"question": "I am a famous female singer known for my hits 'Hello' and 'Someone Like You'. Who am I?", "answer": "Adele"},
    {"question": "I am a large mammal known for my thick fur and is often associated with the Arctic. Who am I?", "answer": "Polar Bear"},
    {"question": "I am a vegetable that is often used in salads and is known for its bitter taste. Who am I?", "answer": "Endive"},
    {"question": "I am a classic animated movie about a young girl who befriends a giant blue genie. Who am I?", "answer": "Aladdin"},
    {"question": "I am a popular sport played on a field with a goal at each end. Who am I?", "answer": "Soccer"},
    {"question": "I am a bright red fruit that is often used to make sauces and is a staple in many kitchens. Who am I?", "answer": "Tomato"},
    {"question": "I am a popular video game series that features a hero who often saves a princess. Who am I?", "answer": "The Legend of Zelda"},
    {"question": "I am a famous physicist known for my work on electromagnetism and the formulation of the laws of motion. Who am I?", "answer": "Isaac Newton"},
    {"question": "I am a well-known author of fantasy novels featuring hobbits and epic quests. Who am I?", "answer": "J.R.R. Tolkien"},
    {"question": "I am a small, round fruit that is often found in pies and is red or green. Who am I?", "answer": "Apple"},
    {"question": "I am a traditional Indian dish made with rice and various spices. Who am I?", "answer": "Biryani"},
    {"question": "I am a type of rock known for its hardness and is often used in construction. Who am I?", "answer": "Granite"},
    {"question": "I am a classic fairy tale character who befriends seven dwarfs. Who am I?", "answer": "Snow White"},
    {"question": "I am a popular beverage made from brewed leaves and is often served hot or iced. Who am I?", "answer": "Tea"},
    {"question": "I am a fictional superhero known for my shield and fighting against villains like Thanos. Who am I?", "answer": "Captain America"},
    {"question": "I am a famous scientist known for my theory of evolution by natural selection. Who am I?", "answer": "Charles Darwin"},
    {"question": "I am a colorful insect known for my beautiful wings and metamorphosis. Who am I?", "answer": "Butterfly"},
    {"question": "I am a famous play written by Arthur Miller about the American Dream. Who am I?", "answer": "Death of a Salesman"},
    {"question": "I am a historical landmark known for being the residence of the President of the United States. Who am I?", "answer": "White House"},
    {"question": "I am a popular social media platform that allows users to share photos and videos. Who am I?", "answer": "Instagram"},
    {"question": "I am a large, carnivorous animal known for my sharp teeth and strong jaws, often found in the ocean. Who am I?", "answer": "Shark"},
    {"question": "I am a popular holiday celebrated with fireworks and barbecues in the United States. Who am I?", "answer": "Independence Day"},
    {"question": "I am a large, graceful mammal known for my long neck and legs. Who am I?", "answer": "Giraffe"},
    {"question": "I am a well-known American author who wrote 'The Great Gatsby'. Who am I?", "answer": "F. Scott Fitzgerald"},
    {"question": "I am a tropical fruit known for my spiky exterior and sweet interior. Who am I?", "answer": "Pineapple"},
    {"question": "I am a famous landmark in India that is often referred to as a symbol of love. Who am I?", "answer": "Taj Mahal"},
    {"question": "I am a famous detective known for solving mysteries with logical reasoning. Who am I?", "answer": "Sherlock Holmes"},
    {"question": "I am a popular board game where players try to buy and sell properties. Who am I?", "answer": "Monopoly"},
    {"question": "I am a well-known author of the 'Sherlock Holmes' series. Who am I?", "answer": "Arthur Conan Doyle"},
    {"question": "I am a country famous for its fjords and northern lights. Who am I?", "answer": "Norway"},
    {"question": "I am a well-known figure in history who was assassinated on April 4, 1968. Who am I?", "answer": "Martin Luther King Jr."},
    {"question": "I am a popular animated film about a young fish searching for his father. Who am I?", "answer": "Finding Nemo"},
    {"question": "I am a fruit that is often mistaken for a vegetable and is commonly used in salads. Who am I?", "answer": "Tomato"},
    {"question": "I am a classic fairy tale character known for losing her glass slipper at a ball. Who am I?", "answer": "Cinderella"},
    {"question": "I am a famous battle fought during World War I that took place in Belgium. Who am I?", "answer": "Battle of Ypres"},
    {"question": "I am a type of plant often used for decoration and is known for its vibrant colors. Who am I?", "answer": "Orchid"},
    {"question": "I am a popular card game often played with friends and family. Who am I?", "answer": "Poker"},
    {"question": "I am a traditional Japanese dish made with vinegared rice and various toppings. Who am I?", "answer": "Sushi"},
    {"question": "I am a large ocean located between Africa and Australia. Who am I?", "answer": "Indian Ocean"},
    {"question": "I am a famous painting by Vincent van Gogh known for its swirling skies. Who am I?", "answer": "Starry Night"},
    {"question": "I am a popular soft drink known for my red color and sweet flavor. Who am I?", "answer": "Coca-Cola"},
    {"question": "I am a well-known American singer famous for my songs 'Like a Prayer' and 'Vogue'. Who am I?", "answer": "Madonna"},
    {"question": "I am a type of grain often used to make bread. Who am I?", "answer": "Wheat"},
    {"question": "I am a popular board game known for its strategy and trading mechanics. Who am I?", "answer": "Settlers of Catan"},
    {"question": "I am a famous artist known for my unique style of painting and use of bright colors. Who am I?", "answer": "Pablo Picasso"},
    {"question": "I am a small, brightly colored bird known for its ability to mimic sounds. Who am I?", "answer": "Mockingbird"},
    {"question": "I am a classic fairytale about a girl who has to spin straw into gold. Who am I?", "answer": "Rumpelstiltskin"},
    {"question": "I am a famous natural landmark known for my colorful rock formations in Arizona. Who am I?", "answer": "Grand Canyon"},
    {"question": "I am a well-known actress who starred in 'Titanic' and 'The Reader'. Who am I?", "answer": "Kate Winslet"},
    {"question": "I am a famous landmark in the USA that serves as a memorial to President Abraham Lincoln. Who am I?", "answer": "Lincoln Memorial"},
    {"question": "I am a type of fruit that is small, round, and often used in baking. Who am I?", "answer": "Cherry"},
    {"question": "I am a large, carnivorous animal that often hunts in packs. Who am I?", "answer": "Wolf"},
    {"question": "I am a famous dish made of thinly sliced raw fish and is popular in Japanese cuisine. Who am I?", "answer": "Sashimi"},
    {"question": "I am a famous scientist known for my work on radioactivity and the discovery of polonium and radium. Who am I?", "answer": "Marie Curie"},
    {"question": "I am a popular comic book character known for my super speed. Who am I?", "answer": "The Flash"},
    {"question": "I am a large, powerful mammal known for my strength and ability to swim long distances. Who am I?", "answer": "Whale"},
    {"question": "I am a type of puzzle where pieces must fit together to create an image. Who am I?", "answer": "Jigsaw puzzle"},
    {"question": "I am a famous novel written by George Orwell about a dystopian future. Who am I?", "answer": "1984"},
    {"question": "I am a famous novel written by George Orwell about a dystopian future. Who am I?", "answer": "1984"},
    {"question": "I am a small, flying insect known for my role in pollination and often found in gardens. Who am I?", "answer": "Bee"},
    {"question": "I am a traditional Italian dish made of dough and topped with various ingredients. Who am I?", "answer": "Pizza"},
    {"question": "I am a large land mammal with a trunk, often associated with intelligence. Who am I?", "answer": "Elephant"},
    {"question": "I am a popular online platform for sharing short videos and music. Who am I?", "answer": "TikTok"},
    {"question": "I am a character from a famous series who has a magic ring and goes on an epic journey. Who am I?", "answer": "Frodo Baggins"},
    {"question": "I am a well-known American artist famous for my colorful paintings of soup cans. Who am I?", "answer": "Andy Warhol"},
    {"question": "I am a type of tree that produces acorns and is known for my strength and longevity. Who am I?", "answer": "Oak tree"},
    {"question": "I am a popular form of entertainment where people watch actors perform live on stage. Who am I?", "answer": "Theater"},
    {"question": "I am a large, herbivorous mammal that is often found in grasslands and is known for my speed. Who am I?", "answer": "Horse"},
    {"question": "I am a traditional Middle Eastern dish made from ground chickpeas and spices. Who am I?", "answer": "Falafel"},
    {"question": "I am a fictional superhero with the ability to climb walls and swing between buildings. Who am I?", "answer": "Spider-Man"},
    {"question": "I am a historical figure known for my contributions to the development of calculus. Who am I?", "answer": "Isaac Newton"},
    {"question": "I am a popular flower known for my beautiful petals and fragrance, often given on Valentine's Day. Who am I?", "answer": "Rose"},
    {"question": "I am a famous explorer known for my voyages across the Pacific Ocean. Who am I?", "answer": "Ferdinand Magellan"},
    {"question": "I am a popular snack food made from corn and often eaten at movie theaters. Who am I?", "answer": "Popcorn"},
    {"question": "I am a large, flightless bird native to Australia, known for its speed and size. Who am I?", "answer": "Emu"},
    {"question": "I am a classic book about a young orphan who discovers he is a wizard. Who am I?", "answer": "Harry Potter"},
    {"question": "I am a famous painter known for my surrealistic works featuring melting clocks. Who am I?", "answer": "Salvador Dalí"},
    {"question": "I am a popular board game where players move pieces around a board to capture each other's pieces. Who am I?", "answer": "Chess"},
    {"question": "I am a large rodent often kept as a pet, known for my ability to run on wheels. Who am I?", "answer": "Hamster"},
    {"question": "I am a traditional Korean dish made of fermented vegetables, commonly cabbage. Who am I?", "answer": "Kimchi"},
    {"question": "I am a popular social media platform known for its tweets and hashtags. Who am I?", "answer": "Twitter"},
    {"question": "I am a famous historical figure known for my role in the American Revolution. Who am I?", "answer": "George Washington"},
    {"question": "I am a popular dessert made of layers of cake, frosting, and often fruit. Who am I?", "answer": "Layer cake"},
    {"question": "I am a large, carnivorous reptile often found in tropical regions. Who am I?", "answer": "Crocodile"},
    {"question": "I am a popular genre of music that originated in the African American community and is known for its rhythmic style. Who am I?", "answer": "Jazz"},
    {"question": "I am a traditional Chinese dish made of thinly sliced meat and vegetables, often stir-fried. Who am I?", "answer": "Chow Mein"},
    {"question": "I am a classic cartoon character known for my love of carrots and my catchphrase 'What's up, Doc?'. Who am I?", "answer": "Bugs Bunny"},
    {"question": "I am a historical figure known for my famous speech 'I Have a Dream'. Who am I?", "answer": "Martin Luther King Jr."},
    {"question": "I am a large bird known for my ability to mimic sounds and speech. Who am I?", "answer": "Parrot"},
    {"question": "I am a popular mobile app for sharing photos and stories. Who am I?", "answer": "Instagram"},
    {"question": "I am a popular type of music characterized by its use of electronic instruments. Who am I?", "answer": "Electronic"},
    {"question": "I am a fictional character known for my iconic red cape and superhuman strength. Who am I?", "answer": "Superman"},
    {"question": "I am a traditional Italian pasta dish made with a creamy white sauce. Who am I?", "answer": "Fettuccine Alfredo"},
    {"question": "I am a large mammal known for my speed and agility, often found in the wild. Who am I?", "answer": "Gazelle"},
    {"question": "I am a famous scientist known for my theory of relativity. Who am I?", "answer": "Albert Einstein"},
    {"question": "I am a popular summer fruit known for my juicy flesh and refreshing taste. Who am I?", "answer": "Watermelon"},
    {"question": "I am a type of bread often associated with Middle Eastern cuisine, used for wraps. Who am I?", "answer": "Pita"},
    {"question": "I am a well-known social activist who fought for women's rights. Who am I?", "answer": "Susan B. Anthony"},
    {"question": "I am a popular television show featuring a group of friends living in New York City. Who am I?", "answer": "Friends"},
    {"question": "I am a type of cheese known for its blue veins and strong flavor. Who am I?", "answer": "Blue cheese"},
    {"question": "I am a famous work of art depicting a woman with an enigmatic smile. Who am I?", "answer": "Mona Lisa"},
    {"question": "I am a large animal known for my long neck and legs, often found in savannas. Who am I?", "answer": "Giraffe"},
    {"question": "I am a popular card game often played with a standard deck of cards. Who am I?", "answer": "Poker"},
    {"question": "I am a classic fairy tale character who was trapped in a tower and let down her hair. Who am I?", "answer": "Rapunzel"},
    {"question": "I am a historical figure known for my contributions to the theory of evolution. Who am I?", "answer": "Charles Darwin"},
    {"question": "I am a popular dance style that originated in the Caribbean and is known for its lively movements. Who am I?", "answer": "Salsa"},
    {"question": "I am a popular fruit known for its high vitamin C content and is often used in drinks. Who am I?", "answer": "Orange"},
    {"question": "I am a famous American landmark known for its iconic statue of a woman holding a torch. Who am I?", "answer": "Statue of Liberty"},
    {"question": "I am a well-known author famous for writing the 'Harry Potter' series. Who am I?", "answer": "J.K. Rowling"},
    {"question": "I am a popular snack food made from corn that is often served at fairs. Who am I?", "answer": "Cotton Candy"},
    {"question": "I am a large fish known for my sharp teeth and fearsome appearance, often found in the ocean. Who am I?", "answer": "Shark"},
    {"question": "I am a popular animated movie about a young princess who befriends a talking snowman. Who am I?", "answer": "Frozen"},
    {"question": "I am a historical figure known for my role in the founding of the United Nations. Who am I?", "answer": "Eleanor Roosevelt"},
    {"question": "I am a type of fruit that is often mistaken for a vegetable and is known for its creamy texture. Who am I?", "answer": "Avocado"},
    {"question": "I am a classic work of literature about a group of stranded boys on an island. Who am I?", "answer": "Lord of the Flies"},
    {"question": "I am a famous fast food chain known for my fried chicken and biscuits. Who am I?", "answer": "Popeyes"},
    {"question": "I am a well-known artist famous for my abstract expressionist paintings. Who am I?", "answer": "Jackson Pollock"},
    {"question": "I am a popular comic book character known for my green skin and incredible strength. Who am I?", "answer": "Hulk"},
    {"question": "I am a historical figure known for my role in the civil rights movement and the abolition of slavery. Who am I?", "answer": "Freder"},
    {"question": "I am a popular television series featuring a family of animated characters living in Springfield. Who am I?", "answer": "The Simpsons"},
    {"question": "I am a large mammal known for my tusks and ability to live in harsh Arctic climates. Who am I?", "answer": "Walrus"},
    {"question": "I am a popular video game character known for my adventures in a fictional world filled with mushrooms. Who am I?", "answer": "Mario"},
    {"question": "I am a famous book about a young girl's adventures in a fantasy land after following a rabbit down a hole. Who am I?", "answer": "Alice's Adventures in Wonderland"},
    {"question": "I am a traditional Indian dish made with lentils and served with rice or bread. Who am I?", "answer": "Daal"},
    {"question": "I am a large bird known for my colorful plumage and ability to mimic human speech. Who am I?", "answer": "Parrot"},
    {"question": "I am a popular dessert made of layers of sponge cake and cream, often with fruit. Who am I?", "answer": "Trifle"},
    {"question": "I am a famous scientist known for my laws of motion and universal gravitation. Who am I?", "answer": "Isaac Newton"},
    {"question": "I am a traditional French dish made of snails cooked in garlic butter. Who am I?", "answer": "Escargot"},
    {"question": "I am a classic fairy tale character known for my magic mirror. Who am I?", "answer": "Snow White"},
    {"question": "I am a popular sport played with a bat and ball, often referred to as America's pastime. Who am I?", "answer": "Baseball"},
    {"question": "I am a well-known author famous for my detective stories featuring Sherlock Holmes. Who am I?", "answer": "Arthur Conan Doyle"},
    {"question": "I am a historical event known for the beginning of the Industrial Revolution. Who am I?", "answer": "The Industrial Revolution"},
    {"question": "I am a popular animated character known for my catchphrase 'What's up, Doc?'. Who am I?", "answer": "Bugs Bunny"},
    {"question": "I am a large, flightless bird native to Australia. Who am I?", "answer": "Emu"},
    {"question": "I am a famous painter known for my abstract works and use of geometric shapes. Who am I?", "answer": "Piet Mondrian"},
    {"question": "I am a popular snack made from deep-fried potatoes and often served with ketchup. Who am I?", "answer": "French fries"},
    {"question": "I am a historical figure known for leading the Soviet Union during World War II. Who am I?", "answer": "Joseph Stalin"},
    {"question": "I am a type of fruit known for its high fiber content and is often dried and eaten as a snack. Who am I?", "answer": "Date"},
    {"question": "I am a famous song by the Beatles about a yellow submarine. Who am I?", "answer": "Yellow Submarine"},
    {"question": "I am a large, majestic bird known for my ability to soar high in the sky. Who am I?", "answer": "Eagle"},
    {"question": "I am a well-known actor famous for my role as Jack Dawson in 'Titanic'. Who am I?", "answer": "Leonardo DiCaprio"},
    {"question": "I am a famous dish made with thinly sliced raw fish and is often served with soy sauce. Who am I?", "answer": "Sashimi"},
    {"question": "I am a popular board game where players must build their own cities and manage resources. Who am I?", "answer": "SimCity"},
    {"question": "I am a popular drink made by brewing coffee beans. Who am I?", "answer": "Coffee"},
    {"question": "I am a classic fairytale character who lost a glass slipper at a ball. Who am I?", "answer": "Cinderella"},
    {"question": "I am a large mammal known for my long tusks and ability to thrive in cold climates. Who am I?", "answer": "Walrus"},
    {"question": "I am a popular social media platform known for its visual content and stories. Who am I?", "answer": "Instagram"},
    {"question": "I am a well-known author famous for my dystopian novel 'Fahrenheit 451'. Who am I?", "answer": "Ray Bradbury"},
    {"question": "I am a type of fruit that is often used in pies and is known for my sweet flavor. Who am I?", "answer": "Cherry"},
    {"question": "I am a classic animated character known for my love of honey. Who am I?", "answer": "Winnie the Pooh"},
    {"question": "I am a historical figure known for my role in the American Civil War and my famous speech at Gettysburg. Who am I?", "answer": "Abraham Lincoln"},
    {"question": "I am a popular snack food made from corn that is often served at fairs. Who am I?", "answer": "Cotton candy"},
    {"question": "I am a famous superhero known for my ability to fly and super strength. Who am I?", "answer": "Superman"},
    {"question": "I am a popular children's book series featuring a young boy who attends a wizarding school. Who am I?", "answer": "Harry Potter"},
    {"question": "I am a well-known American singer famous for my songs 'Like a Prayer' and 'Material Girl'. Who am I?", "answer": "Madonna"},
    {"question": "I am a type of vegetable that is often used in salads and has a crisp texture. Who am I?", "answer": "Cucumber"},
    {"question": "I am a large, gentle giant known for my trunk and big ears. Who am I?", "answer": "Elephant"},
    {"question": "I am a famous landmark known for my large, ancient pyramids. Who am I?", "answer": "Giza"},
    {"question": "I am a popular comic book character known for my web-slinging abilities. Who am I?", "answer": "Spider-Man"},
    {"question": "I am a traditional dish made with rice and various spices, often served with meat. Who am I?", "answer": "Biryani"},
    {"question": "I am a popular musical genre characterized by its use of guitars and drums. Who am I?", "answer": "Rock"},
    {"question": "I am a classic work of literature about a young girl who dreams of becoming a ballerina. Who am I?", "answer": "The Red Shoes"},
    {"question": "I am a famous artist known for my unique style and use of vibrant colors. Who am I?", "answer": "Pablo Picasso"},
    {"question": "I am a well-known animated character who loves to eat lasagna. Who am I?", "answer": "Garfield"},
    {"question": "I am a historical figure known for my work on the theory of electricity and magnetism. Who am I?", "answer": "James Clerk Maxwell"},
    {"question": "I am a popular fruit known for its sweet, juicy flesh and is often used in smoothies. Who am I?", "answer": "Mango"},
    {"question": "I am a famous festival celebrated with fireworks and parades in the United States. Who am I?", "answer": "Fourth of July"},
    {"question": "I am a large, flightless bird known for my ability to run fast and is native to Africa. Who am I?", "answer": "Ostrich"},
    {"question": "I am a well-known actress famous for my role in 'The Hunger Games'. Who am I?", "answer": "Jennifer Lawrence"},
    {"question": "I am a traditional dish made from fermented vegetables, commonly found in Korea. Who am I?", "answer": "Kimchi"},
    {"question": "I am a popular drink made by brewing tea leaves and is often served with milk. Who am I?", "answer": "Chai"},
    {"question": "I am a classic book series featuring a young boy who attends a wizarding school. Who am I?", "answer": "Harry Potter"},
    {"question": "I am a well-known historical figure who fought for women's suffrage. Who am I?", "answer": "Susan B. Anthony"},
    {"question": "I am a popular mobile game that involves building and farming. Who am I?", "answer": "Farmville"},
    {"question": "I am a type of music that originated in the African American community and is known for its rhythmic beats. Who am I?", "answer": "Hip Hop"},
    {"question": "I am a famous character known for my green skin and love of princesses. Who am I?", "answer": "Shrek"},
    {"question": "I am a large animal known for my strength and ability to live in water. Who am I?", "answer": "Hippo"},
    {"question": "I am a popular video game series that features a hero saving a princess. Who am I?", "answer": "The Legend of Zelda"}
]

questions_hard = [
    {"question": "I am a famous physicist known for the theory of relativity. Who am I?", "answer": "Albert Einstein"},
    {"question": "I am a renowned artist known for the painting 'The Starry Night'. Who am I?", "answer": "Vincent van Gogh"},
    {"question": "I am a historical figure who led a revolution in India against British rule. Who am I?", "answer": "Mahatma Gandhi"},
    {"question": "I am a British author known for creating a boy wizard. Who am I?", "answer": "J.K. Rowling"},
    {"question": "I am a fictional detective created by Arthur Conan Doyle. Who am I?", "answer": "Sherlock Holmes"},
    {"question": "I was the first woman to fly solo across the Atlantic Ocean. Who am I?", "answer": "Amelia Earhart"},
    {"question": "I am a famous scientist known for my work in radioactivity and a two-time Nobel Prize winner. Who am I?", "answer": "Marie Curie"},
    {"question": "I am a legendary musician known as the 'King of Rock and Roll'. Who am I?", "answer": "Elvis Presley"},
    {"question": "I am a famous physicist who developed the laws of motion and universal gravitation. Who am I?", "answer": "Isaac Newton"},
    {"question": "I am the first president of the United States. Who am I?", "answer": "George Washington"},
    {"question": "I am a famous Egyptian queen known for my beauty and relationships with Julius Caesar and Mark Antony. Who am I?", "answer": "Cleopatra"},
    {"question": "I am a renowned civil rights leader who delivered the 'I Have a Dream' speech. Who am I?", "answer": "Martin Luther King Jr."},
    {"question": "I am a famous Italian explorer known for my voyages to the Americas. Who am I?", "answer": "Christopher Columbus"},
    {"question": "I am a British Prime Minister known for my role during World War II. Who am I?", "answer": "Winston Churchill"},
    {"question": "I am a famous psychoanalyst known for my theories on the unconscious mind. Who am I?", "answer": "Sigmund Freud"},
    {"question": "I am the author of 'Moby Dick'. Who am I?", "answer": "Herman Melville"},
    {"question": "I am a famous theoretical physicist who proposed the idea of black holes. Who am I?", "answer": "Stephen Hawking"},
    {"question": "I am an ancient Greek philosopher known for my method of questioning. Who am I?", "answer": "Socrates"},
    {"question": "I am a famous artist known for the Mona Lisa. Who am I?", "answer": "Leonardo da Vinci"},
    {"question": "I am a prominent figure in the women's suffrage movement in the United States. Who am I?", "answer": "Susan B. Anthony"},
    {"question": "I am known as the 'Father of Geometry'. Who am I?", "answer": "Euclid"},
    {"question": "I am a scientist known for formulating the laws of thermodynamics. Who am I?", "answer": "Ludwig Boltzmann"},
    {"question": "I am a legendary ancient Greek hero known for my strength and 12 labors. Who am I?", "answer": "Hercules"},
    {"question": "I am a famous artist associated with the surrealist movement, known for my melting clocks. Who am I?", "answer": "Salvador Dalí"},
    {"question": "I am a famous physicist known for my theory of electromagnetism. Who am I?", "answer": "James Clerk Maxwell"},
    {"question": "I am an author known for writing '1984' and 'Animal Farm'. Who am I?", "answer": "George Orwell"},
    {"question": "I am an influential leader of the Cuban Revolution. Who am I?", "answer": "Fidel Castro"},
    {"question": "I am a famous British naturalist known for my theory of evolution. Who am I?", "answer": "Charles Darwin"},
    {"question": "I am a prominent civil rights activist known for my work against apartheid in South Africa. Who am I?", "answer": "Nelson Mandela"},
    {"question": "I am a famous composer known for my symphonies and operas. Who am I?", "answer": "Ludwig van Beethoven"},
    {"question": "I am a famous author known for my horror novels, including 'Dracula'. Who am I?", "answer": "Bram Stoker"},
    {"question": "I am known for the theory of economic capitalism. Who am I?", "answer": "Adam Smith"},
    {"question": "I am a famous astronomer who proposed the heliocentric model of the universe. Who am I?", "answer": "Nicolaus Copernicus"},
    {"question": "I am the first female Prime Minister of the United Kingdom. Who am I?", "answer": "Margaret Thatcher"},
    {"question": "I am a French military leader who became Emperor of France. Who am I?", "answer": "Napoleon Bonaparte"},
    {"question": "I am known for creating the first successful polio vaccine. Who am I?", "answer": "Jonas Salk"},
    {"question": "I am a famous poet known for my work 'The Raven'. Who am I?", "answer": "Edgar Allan Poe"},
    {"question": "I am a prominent figure in the American women's rights movement. Who am I?", "answer": "Elizabeth Cady Stanton"},
    {"question": "I am a famous physicist known for my work on quantum mechanics. Who am I?", "answer": "Niels Bohr"},
    {"question": "I am a historical figure known for unifying Germany in the 19th century. Who am I?", "answer": "Otto von Bismarck"},
    {"question": "I am a famous playwright known for works such as 'Hamlet' and 'Romeo and Juliet'. Who am I?", "answer": "William Shakespeare"},
    {"question": "I am a famous Russian leader known for my role in the October Revolution. Who am I?", "answer": "Vladimir Lenin"},
    {"question": "I am an ancient Roman general known for crossing the Rubicon. Who am I?", "answer": "Julius Caesar"},
    {"question": "I am a famous suffragette known for my militant activism. Who am I?", "answer": "Emmeline Pankhurst"},
    {"question": "I am a historical figure known for my role in the American Revolution. Who am I?", "answer": "Thomas Jefferson"},
    {"question": "I am a prominent advocate for LGBTQ+ rights in the United States. Who am I?", "answer": "Harvey Milk"},
    {"question": "I am a famous painter known for my work 'The Last Supper'. Who am I?", "answer": "Leonardo da Vinci"},
    {"question": "I am a historical figure known for being the first African American president of the United States. Who am I?", "answer": "Barack Obama"},
    {"question": "I am an ancient Egyptian queen known for my intelligence and beauty. Who am I?", "answer": "Cleopatra"},
    {"question": "I am a famous musician known as the 'Queen of Soul'. Who am I?", "answer": "Aretha Franklin"},
    {"question": "I am a famous physicist known for my work on the theory of relativity. Who am I?", "answer": "Albert Einstein"},
    {"question": "I am a famous philosopher known for my theory of utilitarianism. Who am I?", "answer": "John Stuart Mill"},
    {"question": "I am a famous singer-songwriter known for 'Imagine'. Who am I?", "answer": "John Lennon"},
    {"question": "I am a historical figure known for my role in the abolition of slavery in the United States. Who am I?", "answer": "Frederick Douglass"},
    {"question": "I am a famous author known for my book 'Pride and Prejudice'. Who am I?", "answer": "Jane Austen"},
    {"question": "I am a famous ancient Greek philosopher who taught Alexander the Great. Who am I?", "answer": "Aristotle"},
    {"question": "I am a prominent historical figure known for leading the Haitian Revolution. Who am I?", "answer": "Toussaint L'Ouverture"},
    {"question": "I am a famous British author known for writing 'The Chronicles of Narnia'. Who am I?", "answer": "C.S. Lewis"},
    {"question": "I am a famous scientist known for my work on genetics. Who am I?", "answer": "Gregor Mendel"},
    {"question": "I am a famous civil rights leader known for my advocacy of nonviolent protest. Who am I?", "answer": "Martin Luther King Jr."},
    {"question": "I am a famous American author known for 'The Great Gatsby'. Who am I?", "answer": "F. Scott Fitzgerald"},
    {"question": "I am a famous historical figure known for my contributions to the field of nursing. Who am I?", "answer": "Florence Nightingale"},
    {"question": "I am a historical figure known for founding the Mongol Empire. Who am I?", "answer": "Genghis Khan"},
    {"question": "I am a prominent American architect known for designing Fallingwater. Who am I?", "answer": "Frank Lloyd Wright"},
    {"question": "I am a famous physicist known for formulating the laws of electromagnetism. Who am I?", "answer": "James Clerk Maxwell"},
    {"question": "I am a famous psychologist known for my theories on human behavior. Who am I?", "answer": "Carl Jung"},
    {"question": "I am a historical figure known for my leadership during the American Civil War. Who am I?", "answer": "Abraham Lincoln"},
    {"question": "I am a famous poet known for my work 'Leaves of Grass'. Who am I?", "answer": "Walt Whitman"},
    {"question": "I am a famous actress known for my roles in classic films like 'Breakfast at Tiffany's'. Who am I?", "answer": "Audrey Hepburn"},
    {"question": "I am a famous artist known for my work in the Dada movement. Who am I?", "answer": "Marcel Duchamp"},
    {"question": "I am a famous historical figure known for my contributions to the field of astronomy. Who am I?", "answer": "Galileo Galilei"},
    {"question": "I am a prominent scientist known for my work in immunology. Who am I?", "answer": "Louis Pasteur"},
    {"question": "I am a famous African American woman who became a prominent activist for civil rights. Who am I?", "answer": "Rosa Parks"},
    {"question": "I am a famous artist known for my abstract expressionist works. Who am I?", "answer": "Jackson Pollock"},
    {"question": "I am a renowned physicist known for the uncertainty principle. Who am I?", "answer": "Werner Heisenberg"},
    {"question": "I am a famous playwright known for 'A Streetcar Named Desire'. Who am I?", "answer": "Tennessee Williams"},
    {"question": "I am a historical figure known for my contributions to mathematics and physics. Who am I?", "answer": "Isaac Newton"},
    {"question": "I am a famous writer known for my magical realism novels. Who am I?", "answer": "Gabriel García Márquez"},
    {"question": "I am a famous scientist known for my theories on evolution and natural selection. Who am I?", "answer": "Charles Darwin"},
    {"question": "I am a famous musician known for my influential role in jazz music. Who am I?", "answer": "Louis Armstrong"},
    {"question": "I am a historical figure known for my role in the unification of Italy. Who am I?", "answer": "Giuseppe Garibaldi"},
    {"question": "I am a prominent author known for my works in science fiction and fantasy. Who am I?", "answer": "J.R.R. Tolkien"},
    {"question": "I am a famous philosopher known for my social contract theory. Who am I?", "answer": "Jean-Jacques Rousseau"},
    {"question": "I am a historical figure known for my work in the field of political philosophy. Who am I?", "answer": "Niccolò Machiavelli"},
    {"question": "I am a famous chemist known for my contributions to the periodic table. Who am I?", "answer": "Dmitri Mendeleev"},
    {"question": "I am a legendary hero of the Trojan War known for my cunning and intelligence. Who am I?", "answer": "Odysseus"},
    {"question": "I am a famous writer known for my children's books, including 'Charlie and the Chocolate Factory'. Who am I?", "answer": "Roald Dahl"},
    {"question": "I am a famous artist known for my colorful and abstract paintings. Who am I?", "answer": "Pablo Picasso"},
    {"question": "I am a historical figure known for my explorations of the Pacific Ocean. Who am I?", "answer": "James Cook"},
    {"question": "I am a renowned activist known for my work in environmental conservation. Who am I?", "answer": "Greta Thunberg"},
    {"question": "I am a famous director known for my epic films, including 'Titanic' and 'Avatar'. Who am I?", "answer": "James Cameron"},
    {"question": "I am a historical figure known for my role in the founding of the Soviet Union. Who am I?", "answer": "Vladimir Lenin"},
    {"question": "I am a famous figure in literature known for my novels exploring human existence. Who am I?", "answer": "Fyodor Dostoevsky"},
    {"question": "I am a prominent physicist known for my work on nuclear fission. Who am I?", "answer": "Enrico Fermi"},
    {"question": "I am a famous social reformer known for my work in the women's rights movement. Who am I?", "answer": "Sojourner Truth"},
    {"question": "I am a famous scientist known for my contributions to the field of electromagnetism. Who am I?", "answer": "Michael Faraday"},
    {"question": "I am a historical figure known for my contributions to the abolitionist movement. Who am I?", "answer": "Harriet Tubman"},
    {"question": "I am a renowned mathematician known for my work in number theory. Who am I?", "answer": "Carl Friedrich Gauss"},
    {"question": "I am a famous explorer known for my voyages to the Americas in the late 15th century. Who am I?", "answer": "Christopher Columbus"},
    {"question": "I am a historical figure known for my influential role in the feminist movement. Who am I?", "answer": "Simone de Beauvoir"},
    {"question": "I am a prominent historical figure known for my role in the civil rights movement in the United States. Who am I?", "answer": "Malcolm X"},
    {"question": "I am a famous artist known for my work in the Impressionist movement. Who am I?", "answer": "Claude Monet"},
    {"question": "I am a legendary figure known for my role in the American Revolutionary War. Who am I?", "answer": "Benedict Arnold"},
    {"question": "I am a famous composer known for my operas, including 'The Magic Flute'. Who am I?", "answer": "Wolfgang Amadeus Mozart"},
    {"question": "I am a historical figure known for my leadership during the French Revolution. Who am I?", "answer": "Maximilien Robespierre"},
    {"question": "I am a prominent civil rights activist known for my work against racial segregation. Who am I?", "answer": "Rosa Parks"},
    {"question": "I am a famous scientist known for my contributions to the field of genetics and the double helix structure. Who am I?", "answer": "James Watson"},
    {"question": "I am a famous figure in the realm of psychology known for my theories on behaviorism. Who am I?", "answer": "B.F. Skinner"},
    {"question": "I am a renowned artist known for my colorful and vibrant paintings. Who am I?", "answer": "Henri Matisse"},
    {"question": "I am a famous writer known for my dystopian novels, including 'Fahrenheit 451'. Who am I?", "answer": "Ray Bradbury"},
    {"question": "I am a prominent political leader known for my role in the Indian independence movement. Who am I?", "answer": "Jawaharlal Nehru"},
    {"question": "I am a famous mathematician known for my work in calculus. Who am I?", "answer": "Isaac Newton"},
    {"question": "I am a historical figure known for my contributions to the field of anthropology. Who am I?", "answer": "Margaret Mead"},
    {"question": "I am a famous physicist known for my work in quantum mechanics and the uncertainty principle. Who am I?", "answer": "Werner Heisenberg"},
    {"question": "I am a legendary artist known for my beautiful sculptures and architecture. Who am I?", "answer": "Michelangelo"},
    {"question": "I am a prominent historical figure known for my role in the development of socialism. Who am I?", "answer": "Karl Marx"},
    {"question": "I am a famous figure in American literature known for my works on slavery and racial injustice. Who am I?", "answer": "Harriet Beecher Stowe"},
    {"question": "I am a historical figure known for my role in the Russian Revolution. Who am I?", "answer": "Leon Trotsky"},
    {"question": "I am a famous actress known for my roles in films like 'The Sound of Music'. Who am I?", "answer": "Julie Andrews"},
    {"question": "I am a renowned scientist known for my theories on evolution and natural selection. Who am I?", "answer": "Charles Darwin"},
    {"question": "I am a famous playwright known for my tragedies and comedies. Who am I?", "answer": "William Shakespeare"},
    {"question": "I am a historical figure known for my role in the women's suffrage movement. Who am I?", "answer": "Susan B. Anthony"},
    {"question": "I am a prominent author known for my work on existentialism. Who am I?", "answer": "Jean-Paul Sartre"},
    {"question": "I am a famous composer known for my symphonies and concertos. Who am I?", "answer": "Ludwig van Beethoven"},
    {"question": "I am a prominent civil rights leader known for my advocacy for racial equality. Who am I?", "answer": "W.E.B. Du Bois"},
    {"question": "I am a renowned author known for my novel 'One Hundred Years of Solitude'. Who am I?", "answer": "Gabriel García Márquez"},
    {"question": "I am a famous actor known for my roles in 'The Godfather' and 'Apocalypse Now'. Who am I?", "answer": "Marlon Brando"},
    {"question": "I am a historical figure known for my influential role in the abolition of slavery in the British Empire. Who am I?", "answer": "William Wilberforce"},
    {"question": "I am a legendary leader known for uniting the Mongol tribes and founding the Mongol Empire. Who am I?", "answer": "Genghis Khan"},
    {"question": "I am a famous artist known for my avant-garde contributions to the art world. Who am I?", "answer": "Marcel Duchamp"},
    {"question": "I am a prominent historical figure known for my writings on civil disobedience. Who am I?", "answer": "Henry David Thoreau"},
    {"question": "I am a famous scientist known for my theory of evolution through natural selection. Who am I?", "answer": "Charles Darwin"},
    {"question": "I am a historical figure known for leading the Haitian Revolution against colonial rule. Who am I?", "answer": "Toussaint L'Ouverture"},
    {"question": "I am a famous novelist known for my works that explore the human condition. Who am I?", "answer": "Leo Tolstoy"},
    {"question": "I am a renowned scientist known for my groundbreaking work in the field of physics. Who am I?", "answer": "Richard Feynman"},
    {"question": "I am a legendary figure in American folklore known for my strength and feats. Who am I?", "answer": "Paul Bunyan"},
    {"question": "I am a prominent feminist writer known for my book 'The Second Sex'. Who am I?", "answer": "Simone de Beauvoir"},
    {"question": "I am a famous artist known for my bold use of color and form. Who am I?", "answer": "Henri Matisse"},
    {"question": "I am a historical figure known for my contributions to the development of the modern nursing profession. Who am I?", "answer": "Florence Nightingale"},
    {"question": "I am a famous scientist known for my theories in psychoanalysis. Who am I?", "answer": "Sigmund Freud"},
    {"question": "I am a legendary poet known for my epic work 'The Iliad'. Who am I?", "answer": "Homer"},
    {"question": "I am a prominent philosopher known for my ideas about the nature of reality. Who am I?", "answer": "Immanuel Kant"},
    {"question": "I am a famous playwright known for 'Waiting for Godot'. Who am I?", "answer": "Samuel Beckett"},
    {"question": "I am a historical figure known for my role in the discovery of penicillin. Who am I?", "answer": "Alexander Fleming"},
    {"question": "I am a famous composer known for my ballets and orchestral works. Who am I?", "answer": "Igor Stravinsky"},
    {"question": "I am a prominent historical figure known for my contributions to the civil rights movement in America. Who am I?", "answer": "Malcolm X"},
    {"question": "I am a legendary writer known for my dystopian novels, including 'Brave New World'. Who am I?", "answer": "Aldous Huxley"},
    {"question": "I am a famous activist known for my fight against apartheid in South Africa. Who am I?", "answer": "Nelson Mandela"},
    {"question": "I am a renowned scientist known for my work in the field of immunology and vaccines. Who am I?", "answer": "Edward Jenner"},
    {"question": "I am a historical figure known for my contributions to the development of the modern state of Turkey. Who am I?", "answer": "Mustafa Kemal Atatürk"},
    {"question": "I am a famous figure in literature known for my children's book series 'Harry Potter'. Who am I?", "answer": "J.K. Rowling"},
    {"question": "I am a prominent playwright known for my work 'Death of a Salesman'. Who am I?", "answer": "Arthur Miller"},
    {"question": "I am a historical figure known for my explorations in North America during the Age of Discovery. Who am I?", "answer": "John Cabot"},
    {"question": "I am a famous figure known for my role in the American space program and as the first person to walk on the moon. Who am I?", "answer": "Neil Armstrong"},
    {"question": "I am a legendary figure known for my work in the field of human rights and nonviolent resistance. Who am I?", "answer": "Mahatma Gandhi"},
    {"question": "I am a prominent author known for my novels exploring the African American experience. Who am I?", "answer": "Toni Morrison"},
    {"question": "I am a famous figure known for my role in the creation of the United Nations. Who am I?", "answer": "Eleanor Roosevelt"},
    {"question": "I am a renowned mathematician known for my contributions to algebra and number theory. Who am I?", "answer": "Leonhard Euler"},
    {"question": "I am a famous composer known for my contributions to opera, including 'The Marriage of Figaro'. Who am I?", "answer": "Wolfgang Amadeus Mozart"},
    {"question": "I am a historical figure known for my role in the establishment of the Federal Reserve in the United States. Who am I?", "answer": "Woodrow Wilson"},
    {"question": "I am a prominent philosopher known for my work in ethics and political theory. Who am I?", "answer": "John Stuart Mill"},
    {"question": "I am a famous writer known for my contributions to science fiction and fantasy literature. Who am I?", "answer": "Isaac Asimov"},
    {"question": "I am a historical figure known for my leadership in the French Revolution. Who am I?", "answer": "Maximilien Robespierre"},
    {"question": "I am a legendary figure known for my wisdom and justice, often associated with a famous ancient city. Who am I?", "answer": "King Solomon"},
    {"question": "I am a famous artist known for my surrealist paintings and exploration of the subconscious. Who am I?", "answer": "Salvador Dalí"},
    {"question": "I am a prominent scientist known for my work on the structure of DNA. Who am I?", "answer": "Francis Crick"},
    {"question": "I am a famous author known for my writings on existential philosophy and the absurd. Who am I?", "answer": "Albert Camus"},
    {"question": "I am a historical figure known for my contributions to the field of sociology. Who am I?", "answer": "Max Weber"},
    {"question": "I am a famous playwright known for my work 'The Glass Menagerie'. Who am I?", "answer": "Tennessee Williams"},
    {"question": "I am a historical figure known for leading the Soviet Union during World War II. Who am I?", "answer": "Joseph Stalin"},
    {"question": "I am a renowned artist known for my innovative contributions to modern art. Who am I?", "answer": "Pablo Picasso"},
    {"question": "I am a famous scientist known for my contributions to the theory of relativity. Who am I?", "answer": "Albert Einstein"},
    {"question": "I am a prominent leader known for my efforts in the anti-colonial movement in India. Who am I?", "answer": "Jawaharlal Nehru"},
    {"question": "I am a historical figure known for my impact on modern economics. Who am I?", "answer": "John Maynard Keynes"},
    {"question": "I am a legendary figure known for my adventures and quests in Greek mythology. Who am I?", "answer": "Odysseus"},
    {"question": "I am a famous composer known for my contributions to classical music. Who am I?", "answer": "Johann Sebastian Bach"},
    {"question": "I am a prominent figure in the civil rights movement known for my leadership and speeches. Who am I?", "answer": "Martin Luther King Jr."},
    {"question": "I am a historical figure known for my work in the field of environmental conservation. Who am I?", "answer": "John Muir"},
    {"question": "I am a famous author known for my novels about social issues in America. Who am I?", "answer": "Mark Twain"},
    {"question": "I am a historical figure known for my role in the founding of the American Red Cross. Who am I?", "answer": "Clara Barton"},
    {"question": "I am a legendary leader known for my military conquests and empire building. Who am I?", "answer": "Alexander the Great"},
    {"question": "I am a famous artist known for my large-scale installations and contemporary art. Who am I?", "answer": "Damien Hirst"},
    {"question": "I am a famous scientist known for my theory of general relativity. Who am I?", "answer": "Albert Einstein"},
    {"question": "I am a historical figure known for my leadership in the American Revolutionary War. Who am I?", "answer": "George Washington"},
    {"question": "I am a prominent author known for my novels that explore themes of race and identity. Who am I?", "answer": "James Baldwin"},
    {"question": "I am a famous philosopher known for my contributions to utilitarianism. Who am I?", "answer": "Jeremy Bentham"},
    {"question": "I am a legendary figure known for my tragic love story with a princess. Who am I?", "answer": "Romeo"},
    {"question": "I am a renowned scientist known for my contributions to the study of radioactivity. Who am I?", "answer": "Marie Curie"},
    {"question": "I am a famous leader known for my role in the African independence movement. Who am I?", "answer": "Kwame Nkrumah"},
    {"question": "I am a historical figure known for my impact on the civil rights movement in South Africa. Who am I?", "answer": "Nelson Mandela"},
    {"question": "I am a prominent writer known for my works in postcolonial literature. Who am I?", "answer": "Chinua Achebe"},
    {"question": "I am a famous artist known for my mural paintings in public spaces. Who am I?", "answer": "Diego Rivera"},
    {"question": "I am a historical figure known for my leadership in the Indian independence movement against British rule. Who am I?", "answer": "Mahatma Gandhi"},
    {"question": "I am a prominent thinker known for my critique of capitalism and class struggle. Who am I?", "answer": "Karl Marx"},
    {"question": "I am a famous actor known for my role in 'The Silence of the Lambs'. Who am I?", "answer": "Anthony Hopkins"},
    {"question": "I am a renowned scientist known for my work in the field of genetics and heredity. Who am I?", "answer": "Gregor Mendel"},
    {"question": "I am a famous writer known for my poetry that explores themes of love and nature. Who am I?", "answer": "Robert Frost"},
    {"question": "I am a historical figure known for my contributions to the founding of the United States and the Constitution. Who am I?", "answer": "James Madison"},
    {"question": "I am a legendary figure known for my cunning and resourcefulness in Greek mythology. Who am I?", "answer": "Odysseus"},
    {"question": "I am a famous composer known for my operas and symphonic works. Who am I?", "answer": "Giuseppe Verdi"},
    {"question": "I am a prominent scientist known for my theories about black holes. Who am I?", "answer": "Stephen Hawking"},
    {"question": "I am a famous playwright known for my contributions to American theater in the 20th century. Who am I?", "answer": "Eugene O'Neill"},
    {"question": "I am a historical figure known for my pioneering work in the field of nursing. Who am I?", "answer": "Florence Nightingale"},
    {"question": "I am a legendary hero known for my strength and bravery in battles. Who am I?", "answer": "Hercules"},
    {"question": "I am a famous artist known for my innovative use of color and form. Who am I?", "answer": "Vincent van Gogh"},
    {"question": "I am a prominent political leader known for my efforts in peace negotiations in the Middle East. Who am I?", "answer": "Yitzhak Rabin"},
    {"question": "I am a historical figure known for my role in the civil rights movement and advocacy for nonviolent protest. Who am I?", "answer": "Martin Luther King Jr."},
    {"question": "I am a famous scientist known for my discovery of the laws of motion and universal gravitation. Who am I?", "answer": "Isaac Newton"},
    {"question": "I am a renowned author known for my novels about the American South and its social issues. Who am I?", "answer": "Harper Lee"},
    {"question": "I am a historical figure known for my work in promoting democracy and human rights. Who am I?", "answer": "Eleanor Roosevelt"},
    {"question": "I am a famous artist known for my abstract paintings and geometric shapes. Who am I?", "answer": "Piet Mondrian"},
    {"question": "I am a prominent leader known for my role in the fight against apartheid in South Africa. Who am I?", "answer": "Nelson Mandela"},
    {"question": "I am a historical figure known for my influence on modern philosophy and political theory. Who am I?", "answer": "John Locke"},
    {"question": "I am a famous musician known for my contributions to rock music and my charismatic stage presence. Who am I?", "answer": "Freddie Mercury"},
    {"question": "I am a renowned author known for my explorations of the human psyche and existential themes. Who am I?", "answer": "Franz Kafka"},
    {"question": "I am a famous scientist known for my contributions to the field of thermodynamics. Who am I?", "answer": "Ludwig Boltzmann"},
    {"question": "I am a historical figure known for my role in the founding of the Soviet Union and communism. Who am I?", "answer": "Vladimir Lenin"},
    {"question": "I am a prominent author known for my social criticism and exploration of gender issues. Who am I?", "answer": "Virginia Woolf"},
    {"question": "I am a legendary figure in literature known for my adventures and quests in ancient mythology. Who am I?", "answer": "Jason"},
    {"question": "I am a famous composer known for my contributions to film music and orchestration. Who am I?", "answer": "John Williams"},
    {"question": "I am a renowned scientist known for my discoveries in the field of microbiology and vaccination. Who am I?", "answer": "Louis Pasteur"},
    {"question": "I am a famous playwright known for my works that challenge social norms and conventions. Who am I?", "answer": "Henrik Ibsen"},
    {"question": "I am a historical figure known for my role in the American Civil War and the Emancipation Proclamation. Who am I?", "answer": "Abraham Lincoln"},
    {"question": "I am a prominent figure in the realm of philosophy known for my ideas about the social contract. Who am I?", "answer": "Thomas Hobbes"},
    {"question": "I am a famous musician known for my pioneering work in blues and rock and roll. Who am I?", "answer": "Chuck Berry"},
    {"question": "I am a legendary figure known for my literary contributions and influence on the modern novel. Who am I?", "answer": "James Joyce"},
    {"question": "I am a prominent scientist known for my work in the field of evolutionary biology. Who am I?", "answer": "Stephen Jay Gould"},
    {"question": "I am a famous artist known for my contributions to surrealism and dream imagery. Who am I?", "answer": "Salvador Dalí"},
    {"question": "I am a historical figure known for my contributions to the development of modern physics. Who am I?", "answer": "Niels Bohr"},
    {"question": "I am a prominent leader known for my efforts in humanitarian work and social justice. Who am I?", "answer": "Malala Yousafzai"},
    {"question": "I am a famous philosopher known for my work in ethics and moral philosophy. Who am I?", "answer": "Aristotle"},
    {"question": "I am a renowned author known for my works on dystopian futures and societal critique. Who am I?", "answer": "George Orwell"},
    {"question": "I am a legendary artist known for my colorful and emotional paintings. Who am I?", "answer": "Vincent van Gogh"},
    {"question": "I am a famous scientist known for my contributions to the theory of electromagnetism. Who am I?", "answer": "James Clerk Maxwell"},
    {"question": "I am a historical figure known for my leadership in the women's suffrage movement. Who am I?", "answer": "Susan B. Anthony"},
    {"question": "I am a prominent thinker known for my contributions to the field of psychology. Who am I?", "answer": "Sigmund Freud"},
    {"question": "I am a famous author known for my writings on social and political issues in America. Who am I?", "answer": "Upton Sinclair"},
    {"question": "I am a legendary figure known for my bravery and heroism in ancient Greece. Who am I?", "answer": "Achilles"},
    {"question": "I am a prominent leader known for my advocacy for social justice and equality. Who am I?", "answer": "Angela Davis"},
    {"question": "I am a famous composer known for my innovative symphonies and musical compositions. Who am I?", "answer": "Gustav Mahler"},
    {"question": "I am a historical figure known for my role in the establishment of modern Italy. Who am I?", "answer": "Giuseppe Garibaldi"}
]

current_games = {}

# Function to check if an answer is correct
def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer.strip().lower() == correct_answer.strip().lower()

@app.on_message(filters.command("play"))
async def play_game(client: Client, message: Message):
    chat_id = message.chat.id
    
    # Check if a game is already in progress
    if chat_id in current_games:
        await message.reply_text("🚫 A game is already in progress! Please finish the current game before starting a new one.")
        return

    rules = (
    "🕵️‍♂️ *Who Am I? - Game Overview* 🕵️‍♀️\n\n"
    "Welcome to **Who Am I?**, the thrilling guessing game where wits, speed, and a little bit of mystery come together for an unforgettable experience! Gather your friends, family, or challenge yourself to uncover the identities of some of the most famous figures in history, pop culture, and beyond!\n\n"
    "### 🌟 *Game Overview:*\n"
    "In **Who Am I?**, players will receive clues about a mystery character, and the goal is to guess their identity as quickly as possible. Each player takes turns asking yes-or-no questions while racing against the clock!\n\n"
    "### 🎮 *How to Play:*\n"
    "1. **Choose a Difficulty Level:**\n"
    "   - **Easy**: Familiar characters and figures.\n"
    "   - **Medium**: A mix of well-known and slightly obscure identities.\n"
    "   - **Hard**: Challenging and lesser-known figures that will test your knowledge!\n\n"
    "2. **Select the Number of Questions:**\n"
    "   - Players can agree on a limit (e.g., 10 questions) to make each round exciting and quick-paced.\n\n"
    "3. **Start the Game:**\n"
    "   - One player thinks of a character, and the others take turns asking questions.\n"
    "   - Each question must be answered with a simple “Yes” or “No.”\n\n"
    "4. **Time Limit:**\n"
    "   - Players have **30 seconds** to answer each question. Quick thinking and sharp questioning tactics will help you win!\n\n"
    "5. **Winning the Game:**\n"
    "   - The player who correctly guesses the most identities wins! Keep track of the scores for a competitive edge!\n\n"
    "### 📜 *Game Rules:*\n"
    "- Only yes-or-no questions are allowed to narrow down options effectively.\n"
    "- Players must stick to the character limits of the chosen difficulty level.\n"
    "- If time runs out before a question is answered, that round will end, and players can move on to the next character.\n"
    "- Players can decide on a maximum number of rounds to keep the game exciting!\n"
    "- Have fun and encourage others! It's all about enjoyment and testing your knowledge!\n\n"
    "### 🎉 *Why Play Who Am I?:*\n"
    "- **Enhances Knowledge**: Discover new personalities and historical figures.\n"
    "- **Sharpens Quick Thinking**: The time limit pushes players to think on their feet.\n"
    "- **Fun for Everyone**: Suitable for players of all ages and interests.\n"
    "- **Flexible Gameplay**: Perfect for parties, family gatherings, or just a fun night in!\n\n"
    "### 🚀 *Get Ready to Unmask the Mystery!*\n"
    "Let’s kick off this exciting adventure and see who will emerge as the ultimate identity detective! Are you ready to find out **Who Am I?** Gather your crew, choose your difficulty, and let the guessing games begin! Happy playing! 🕵️‍♂️🔍🎉"
)
    
    # Show difficulty level buttons
    keyboard = [
        [InlineKeyboardButton("😇Easy", callback_data="difficulty_easy")],
        [InlineKeyboardButton("😵Medium", callback_data="difficulty_medium")],
        [InlineKeyboardButton("☠️Hard", callback_data="difficulty_hard")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text(rules, reply_markup=reply_markup)

# Callback for difficulty selection
@app.on_callback_query(filters.regex("difficulty_"))
async def select_difficulty(client: Client, callback_query: CallbackQuery):
    difficulty = callback_query.data.split("_")[1]  # Get difficulty level from callback data
    
    # Ask for number of questions
    keyboard = [
        [InlineKeyboardButton("20 Questions", callback_data=f"{difficulty}_20")],
        [InlineKeyboardButton("30 Questions", callback_data=f"{difficulty}_30")],
        [InlineKeyboardButton("50 Questions", callback_data=f"{difficulty}_50")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await callback_query.edit_message_text(f"🌟 **Exciting Challenge Awaits!** 🌟\n\nYou’ve selected the *{difficulty.capitalize()}* mode! Are you ready to put your knowledge to the test? 🤔✨\n\n Now, take your pick on how many questions you'd like to tackle! 📚💡\n\n**🔄 Choose your number of questions below**", reply_markup=reply_markup)

# Start the game after selecting the number of questions
@app.on_callback_query(filters.regex("(easy|medium|hard)_"))
async def start_game(client: Client, callback_query: CallbackQuery):
    data = callback_query.data.split("_")
    difficulty = data[0]
    num_questions = int(data[1])

    # Select the question set based on difficulty
    if difficulty == "easy":
        questions = random.sample(questions_easy, num_questions)
    elif difficulty == "medium":
        questions = random.sample(questions_medium, num_questions)
    else:
        questions = random.sample(questions_hard, num_questions)

    # Initialize scores and game state
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    current_games[chat_id] = {
        "questions": questions,
        "current_question": 0,
        "scores": {user_id: 0},
        "answer_received": False,
        "timer_task": None
    }

    # Ask the first question
    await ask_question(client, chat_id)

async def ask_question(client, chat_id):
    game = current_games[chat_id]
    question = game["questions"][game["current_question"]]
    
    # Eye-catching question format
    await client.send_message(
        chat_id, 
        f"🎉 *Question {game['current_question'] + 1}/{len(game['questions'])}:*\n\n"
        f"🔍 {question['question']} \n\n"
        "⏳ You have *30 seconds* to answer! 🕰️"
    )
    # Start a timer for 30 seconds
    game["answer_received"] = False  # Reset answer received status

    # Cancel any previous timer task
    if game["timer_task"]:
        game["timer_task"].cancel()

    # Start a new timer task
    game["timer_task"] = asyncio.create_task(start_timer(client, chat_id, 30))

async def start_timer(client, chat_id, duration):
    game = current_games[chat_id]

    try:
        for i in range(10, duration + 1, 10):  # Show timer at 10, 20, and 30 seconds
            await asyncio.sleep(10)

            # Check if an answer was received, if so, stop the timer
            if game["answer_received"]:
                break
            
            await client.send_message(chat_id, f"⏳ {i} seconds have passed, still waiting for your answer!")
        
        # If time runs out without a correct answer, move to the next question
        if not game["answer_received"]:
            await time_up(client, chat_id)
    
    except asyncio.CancelledError:
        # If the task is cancelled (due to correct answer), do nothing
        pass

async def time_up(client, chat_id):
    if chat_id in current_games and not current_games[chat_id]["answer_received"]:
        await client.send_message(chat_id, "⏳ Time's up! Moving to the next question.")
        await move_to_next_question(client, chat_id)

@app.on_message(filters.command("stop"))
async def stop_game(client: Client, message: Message):
    chat_id = message.chat.id
    
    # Check if there's an ongoing game in this chat
    if chat_id in current_games:
        del current_games[chat_id]  # End the game by removing it from the current_games dictionary
        await message.reply_text("🛑 The game has been stopped successfully!")
    else:
        await message.reply_text("⚠️ There's no game currently in progress to stop.")

# Handle user answers
@app.on_message(filters.text)
async def handle_answer(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_id not in current_games:
        return  # Not currently in a game

    game = current_games[chat_id]
    question = game["questions"][game["current_question"]]

    # Check if the answer is correct
    if check_answer(message.text, question['answer']):
        player = message.from_user.username or message.from_user.first_name
        game["scores"][user_id] = game["scores"].get(user_id, 0) + 1
        
        # Mark that an answer has been received
        game["answer_received"] = True

        # Cancel the timer task
        if game["timer_task"]:
            game["timer_task"].cancel()

        # Send an eye-catching congratulatory message
        await message.reply_text(f"🎉🎉 *Correct!* 💯 @{player} got it right . You seem to be smart among all! You've earned a point! 🏆")

        await move_to_next_question(client, chat_id)
    else:
        await message.reply_text("❌ Wrong answer! Keep trying.")

async def move_to_next_question(client, chat_id):
    game = current_games[chat_id]

    # Move to the next question
    game["current_question"] += 1
    if game["current_question"] < len(game["questions"]):
        await ask_question(client, chat_id)
    else:
        await show_leaderboard(client, chat_id, game["scores"])

# Function to display leaderboard
async def show_leaderboard(client: Client, chat_id: int, scores: dict):
    if not scores:
        await client.send_message(chat_id, "No one scored any points this time!")
        return
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    leaderboard = "🏆 *Leaderboard* 🏆\n\n"

    for rank, (user_id, score) in enumerate(sorted_scores, 1):
        user = await client.get_chat(user_id)  # Get user info
        username = f"@{user.username}" if user.username else f"{user.first_name}"
        full_name = user.first_name  # Store first name for later use
        leaderboard += f"*{rank}. {full_name} ({username})* - {score} points\n"
    
    # Tag the winner and congratulate
    winner_id = sorted_scores[0][0]
    winner = await client.get_chat(winner_id)  # Get winner info
    winner_username = f"@{winner.username}" if winner.username else f"{winner.first_name}"
    winner_name = winner.first_name  # Get winner's first name
    leaderboard += f"\n🎉 *Congratulations {winner_name} ({winner_username})! You're the ultimate guesser!* 🎉"

    await client.send_message(chat_id, leaderboard)

    del current_games[chat_id]







if __name__ == "__main__":
    app.run()
