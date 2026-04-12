import os
import subprocess
import requests
import json
from datetime import datetime

# Path setups
CASCADE_DIR = os.path.expanduser("~/CascadeProjects")
SHARE_DIR = os.path.join(CASCADE_DIR, "Share")
INDEX_FILE = os.path.join(SHARE_DIR, "content", "Now", "index.md")

def load_env_shared():
    """Parses ~/.foundry-suite/.env.shared to extract default values."""
    env_path = os.path.expanduser("~/.foundry-suite/.env.shared")
    env_vars = {}
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("export "):
                    # example: export OLLAMA_HOST="${OLLAMA_HOST:-http://home-win-4:11434}"
                    key_val = line[7:].split("=", 1)
                    if len(key_val) == 2:
                        key = key_val[0]
                        val = key_val[1]
                        
                        # Strip shell fallback syntax and quotes
                        if "${" in val:
                            val = val.split(":-")[-1].replace("}", "").replace('"', "")
                        else:
                            val = val.replace('"', '')
                            
                        env_vars[key] = val
    return env_vars

def get_git_activity():
    activity = []
    print("Scanning repositories in", CASCADE_DIR)
    for d in os.listdir(CASCADE_DIR):
        repo_path = os.path.join(CASCADE_DIR, d)
        if os.path.isdir(os.path.join(repo_path, ".git")):
            try:
                # Get last 7 days to capture reasonable activity amount
                out = subprocess.check_output(
                    ["git", "log", "--since=7 days ago", "--oneline"],
                    cwd=repo_path,
                    text=True,
                    stderr=subprocess.DEVNULL
                )
                if out.strip():
                    activity.append(f"Repository {d}:\n{out.strip()}")
            except subprocess.CalledProcessError:
                pass
    return "\n\n".join(activity)

def generate_summary(git_log):
    if not git_log:
        return "- Maintained stable operations across the Foundry ecosystem this week."
    
    env_vars = load_env_shared()
    ollama_host = env_vars.get("OLLAMA_HOST", "http://home-win-4:11434")
    # Using the local primary model specified in the Foundry suite (or fall back to qwen3:8b)
    model = env_vars.get("OLLAMA_PRIMARY_MODEL", "qwen3:8b")
    
    prompt = f"""You are a high-level technical PR agent. Review the following git commits. Do not reveal any specific features, secrets, or exact algorithms. Instead, write 2-3 short, impressive bullet points stating which 'Foundries' saw significant progress this week, using terms like 'architectural hardening', 'pipeline automation', or 'infrastructure scaling'. Keep it professional but vague. Output ONLY the markdown bullet points starting with '-'.

Git Log:
{git_log}"""
    
    url = f"{ollama_host}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3
        }
    }
    
    print(f"Calling local Ollama server ({model} at {ollama_host}) to generate summaries...")
    try:
        resp = requests.post(url, json=payload, timeout=120)
        if resp.status_code == 200:
            return resp.json().get("response", "").strip()
        else:
            print("Ollama API Error:", resp.text)
            return "- Ongoing architecture refinements, pipeline automation, and infrastructural scaling."
    except Exception as e:
        print(f"Ollama Connection Error: {e}")
        return "- Ongoing architecture refinements, pipeline automation, and infrastructural scaling."

def update_now_page(summary):
    if not os.path.exists(INDEX_FILE):
        print(f"Error: {INDEX_FILE} not found.")
        return

    with open(INDEX_FILE, "r") as f:
        content = f.read()

    section_start = "## Active Developments (Automated Pulse)\n"
    section_title_index = content.find(section_start)
    
    new_section = f"{section_start}\n*Last updated: {datetime.now().strftime('%Y-%m-%d')}*\n\n{summary}\n\n"
    
    if section_title_index != -1:
        # Find the next section
        next_section_index = content.find("##", section_title_index + 2)
        if next_section_index != -1:
            content = content[:section_title_index] + new_section + content[next_section_index:]
        else:
            content = content[:section_title_index] + new_section
    else:
        # Insert before '## How to navigate'
        nav_index = content.find("## How to navigate")
        if nav_index != -1:
            content = content[:nav_index] + new_section + content[nav_index:]
        else:
            content += "\n" + new_section
            
    with open(INDEX_FILE, "w") as f:
        f.write(content)
    print("Successfully injected the pulse summary into Now/index.md!")

if __name__ == "__main__":
    print("Gathering Git Activity...")
    git_activity = get_git_activity()
    summary = generate_summary(git_activity)
    print("Summary Generated:\n" + summary)
    update_now_page(summary)
    
    print("Syncing to remote via quartz-sync.sh...")
    try:
        subprocess.run(["./quartz-sync.sh", "Automated Now text pulse update (Local LLM)"], cwd=SHARE_DIR, check=True)
        print("Done!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to sync updates: {e}")
