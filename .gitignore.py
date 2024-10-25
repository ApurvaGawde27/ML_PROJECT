# Define patterns to ignore (customize as needed)
gitignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Logs and databases
*.log
*.sql
*.sqlite

# Unit test / coverage reports
.coverage
.tox/
.nox/
"""

# Write content to .gitignore file
with open('.gitignore', 'w') as file:
    file.write(gitignore_content)

print(".gitignore file created.")
