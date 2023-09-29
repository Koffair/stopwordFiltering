from src.remove_stopwords import filter_words

if __name__ == "__main__":
    import os
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="the path to the input directory")
    parser.add_argument("-o", "--output", help="the path to the output directory")
    parser.add_argument("-s", "--stopfile", default="data/hungarian_swear_words.txt",
                        help="the path to the stop/swear words")
    args = parser.parse_args()

    txt_files = [os.path.join(args.input, f) for f in os.listdir(args.input)
                 if os.path.isfile(os.path.join(args.input, f))]
    for txt_file in txt_files:
        filtered_text = filter_words(txt_file, args.stopfile)
        fname = txt_file.split("/")[-1]
        filtered_file = os.path.join(args.output, fname)
        with open(filtered_file, "w") as outfile:
            outfile.write(filtered_text)
