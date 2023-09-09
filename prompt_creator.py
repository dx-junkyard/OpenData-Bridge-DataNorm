import os
import csv
import argparse

def read_csv_first_two_lines(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as f:
        reader = csv.reader(f)
        header = next(reader)
        # Skip lines that start with "#"
        while header[0].startswith("#"):
            header = next(reader)
        first_row = next(reader)
    return header, first_row

def load_template(file_path="./prompt_template.txt"):
    with open(file_path, 'r') as f:
        return f.read()

def main(directory, master_file):
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    output = []
    master_header, master_first_row = None, None
    slave_data = []
    slave_count = 1

    for file in files:
        file_path = os.path.join(directory, file)
        
        # Detect encoding (SJIS or UTF-8)
        try:
            header, first_row = read_csv_first_two_lines(file_path, 'utf-8')
        except:
            header, first_row = read_csv_first_two_lines(file_path, 'shift_jis')
        
        if file == master_file:
            master_header = header
            master_first_row = first_row
        else:
            slave_data.append((f'slave{slave_count}.csv', header, first_row))
            slave_count += 1

    # Append master.csv definition
    output.append("master.csv")
    output.append("---")
    output.append(",".join(master_header))
    output.append(",".join(master_first_row))
    output.append("---\n")
    
    # Append slave[n].csv definitions
    for slave_file, header, first_row in sorted(slave_data, key=lambda x: x[0]):
        output.append(slave_file)
        output.append("---")
        output.append(",".join(header))
        output.append(",".join(first_row))
        output.append("---\n")
    
    output_str = "\n".join(output)
    
    # Replace [[INPUT]] in the template with the generated output
    template = load_template()
    final_output = template.replace("[[INPUT]]", output_str)
    
    print(final_output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-dir", help="Directory containing CSV files", required=True)
    parser.add_argument("-m", help="Master CSV file", required=True)
    args = parser.parse_args()

    main(args.dir, args.m)

