#!/usr/bin/env python3
"""
Demo Data Script for Barangay Survey Generator
This script creates sample surveys and questions for demonstration purposes
"""

from app import SessionLocal, Survey, Question
from datetime import datetime

def create_demo_data():
    """Create sample surveys and questions for demonstration"""
    
    db = SessionLocal()
    
    try:
        # Create sample survey 1: Community Needs Assessment
        survey1 = Survey(
            title="Community Needs Assessment 2025",
            description="Help us understand the most pressing needs in our barangay to better serve our community.",
            created_at=datetime.utcnow()
        )
        db.add(survey1)
        db.flush()  # Get the ID
        
        # Add questions for survey 1
        questions1 = [
            Question(
                survey_id=survey1.id,
                question_text="What is your age group?",
                question_type="single_choice",
                options="18-25, 26-35, 36-45, 46-55, 56-65, 65+",
                is_required=True,
                order=1
            ),
            Question(
                survey_id=survey1.id,
                question_text="What are the most important issues facing our barangay? (Select all that apply)",
                question_type="multiple_choice",
                options="Road maintenance, Water supply, Waste management, Security, Health services, Education, Employment opportunities, Public transportation",
                is_required=True,
                order=2
            ),
            Question(
                survey_id=survey1.id,
                question_text="How would you rate the current barangay services?",
                question_type="single_choice",
                options="Excellent, Good, Fair, Poor, Very Poor",
                is_required=True,
                order=3
            ),
            Question(
                survey_id=survey1.id,
                question_text="What suggestions do you have to improve our barangay?",
                question_type="text",
                is_required=False,
                order=4
            )
        ]
        
        for question in questions1:
            db.add(question)
        
        # Create sample survey 2: Event Planning
        survey2 = Survey(
            title="Barangay Fiesta Planning Survey",
            description="Help us plan the upcoming barangay fiesta by sharing your preferences and ideas.",
            created_at=datetime.utcnow()
        )
        db.add(survey2)
        db.flush()
        
        # Add questions for survey 2
        questions2 = [
            Question(
                survey_id=survey2.id,
                question_text="Which activities would you like to see during the fiesta? (Select all that apply)",
                question_type="multiple_choice",
                options="Cultural dance competition, Cooking contest, Sports tournament, Talent show, Bingo games, Food fair, Live music, Fireworks display",
                is_required=True,
                order=1
            ),
            Question(
                survey_id=survey2.id,
                question_text="What type of food would you prefer for the community feast?",
                question_type="single_choice",
                options="Traditional Filipino dishes, International cuisine, Local specialties, Vegetarian options, All of the above",
                is_required=True,
                order=2
            ),
            Question(
                survey_id=survey2.id,
                question_text="Would you be willing to volunteer for the fiesta preparations?",
                question_type="single_choice",
                options="Yes, definitely, Maybe, depending on the task, No, but I can help in other ways, No, I cannot participate",
                is_required=True,
                order=3
            ),
            Question(
                survey_id=survey2.id,
                question_text="Any additional suggestions or ideas for the fiesta?",
                question_type="text",
                is_required=False,
                order=4
            )
        ]
        
        for question in questions2:
            db.add(question)
        
        # Create sample survey 3: Health and Safety
        survey3 = Survey(
            title="Health and Safety Awareness Survey",
            description="Help us assess the health and safety needs of our community members.",
            created_at=datetime.utcnow()
        )
        db.add(survey3)
        db.flush()
        
        # Add questions for survey 3
        questions3 = [
            Question(
                survey_id=survey3.id,
                question_text="How often do you visit the barangay health center?",
                question_type="single_choice",
                options="Weekly, Monthly, Every few months, Only when needed, Never",
                is_required=True,
                order=1
            ),
            Question(
                survey_id=survey3.id,
                question_text="What health services would you like to see improved? (Select all that apply)",
                question_type="multiple_choice",
                options="Medical consultations, Vaccination programs, Health education, Emergency services, Dental care, Mental health support, Maternal and child health",
                is_required=True,
                order=2
            ),
            Question(
                survey_id=survey3.id,
                question_text="How safe do you feel in your neighborhood?",
                question_type="single_choice",
                options="Very safe, Somewhat safe, Neutral, Somewhat unsafe, Very unsafe",
                is_required=True,
                order=3
            ),
            Question(
                survey_id=survey3.id,
                question_text="What safety concerns do you have in our barangay?",
                question_type="text",
                is_required=False,
                order=4
            )
        ]
        
        for question in questions3:
            db.add(question)
        
        db.commit()
        print("✅ Demo data created successfully!")
        print(f"📊 Created 3 sample surveys:")
        print(f"   1. Community Needs Assessment 2025")
        print(f"   2. Barangay Fiesta Planning Survey")
        print(f"   3. Health and Safety Awareness Survey")
        print(f"📝 Total questions created: {len(questions1) + len(questions2) + len(questions3)}")
        print("\n🚀 You can now run the application and see the sample surveys!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error creating demo data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_demo_data()
