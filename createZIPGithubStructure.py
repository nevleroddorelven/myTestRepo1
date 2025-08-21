import os
import zipfile

# Define the structure
structure = {
    ".github/workflows/": ["deploy-on-jsm-approval.yml"],
    "src/": ["index.js"],
    "": ["README.md", ".gitignore", "package.json"]
}

# Create a temporary folder structure
base_dir = "my-project"
os.makedirs(base_dir, exist_ok=True)

for folder, files in structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "w") as f:
            # Add placeholder content
            if file.endswith(".yml"):
                f.write(
                    "name: Example Workflow\n"
                    "on: push\n"
                    "jobs:\n"
                    "  build:\n"
                    "    runs-on: ubuntu-latest\n"
                    "    steps:\n"
                    "      - run: echo 'Hello world'"
                )
            elif file == "index.js":
                f.write("console.log('Hello from src/index.js');")
            elif file == "README.md":
                f.write("# My Project\n\nThis is a sample project structure.")
            elif file == ".gitignore":
                f.write("node_modules/\n.env")
            elif file == "package.json":
                f.write('{\n  "name": "my-project",\n  "version": "1.0.0"\n}')

# Create a zip file
zip_filename = "my-project-structure.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, base_dir)
            zipf.write(filepath, arcname)

print(f"ZIP file created: {zip_filename}")
