import sys
import os
import site

def is_in_venv() -> bool:
    """Check, if Python is working in virtual env."""
    return sys.prefix != sys.base_prefix

def main() -> None:
    current_python = sys.executable

    if is_in_venv():
        env_path = sys.prefix
        env_name = os.path.basename(env_path)
        site_packages = site.getsitepackages()[0]
        
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(site_packages)
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("Then run this program again.")

if __name__ == "__main__":
    main()
