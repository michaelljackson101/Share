# Complete Digital Garden Setup Guide
## Quartz v4 + GitHub Pages - Step by Step

This guide walks you through setting up a digital garden exactly like the one at [michaelljackson101.github.io/Share](https://michaelljackson101.github.io/Share). It's based on Quartz v4, a powerful static site generator perfect for personal knowledge management and publishing.

---

## 🎯 What You'll Get

- A personal digital garden website hosted on GitHub Pages
- Markdown-based content management
- Beautiful, responsive design with built-in search
- Automatic deployment when you push changes
- Support for both regular content and direct-link static assets
- Professional setup with GitHub Actions CI/CD

---

## 📋 Prerequisites

1. **GitHub Account** - Free tier is fine
2. **Node.js** - Version 22 or higher (check with `node --version`)
3. **Git** - Basic familiarity with commands
4. **Code Editor** - VS Code recommended

---

## 🍎 MacBook Setup Instructions

### Installing Node.js on macOS

**Option 1: Direct Download (Easiest)**
1. Go to [nodejs.org](https://nodejs.org/)
2. Download the macOS installer (LTS version)
3. Double-click the `.pkg` file and follow installation wizard
4. Restart Terminal and verify: `node --version`

**Option 2: Homebrew (Recommended for developers)**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js
brew install node

# Verify installation
node --version
npm --version
```

**Option 3: Node Version Manager (nvm) - For Multiple Projects**
```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Restart Terminal or run:
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Install and use Node.js 22
nvm install 22
nvm use 22
nvm alias default 22
```

### Git on macOS

Git usually comes pre-installed on macOS. Verify with:
```bash
git --version
```

If not installed, install via Xcode Command Line Tools:
```bash
xcode-select --install
```

### Terminal Tips for macOS

- Use **Terminal.app** (built-in) or download **iTerm2** for better features
- If you use Zsh (default on modern macOS), commands work the same as Bash
- Consider adding these useful aliases to your `~/.zshrc`:
  ```bash
  alias gs="git status"
  alias ga="git add ."
  alias gc="git commit -m"
  alias gp="git push"
  alias ql="npx quartz build --serve"  # Quick local preview
  ```

---

## 🚀 Step 1: Create Your GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it: `Share` (or your preferred name)
3. Make it **Public** (required for GitHub Pages free tier)
4. **Do NOT** initialize with README, .gitignore, or license
5. Click "Create repository"

---

## 🚀 Step 2: Clone Quartz Template

```bash
# Replace YOUR_USERNAME with your GitHub username
git clone https://github.com/jackyzha0/quartz-starter-v4 Share
cd Share

# Set your repository as the remote origin
git remote set-url origin https://github.com/YOUR_USERNAME/Share.git
```

---

## 🚀 Step 3: Install Dependencies

```bash
# Install npm dependencies
npm install

# This may take a few minutes as it downloads Quartz and all dependencies
```

---

## 🚀 Step 4: Configure Your Site

### 4.1 Update Basic Configuration

Edit `quartz.config.ts`:

```typescript
import { QuartzConfig } from "./quartz/cfg"

const config: QuartzConfig = {
  // Replace with your name and site info
  baseUrl: "https://YOUR_USERNAME.github.io/Share",
  pageTitle: "Your Name - Digital Garden",
  description: "A digital garden for my thoughts and notes",
  author: "Your Name",
  
  // Keep the rest of the default configuration for now
  // ... (rest of file)
}

export default config
```

### 4.2 Update Package.json

Edit `package.json` to update repository info:

```json
{
  "name": "@YOUR_USERNAME/share",
  "repository": {
    "type": "git",
    "url": "https://github.com/YOUR_USERNAME/Share.git"
  }
}
```

---

## 🚀 Step 5: Set Up GitHub Pages Deployment

### 5.1 Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** in the left sidebar
4. Under "Build and deployment", set **Source** to **GitHub Actions**

### 5.2 Create Deployment Workflow

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy Quartz site to GitHub Pages

on:
  push:
    branches:
      - v4  # This matches the default Quartz branch

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - name: Install Dependencies
        run: npm ci
      - name: Build Quartz
        run: npx quartz build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: public

  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

---

## 🚀 Step 6: Create Your First Content

### 6.1 Create Index Page

Create `content/index.md`:

```markdown
---
title: Welcome to My Digital Garden
date: 2025-01-01
tags:
  - welcome
---

# Welcome to My Digital Garden

This is my personal space for thoughts, notes, and ideas.

## Getting Started

- Check out the [navigation](/index) to explore content
- Use the search功能 to find specific topics
- Everything is written in Markdown for easy editing

## Recent Notes

Here are some of my recent thoughts and notes...

---

*Built with [Quartz](https://quartz.jzhao.xyz/) and hosted on [GitHub Pages](https://pages.github.com/)*
```

### 6.2 Create Additional Content

Create `content/notes/my-first-note.md`:

```markdown
---
title: My First Note
date: 2025-01-01
tags:
  - personal
  - learning
---

# My First Note

This is my first note in the digital garden. I can write anything here using Markdown!

## Why Digital Gardens?

Digital gardens are great for:
- Capturing thoughts over time
- Connecting ideas
- Personal knowledge management

## Next Steps

- Add more notes
- Organize with tags
- Build connections between ideas
```

---

## 🚀 Step 7: Test Locally (Optional)

```bash
# Start local development server
npx quartz build --serve

# This will start a server at http://localhost:8080
# You can preview your site before pushing
```

---

## 🚀 Step 8: Push to GitHub

```bash
# Add all your changes
git add .

# Commit your changes
git commit -m "Initial setup of digital garden"

# Push to GitHub (this will trigger the deployment)
git push -u origin v4
```

---

## 🚀 Step 9: Wait for Deployment

1. Go to your repository on GitHub
2. Click **Actions** tab to watch the deployment progress
3. After a few minutes, your site will be live at: `https://YOUR_USERNAME.github.io/Share`

---

## 📝 Daily Workflow

### Adding New Content

1. Create new `.md` files in `content/` folder
2. Add frontmatter with title, date, and tags
3. Write content in Markdown
4. Commit and push:

```bash
git add content/
git commit -m "Add new note about [topic]"
git push
```

### Quick Sync Script (Optional)

Create `quartz-sync.sh` for easy commits:

```bash
#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

if [[ -z "$(git status --porcelain)" ]]; then
  echo "No changes to sync."
  exit 0
fi

msg="${1:-}"
if [[ -z "$msg" ]]; then
  ts="$(date '+%Y-%m-%d %H:%M')"
  msg="Quartz sync: $ts"
fi

git add .
git commit -m "$msg"
git push

echo "✅ Changes synced and deployed!"
```

Make it executable:
```bash
chmod +x quartz-sync.sh
```

Now you can simply run:
```bash
./quartz-sync.sh "Added new note about productivity"
```

**macOS Note:** If you get permission errors, you might need to allow the script execution in System Preferences > Security & Privacy, or use:
```bash
chmod +x quartz-sync.sh
./quartz-sync.sh "Added new note about productivity"
```

---

## 🎨 Customization Tips

### Change Theme Colors

Edit `quartz.layout.ts` and look for theme configuration.

### Add Custom CSS

Create `quartz/styles/custom.css` and reference it in your layout config.

### Configure Navigation

Edit `quartz.config.ts` to adjust sidebar, page layout, and components.

---

## 📁 Important File Structure

```
Share/
├── content/              # Your markdown files go here
│   ├── index.md         # Home page
│   ├── notes/           # Organized notes
│   └── static/          # Direct-link assets (HTML, PDFs, etc.)
├── quartz/              # Quartz engine (don't edit)
├── quartz.config.ts     # Main configuration
├── quartz.layout.ts     # Layout and styling
├── .github/workflows/   # GitHub Actions
└── package.json         # Dependencies and scripts
```

---

## 🔧 Advanced Features

### Static Assets

For files you want to directly link (like the Foundry Suite HTML):

1. Place files in `content/static/`
2. Access them at `https://YOUR_USERNAME.github.io/Share/static/filename.html`

### Tags and Categories

Use frontmatter to organize content:

```markdown
---
title: Your Note Title
tags:
  - productivity
  - learning
  - technology
categories:
  - personal-development
---
```

### Linking Between Notes

Use standard Markdown links or Quartz's internal linking:

```markdown
# Link to another note
See my [productivity tips](/notes/productivity-tips)

# Wiki-style link
[[Productivity Tips]]
```

---

## 🚨 Troubleshooting

### Build Fails

1. Check GitHub Actions logs for errors
2. Ensure all Markdown files have proper frontmatter
3. Verify Node.js version compatibility

### Site Not Updating

1. Check if GitHub Actions are running
2. Ensure you're pushing to the correct branch (`v4`)
3. Clear browser cache

### Permission Errors

1. Ensure repository is public
2. Check GitHub Pages is enabled in Settings
3. Verify GitHub Actions permissions

### macOS-Specific Issues

**Node.js Command Not Found**
```bash
# If using Homebrew, ensure PATH is set
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# If using nvm, ensure it's loaded
echo 'source ~/.nvm/nvm.sh' >> ~/.zshrc
source ~/.zshrc
```

**Script Permission Issues**
```bash
# If quartz-sync.sh won't execute
chmod +x quartz-sync.sh

# If still blocked, macOS security might be blocking it
# Go to System Preferences > Security & Privacy > General
# Click "Allow Anyway" if you see a blocked app message
```

**Git Issues on macOS**
```bash
# If Git asks for Xcode tools
xcode-select --install

# Configure Git (first time setup)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 📚 Resources

- [Official Quartz Documentation](https://quartz.jzhao.xyz/)
- [Quartz Discord Community](https://discord.gg/cRFFHYye7t)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)

---

## 🎉 You're Done!

You now have a fully functional digital garden that:

- ✅ Automatically deploys when you push changes
- ✅ Supports rich Markdown content
- ✅ Has built-in search and navigation
- ✅ Works great on mobile and desktop
- ✅ Is completely free to host

Happy writing and gardening! 🌱

---

*This guide is based on the exact setup used for [michaelljackson101.github.io/Share](https://michaelljackson101.github.io/Share). Feel free to adapt it to your needs.*
