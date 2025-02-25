import zipfile
import os

def create_protected_zip(input_file, output_zip, password):
    # Create a ZipFile object
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Set the password
        zipf.setpassword(password.encode())
        # Add the file to the zip
        zipf.write(input_file, os.path.basename(input_file))
        
def protect_zip(input_zip, output_zip, password):
    # Create a ZipFile object
    with zipfile.ZipFile(input_zip, 'r') as zipf:
        # Set the password
        zipf.setpassword(password.encode())
        
def test():
    output_zip = "c:/Users/22sebali/Desktop/Important/cybersäkerhet/ctf-220s-grupp/This/protected.zip"
    password = "ivuffuygf"  # Replace with your desired password
    protect_zip(output_zip, output_zip, password)
    print(f"Successfully protected ZIP file: {output_zip}")

def main():
        # Example usage
    input_file = "c:/Users/22sebali/Desktop/Important/cybersäkerhet/ctf-220s-grupp/This/moose-alg-modified.png" # Get absolute path of input file
    output_zip = "c:/Users/22sebali/Desktop/Important/cybersäkerhet/ctf-220s-grupp/This/protected.zip"
    password = "password"  # Replace with your desired password
    try:
        create_protected_zip(input_file, output_zip, password)
        print(f"Successfully created encrypted ZIP file: {output_zip}")
    except Exception as e:
        print(f"Error: {e}")
        
main()
