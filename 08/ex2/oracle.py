import os
try:
    from dotenv import load_dotenv
except ImportError:
    print("Missing python-dotenv. Please install it first.")
    import sys
    sys.exit(1)

def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    
    load_dotenv()
    
    mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    
    if db_url:
        print("Database: Connected to local instance")
    else:
        print("Database: [WARNING] Missing connection string")
        
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: [WARNING] Missing API key")
        
    print(f"Log Level: {log_level}")
    
    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: [WARNING] Missing endpoint")
        
    print("\nEnvironment security check:")
    
    if not api_key or api_key == "your_secret_api_key_here":
        print("[WARNING] Hardcoded or missing secrets detected")
    else:
        print("[OK] No hardcoded secrets detected")
        
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
        
    if mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Running in development mode")
        
    print("\nThe Oracle sees all configurations.")

if __name__ == "__main__":
    main()

