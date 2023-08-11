import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="text file for color scheme to convert")
parser.add_argument(
    "--to",
    help="color scheme source type, used to determine the destination type. subl2code will infer from file extension, but this helps.",
)

args = parser.parse_args()

filepath = args.file
source_type = args.to
supported_source = ["subl", "code"]

if not source_type:
    source_type = get_source_type(filepath)
else:
    if source_type not in supported_source:
        print(
            f"ERROR: the --to argument must be a supported source type, currently only {supported_source}"
        )
        exit(1)

if source_type == "code":
    to_subl(filepath)
elif source_type == "subl":
    to_code(filepath)
