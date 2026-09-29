from django.core.management.base import BaseCommand
from quiz_app.models import Category, Question

class Command(BaseCommand):
    help = 'Seeds the database with demo categories and quiz questions.'

    def handle(self, *args, **options):
        data = {
            'General Knowledge': [
                ('What is the capital of France?', 'London', 'Paris', 'Berlin', 'Madrid', 'B'),
                ('Which planet is known as the Red Planet?', 'Venus', 'Jupiter', 'Mars', 'Saturn', 'C'),
                ('Who wrote the play "Romeo and Juliet"?', 'Charles Dickens', 'William Shakespeare', 'Mark Twain', 'Leo Tolstoy', 'B'),
                ('What is the largest ocean on Earth?', 'Atlantic', 'Indian', 'Arctic', 'Pacific', 'D'),
                ('How many continents are there on Earth?', '5', '6', '7', '8', 'C'),
                ('What is the currency of Japan?', 'Won', 'Yuan', 'Yen', 'Ringgit', 'C'),
                ('Which gas do plants absorb from the atmosphere?', 'Oxygen', 'Nitrogen', 'Carbon Dioxide', 'Hydrogen', 'C'),
                ('Who painted the Mona Lisa?', 'Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Claude Monet', 'C'),
                ('Which is the longest river in the world?', 'Amazon', 'Nile', 'Yangtze', 'Mississippi', 'B'),
                ('Who is known as the Father of the Nation in India?', 'Jawaharlal Nehru', 'Subhas Chandra Bose', 'Mahatma Gandhi', 'Sardar Patel', 'C'),
            ],
            'Aptitude': [
                ('A train travels 60 km in 45 minutes. What is its speed in km/h?', '60 km/h', '75 km/h', '80 km/h', '90 km/h', 'C'),
                ('If the cost price of an item is Rs 400 and it is sold for Rs 500, what is the profit percentage?', '20%', '25%', '15%', '30%', 'B'),
                ('What is the average of the first 10 natural numbers?', '5', '5.5', '6', '4.5', 'B'),
                ('A sum of money doubles itself in 8 years at simple interest. What is the rate of interest per annum?', '10%', '12.5%', '8%', '15%', 'B'),
                ('If 5 workers can complete a task in 12 days, how many days will 10 workers take?', '4 days', '6 days', '8 days', '10 days', 'B'),
                ('What is 15% of 200?', '20', '25', '30', '35', 'C'),
                ('The ratio of two numbers is 3:4 and their sum is 63. What is the larger number?', '27', '36', '32', '30', 'B'),
                ('A person walks 6 km in 1.5 hours. What is their speed in m/s?', '1.11 m/s', '2 m/s', '1.5 m/s', '2.5 m/s', 'A'),
                ('If x + y = 10 and x - y = 4, what is the value of x?', '5', '6', '7', '8', 'C'),
                ('A shopkeeper marks an item 20% above cost price and gives a 10% discount. What is the overall profit percentage?', '8%', '10%', '12%', '6%', 'A'),
            ],
            'Reasoning': [
                ('Find the odd one out: Apple, Banana, Carrot, Mango', 'Apple', 'Banana', 'Carrot', 'Mango', 'C'),
                ('If CAT is coded as 3120, how is DOG coded using the same logic?', '4157', '4715', '4157', '4517', 'A'),
                ('Complete the series: 2, 4, 8, 16, __', '18', '24', '32', '30', 'C'),
                ("Pointing to a photograph, a man says: She is the daughter of my grandfather's only son. How is the woman related to the man?", 'Mother', 'Sister', 'Aunt', 'Cousin', 'B'),
                ('Which number should come next: 1, 4, 9, 16, 25, __?', '30', '36', '32', '49', 'B'),
                ('If North becomes East, East becomes South, and so on, what will South become?', 'North', 'West', 'East', 'South', 'B'),
                ('Find the missing letter in the series: A, C, F, J, __', 'M', 'N', 'O', 'P', 'C'),
                ('If all Roses are Flowers and some Flowers fade quickly, which of the following is true?', 'All Roses fade quickly', 'Some Roses may fade quickly', 'No Roses fade quickly', 'All Flowers are Roses', 'B'),
                ('A is taller than B, B is taller than C. Who is the shortest?', 'A', 'B', 'C', 'Cannot be determined', 'C'),
                ('Choose the word that is least like the others: Dog, Cat, Lion, Chair', 'Dog', 'Cat', 'Lion', 'Chair', 'D'),
            ],
        }

        for category_name, questions in data.items():
            category, created = Category.objects.get_or_create(name=category_name)
            for text, a, b, c, d, correct in questions:
                Question.objects.get_or_create(
                    category=category, text=text,
                    defaults={'option_a': a, 'option_b': b, 'option_c': c, 'option_d': d, 'correct_option': correct},
                )

        total_questions = Question.objects.count()
        total_categories = Category.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Done. {total_categories} categories and {total_questions} questions ready.'))
