import os

# Save a message and automatically run the git routine
commit_message = "Auto-update from Spyder"

print("Syncing with GitHub...")
os.system("!git add .")
os.system(f'!git commit -m "{commit_message}"')
os.system("!git push origin main")
print("Done!")