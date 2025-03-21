#!/usr/bin/env python
# coding: utf-8

import time
import pandas as pd
import csv as csv
import datetime
import random

class NameDataValues:
    def getFirstNames(self):
        return ["Aaron", "Abby", "Abigail", "Adam",
                  "Alan", "Albert", "Alex", "Alexandra", "Alexis", "Alice", "Alicia",
                  "Alisha", "Alissa", "Allen", "Allison", "Alyssa", "Amanda",
                  "Amber", "Amy", "Andrea", "Andrew", "Andy", "Angel", "Angela",
                  "Angie", "Anita", "Ann", "Anna", "Annette", "Anthony", "Antonio",
                  "April", "Arthur", "Ashley", "Audrey", "Austin", "Autumn", "Baby",
                  "Barb", "Barbara", "Becky", "Benjamin", "Beth", "Bethany", "Betty",
                  "Beverly", "Bill", "Billie", "Billy", "Blake", "Bob", "Bobbie",
                  "Bobby", "Bonnie", "Brad", "Bradley", "Brady", "Brandi", "Brandon",
                  "Brandy", "Breanna", "Brenda", "Brent", "Brett", "Brian",
                  "Brianna", "Brittany", "Brooke", "Brooklyn", "Bruce", "Bryan",
                  "Caleb", "Cameron", "Candy", "Carl", "Carla", "Carmen", "Carol",
                  "Carolyn", "Carrie", "Casey", "Cassandra", "Catherine", "Cathy",
                  "Chad", "Charlene", "Charles", "Charlie", "Charlotte", "Chase",
                  "Chasity", "Chastity", "Chelsea", "Cheryl", "Chester", "Cheyenne",
                  "Chris", "Christian", "Christina", "Christine", "Christoph",
                  "Christopher", "Christy", "Chuck", "Cindy", "Clara", "Clarence",
                  "Clayton", "Clifford", "Clint", "Cody", "Colton", "Connie",
                  "Corey", "Cory", "Courtney", "Craig", "Crystal", "Curtis",
                  "Cynthia", "Dakota", "Dale", "Dallas", "Dalton", "Dan", "Dana",
                  "Daniel", "Danielle", "Danny", "Darla", "Darlene", "Darrell",
                  "Darren", "Dave", "David", "Dawn", "Dean", "Deanna", "Debbie",
                  "Deborah", "Debra", "Denise", "Dennis", "Derek", "Derrick",
                  "Destiny", "Devin", "Diana", "Diane", "Dillon", "Dixie", "Dominic",
                  "Don", "Donald", "Donna", "Donnie", "Doris", "Dorothy", "Doug",
                  "Douglas", "Drew", "Duane", "Dustin", "Dusty", "Dylan", "Earl",
                  "Ed", "Eddie", "Edward", "Elaine", "Elizabeth", "Ellen", "Emily",
                  "Eric", "Erica", "Erika", "Erin", "Ernest", "Ethan", "Eugene",
                  "Eva", "Evelyn", "Everett", "Faith", "Father", "Felicia", "Floyd",
                  "Francis", "Frank", "Fred", "Gabriel", "Gage", "Gail", "Gary",
                  "Gene", "George", "Gerald", "Gina", "Ginger", "Glen", "Glenn",
                  "Gloria", "Grace", "Greg", "Gregory", "Haley", "Hannah", "Harley",
                  "Harold", "Harry", "Heath", "Heather", "Heidi", "Helen", "Herbert",
                  "Holly", "Hope", "Howard", "Hunter", "Ian", "Isaac", "Jack",
                  "Jackie", "Jacob", "Jade", "Jake", "James", "Jamie", "Jan", "Jane",
                  "Janet", "Janice", "Jared", "Jasmine", "Jason", "Jay", "Jean",
                  "Jeannie", "Jeff", "Jeffery", "Jeffrey", "Jenna", "Jennifer",
                  "Jenny", "Jeremiah", "Jeremy", "Jerry", "Jesse", "Jessica",
                  "Jessie", "Jill", "Jim", "Jimmy", "Joann", "Joanne", "Jodi",
                  "Jody", "Joe", "Joel", "Joey", "John", "Johnathan", "Johnny",
                  "Jon", "Jonathan", "Jonathon", "Jordan", "Joseph", "Josh",
                  "Joshua", "Joyce", "Juanita", "Judy", "Julia", "Julie", "Justin",
                  "Kaitlyn", "Karen", "Katelyn", "Katherine", "Kathleen", "Kathryn",
                  "Kathy", "Katie", "Katrina", "Kay", "Kayla", "Kaylee", "Keith",
                  "Kelly", "Kelsey", "Ken", "Kendra", "Kenneth", "Kenny", "Kevin",
                  "Kim", "Kimberly", "Kris", "Krista", "Kristen", "Kristin",
                  "Kristina", "Kristy", "Kyle", "Kylie", "Lacey", "Laken", "Lance",
                  "Larry", "Laura", "Lawrence", "Leah", "Lee", "Leonard", "Leroy",
                  "Leslie", "Levi", "Lewis", "Linda", "Lindsay", "Lindsey", "Lisa",
                  "Lloyd", "Logan", "Lois", "Loretta", "Lori", "Louis", "Lynn",
                  "Madison", "Mandy", "Marcus", "Margaret", "Maria", "Mariah",
                  "Marie", "Marilyn", "Marion", "Mark", "Marlene", "Marsha",
                  "Martha", "Martin", "Marty", "Marvin", "Mary", "Mary ann", "Mason",
                  "Matt", "Matthew", "Max", "Megan", "Melanie", "Melinda", "Melissa",
                  "Melody", "Michael", "Michelle", "Mickey", "Mike", "Mindy",
                  "Miranda", "Misty", "Mitchell", "Molly", "Monica", "Morgan",
                  "Mother", "Myron", "Nancy", "Natasha", "Nathan", "Nicholas",
                  "Nick", "Nicole", "Nina", "Noah", "Norma", "Norman", "Olivia",
                  "Paige", "Pam", "Pamela", "Pat", "Patricia", "Patrick", "Patty",
                  "Paul", "Paula", "Peggy", "Penny", "Pete", "Phillip", "Phyllis",
                  "Rachael", "Rachel", "Ralph", "Randall", "Randi", "Randy", "Ray",
                  "Raymond", "Rebecca", "Regina", "Renee", "Rex", "Rhonda",
                  "Richard", "Rick", "Ricky", "Rita", "Rob", "Robbie", "Robert",
                  "Roberta", "Robin", "Rochelle", "Rocky", "Rod", "Rodney", "Roger",
                  "Ron", "Ronald", "Ronda", "Ronnie", "Rose", "Roxanne", "Roy",
                  "Russ", "Russell", "Rusty", "Ruth", "Ryan", "Sabrina", "Sally",
                  "Sam", "Samantha", "Samuel", "Sandra", "Sandy", "Sara", "Sarah",
                  "Savannah", "Scott", "Sean", "Seth", "Shanda", "Shane", "Shanna",
                  "Shannon", "Sharon", "Shaun", "Shawn", "Shawna", "Sheila",
                  "Shelly", "Sher", "Sherri", "Sherry", "Shirley", "Sierra",
                  "Skyler", "Stacey", "Stacy", "Stanley", "Stephanie", "Stephen",
                  "Steve", "Steven", "Sue", "Summer", "Susan", "Sydney", "Tabatha",
                  "Tabitha", "Tamara", "Tammy", "Tara", "Tasha", "Tashia", "Taylor",
                  "Ted", "Teresa", "Terri", "Terry", "Tessa", "Thelma", "Theresa",
                  "Thomas", "Tia", "Tiffany", "Tim", "Timmy", "Timothy", "Tina",
                  "Todd", "Tom", "Tommy", "Toni", "Tony", "Tonya", "Tracey",
                  "Tracie", "Tracy", "Travis", "Trent", "Trevor", "Trey", "Trisha",
                  "Tristan", "Troy", "Tyler", "Tyrone", "Unborn", "Valerie",
                  "Vanessa", "Vernon", "Veronica", "Vicki", "Vickie", "Vicky",
                  "Victor", "Victoria", "Vincent", "Virginia", "Vivian", "Walter",
                  "Wanda", "Wayne", "Wendy", "Wesley", "Whitney", "William",
                  "Willie", "Wyatt", "Zachary"]

    def getLastNames(self):
        return ["Abbott", "Acevedo", "Acosta",
                 "Adams", "Adkins", "Aguilar", "Aguirre", "Albert", "Alexander",
                 "Alford", "Allen", "Allison", "Alston", "Alvarado", "Alvarez",
                 "Anderson", "Andrews", "Anthony", "Armstrong", "Arnold", "Ashley",
                 "Atkins", "Atkinson", "Austin", "Avery", "Avila", "Ayala", "Ayers",
                 "Bailey", "Baird", "Baker", "Baldwin", "Ball", "Ballard", "Banks",
                 "Barber", "Smith", "Johnson", "Williams", "Jones", "Brown",
                 "Davis", "Miller", "Wilson", "Moore", "Taylor", "Thomas",
                 "Jackson", "Barker", "Barlow", "Barnes", "Barnett", "Barr",
                 "Barrera", "Barrett", "Barron", "Barry", "Bartlett", "Barton",
                 "Bass", "Bates", "Battle", "Bauer", "Baxter", "Beach", "Bean",
                 "Beard", "Beasley", "Beck", "Becker", "Bell", "Bender", "Benjamin",
                 "Bennett", "Benson", "Bentley", "Benton", "Berg", "Berger",
                 "Bernard", "Berry", "Best", "Bird", "Bishop", "Black", "Blackburn",
                 "Blackwell", "Blair", "Blake", "Blanchard", "Blankenship",
                 "Blevins", "Bolton", "Bond", "Bonner", "Booker", "Boone", "Booth",
                 "Bowen", "Bowers", "Bowman", "Boyd", "Boyer", "Boyle", "Bradford",
                 "Bradley", "Bradshaw", "Brady", "Branch", "Bray", "Brennan",
                 "Brewer", "Bridges", "Briggs", "Bright", "Britt", "Brock",
                 "Brooks", "Browning", "Bruce", "Bryan", "Bryant", "Buchanan",
                 "Buck", "Buckley", "Buckner", "Bullock", "Burch", "Burgess",
                 "Burke", "Burks", "Burnett", "Burns", "Burris", "Burt", "Burton",
                 "Bush", "Butler", "Byers", "Byrd", "Cabrera", "Cain", "Calderon",
                 "Caldwell", "Calhoun", "Callahan", "Camacho", "Cameron",
                 "Campbell", "Campos", "Cannon", "Cantrell", "Cantu", "Cardenas",
                 "Carey", "Carlson", "Carney", "Carpenter", "Carr", "Carrillo",
                 "Carroll", "Carson", "Carter", "Carver", "Case", "Casey", "Cash",
                 "Castaneda", "Castillo", "Castro", "Cervantes", "Chambers", "Chan",
                 "Chandler", "Chaney", "Chang", "Chapman", "Charles", "Chase",
                 "Chavez", "Chen", "Cherry", "Christensen", "Christian", "Church",
                 "Clark", "Clarke", "Clay", "Clayton", "Clements", "Clemons",
                 "Cleveland", "Cline", "Cobb", "Cochran", "Coffey", "Cohen", "Cole",
                 "Coleman", "Collier", "Collins", "Colon", "Combs", "Compton",
                 "Conley", "Conner", "Conrad", "Contreras", "Conway", "Cook",
                 "Cooke", "Cooley", "Cooper", "Copeland", "Cortez", "Cote",
                 "Cotton", "Cox", "Craft", "Craig", "Crane", "Crawford", "Crosby",
                 "Cross", "Cruz", "Cummings", "Cunningham", "Curry", "Curtis",
                 "Dale", "Dalton", "Daniel", "Daniels", "Daugherty", "Davenport",
                 "David", "Davidson", "Dawson", "Day", "Dean", "Decker", "Dejesus",
                 "Delacruz", "Delaney", "Deleon", "Delgado", "Dennis", "Diaz",
                 "Dickerson", "Dickinson", "Dillard", "Dillon", "Dixon", "Dodson",
                 "Dominguez", "Donaldson", "Donovan", "Dorsey", "Dotson", "Douglas",
                 "Downs", "Doyle", "Drake", "Dudley", "Duffy", "Duke", "Duncan",
                 "Dunlap", "Dunn", "Duran", "Durham", "Dyer", "Eaton", "Edwards",
                 "Elliott", "Ellis", "Ellison", "Emerson", "England", "English",
                 "Erickson", "Espinoza", "Estes", "Estrada", "Evans", "Everett",
                 "Ewing", "Farley", "Farmer", "Farrell", "Faulkner", "Ferguson",
                 "Fernandez", "Ferrell", "Fields", "Figueroa", "Finch", "Finley",
                 "Fischer", "Fisher", "Fitzgerald", "Fitzpatrick", "Fleming",
                 "Fletcher", "Flores", "Flowers", "Floyd", "Flynn", "Foley",
                 "Forbes", "Ford", "Foreman", "Foster", "Fowler", "Fox", "Francis",
                 "Franco", "Frank", "Franklin", "Franks", "Frazier", "Frederick",
                 "Freeman", "French", "Frost", "Fry", "Frye", "Fuentes", "Fuller",
                 "Fulton", "Gaines", "Gallagher", "Gallegos", "Galloway", "Gamble",
                 "Garcia", "Gardner", "Garner", "Garrett", "Garrison", "Garza",
                 "Gates", "Gay", "Gentry", "George", "Gibbs", "Gibson", "Gilbert",
                 "Giles", "Gill", "Gillespie", "Gilliam", "Gilmore", "Glass",
                 "Glenn", "Glover", "Goff", "Golden", "Gomez", "Gonzales",
                 "Gonzalez", "Good", "Goodman", "Goodwin", "Gordon", "Gould",
                 "Graham", "Grant", "Graves", "Gray", "Green", "Greene", "Greer",
                 "Gregory", "Griffin", "Griffith", "Grimes", "Gross", "Guerra",
                 "Guerrero", "Guthrie", "Gutierrez", "Guy", "Guzman", "Hahn",
                 "Hale", "Haley", "Hall", "Hamilton", "Hammond", "Hampton",
                 "Hancock", "Haney", "Hansen", "Hanson", "Hardin", "Harding",
                 "Hardy", "Harmon", "Harper", "Harris", "Harrington", "Harrison",
                 "Hart", "Hartman", "Harvey", "Hatfield", "Hawkins", "Hayden",
                 "Hayes", "Haynes", "Hays", "Head", "Heath", "Hebert", "Henderson",
                 "Hendricks", "Hendrix", "Henry", "Hensley", "Henson", "Herman",
                 "Hernandez", "Herrera", "Herring", "Hess", "Hester", "Hewitt",
                 "Hickman", "Hicks", "Higgins", "Hill", "Hines", "Hinton", "Hobbs",
                 "Hodge", "Hodges", "Hoffman", "Hogan", "Holcomb", "Holden",
                 "Holder", "Holland", "Holloway", "Holman", "Holmes", "Holt",
                 "Hood", "Hooper", "Hoover", "Hopkins", "Hopper", "Horn", "Horne",
                 "Horton", "House", "Houston", "Howard", "Howe", "Howell",
                 "Hubbard", "Huber", "Hudson", "Huff", "Huffman", "Hughes", "Hull",
                 "Humphrey", "Hunt", "Hunter", "Hurley", "Hurst", "Hutchinson",
                 "Hyde", "Ingram", "Irwin", "Jacobs", "Jacobson", "James", "Jarvis",
                 "Jefferson", "Jenkins", "Jennings", "Jensen", "Jimenez", "Johns",
                 "Johnston", "Jordan", "Joseph", "Joyce", "Joyner", "Juarez",
                 "Justice", "Kane", "Kaufman", "Keith", "Keller", "Kelley", "Kelly",
                 "Kemp", "Kennedy", "Kent", "Kerr", "Key", "Kidd", "Kim", "King",
                 "Kinney", "Kirby", "Kirk", "Kirkland", "Klein", "Kline", "Knapp",
                 "Knight", "Knowles", "Knox", "Koch", "Kramer", "Lamb", "Lambert",
                 "Lancaster", "Landry", "Lane", "Lang", "Langley", "Lara", "Larsen",
                 "Larson", "Lawrence", "Lawson", "Le", "Leach", "Leblanc", "Lee",
                 "Leon", "Leonard", "Lester", "Levine", "Levy", "Lewis", "Lindsay",
                 "Lindsey", "Little", "Livingston", "Lloyd", "Logan", "Long",
                 "Lopez", "Lott", "Love", "Lowe", "Lowery", "Lucas", "Luna",
                 "Lynch", "Lynn", "Lyons", "Macdonald", "Macias", "Mack", "Madden",
                 "Maddox", "Maldonado", "Malone", "Mann", "Manning", "Marks",
                 "Marquez", "Marsh", "Marshall", "Martin", "Martinez", "Mason",
                 "Massey", "Mathews", "Mathis", "Matthews", "Maxwell", "May",
                 "Mayer", "Maynard", "Mayo", "Mays", "McBride", "McCall",
                 "McCarthy", "McCarty", "McClain", "McClure", "McConnell",
                 "McCormick", "McCoy", "McCray", "McCullough", "McDaniel",
                 "McDonald", "McDowell", "McFadden", "McFarland", "McGee",
                 "McGowan", "McGuire", "McIntosh", "McIntyre", "McKay", "McKee",
                 "McKenzie", "McKinney", "McKnight", "McLaughlin", "McLean",
                 "McLeod", "McMahon", "McMillan", "McNeil", "McPherson", "Meadows",
                 "Medina", "Mejia", "Melendez", "Melton", "Mendez", "Mendoza",
                 "Mercado", "Mercer", "Merrill", "Merritt", "Meyer", "Meyers",
                 "Michael", "Middleton", "Miles", "Mills", "Miranda", "Mitchell",
                 "Molina", "Monroe", "Montgomery", "Montoya", "Moody", "Moon",
                 "Mooney", "Morales", "Moran", "Moreno", "Morgan", "Morin",
                 "Morris", "Morrison", "Morrow", "Morse", "Morton", "Moses",
                 "Mosley", "Moss", "Mueller", "Mullen", "Mullins", "Munoz",
                 "Murphy", "Murray", "Myers", "Nash", "Navarro", "Neal", "Nelson",
                 "Newman", "Newton", "Nguyen", "Nichols", "Nicholson", "Nielsen",
                 "Nieves", "Nixon", "Noble", "Noel", "Nolan", "Norman", "Norris",
                 "Norton", "Nunez", "Obrien", "Ochoa", "Oconnor", "Odom",
                 "Odonnell", "Oliver", "Olsen", "Olson", "O'neal", "O'neil",
                 "O'neill", "Orr", "Ortega", "Ortiz", "Osborn", "Osborne", "Owen",
                 "Owens", "Pace", "Pacheco", "Padilla", "Page", "Palmer", "Park",
                 "Parker", "Parks", "Parrish", "Parsons", "Pate", "Patel",
                 "Patrick", "Patterson", "Patton", "Paul", "Payne", "Pearson",
                 "Peck", "Pena", "Pennington", "Perez", "Perkins", "Perry",
                 "Peters", "Petersen", "Peterson", "Petty", "Phelps", "Phillips",
                 "Pickett", "Pierce", "Pittman", "Pitts", "Pollard", "Poole",
                 "Pope", "Porter", "Potter", "Potts", "Powell", "Powers", "Pratt",
                 "Preston", "Price", "Prince", "Pruitt", "Puckett", "Pugh", "Quinn",
                 "Ramirez", "Ramos", "Ramsey", "Randall", "Randolph", "Rasmussen",
                 "Ratliff", "Ray", "Raymond", "Reed", "Reese", "Reeves", "Reid",
                 "Reilly", "Reyes", "Reynolds", "Rhodes", "Rice", "Rich", "Richard",
                 "Richards", "Richardson", "Richmond", "Riddle", "Riggs", "Riley",
                 "Rios", "Rivas", "Rivera", "Rivers", "Roach", "Robbins",
                 "Roberson", "Roberts", "Robertson", "Robinson", "Robles", "Rocha",
                 "Rodgers", "Rodriguez", "Rodriquez", "Rogers", "Rojas", "Rollins",
                 "Roman", "Romero", "Rosa", "Rosales", "Rosario", "Rose", "Ross",
                 "Roth", "Rowe", "Rowland", "Roy", "Ruiz", "Rush", "Russell",
                 "Russo", "Rutledge", "Ryan", "Salas", "Salazar", "Salinas",
                 "Sampson", "Sanchez", "Sanders", "Sandoval", "Sanford", "Santana",
                 "Santiago", "Santos", "Sargent", "Saunders", "Savage", "Sawyer",
                 "Schmidt", "Schneider", "Schroeder", "Schultz", "Schwartz",
                 "Scott", "Sears", "Sellers", "Serrano", "Sexton", "Shaffer",
                 "Shannon", "Sharp", "Sharpe", "Shaw", "Shelton", "Shepard",
                 "Shepherd", "Sheppard", "Sherman", "Shields", "Short", "Silva",
                 "Simmons", "Simon", "Simpson", "Sims", "Singleton", "Skinner",
                 "Slater", "Sloan", "Small", "Snider", "Snow", "Snyder", "Solis",
                 "Solomon", "Sosa", "Soto", "Sparks", "Spears", "Spence", "Spencer",
                 "Stafford", "Stanley", "Stanton", "Stark", "Steele", "Stein",
                 "Stephens", "Stephenson", "Stevens", "Stevenson", "Stewart",
                 "Stokes", "Stone", "Stout", "Strickland", "Strong", "Stuart",
                 "Suarez", "Sullivan", "Summers", "Sutton", "Swanson", "Sweeney",
                 "Sweet", "Sykes", "Talley", "Tanner", "Tate", "Terrell", "Terry",
                 "Thompson", "Thornton", "Tillman", "Todd", "Torres", "Townsend",
                 "Tran", "Travis", "Trevino", "Trujillo", "Tucker", "Turner",
                 "Tyler", "Tyson", "Underwood", "Valdez", "Valencia", "Valentine",
                 "Valenzuela", "Vance", "Vang", "Vargas", "Vasquez", "Vaughan",
                 "Vaughn", "Vazquez", "Vega", "Velasquez", "Velazquez", "Velez",
                 "Van halen", "Vincent", "Vinson", "Wade", "Wagner", "Walker",
                 "Wall", "Wallace", "Waller", "Walls", "Walsh", "Walter", "Walters",
                 "Walton", "Ward", "Ware", "Warner", "Warren", "Washington",
                 "Waters", "Watkins", "Watson", "Watts", "Weaver", "Webb", "Weber",
                 "Webster", "Weeks", "Weiss", "Welch", "Wells", "West", "Wheeler",
                 "Whitaker", "White", "Whitehead", "Whitfield", "Whitley",
                 "Whitney", "Wiggins", "Wilcox", "Wilder", "Wiley", "Wilkerson",
                 "Wilkins", "Wilkinson", "William", "Williamson", "Willis",
                 "Winters", "Wise", "Witt", "Wolf", "Wolfe", "Wong", "Wood",
                 "Woodard", "Woods", "Woodward", "Wooten", "Workman", "Wright",
                 "Wyatt", "Wynn", "Yang", "Yates", "York", "Young", "Zamora",
                 "Zimmerman"]

    def getSuffixes(self):
        return ["II", "III", "Phd", "Jr", "Sr"]



class ContentDataValues:
    def getWords(self):
        return ["throw", "ball", "hat", "red", "worn",
             "list", "words", "computer", "in", "out", "hot", "cold", "warp",
             "speed", "captain", "assert", "hold", "room", "ship", "lost", "is",
             "television", "show", "about", "plane", "crash", "island",
             "monster", "trees", "banging", "smoke", "where", "are", "we",
             "was", "asked", "no", "rescue", "came", "build", "fire", "waited",
             "days", "moved", "to", "caves", "found", "with", "ghost", "dad",
             "in", "white", "rabbit", "lock", "discovered", "hatch", "with",
             "boon", "secretly", "hid", "it", "while", "trying", "to", "open",
             "it", "until", "sidekick", "died", "as", "sacrifice", "island",
             "demanded", "many", "had", "dreams", "or", "visions", "others",
             "came", "took", "people", "who", "are", "they", "what", "do",
             "they", "want", "light", "came", "on", "through", "window",
             "leader", "is", "a", "good", "man", "numbers", "in", "room",
             "enter", "keys", "computer", "end", "of", "world", "wicket",
             "magnetic", "pull", "shepherd", "always", "wrong", "much",
             "suspense", "what", "to", "do", "when", "it", "ends", "I", "will",
             "have", "to", "find", "something", "else", "to", "pique", "my",
             "interest", "or maybe", "write", "lots", "of", "code", "probably",
             "should", "have", "generated", "this", "text", "automatically",
             "so", "will", "from", "the", "web", "ending", "badly", "library",
             "handled", "books", "constantly", "headphones", "of", "ill", "on",
             "it's", "sill", "sits", "sofa"]

    def getEmailHosts(self):
        return ["gma1l", "hotma1l", "yah00",
                  "somema1l", "everyma1l", "ma1lbox", "b1zmail", "ma1l2u"]

    def getTlds(self):
        return ["org", "net", "com", "biz", "us", "co.uk"]

    def getBusinessTypes(self):
        return ["Furnishings", "Bakery",
                     "Accounting", "Textiles", "Manufacturing", "Industries",
                     "Pro Services", "Landscaping", "Realty", "Travel",
                     "Medical supplies", "Office supplies", "Insurance", "Software",
                     "Motors", "Cafe", "Services", "Gymnasium", "Motor Services",
                     "Signs", "Development", "Studios", "Engineering", "Development"]



class AddressDataValues:
    def getStreetNames(self):
        return ["Aberdeen", "Abington", "Academy",
                   "Adair", "Adams", "Adamsville", "Aeryview", "Agines", "Airport",
                   "Airwood", "Akron", "Alameda", "Albert", "Albright", "Alburn",
                   "Alexis", "Alfred", "Alice", "Alkire", "Allen", "Allison", "Alvin",
                   "Ambarassdor", "Amber", "Amhurst", "Amsterdam", "Antigua",
                   "Applegate", "Arborwood", "Arcadia", "Arch", "Archer", "Arlington",
                   "Armco", "Armstrong", "Arnold", "Arrowhead", "Arthur", "Ashburton",
                   "Ashley", "Aspen", "Athena", "Athens", "Atlantic", "Auburn",
                   "Austin", "Avalon", "Avon", "Axline", "Ayers", "Babbs", "Back",
                   "Bagley", "Bailey", "Baird", "Baker", "Ball", "Ballard", "Ballov",
                   "Bank", "Bardith", "Barkey", "Barkley", "Barnes", "Barr", "Basil",
                   "Basin", "Bateman", "Baughman", "Beam", "Beard", "Beatty",
                   "Beauty", "Beech", "Beechcreek", "Beechmont", "Beeline", "Belden",
                   "Bell", "Bellflower", "Bellview", "Bellwood", "Belmont",
                   "Benjamin", "Bennett", "Benwood", "Berkley", "Best", "Bethesda",
                   "Beulah", "Beverly", "Bexley", "Billingsley", "Bissett", "Bisson",
                   "Black", "Blackburn", "Blackrun", "Blackstone", "Blackwood",
                   "Blaine", "Blalock", "Blandy", "Blennerhassett", "Blocksom",
                   "Bloomfield", "Blossom", "Blue", "Bluff", "Bobby", "Bodmann",
                   "Boggs", "Bolen", "Bolton", "Bonaparte", "Bonifield", "Bonnair",
                   "Bonsels", "Boston", "Bottom", "Bowman", "Bowser", "Bowtown",
                   "Bradington", "Branch", "Brandywine", "Breezewood", "Brewers",
                   "Briarbush", "Briarcliff", "Briarleigh", "Brick", "Bridge",
                   "Brighton", "Brill", "Bristol", "Britton", "Broad", "Broadvue",
                   "Broadway", "Brookfield", "Brookover", "Brookside", "Brown",
                   "Browns", "Bryan", "Buck", "Buckeye", "Buckingham", "Burbank",
                   "Burlington", "Burnell", "Burnet", "Burns", "Busch", "Butler",
                   "Butter", "Buttermilk", "Byrne", "Caleb", "Calvert", "Cambon",
                   "Cambridge", "Camden", "Camp", "Campbell", "Canal", "Candlestick",
                   "Canewood", "Canfield", "Cannelville", "Canneville", "Cannon",
                   "Carbondale", "Carey", "Carl", "Carlisle", "Carlton", "Carlysle",
                   "Carmen", "Carol", "Carpenter", "Carroll", "Carson", "Carver",
                   "Cass", "Caston", "Castor", "Catalpa", "Cathy", "Catt", "Cattail",
                   "Cattle", "Cecil", "Cedar", "Cedarhurst", "Celina", "Cementary",
                   "Cemetery", "Center", "Central", "Ceramic", "Chalfant",
                   "Chandlersville", "Chapman", "Chardon", "Charlene", "Charles",
                   "Chase", "Chatauqua", "Chatham", "Cheney", "Cherlick", "Cherry",
                   "Chesapeake", "Chester", "Chesterfield", "Chestnut", "Chevington",
                   "Chewelah", "Childrens", "Chillicothe", "China", "Choctaw",
                   "Christopher", "Christy", "Church", "Churchfield", "Circle",
                   "Circleville", "Clairbourne", "Claire", "Clarence", "Clarendon",
                   "Clarice", "Clark", "Clary", "Clay", "Claysville", "Clearcreek",
                   "Clearey", "Clearport", "Clearview", "Cleve", "Cleveland",
                   "Clevenger", "Cliffrock", "Cliffwood", "Clinton", "Clover",
                   "Cloveridge", "Clyde", "Coburg", "Cochran", "Codell", "Cohen",
                   "Colburn", "College", "Collingwood", "Collins", "Colony",
                   "Columbia", "Columbus", "Comin", "Commissioner", "Commonwealth",
                   "Conn", "Convers", "Coopermill", "Cooperriders", "Cooperwell",
                   "Cornell", "Cornstill", "Coronado", "Corvus", "Corwin", "Cosgrave",
                   "Coshocton", "Cottage", "Countiss", "Countryside", "Court", "Cove",
                   "Coventry", "Cowden", "Cranfield", "Crawford", "Creamery",
                   "Creedmoor", "Creekview", "Crestway", "Crock", "Crooks", "Crosier",
                   "Cross", "Crossgate", "Crow", "Crown", "Culbertson", "Curtis",
                   "Dads", "Daisy", "Dale", "Dallman", "Dana", "Daniels", "Danville",
                   "Darcie", "Darla", "Darlington", "Date", "Davis", "Dawnlight",
                   "Dawson", "Dearborn", "December", "Decrow", "Deer", "Deerfield",
                   "Deerpath", "Deewood", "Dellwood", "Delmont", "Delwood", "Denbigh",
                   "Denlinger", "Denmark", "Denning", "Dennis", "Denny", "Depot",
                   "Detroit", "Devin", "Devlin", "Dewey", "Diagonal", "Dickinson",
                   "Dickson", "Dietz", "Dillon", "Discovery", "Dixie", "Dixon",
                   "Dogwood", "Dona", "Donald", "Dooleys", "Dorothy", "Doru",
                   "Douglas", "Dowling", "Downard", "Downing", "Dragoo", "Dresden",
                   "Dryden", "Dundee", "Dunham", "Dunzweiler", "Durban", "Duvall",
                   "Dyer", "East", "Easter", "Eastern", "Eastfield", "Eastlawn",
                   "Eastman", "Eastmoor", "Eastport", "Eastview", "Eastward",
                   "Eastwood", "Eaton", "Echo", "Edalbert", "Eddie", "Eddy", "Ederer",
                   "Edgewater", "Edison", "Edna", "Edward", "Edwards", "Eldwood",
                   "Elfin", "Elida", "Elizabeth", "Ellen", "Eller", "Ellis",
                   "Ellsworth", "Elmville", "Emily", "Englewood", "Enon", "Eppley",
                   "Erie", "Erin", "Essex", "Euclid", "Evans", "Evansport", "Evelyn",
                   "Evergreen", "Ewing", "Exchange", "Extension", "Fair", "Fairall",
                   "Fairbanks", "Faircrest", "Fairmont", "Fairmount", "Fairview",
                   "Fairway", "Fallsburg", "Falt", "Farson", "Fawn", "Faye",
                   "Fayette", "Federal", "Ferncliff", "Fernstone", "Ferrell", "Fess",
                   "Field", "Findley", "First", "Fishers", "Fitzgerald", "Fleek",
                   "Fleming", "Flint", "Flintridge", "Flintwood", "Florence",
                   "Forest", "Forry", "Foster", "Founds", "Fountain", "Fowlers",
                   "Foxfire", "Frame", "Francis", "Franklin", "Frazeysburg",
                   "Freeborn", "Freedom", "Frick", "Friendship", "Frisco", "Fritter",
                   "Front", "Frontier", "Fulbrook", "Fulton", "Fultonrose",
                   "Galbraith", "Galena", "Galigher", "Galighner", "Gallia", "Galway",
                   "Gant", "Gantz", "Garden", "Gardenway", "Garey", "Garfield",
                   "Garner", "Garrell", "Garrett", "Garst", "Gaslight", "Gayla",
                   "Genessee", "George", "Gest", "Gibbard", "Gifford", "Gilbert",
                   "Glade", "Glena", "Glenaven", "Glendale", "Glenhaven", "Glenn",
                   "Glenwillow", "Glenwood", "Glessner", "Goddard", "Gomber",
                   "Goosecreek", "Gordon", "Gorrell", "Gorsuch", "Goslen", "Grace",
                   "Graffis", "Grand", "Grandview", "Granger", "Grant", "Granville",
                   "Gratiot-Newark", "Gray", "Graylock", "Green", "Greenbriar",
                   "Greenbrier", "Greengold", "Greenhouse", "Greenville", "Greenwood",
                   "Greiner", "Grieves", "Grove", "Guava", "Haessler", "Hale", "Hall",
                   "Hamburg", "Hamilton", "Hamline", "Hampton", "Hanawalt", "Hannah",
                   "Hannawalt", "Hanover", "Hanson", "Harbor", "Hardesty", "Harding",
                   "Hardy", "Harkers", "Harlan", "Harmon", "Harmony", "Harper",
                   "Harris", "Harrison", "Harshman", "Hartford", "Hartman",
                   "Hartville", "Hartwell", "Harvey", "Haught", "Hawk", "Hawkes",
                   "Hayes", "Hazel", "Hazlett", "Heath", "Heber", "Hebron", "Heckak",
                   "Heckel", "Hedgewood", "Helene", "Helpar", "Hendershot", "Henry",
                   "Heritage", "Herron", "Hewitt", "Hickam", "Hickman", "Hickory",
                   "Hicks", "Hideaway", "Higgins", "High", "Highland", "Highview",
                   "Hilbish", "Hildreth", "Hill", "Hinman", "Hogans", "Hoge",
                   "Hoiles", "Holbein", "Holbert", "Holliday", "Holmes", "Home",
                   "Homeless", "Homer", "Homes", "Homestead", "Homewood", "Hoover",
                   "Hopewell", "Hospital", "Howard", "Howell", "Hudson", "Huey",
                   "Hughes", "Humphrey", "Hunt", "Hunter", "Hunterdon", "Huntington",
                   "Idaho", "Idlewood", "Ildewood", "Iliamna", "Imlay",
                   "Independence", "Indiana", "Indianola", "Inwood", "Ireland",
                   "Iron", "Island", "Jackson", "James", "Jamestown", "Jannett",
                   "Jefferson", "Jenkins", "Jensen", "Jessamine", "Jewett", "Jewitt",
                   "Jody", "John", "Johnson", "Johnstown", "Jonathan", "Jones",
                   "Jordan", "Joyce", "Juanita", "Julian", "Juniper", "Kahler",
                   "Katherine", "Kauffman", "Kearns", "Keen", "Kegs", "Kelly",
                   "Kennedy", "Kenny", "Kensington", "Kenton", "Kerri", "Kettering",
                   "Kevrob", "Keystone", "Kibler", "Kimes", "King", "Kings",
                   "Kingsley", "Kingswood", "Kinsman", "Kinzel", "Kirk", "Klotz",
                   "Knipe", "Knox", "Kopchak", "Kossuch", "Lacon", "Lafayette",
                   "Lagonda", "Lake", "Lakeside", "Lakewood", "Lambert", "Lancaster",
                   "Lancaster-Chillicoth", "Lander", "Laneway", "Langan", "Lark",
                   "Larkspur", "Larry", "Larzelere", "Lasalle", "Lashley", "Laurel",
                   "Lavona", "Lawhead", "Lawn", "Lawndale", "Lawson", "Lawyers",
                   "Layton", "Lazelere", "Lectric", "Ledbetter", "Leedom", "Leffler",
                   "Lefter", "Legion", "Lenox", "Lent", "Leon", "Leonard",
                   "Leonardville", "Leslie", "Lesslar", "Lewis", "Lexington",
                   "Liberty", "Licking", "Lillian", "Lima", "Limestone", "Lincoln",
                   "Lincolnway", "Lindale", "Lindbergh", "Linden", "Lindsay", "Linn",
                   "Linwood", "Lisa", "Lithopolis", "Livingston", "Lock", "Locksmith",
                   "Locust", "Lodge", "Lomita", "London", "Long", "Lookout", "Lost",
                   "Loudon", "Louise", "Lovers", "Lubring", "Lucas", "Lucasburg",
                   "Luck", "Lundgren", "Lutz", "Macedonia", "Mackenzie", "Madison",
                   "Mailey", "Main", "Malibu", "Manning", "Manor", "Mansfield",
                   "Maple", "Maplecraft", "Mapleview", "Maplewood", "Marchmont",
                   "Marietta", "Marion", "Mark", "Market", "Marketing", "Marlo",
                   "Marne", "Marsha", "Marshdale", "Martin", "Martinel", "Mary",
                   "Mast", "Matthews", "Mayfair", "Maysville", "Mcarthur", "Mccarley",
                   "Mccaslin", "Mcclain", "Mcclure", "Mcconnell", "Mcconnellsville",
                   "Mcdaniel", "Mcdonald", "Mcfarland", "Mcintire", "Mckaig",
                   "Mckeever", "Mckinley", "Mcmillan", "Mcowens", "Mead", "Meadow",
                   "Meadowbrook", "Meadowhaven", "Meadowood", "Mechanicsburg", "Meek",
                   "Melick", "Melrose", "Memory", "Meridian", "Meriwether", "Merlin",
                   "Merriam", "Merrick", "Merrimac", "Merryhill", "Mershon",
                   "Messimer", "Metro", "Miami", "Michael", "Michigan", "Middle",
                   "Middlefork", "Middleton", "Midway", "Milagra", "Military", "Mill",
                   "Miller", "Millers", "Milton", "Miner", "Missouri", "Mitchell",
                   "Moccasin", "Mock", "Mohawk", "Mollysrock", "Mona", "Monroe",
                   "Montague", "Montgomery", "Moonlight", "Moore", "Moorehead",
                   "Moores", "Moorewood", "Morgan", "Morgantown", "Morganville",
                   "Morningstar", "Morrison", "Morse", "Mound", "Moxadarla",
                   "Moxahala", "Muirwood", "Mulberry", "Mundy", "Munson", "Murray",
                   "Muskingum", "Musselman", "Myrtle", "Nancy", "Narrows", "National",
                   "Navy", "Neal", "Neil", "Nelson", "Neptune", "Newark", "Newgate",
                   "Newlon", "Newman", "Newport", "Nichalas", "Nolan", "None",
                   "Nor-Bixbey", "Nora", "Norfield", "Normandy", "Norris", "North",
                   "Northcrest", "Northland", "Norwich", "Norwood", "Nottingham",
                   "Nottinghamshire", "Nugent", "Oakland", "Oakwood", "Obetz",
                   "Odell", "Ohio", "Okey", "Olive", "Olney", "Ontario", "Opera",
                   "Orange", "Orchard", "Orders", "Orton", "Osage", "Osceola",
                   "Otterbein", "Overlook", "Owens", "Oxford", "Paint", "Palamino",
                   "Pallas", "Palmer", "Palmeraway", "Palmwood", "Palomino",
                   "Paragon", "Parish", "Park", "Parker", "Parks", "Parkview",
                   "Parkway", "Parkwood", "Parliament", "Parry", "Partridge", "Patch",
                   "Patricia", "Peachblow", "Pear", "Pearl", "Pembroke", "Penn",
                   "Penney", "Pennisula", "Pennsylvania", "Penrick", "Perdue",
                   "Perine", "Perkins", "Perry", "Perryton", "Pershing", "Peters",
                   "Petersburg", "Peterson", "Pfeifer", "Pfeiffer", "Philadelphia",
                   "Phillips", "Pickwick", "Pierce", "Pike", "Pine", "Pinecrest",
                   "Pinetown", "Pineview", "Pinewood", "Pinkerton", "Pinkley",
                   "Pioneer", "Piper", "Plainfield", "Plantation", "Playford",
                   "Pleasant", "Pleasantview", "Pleasantville", "Pointe", "Poplar",
                   "Portage", "Porter", "Portland", "Potters", "Potts", "Powell",
                   "Prame", "Pratt", "Price", "Princeton", "Prior", "Prison",
                   "Promway", "Prospect", "Pryor", "Public", "Purdy", "Purvis",
                   "Putnam", "Quarry", "Quick", "Quincy", "Quinlan", "Race", "Radnor",
                   "Raiders", "Railroad", "Rains", "Raintree", "Range", "Rankin",
                   "Ransbottom", "Raven", "Ravenwood", "Rawson", "Reading", "Ream",
                   "Redman", "Redondo", "Reed", "Reeves", "Rehl", "Restless",
                   "Reynolds", "Rhonda", "Rice", "Richards", "Richey", "Richman",
                   "Richmond", "Richvale", "Richwood", "Rider", "Ridge", "Ridgefield",
                   "Ridgeland", "Ridgeview", "Ridgewood", "Rigby", "Riggin", "Rigny",
                   "Ritchey", "Ritenour", "River", "Riverside", "Riverview",
                   "Roadayle", "Robertson", "Robin", "Robinson", "Robinwood", "Rock",
                   "Rockville", "Roemer", "Roland", "Rollins", "Rondayle",
                   "Roosevelt", "Roper", "Rose", "Roseville", "Rosewood", "Rowland",
                   "Royalton", "Royma", "Rucker", "Runyan", "Russell", "Rustle",
                   "Ruth", "Ryan", "Salem", "Salgarber", "Sally", "Saltzgaber",
                   "Sampson", "Samuel", "Sand", "Sandhurst", "Sandra", "Sandusky",
                   "Sandvik", "Santoy", "Sarah", "Scarborough", "Scenic", "Schaum",
                   "Schneider", "Scholl", "School", "Schuler", "Schultz", "Schwallie",
                   "Scott", "Scout", "Sealover", "Seaman", "Seborn", "Sells",
                   "Selsam", "Senator", "Seroco", "Sevall", "Severt", "Seward",
                   "Seymore", "Shady", "Shagbark", "Shaliman", "Shandon", "Sharon",
                   "Sharonwood", "Shasta", "Shaw", "Shawnee", "Sheandoah", "Sheila",
                   "Shellhart", "Shenandoah", "Shepherd", "Sherborne", "Sheridan",
                   "Sherman", "Sherwood", "Shindern", "Shinick", "Shinnick",
                   "Shiplett", "Shoop", "Shore", "Short", "Shumaker", "Sibley",
                   "Silliman", "Silmore", "Skyline", "Skyview", "Slack", "Smithfield",
                   "Smithwood", "Snoke", "Snyder", "Sofin", "Solida", "Somers",
                   "Somerset", "Sonora", "Souder", "South", "Southard", "Southeast",
                   "Southern", "Southward", "Spangler", "Sparling", "Spellman",
                   "Spence", "Spencer", "Spielbusch", "Spratt", "Spring",
                   "Springdale", "Spruce", "Spry", "Stacy", "Stalder", "Stalling",
                   "Stanley", "Stansberry", "Stanton", "Stanway", "State", "Steele",
                   "Stein", "Stephens", "Stevens", "Stevy", "Stewart", "Stiers",
                   "Stillmeadow", "Stillwell", "Stine", "Stiver", "Stokely", "Stone",
                   "Stonecreek", "Stormont", "Stout", "Stoutsville", "Strawberry",
                   "Street", "Sturtz", "Stygler", "Sudbury", "Sugargrove",
                   "Sugartree", "Summit", "Sundale", "Sunflower", "Sunkel", "Sunray",
                   "Sunrise", "Sunset", "Superior", "Surger", "Swans", "Swartz",
                   "Swingle", "Sycamore", "Talford", "Talley", "Tamarron", "Tammy",
                   "Tannehill", "Tarkman", "Taylor", "Teakwood", "Tedrick", "Temple",
                   "Terrace", "Terry", "Theobald", "Third", "Thomas", "Thompson",
                   "Thorn", "Thornberry", "Thornhill", "Thurman", "Tiffany",
                   "Tileston", "Titus", "Todd", "Toni", "Towers", "Town", "Trabue",
                   "Traci", "Traco", "Tranquility", "Treehouse", "Tremont", "Trend",
                   "Tridelphia", "Tupedo", "Turner", "Turtle", "Tuscarawas",
                   "Twimenhill", "Tyman", "Underwood", "Uneeda", "Union", "Unknown",
                   "Valley", "Vance", "Vaughn", "Venture", "Venus", "Vernon",
                   "Vetter", "Vicki", "Victory", "Villa", "Village", "Vine", "Vinsel",
                   "Virginia", "Vista", "Vroom", "Wabash", "Wacker", "Wakatomika",
                   "Waldolf", "Walker", "Wall", "Wallwork", "Walnut", "Walter",
                   "Waltham", "Ward", "Wargo", "Warner", "Warners", "Warren",
                   "Warwick", "Washington", "Water", "Waters", "Watkins", "Watson",
                   "Watts", "Wayne", "Weaver", "Webb", "Webster", "Wedgewood",
                   "Weedon", "Weller", "Wells", "Wentz", "Wessex", "West",
                   "Westbourne", "Western", "Westmoor", "Westmore", "Westwood",
                   "Wetsell", "Whaley", "Wheatland", "Wheelabout", "Wheeler",
                   "Wheeling", "Whipple", "Whites", "Whitman", "Wilhelm", "Wilkins",
                   "Williams", "Willis", "Willow", "Wilmer", "Wilmington", "Wilshire",
                   "Wilson", "Winding", "Windmill", "Windsong", "Winfield",
                   "Winlwood", "Winter", "Winton", "Wise", "Wisteria", "Wogan",
                   "Wolfe", "Wolford", "Woodberry", "Woodbrook", "Woodland",
                   "Woodlawn", "Woolper", "Workman", "Wortman", "Wrexham", "Yale",
                   "Yingling", "Yost", "Young", "Zane", "Zanesville", "Zella"]

    def getAddressSuffixes(self):
        return ["Avenue", "Boulevard",
                       "Circle", "Crescent", "Court", "Drive", "Heights", "Lane", "Park",
                       "Path", "Parkway", "Place", "Road", "Ridge", "Run", "Square",
                       "Street", "Station", "Terrace", "Trail", "Way", "Rd", "Ln", "St",
                       "Blvd", "Ave", "Drv"]

    def getCities(self):
        return ["Abba", "Abbeville", "Acworth",
              "Adairsville", "Adel", "Adrian", "Ailey", "Alamo", "Alapaha",
              "Albany", "Allenhurst", "Alma", "Alma", "Alpharetta", "Alston",
              "Amboy", "Ambrose", "Americus", "Appling", "Arlington", "Ashburn",
              "Athens", "Atkinson", "Atlanta", "Attapulgus", "Auburn", "Augusta",
              "Augusta-Richmond County", "Austell", "Avondale Estates", "Axson",
              "Baconton", "Baden", "Bainbridge", "Bainbridge", "Baldwin",
              "Bannockburn", "Barnesville", "Barney", "Barretts", "Barwick",
              "Baxley", "Bemiss", "Berkeley Lake", "Berlin", "Blackshear",
              "Blairsville", "Blakely", "Bloomingdale", "Blue Ridge", "Bogart",
              "Boston", "Bowdon", "Bowens Mill", "Bowman", "Braselton", "Bremen",
              "Brinson", "Bristol", "Bronwood", "Brookfield", "Brooklet",
              "Brooks", "Broxton", "Brunswick", "Buchanan", "Buena Vista",
              "Buford", "Bushnell", "Byromville", "Byron", "Cairo", "Camilla",
              "Canton", "Carnesville", "Carrollton", "Cartersville",
              "Cave Spring", "Cecil", "Cedartown", "Centerville", "Chamblee",
              "Chatsworth", "Chauncey", "Chester", "Chickamauga", "Chula",
              "Clarkston", "Claxton", "Clayton", "Cleveland", "Clyatteville",
              "Clyo", "Cobbtown", "Cochran", "Cogdell", "Cohutta", "Colesburg",
              "College Park", "Collins", "Colquitt", "Columbus", "Commerce",
              "Conyers", "Coolidge", "Cordele", "Cornelia", "Council",
              "Country Club Estate", "Coverdale", "Covington", "Cox",
              "Crawfordville", "Crescent", "Culloden", "Cumming", "Cusseta",
              "Cuthbert", "Dacula", "Dahlonega", "Daisy", "Dakota", "Dallas",
              "Dalton", "Damascus", "Danielsville", "Darien", "Dasher", "Dawson",
              "Dawsonville", "Decatur", "Denmark", "Dillard", "Dixie",
              "Dock Junction", "Doerun", "Donalsonville", "Doraville", "Douglas",
              "Douglasville", "Dover Bluff", "Dupont", "Dublin", "Dudley",
              "Duluth", "Dunwoody", "East Dublin", "East Point", "Eastman",
              "Eatonton", "Ebenezer", "Edison", "Edith", "Egypt", "Elberton",
              "Eldorado", "Ellabelle", "Ellaville", "Ellenton", "Ellijay",
              "Enigma", "Euharlee", "Eulonia", "Everitt", "Fairburn", "Fairmont",
              "Fargo", "Fayetteville", "Fitzgerald", "Flemington",
              "Flowery Branch", "Folkston", "Forest Park", "Forsyth",
              "Fort Gaines", "Fort Oglethorpe", "Fort Stewart", "Fort Valley",
              "Franklin", "Fruitland", "Funston", "Gainesville", "Garden City",
              "Garfield", "Geneva", "Georgetown", "Gibson", "Glennville",
              "Glenwood", "Glory", "Graham", "Gray", "Greensboro", "Greenville",
              "Griffin", "Grooverville", "Groveland", "Grovetown", "Gumbranch",
              "Guyton", "Hagan", "Hahira", "Hamilton", "Hampton", "Hapeville",
              "Harding", "Harding", "Hardwicke", "Harrietts Bluff", "Hartwell",
              "Hawkinsville", "Haylon", "Hazlehurst", "Helena", "Hepzibah",
              "Hiawassee", "Hickox", "Higgston", "Hinesville", "Hiram",
              "Hoboken", "Hogansville", "Holly Springs", "Holt", "Homeland",
              "Homer", "Homerville", "Hopeulikit", "Hortense", "Howell", "Inaha",
              "Iron City", "Irwinton", "Irwinville", "Isle Of Hope-Dutch Island",
              "Jackson", "Janis", "Jasper", "Jefferson", "Jeffersonville",
              "Jesup", "Johns Creek", "Jonesboro", "Keller", "Kennesaw",
              "Kinderlou", "Kings Bay Base", "Kingsland", "Kirkland", "Kite",
              "Lafayette", "Lagrange", "Lake City", "Lake Park", "Lakeland",
              "Lanier", "Lawrenceville", "Lax", "Leary", "Leefield", "Leesburg",
              "Lenox", "Lexington", "Lilburn", "Lincolnton", "Lithonia",
              "Locust Grove", "Loganville", "Lookout Mountain", "Louisville",
              "Lovejoy", "Ludowici", "Lulaton", "Lumber City", "Lumpkin",
              "Lyons", "Macon", "Madison", "Manassas", "Manchester", "Marietta",
              "Maxeys", "Mayday", "Mcdonough", "Mcintosh", "Mcintyre", "Mcrae",
              "Meigs", "Meldrim", "Mershon", "Metter", "Midway", "Milan",
              "Milledgeville", "Millen", "Milton", "Moniac", "Monroe",
              "Montezuma", "Montgomery", "Monticello", "Montrose", "Mora",
              "Morgan", "Morrow", "Morven", "Moultrie", "Mount Vernon",
              "Mount Zion", "Mountain Park", "Mystic", "Nahunta", "Nankin",
              "Nashville", "Needmore", "Nelson", "Nevils", "New Rock Hill",
              "Newnan", "Newton", "Nicholls", "Norcross", "Norman Park",
              "Oakwood", "Ochlocknee", "Ocilla", "Odum", "Offerman", "Offerman",
              "Oglethorpe", "Omega", "Osterfield", "Ousley", "Oxford",
              "Palmetto", "Parrott", "Patterson", "Peachtree City Website",
              "Pearson", "Pelham", "Pembroke", "Perry", "Phillipsburg",
              "Pine Lake", "Pineora", "Pineview", "Pooler", "Port Wentworth",
              "Portal", "Potter", "Poulan", "Powder Springs", "Preston",
              "Pridgen", "Pulaski", "Queensland", "Quitman", "Ray City",
              "Rebecca", "Register", "Reidsville", "Remerton", "Rentz",
              "Retreat", "Riceboro", "Richmond Hill", "Ridgeville", "Rincon",
              "Ringgold", "Riverdale", "Riverside", "Rochelle", "Rockingham",
              "Rockmart", "Rome", "Roswell", "Royston", "Rutledge",
              "Saint George", "Sale City", "Sandersville", "Sandy Springs",
              "Sasser", "Savannah", "Screven", "Senoia", "Sessoms", "Shawnee",
              "Shellman Bluff", "Sirmans", "Skidaway Island", "Smithville",
              "Smyrna", "Snellville", "Social Circle", "Soperton",
              "South Newport", "Sparks", "Sparta", "Springfield", "Strongsville",
              "St. Simons Island", "Statenville", "Statesboro", "Sterling",
              "Stillmore", "Stillwell", "Stilson", "Stockbridge", "Stockton",
              "Stone Mountain", "Sugar Hill", "Sumner", "Sunbury", "Sunsweet",
              "Surrency", "Suwanee", "Swainsboro", "Sycamore", "Sylvania",
              "Sylvester", "Talbotton", "Tallapoosa", "Tarboro", "Tarver",
              "Temple", "Thalman", "Thelma", "Thomaston", "Thomasville",
              "Thomson", "Thunderbolt", "Tifton", "Toccoa", "Toomsboro",
              "Townsend", "Trenton", "Trudie", "Tucker", "Twin City",
              "Twin Peaks", "Tybee Island", "Tyrone", "Unadilla", "Union City",
              "Unionville", "Upton", "Uvalda", "Valdosta", "Valona",
              "Vernonburg", "Vidalia", "Vienna", "Villa Rica", "Walthourville",
              "Warrenton", "Warwick", "Washington", "Waterloo", "Watkinsville",
              "Waverly", "Waycross", "Waynesboro", "Waynesville", "Weber",
              "West Green", "West Point", "Westwood", "Whigham", "White Oak",
              "Whitmarsh Island", "Willacoochee", "Wilmington Island", "Winder",
              "Winokur", "Withers", "Woodbine", "Woodstock", "Worth", "Wray",
              "Wrightsville"]
    
    def getLatitude(self):
        return round(random.uniform(-90, 90), 6)

    def getLongitude(self):
        return round(random.uniform(-180, 180), 6)


class DataFactory:
    def __init__(self, randomnew):
        self.random = randomnew
        self.nameDataValues = NameDataValues()
        self.addressDataValues = AddressDataValues()
        self.contentDataValues = ContentDataValues()

    def getName(self):
        firstName = self.random.choice(self.nameDataValues.getFirstNames())
        lastName = self.random.choice(self.nameDataValues.getLastNames())
        suffix = self.random.choice(self.nameDataValues.getSuffixes())

        return f"{firstName} {lastName} {suffix}".strip()

    def getAddress(self):
        streetName = self.random.choice(self.addressDataValues.getStreetNames())
        addressSuffix = self.random.choice(self.addressDataValues.getAddressSuffixes())
        city = self.random.choice(self.addressDataValues.getCities())
        zip_code = self.random.randint(10000, 99999)
        home_number = self.random.randint(100, 9999)

        return f"{home_number} {streetName} {addressSuffix}, {city}, {zip_code}"

    def getEmail(self, name):
        names = name.split(" ")
        if len(names) >= 2:
            firstName = names[0].lower()
            lastName = ".".join(names[1:]).lower()
        else:
            firstName = names[0].lower()
            lastName = ""

        emailHost = self.random.choice(self.contentDataValues.getEmailHosts())
        tld = self.random.choice(self.contentDataValues.getTlds())

        return f"{firstName}.{lastName}@{emailHost}.{tld}"

    def getContent(self, amount=100):
        words = self.contentDataValues.getWords()
        content = [self.random.choice(words) for _ in range(amount)]

        return "\n".join(content)

    def getLicensePlate(self):
        letters = [chr(random.randint(65, 90)) for _ in range(3)]
        numbers = [str(random.randint(0, 9)) for _ in range(3)]
        return f"{''.join(letters)}{''.join(numbers)}"

    def getDate(self):
        year = self.random.randint(1960, datetime.datetime.now().year)
        month = self.random.randint(1, 12)
        day = self.random.randint(1, 28)
        return f"{year:04d}-{month:02d}-{day:02d}"

    def getBusinessType(self):
        businessTypes = self.contentDataValues.getBusinessTypes()
        return self.random.choice(businessTypes)
    
    def getSocialSecurityNumber(self):
        ssn = [str(random.randint(0, 9)) for _ in range(9)]
        return f"{''.join(ssn[:3])}-{''.join(ssn[3:5])}-{''.join(ssn[5:])}"

    def getLicenseNumber(self):
        letters = [chr(random.randint(65, 90)) for _ in range(3)]
        numbers = [str(random.randint(0, 9)) for _ in range(7)]
        return f"{''.join(letters)}{''.join(numbers)}"


randomnew = random.Random(datetime.datetime.now().microsecond)
dataFactory = DataFactory(randomnew)

# amounts = {
#    "Names": 10,
#    "Dates": 9,
#    "Addresses": 8,
#    "License Plates": 7,
#    "Emails": 6,
#    "Social Security Numbers": 5,
#    "License Numbers": 4,
#    "Business Types": 3,
#    "Content": 2,
#    "Latitude and Longitude": 1,
# }

##########################################################
########################################################## part 1 (MidTerm)
##########################################################

factory = DataFactory(randomnew = random.Random())
output_file = 'large_1000mil_records.csv'

total_records = 100_000_000
batch_size = 1_000_000        # to process 1 million records at a time

# we capture the simulated data in a data frame
headers = [
    "First Name", "Last Name", "Suffixes", "Words", "Email Hosts", "TLD",
    "Business Type", "Street Names", "Address", "Address Suffixes",
    "Cities", "Latitude", "Longitude", "License Plate", "SSN", "License Number"
]

# Starting the  timing
start_time = time.time()
print(f"Start time : {start_time}")

now = datetime.datetime.now()
# Format the time in a human-readable format
human_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current time:", human_time)

# Writing the data in a csv file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)    # sets up the csv writer object
    writer.writerow(headers)     # writes the header

# Generate and append data in batches
for batch in range(total_records // batch_size):

    # For each batch, we record the simulated data in a dictionary
    # Each key in the dictionary represents a column name
    # The average time complexity of working with dictionaries is O(1)

    batch_data = {
        "First Name": [],
        "Last Name": [],
        "Suffixes": [],
        "Words": [],
        "Email Hosts": [],
        "TLD": [],
        "Business Type": [],
        "Street Names": [],
        "Address": [],
        "Address Suffixes": [],
        "Cities": [],
        "Latitude": [],
        "Longitude": [],
        "License Plate": [],
        "SSN": [],
        "License Number": []
    }

    # Populate each field with random data for chunk_size records
    for _ in range(batch_size):

       # Name data
        batch_data["First Name"].append(factory.random.choice(factory.nameDataValues.getFirstNames()))
        batch_data["Last Name"].append(factory.random.choice(factory.nameDataValues.getLastNames()))
        batch_data["Suffixes"].append(factory.random.choice(factory.nameDataValues.getSuffixes()))

        # Business data
        batch_data["Words"].append(factory.random.choice(factory.contentDataValues.getWords()))
        batch_data["Email Hosts"].append(factory.random.choice(factory.contentDataValues.getEmailHosts()))
        batch_data["TLD"].append(factory.random.choice(factory.contentDataValues.getTlds()))
        batch_data["Business Type"].append(factory.getBusinessType())

       # Address data
        batch_data["Street Names"].append(factory.random.choice(factory.addressDataValues.getStreetNames()))
        batch_data["Address"].append(factory.getAddress())
        batch_data["Address Suffixes"].append(factory.random.choice(factory.addressDataValues.getAddressSuffixes()))

        batch_data["Cities"].append(factory.random.choice(factory.addressDataValues.getCities()))
        batch_data["Latitude"].append(random.uniform(-90, 90))
        batch_data["Longitude"].append(random.uniform(-180, 180))

       # Additional data
        batch_data["License Plate"].append(factory.getLicensePlate())
        batch_data["SSN"].append(factory.getSocialSecurityNumber())
        batch_data["License Number"].append(factory.getLicenseNumber())

    # Convert the Dictionary to DataFrame for easier CSV writing
    df_batch_data = pd.DataFrame(batch_data)

    # Append chunk to CSV
    df_batch_data.to_csv(output_file, mode='a', header = False, index = False)

    # Print progress
    print(f"Batch {batch + 1} is written to the output file.")

# Ending the timing
end_time = time.time()
print(f"End time : {end_time}")

print(f"Data generation of 100 millions records is complete. Total time: {end_time - start_time} seconds.")