import subprocess
import sys
import os

def main():
    # Get the list of staged files.
    result = subprocess.run(['git', 'diff', '--cached', '--name-only', '--diff-filter=ACM'], capture_output=True, text=True)
    
    html_folder = "Controle de versao"

    # Get all the HTML files in the html folder.
    html_files = [file for file in result.stdout.split('\n') if file.startswith(html_folder) and file.endswith('.html')]

    if html_files:
        print("Linting HTML files...")

        for file in html_files:
            # Run htmlhint on each file.
            result = subprocess.run(['htmlhint', file])

            # If htmlhint returns a non-zero exit code, exit the script.
            if result.returncode != 0:
                print(f"HTML linting failed for {file}. Please fix the errors and commit again.")
                sys.exit(1)

        print("All HTML files passed linting.")
    else:
        print("No HTML files to lint.")

if __name__ == '__main__':
    main()
