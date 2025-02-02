# Create a new branch for your fix/feature
git checkout -b fix/footer-link

# Edit the file (e.g., Footer.js) in your code editor (VS Code, Sublime, etc.)
code src/components/Footer.js  # Opens VS Code

# Stage the modified file
git add src/components/Footer.js

# Commit the changes with a descriptive message
git commit -m "Fix broken link in footer"

# Push the branch to your GitHub fork
git push origin fix/footer-link