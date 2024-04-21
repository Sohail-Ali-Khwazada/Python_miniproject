# from django.shortcuts import render, HttpResponse
# from . import main





# def home(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('Question')
#         print("Received user input:", user_input)  g
        

#         if user_input:
#             # Call the start function from your Python script to process the user input
#             response = main.start(user_input)
#             return HttpResponse(response)
#         else:
#             return HttpResponse("Error: No user input received")

    # return render(request, "index.html")

from django.shortcuts import render, HttpResponse
from . import main
from .models import Question_Answer

def home(request):
    if request.method == 'POST':
        user_input = request.POST.get('Question')
        print("Received user input:", user_input)
        
        if user_input:
            # Calculate response
            response = main.start(user_input)
            
            # Save new question and answer to the database
            if not response:
                return HttpResponse("Error: No user input received")
            new_qa = Question_Answer(question=user_input, answer=response)
            new_qa.save()
        else:
            return HttpResponse("Error: No user input received")

    # Fetch all Question_Answer objects from the database
    question_answers = Question_Answer.objects.all()

    return render(request, "index.html", {'question_answers': question_answers})

