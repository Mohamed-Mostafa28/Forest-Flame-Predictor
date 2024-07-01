import os

curr=os.getcwd()
libname=os.path.dirname(curr)
print(libname)


# Define directories and files
directories_and_files = [
    'data/source',
    'data/processed',
    "assets",
    'output/models',
    'output/info',
    'output/images',
    "Notebooks",    
    "Notebooks/EDA.ipynb",    
    f"{libname.lower()}/utiles",
    f"{libname.lower()}/src",
    'requirements.txt',
    'README.md',
]

# Create directories and files
for item in directories_and_files:
    if os.path.exists(item):
        print(f"{item} already exists. Skipping...")
        continue
    if '.' in item:
        # It's a file
        directory = os.path.dirname(item)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)  # Ensure parent directories are created
        with open(item, 'w') as f:
            pass  # Create an empty file
        print(f"File created: {item}")
    else:
        # It's a directory
        os.makedirs(item, exist_ok=True)
        print(f"Directory created: {item}")

print("Project structure setup completed!")












