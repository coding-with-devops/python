#Write a program to find out whether a given post is talking about “Harry” or not.
# If yes, then print “Yes” else print “No”.

post = input("Enter the post: ")
if "Harry".lower() in post.lower():
    # Using lower() method to make the comparison case insensitive
    print("Yes, We are talking about Harry.")
else:
    print("No, We are not talking about Harry.")