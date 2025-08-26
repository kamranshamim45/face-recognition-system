# GitHub Setup Guide for Face Recognition Project

## Step 1: Install Git

Git is not currently installed on your system. You need to install it to push your project to GitHub.

### Download and Install Git:
1. Go to the official Git website: https://git-scm.com/download/win
2. Download the Windows installer
3. Run the installer and follow the installation wizard
   - Use the default settings (recommended for most users)
   - Make sure to select "Git from the command line and also from 3rd-party software" option
   - Complete the installation

### Verify Git Installation:
After installation, open a new Command Prompt or PowerShell window and run:
```cmd
git --version
```

You should see the Git version number if installation was successful.

## Step 2: Initialize Git Repository

Once Git is installed, navigate to your project directory and run:

```cmd
git init
git add .
git commit -m "Initial commit - Face Recognition System"
```

## Step 3: Create GitHub Account (if you don't have one)

1. Go to https://github.com/
2. Sign up for a free account
3. Verify your email address

## Step 4: Create New Repository on GitHub

1. Log in to your GitHub account
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository (e.g., "face-recognition-system")
5. Add a description (optional)
6. Choose public or private visibility
7. **DO NOT** initialize with README (since you already have files)
8. Click "Create repository"

## Step 5: Connect Local Repository to GitHub

Copy the commands from the GitHub repository page (they will look like this):

```cmd
git remote add origin https://github.com/your-username/your-repo-name.git
git branch -M main
git push -u origin main
```

## Step 6: Push Your Code

Run the commands from Step 5 to push your code to GitHub.

## Important Notes:

- Your `.gitignore` file has been created to exclude unnecessary files
- The project contains sensitive files like `classifier.xml` and image data in the `Data/` folder
- Consider whether you want to include the training data in your repository or use Git LFS for large files

## Troubleshooting:

If you encounter authentication issues, you may need to set up Git credentials:
```cmd
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

For SSH authentication (recommended for security):
1. Generate SSH keys: `ssh-keygen -t ed25519 -C "your.email@example.com"`
2. Add SSH key to GitHub: https://github.com/settings/keys
