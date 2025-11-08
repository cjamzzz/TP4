import os

# Replace these with the commit hashes given in your lab
good_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"  # last known good commit
bad_hash = "c1a4be04b972b6c17db242fc37752ad517c29402"  # first bad commit

# Start git bisect between those commits
os.system(f"git bisect start")
os.system(f"git bisect good {good_hash}")
os.system(f"git bisect bad {bad_hash}")

# Run tests automatically on each checked-out commit
os.system("git bisect run python manage.py test")

# Reset to the original state after bisect finishes
os.system("git bisect reset")

# Feature 1 modified by main
