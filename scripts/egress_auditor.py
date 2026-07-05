import os
import re
import sys
import hashlib
import subprocess

# Modular Regex Capability (Adapted from Parser-Foundry)
RESTRICTED_PATTERNS = {
    "AWS_ACCESS_KEY": r"(?i)AKIA[0-9A-Z]{16}",
    "INTERNAL_IP": r"10\.\d{1,3}\.\d{1,3}\.\d{1,3}",
    "PROPRIETARY_MARKER": r"(?i)\b(PROPRIETARY|INTERNAL ONLY|CONFIDENTIAL)\b",
    # Add more patterns here as the capability matures
}

# Modular Hashing Capability (Adapted from file-integrity-checker)
BLACKLISTED_HASHES = set([
    # Add MD5 or SHA256 hashes of known internal docs/images here
    # e.g., "d41d8cd98f00b204e9800998ecf8427e",
])

def hash_file(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def get_staged_files():
    result = subprocess.run(['git', 'diff', '--cached', '--name-only'], stdout=subprocess.PIPE, text=True)
    return [f for f in result.stdout.splitlines() if f.strip() and os.path.exists(f)]

def scan_file(filepath):
    # Check File Hash
    file_hash = hash_file(filepath)
    if file_hash in BLACKLISTED_HASHES:
        return f"File matches blacklisted cryptographic hash (Integrity Check Failed)."

    # Check Regex Patterns for Text Files
    if filepath.endswith('.md') or filepath.endswith('.txt') or filepath.endswith('.html'):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for rule_name, pattern in RESTRICTED_PATTERNS.items():
                if re.search(pattern, content):
                    return f"Content matched restricted regex pattern: {rule_name}"
        except UnicodeDecodeError:
            pass # Skip binary files

    return None

def main():
    print("[EGRESS AUDITOR] Scanning staged files for sensitive data...")
    staged_files = get_staged_files()
    
    if not staged_files:
        sys.exit(0)
    
    violations = []
    for filepath in staged_files:
        error = scan_file(filepath)
        if error:
            violations.append((filepath, error))

    if violations:
        print("\n" + "="*50)
        print("🚨 EGRESS VIOLATION DETECTED 🚨")
        print("="*50)
        for fp, err in violations:
            print(f"File: {fp}\nReason: {err}\n")
        print("Publishing suspended. Please remediate the sensitive data and try again.")
        sys.exit(1)
        
    print("[EGRESS AUDITOR] All checks passed. Safe to publish.")
    sys.exit(0)

if __name__ == "__main__":
    main()
