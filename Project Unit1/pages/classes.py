## The TripRecommendation class recommends cafes, restaurants, entertainment, and tourist destinations based on the user's city, budget, and travel type.


class TripRecommendation:
    def cities(self):
# The essential and important function in this class lists all cafes, restaurants, tourist destinations, and entertainment options using dictionaries.
      #Riyadh Recommendations
        city1 = {
            "Riyadh": {
                "High": {
                    "Solo": {
                        "Entertainment": ["Six Flags", "Kan Ya Ma Kan Farm", "Cinema House"],
                        "Tourism": ["KAFD", "Via Riyadh", "Solitaire"],
                        "Restaurants": ["Mayzo", "Nomas", "Benoit"],
                        "cafes": ["Bacha Cofee", "Cafe boulud", "NOOA"]
                    },
                    "Friends": {
                        "Entertainment": ["The Escape Hotel", "Six Flags", "Last Hour"],
                        "Tourism": ["Camel Farm Visit", "KAFD", "Via Riyadh"],
                        "Restaurants": ["Benoit", "Ilbaretto", "Flamingo"],
                        "cafes": ["Sadelle", "Bacha Cofee", "Du Ble"]
                    },
                    "Family": {
                        "Entertainment": ["Six Flags", "Aqurabia", "Buggy Adventure"],
                        "Tourism": ["KAFD", "Via Riyadh", "Solitaire"],
                        "Restaurants": ["L'ami dave", "Cipriani", "Asseb"],
                        "cafes": ["Laduree", "Alain Ducasse", "Sadelle"]
                    }
                },
                "Medium": {
                    "Solo": {
                        "Entertainment": ["FlyingOver", "Day Day Game", "Yalla Hike"],
                        "Tourism": ["Diryah", "Laysen Valley", "Edge of the world"],
                        "Restaurants": ["Alps", "Shogun", "Sando"],
                        "cafes": ["Al bisat ahmadi", "Easy Bakery", "Some"]
                    },
                    "Friends": {
                        "Entertainment": ["Yalla hike", "Otta", "Wonder Garden"],
                        "Tourism": ["Diryah", "The roof", "Bayt Isa"],
                        "Restaurants": ["Jon and vinnys", "The Villa", "Shogun"],
                        "cafes": ["Atmosphere", "MLT", "Al bisat ahmadi"]
                    },
                    "Family": {
                        "Entertainment": ["Wonder graden", "BLVD city", "COOL ARENA"],
                        "Tourism": ["Diryah", "King Khalid Royal reserve", "The roof"],
                        "Restaurants": ["Jon and vinnys", "The cheese cake factory", "Bait Alakaber"],
                        "cafes": ["Atmosphere", "M DEE", "Al bisat ahmadi"]
                    }
                },
                "Low": {
                    "Solo": {
                        "Entertainment": ["Black Gold Museum", "Misk Art Institute", "Sport BLVD"],
                        "Tourism": ["The National Museum", "Al masmak Palace", "King Abdullah Palace"],
                        "Restaurants": ["WBJ", "Sign", "Mama Noura"],
                        "cafes": ["Teller", "Wasf", "Rift"]
                    },
                    "Friends": {
                        "Entertainment": ["COOL ARENA", "Misk Art Institute", "COOL ARENA"],
                        "Tourism": ["Almuaiqlilyah", "Wadi Hanifah", "Al masmak Palace"],
                        "Restaurants": ["WBJ", "Sign", "Mama Noura"],
                        "cafes": ["Teller", "Coffee Adress", "Rift"]
                    },
                    "Family": {
                        "Entertainment": ["Zoo Riyadh", "Amazonia", "COOL ARENA"],
                        "Tourism": ["Almuaiqlilyah", "Wadi Hanifah", "Salam Park"],
                        "Restaurants": ["Abu Alez", "Hdebh", "Houmous house"],
                        "cafes": ["Teller", "Coffee Adress", "Brsk"]
                    }
                }
            }
        }
        #Abha Recommendations
        city2={
                  'Abha':{
                     'High':{
                       'Solo':{
                        'Entertinment':['Abha Airport Park','Terhap','Hiking in Al-Soudah'],
                        'Tourism':['Green Mountain','Al-Soudah Mountain','Fog Walkway'],
                        'Restaurants':['Red Puzzle','Zurna ','Mashraq'],
                              'Cafes':['To Be Gather','Haiz','Gia']
                               
                   },
                   'Friends':{
                         'Entertinment':['Paintball','BattleKart Abha','Hiking in Al-Soudah'],
                        'Tourism':['Abu Sarrah Palaces','Outdoor Games','Al-Miftaha village'],
                         'Restaurants':['The Bond','Joy Venue','The Village'],
                              'Cafes':['Night tea','Suthab','Dukka']
                               
                   },
                   'Family':{
                       'Entertinment':['Zipline / Adventure Experiences','Seven','Rijal Almaa Heritage Village'],
                       'Tourism':['Abu Khayal Park','High City','Al Rashid Mall'],
                       'Restaurants':['Jouri Elite','Royal Tikka','Lantico'],
                              'Cafes':['Hamads place','Palm Court Cafe','Rahaa Cafe']
                               
                   }
                   
               },
             'Medium': {
                   'Solo':{
                       'Entertinment':['BattleKart Abha','Shamsan Castle','Hiking in Al-Soudah'],
                      'Tourism':['Abha Dam Lake','Boating at Abha Dam Lake','Fog Walkway'],
                      'Restaurants':['Olive Garden Abha','Shawarmer ','Al Baik'],
                              'Cafes':['One Sip Coffee','Kaya Cafe','Black By Location']
                               
                   },
                   'Friends':{
                       'Entertinment':['Aryash','Al-Habala Cable Car','Paintball'],
                     'Tourism':['Carnival Activities','Camping in Al-Soudah','Al-Miftaha village'],
                      'Restaurants':['Alkarkand','Farfili Italian Restauran','Maharani'],
                              'Cafes':['Bakar Cafe','Wzab Cafe','Archi Abha']
                               
                   },
                   'Family':{
                       'Entertinment':['Abha Cable Car','Seven','Valley Resort'],
                     'Tourism':['Mogan Park','High City','Abha Airport Park'],
                      'Restaurant':['Namliya','Nights India','Al Sinara'],
                              'Cafes':['Beit Cafe','Violeta Cafe','Lo Cakeery']
                               
                   }
               },
               'Low':{
                    'Solo':{
                       'Entertinment':['Al-Basta Village','Shamsan Castle','Hiking in Al-Soudah'],
                        'Tourism':['Abha Dam Lake','Al-Soudah Mountain','Fog Walkway'],
                         'Restaurants':['Broast Almadina','Burger King ','DO Burger'],
                              'Cafes':['Albustan Coffee','R2 Cafe','Riza Tea']
                               
                   },
                   'Friends':{
                           'Entertinment':['Aryash','Al-Soudah Cable Car','Hiking in Al-Soudah'],
                          'Tourism':['Abu Sarrah Palaces','','Al-Miftaha village'],
                          'Restaurants':['Shax','Benbastek','Tender'],
                              'Cafes':['Daily Cup','Enjoy Cafe','AOKAF Cafe']
                               
                   },
                   'Family':{
                       'Entertinment':['Al Rashid Mall','Seven','Lavanda Park'],
                       'Tourism':['Abu Khayal Park','Lee Premier','Art Street'],
                       'Restaurants':['Al-Adhariya','Du Source','Ansa'],
                              'Cafes':['CULT Cafe','Abha Coffee Land','Lumiera Sweets & Coffee']
                               
                   }
               }
                
            }
        }
#Jeddah Recommendations
        city3 = {
            "Jeddah": {
                "High": {
                    "Solo": {
                        "Entertainment": ["Hayy Jameel", "Craze Activities", "Sian Waterpark"],
                        "Tourism": ["Fakieh Aquarium", "Private Yacht Charter", "Bayadah Island (Bayadah Island Trip)"],
                        "Restaurants": ["Le Petit Chef", "Kuuru", "Shang Palace"],
                        "cafes": ["Aliae", "L'ETO", "Laperouse"]
                    },
                    "Friends": {
                        "Entertainment": ["Cube Challenges", "TeamLab", "Arty cafe"],
                        "Tourism": ["Editon", "Rixos Murjan", "City Walk"],
                        "Restaurants": ["Aliea", "Khalila", "Toscane"],
                        "cafes": ["Solo", "Aque E Salr", "Noto"]
                    },
                    "Family": {
                        "Entertainment": ["TeamLab", "Le Meridien", "The DockX"],
                        "Tourism": ["RedSeaMall", "Fakieh Aquarium", "City Walk"],
                        "Restaurants": ["Manko", "Amar", "Mumoza"],
                        "cafes": ["Bo&min", "ENG", "Paul"]
                    }
                },
                "Medium": {
                    "Solo": {
                        "Entertainment": ["Biennale", "Albalad", "Hayy Jameel"],
                        "Tourism": ["Fakieh Aquarium", "Albalad", "Sian Waterpark"],
                        "Restaurants": ["Steakcut", "Verre pizza", "Alromansiah"],
                        "cafes": ["Saroo", "Ki", "Cup&Couch"]
                    },
                    "Friends": {
                        "Entertainment": ["Water Taxi", "Volt", "The Round"],
                        "Tourism": ["Biennale", "Albalad", "Al Tayebat International City"],
                        "Restaurants": ["Meez", "Mazencito", "Asian Ocean"],
                        "cafes": ["Olev", " NAS", "After Six"]
                    },
                    "Family": {
                        "Entertainment": ["Water Taxi", "Volt", "Tropical Land"],
                        "Tourism": ["Albalad", "Historical District", "Jeddah Jungle"],
                        "Restaurants": ["Chindia Delices", "Meez", "HonaDamascus"],
                        "cafes": ["Mooma", "Urth", "Woods"]
                    }
                },
                "Low": {
                    "Solo": {
                        "Entertainment": ["Seasons Event", "Pearl Beach", "Uwalk"],
                        "Tourism": ["Jeddah Corniche", "Albalad", "Promende"],
                        "Restaurants": ["Albaik", "Wong Solo", "Byblos Xpress"],
                        "cafes": ["Camel Step", "Basic", "Urban"]
                    },
                    "Friends": {
                        "Entertainment": ["Seasons Event", "Fayhaa Park", "Pearl Beach"],
                        "Tourism": ["Yacht Club", "King Fahd Fountain", ""],
                        "Restaurants": ["Must Eatery", "Albaik", "Shawarma Shakir"],
                        "cafes": ["Talent", "Cle", "Brew92"]
                    },
                    "Family": {
                        "Entertainment": ["Seasons Event", "Uwalk", "Corniche Park"],
                        "Tourism": ["Yacht Club", "Albalad", "Promende"],
                        "Restaurants": ["Biryani Gate", "Albaik", "Abo Zaid"],
                        "cafes": ["Eva", "Hemi", "Nishan"]
                    }
                }
            }
        }
        
        city4 = {
          "AlUla": {
             "High": {
               "Solo": {
                "Restaurants": ["Tama", "Harrat", "Saffron"],
                "Cafes": ["Luxury resort", "Banyan tree lounge", "premium dessert experience" ],
                "Entertainment": ["Private desert tour", "Luxury horse riding", "Hot-air balloon" ],
                "Tourism": ["private hegra tour", "private canyon tour", "premium AlUla sightseeing tour"]
            },
            "Friends": {
                "Restaurants": ["Maraya social", "SASS AlUla", "Entercote"],
                "Cafes": ["Maraya lounge", "luxury hotel aftrnoon tea", "high-end dessert experience"],
                "Entertainment": ["Private buggy", "private stargazing", "private desert safari"],
                "Tourism": ["private hegra tour", "private Dandan & Jabal Ikmah tour", "Luxury desert tour"]
            },
            "Family": {
                "Restaurants": ["Banyan tree harrat", "Saffron", "Somewhere"],
                "Cafes": ["Banyan tree cafe", "off-road cafe", "Tomoor"],
                "Entertainment": ["Private desert safari", "private air-balloon", "private horse riding"],
                "Tourism": ["private hegra tour", "private AlUla oasis experience", "Luxury sightseeing tour"]
            }
        },

        "Medium": {
            "Solo": {
                "Restaurants": ["Somewhere", "Joontos", "Circolo"],
                "Cafes": ["Archi", "Kabatilo", "Specialty coffee"],
                "Entertainment": ["Hegra guided tour", "Maraya tour", "Tethered hot-air balloon"],
                "Tourism": ["Oasis heritage trail", "Dadan", "Jabal Ikmah"]
            },
            "Friends": {
                "Restaurants": ["Entercote", "Suhail", "somewhere"],
                "Cafes": ["Groovy", "Minzal", "Old town cafe"],
                "Entertainment": ["Gharameel stargazing", "AlUla adventure hub", "Hegra hop-on hop-off"],
                "Tourism": ["Hegra", "Maraya","AlUla old town guided tour"]
            },
            "Family": {
                "Restaurants": ["Tofareya", "Tama", "Saudi heritage"],
                "Cafes": ["dessert cafe", "Oasis", "Aljadidah"],
                "Entertainment": ["Hegra experience", "Adventure activity", "stargazing"],
                "Tourism": ["AlUla oasis", "Dandan & Jabal Ikmah", "Maraya"]
            }
        },

        "Low": {
            "Solo": {
                "Restaurants": ["Freshhouse", "local shawarma", "Heritage food stalls"],
                "Cafes": ["Hinat", "Nabat", "Special cup"],
                "Entertainment": ["AlUla park", "old town walks", "Hot-air balloon glow show"],
                "Tourism": ["Elephant rock", "Harrat viewpoint", "AlUla oasis"]
            },
            "Friends": {
                "Restaurants": ["Tofareya", "Local food trucks", "AlUla heritage"],
                "Cafes": ["70s cafe", "Groovy","Minzal"],
                "Entertainment": ["Outdoor picnic","Old town streets", "Aljadidah evening activities"],
                "Tourism": ["old down market","Art district", "Walls of art"]
            },
            "Family": {
                "Restaurants": ["AlUla heritage", "AlUla palace", "Underrated"],
                "Cafes": ["Shalal cafe", "Pink camel","Ghson"],
                "Entertainment": ["Family picnic", "AlUla park", "AlUla heritage walk"],
                "Tourism": ["Fort area", "Tantora", "Art district"]
            }
        }
    }
}




        #return dictonries
        return city1,city2,city3,city4

#The TripPreferences class inherits from the TripRecommendation class to provide more flexibility 
#and scalability when accessing the cities. The relationship between them depends on the user's preferences. 
#This is the main recommendation feature of Rihlati.


class TripPrefrences(TripRecommendation):

  #attributes : by using list ..

    def __init__(self, city, budget, travel_type):

        # Save user's choices
        self.city = city
        self.budget = budget
        self.travel_type = travel_type

    def check_choses(self):

        city1, city2, city3, city4 = super().cities()

        # Select city
        if self.city == "Riyadh":
            result1 = city1

        elif self.city == "Abha":
            result1 = city2

        elif self.city == "Jeddah":
            result1 = city3

        elif self.city == "AlUla":
            result1 = city4

        else:
            return {}

        # Select budget
        result2 = result1[self.city][self.budget]

        # Select travel type
        result3 = result2[self.travel_type]

        # Return the recommendations to Streamlit
        return result3

#Asking the user:

#city_chose = input("Where do you want to go? ")
#budget_chose = input("What is your budget? ")
#travelType_chose = input("Who are you going with? ")
#create an object:
#trip = TripPrefrences(city_chose, budget_chose, travelType_chose)
#calling check_method :
#trip.check_choses(city_chose, budget_chose, travelType_chose)