# Project Workflow & Git Guide

## Part 1: How to Initialize Git (One-Time Setup per Project)
You only need to do this **once** when starting a brand new project folder from scratch:

1. Open your project folder in VS Code (`File > Open Folder...`).
2. Open the terminal inside VS Code (press `` Ctrl + ` ``).
3. Run these commands one by one:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git push -u origin main
```
*(Make sure to replace the GitHub URL with your actual repository link).*

---

## Part 2: What to Do When You Sit Near Your Project Again (Daily Routine)
Whenever you come back to work on your project later, follow this simple **Start-Work & End-Work** routine:

### 📥 Step A: BEFORE you start coding (Pull the latest changes)
If you worked on the project from another computer or want to make sure your local folder is up to date, run:
```bash
git pull
```

### 💻 Step B: WHILE you work (Write code normally)
Do your coding, modify your scripts, add new CSV files, and test things in VS Code as you normally would.

### 🚀 Step C: AFTER you finish working (Save and sync to GitHub)
When you are done for the day and want to save your progress to GitHub, follow these 3 quick steps:

1. **Stage your changes** (tell Git which files to track):
   * *In the terminal:* Type `git add .`
   * *Alternative in VS Code:* Click the **Source Control** icon on the left sidebar (branch icon) and click the `+` icon next to "Changes".
2. **Commit your changes** (add a label explaining what you did):
   * *In the terminal:* Type `git commit -m "Describe what you changed here"`
   * *Alternative in VS Code:* Type your message in the text box at the top of the Source Control panel and click the blue **Commit** button.
3. **Push to GitHub** (upload your saved work):
   * *In the terminal:* Type `git push`
   * *Alternative in VS Code:* Click the **Sync Changes** button (or the three dots `...` menu -> **Push**).