import sys
import importlib

def check_and_get_version(module_name: str) -> str | None:
    """Check if module is existing with version."""
    try:
        mod = importlib.import_module(module_name)
        return getattr(mod, "__version__", "unknown")
    except ImportError:
        return None

def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    
    deps = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization"
    }
    
    all_ready = True
    for mod, desc in deps.items():
        version = check_and_get_version(mod)
        if version:
            print(f"[OK] {mod} ({version})")
            print(f"{desc} ready")
        else:
            all_ready = False
            
    req_version = check_and_get_version("requests")
    if req_version:
        print(f"[OK] requests ({req_version})")
        print("Network access ready")
        
    if not all_ready:
        print("\nMissing dependencies detected!")
        print("Install via pip: pip install -r requirements.txt")
        print("Install via Poetry: poetry install")
        sys.exit(1)
        
    print("\nAnalyzing Matrix data...")
    
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
    
    print("Processing 1000 data points...")
    data = np.random.rand(1000, 2)
    df = pd.DataFrame(data, columns=['x', 'y'])
    
    print("Generating visualization...")
    plt.figure(figsize=(8, 6))
    plt.scatter(df['x'], df['y'], c='green', alpha=0.5)
    plt.title("Matrix Data Simulation")
    plt.savefig("matrix_analysis.png")
    
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")

if __name__ == "__main__":
    main()
