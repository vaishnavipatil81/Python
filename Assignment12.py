


# views.py 
from django.shortcuts import render
import re

def login_view(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Regular expression for validation
        username_pattern = r'^[A-Za-z0-9_]{4,15}$'
        password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{6,}$'

        if not re.match(username_pattern, username):
            message = "Invalid Username! (Only letters, numbers, 4–15 chars)"
        elif not re.match(password_pattern, password):
            message = "Weak Password! (Must contain uppercase, lowercase, number, min 6 chars)"
        else:
            message = f"Login Successful! Welcome, {username}"

    return render(request, 'login.html', {'message': message})

#login.html
<!DOCTYPE html>
<html>
<head>
    <title>User Login</title>
    <style>
        body {
            font-family: Arial;
            background: #f0f4f7;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px gray;
            width: 350px;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        input {
            width: 100%;
            padding: 8px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            width: 100%;
            background: #2196f3;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            font-size: 15px;
            cursor: pointer;
        }
        p {
            text-align: center;
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>User Login</h2>
        <form method="POST">
            {% csrf_token %}
            <label>Username:</label>
            <input type="text" name="username" required>

            <label>Password:</label>
            <input type="password" name="password" required>

            <button type="submit">Login</button>
        </form>
        <p>{{ message }}</p>
    </div>
</body>
</html>
