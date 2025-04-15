print("🔍 WEBSITE URL CHECKER 🔍")
url = input("Enter the URL of the website you want to check: ") # get the URL from the user
print("Checking the URL...") # print a message indicating that the URL is being checked

if url.startswith("https://"):
    print("🔐 This website uses HTTPs (secure)") # 

elif url.startswith("http://"):
    print("🔓 This website uses HTTP (not secure)")
    
else:
    print("❌Invalid URL. Please enter a valid URL starting with http:// or https://")
print("🔍 URL check completed.") # print a message indicating that the URL check is completed