def load_list(csv_file):
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            # Assuming the 'Word' column is in the first position (index 0)
            for row in reader:
                word_list.append(row[0])    
        print("Words loaded successfully!")
        print("Words List:", word_list)
    except FileNotFoundError:
        print(f"File '{csv_file}' not found.")
    except Exception as e:
        print("An error occurred:", str(e))
