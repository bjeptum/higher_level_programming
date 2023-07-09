#!/usr/bin/python3
"""
Takes my GitHub credentials(username and password)
Uses GitHub API to display my id
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python github_user_id.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    url = f'https://api.github.com/users/{username}'
    headers = {'Authorization': f'token {password}'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        user_data = response.json()
        user_id = user_data['id']
        print(f"User ID: {user_id}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyError:
        print("Error: Failed to retrieve user ID.")
        sys.exit(1)
