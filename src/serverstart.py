from app import application
import argparse
from app.data import DataStrategy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    DataStrategy.initializeDataStrategy(args.data)
    if args.debug:
        application.run(host='0.0.0.0', port=5000, debug=True)
    else:
        application.run(host='0.0.0.0', port=5000, debug=False)

