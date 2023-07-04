# myapp/views.py
import pandas as pd
from django.shortcuts import render
n=[]
e=[]

def form_submission(request):
    if request.method == 'POST':
        # Extract form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        n.append(name)
        e.append(email)  
        
        # Create a DataFrame to hold the form data
        data = {'Name': n, 'Email': e, }
        df = pd.DataFrame(data)

        # Save DataFrame to Excel
        df.to_excel('data.xlsx', index=False)

        # Render a success template
       
    # Render the form template for GET requests
    return render(request, 'home.html')
