import webbrowser

user_term = input('Provide search term: ').replace(' ', '+')

webbrowser.open(f'https://www.google.com/search?q={user_term}')
