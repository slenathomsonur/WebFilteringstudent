# Simple Student Web Filter Prototype (Inspired by Linewize)
# This is a basic console-based tool for educational purposes.
# It checks URLs against blocked categories and simulates allowing/blocking access.

# Define blocked categories with example keywords/domains
BLOCKED_CATEGORIES = {
    'adult_content': ['porn', 'adult', 'xvideos', 'pornhub'],
    'violence': ['kill', 'bomb', 'terror', 'fightclub'],
    'social_media': ['facebook', 'instagram', 'tiktok', 'twitter'],
    'gambling': ['casino', 'bet', 'pokerstars'],
}

def is_blocked(url, categories=BLOCKED_CATEGORIES):
    """
    Check if the URL matches any blocked keywords in the categories.
    Returns tuple: (is_blocked: bool, matched_category: str or None)
    """
    url_lower = url.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in url_lower:
                return True, category
    return False, None

def filter_url(url):
    """
    Main filtering function.
    Simulates access decision and logs it.
    """
    blocked, category = is_blocked(url)
    if blocked:
        print(f"ACCESS BLOCKED: {url} matches category '{category}'. This content is not allowed for student safety.")
        print("Logged for monitoring. Potential risk detected.")
    else:
        print(f"ACCESS ALLOWED: {url} is safe for viewing.")
    print("-" * 50)

def main():
    """
    Interactive loop for testing URLs.
    """
    print("Simple Student Web Filter Prototype")
    print("Enter URLs to test (type 'quit' to exit).")
    while True:
        user_input = input("\nEnter a URL: ").strip()
        if user_input.lower() == 'quit':
            break
        if not user_input.startswith(('http://', 'https://')):
            user_input = 'https://' + user_input  # Assume https if not specified
        filter_url(user_input)

if __name__ == "__main__":
    main()
