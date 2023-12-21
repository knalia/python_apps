import requests

def get_github_users(token):
     # Set headers for request using access token
     headers = {
         'Authorization': f'Token {token}',
         'Accept': 'application/vnd.github.v3+json',
     }

     # Endpoint URL to get a list of users
     endpoint = 'https://api.github.com/users?per_page=100'
    

     # Execute the request
     response = requests.get(endpoint, headers=headers)

     # Check the success of the request
     if response.status_code == 200:
         print(response.status_code)
         # Return data in JSON format
         return response.json()
     else:
         # Display an error message
         print(f"Error: {response.status_code}, {response.text}")

# Replace 'YOUR_GITHUB_TOKEN' with your GitHub token
github_token = 'YOUR_TOKEN'
users = get_github_users(github_token)

# Display a list of users
for user in users:
     print(user['login'])
