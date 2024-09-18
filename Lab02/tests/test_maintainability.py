import os

def run_maintainability_tests():
    print("Running pylint for server.py...")
    os.system("pylint ../server/server.py")

    print("\nRunning pylint for client.py...")
    os.system("pylint ../client/client.py")

if __name__ == "__main__":
    run_maintainability_tests()

