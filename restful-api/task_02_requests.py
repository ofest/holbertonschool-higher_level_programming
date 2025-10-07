import csv
import requests

def fetch_and_print_posts():
    """Fetch JSONPlaceholder."""
    
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        
        print("\nTitles of all posts:\n" + "-" * 30)
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")

fetch_and_print_posts()

def fetch_and_save_posts():
    """
    Fetch JSONPlaceholder and save them to a CSV file.
    
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()  
   
        structured_data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(structured_data)
        
        print(f"Successfully saved {len(structured_data)} posts to 'posts.csv'.")
    else:
        print("Failed to fetch posts from API.")

if __name__ == "__main__":
    fetch_and_save_posts()
