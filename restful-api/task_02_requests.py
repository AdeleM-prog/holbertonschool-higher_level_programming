#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", r.status_code)
    if r.status_code == 200:
        data = r.json()
    for post in data:
        print(post["title"])

def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", r.status_code)
    if r.status_code == 200:
        data = r.json()
        posts_list = []
        for element in data:
            new_dict = {}
            new_dict["id"] = element.get("id")
            new_dict["title"] = element.get("title")
            new_dict["body"] = element.get("body")
            posts_list.append(new_dict)
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_list)
