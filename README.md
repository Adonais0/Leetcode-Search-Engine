# 507FinalProject

Data Source:
--------------------------------------
  1.Firstly, I will crawl all the decks of each hero from http://www.hearthstonetopdecks.com/deck-category/deck-class/  and add hero to this baseurl. for example, like http://www.hearthstonetopdecks.com/deck-category/deck-class/druid/ For this page, there are all the decks that could be used by this hero, and there is a score number beside each deck name to show where this deck is popular.<br>
  2.Then I will rank them to find top 10 favorite decks of each hero. And crawl each specific deck composition and get each card’s name and kind of the card(classic or neutral),, for example, like http://www.hearthstonetopdecks.com/decks/zarathustras-cthun-spiteful-druid/<br>
  3.After that I will crawl each card of the deck to get more information. For example, I will crawl http://www.hearthstonetopdecks.com/cards/enchanted-raven/ this druid’s card to get the mana cost of it, attack value and health value and etc.<br>
<br>
  Data source challenge score:<br>
  I will crawling [and scraping] multiple pages in a site you haven’t used before(As I describe above). So the total challenge score is 8.<br>

Any other information needed to run the program:
--------------------------------------
  1.Using flask virtual environment<br>
  2.Install all packages in the requirements<br>

Structure:
--------------------------------------
  My codes are divided into five parts, GetData.py, Database.py, DataProcessing.py, Test.py and DataPresentation.py.<br>
<br>
  GetData.py includes are used to crawl data from http://www.hearthstonetopdecks.com/ ,there are three main functions :<br>
    get_hero_data: to get decks of hero<br>
    get_top_10_deck_component: to get compositions of one deck<br>
    get_card_information: to gets all cards card_information<br>
<br>
  Database.py is used to get the cached data and put them into database, there are four main functions :<br>
    create_db: to create hearthstone.db<br>
    insert_cards: get the cached data of cards and put them into database<br>
    insert_decks: get the cached data of decks and put them into database<br>
    insert_heros: get list of hero and put them into database<br>
    insert_compositions: get the cached data of compositions and put them into database<br>
<br>
  DataProcessing.py is used to get data from database and prepare for the DataPresentation, there are four main functions:<br>
    process_top_10_decks:get the top 10 deck from database<br>
    process_crystal_usage:get the crystal usage of class and neutral of a deck<br>
    process_attack_or_health_usage:get the attack and health information of a deck<br>
    process_race_composition:get the composition of a deck<br>
<br>
  Test.py is a unittest file, there are three main test classes:<br>
    TestStoreData:used to test stored information in Database<br>
    TestProcessData: used to test all functions in DataProcessing works well.<br>
    TestGetData: to test whether GetData.py can get data from website.<br>
<br>
  DataPresentation.py is a presentation file, there are four functions insides it:<br>
    index: used to handle the index page, user can choose one of the heros<br>
    hero: used to show the barchart of the top 10 deck and its score of the hero<br>
    deck: used to show crystal_usage, attack_health and composition of the deck<br>
    getchart: used to get correct chart from plotly<br>

Brief Guide:
--------------------------------------
  1.first input "source finalproj/bin/activate" in command line to activate the virtual environment.<br>
  2.install all required files that requirements.txt, for example plotly<br>
  2.run DataPresentation.py as "python DataPresentation.py" in command line<br>
  3.Open "http://127.0.0.1:5000/" the localhost page and to choose what page you want to go<br>
