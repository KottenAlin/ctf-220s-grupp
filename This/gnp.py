def read_gnp_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'GNP.gnp'
read_gnp_file(file_path)
