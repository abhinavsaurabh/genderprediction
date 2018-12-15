from collections import Counter
from sys import argv
from gender_predictor.py import GenderPredictor


def main():
    gp = GenderPredictor()
    accuracy = gp.train_and_test(training_percent=0.80)*100
    features = gp.get_most_informative_features(n=10)


    output = []
    finaloutput = []
    try:
        filename = argv[1]
        output_name = argv[2]
    except:
        print ("Usage: python generate.py <starting-file> <output-file>")
        exit(0)
    with open(filename) as file:
        data = file.readlines()

    # Skip the csv headers
    data = data[1:]
    print ("Read {} names from the file.".format(len(data)))

    # Parse CSV data to Python List
    for d in data:
        name, gender = d.lower().split(',')
        firstname = name.split()[0]  # Take only the first name
        output.append("{},{}".format(firstname, gender))

    withcount = Counter(output)
    for key, value in withcount.items():
        finaloutput.append("{},{}\n".format(key.strip(), value))

    finaloutput.sort()

    with open(output_name, 'w') as finalfile:
        for line in finaloutput:
            finalfile.write(line)
    print ("Completed. Unique Names scraped: {}".format(len(finaloutput)))
    print ("Saved to: %s" % (output_name))

if __name__ == "__main__":
    main()
