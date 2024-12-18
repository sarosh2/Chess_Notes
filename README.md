# Chess Notes

**Chess Notes** is a Python application that helps chess players analyze positions, study openings, and save personal analysis. It integrates chess engines, opening databases, and allows players to store and review lines they've studied.

![image](https://github.com/user-attachments/assets/a56dc972-a1bc-4037-b97c-84db86fb9eb8)


## Requirements

- **Python 3.12.2**  
  Download Python from [here](https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe).
  
- **Python Libraries:**
  - `python-chess` library for chess-related functionality.
  - Install dependencies via pip:
    ```bash
    pip install python-chess
    ```

## Installation

1. **Clone the Repository:**
   Clone the Chess Notes repository to your local machine:
   ```bash
   git clone https://github.com/sarosh2/Chess_Notes.git

## Features

### 1. **Opening Database Compilation**
Chess Notes supports compiling opening books from multiple **Polyglot** `.bin` books. The database I personally used includes a collection of 15.9 million games categorized into six parts.

![image](https://github.com/user-attachments/assets/e1b0a99c-2bf2-4768-a93a-9d5849cf2aa5)


#### Instructions:
- Download the opening book collection from [here](https://sourceforge.net/projects/codekiddy-chess/files/Books/Polyglot%20books/Update1/polyglot-collection.7z/download).
- Extract the downloaded `.7z` archive.
- Copy the extracted files into the **"openings"** folder in the project directory.
- Update the paths for the opening book files in the `config.py` file if necessary.

### 2. **Engine Analysis**
The app integrates with the **Stockfish** chess engine to analyze positions. It provides the evaluation of the current position and suggests future moves with their evaluations.

#### Instructions:
- Download **Stockfish** from [this link](https://github.com/official-stockfish/Stockfish/releases/latest/download/stockfish-windows-x86-64-avx2.zip).
- Extract the folder and place it in the **"engine"** folder of the project.
- Update the path to the Stockfish engine in the `config.py` file if necessary.

### 3. **Saved Lines**
Chess Notes allows you to store and review positions and moves you've personally analyzed and saved. You can go through these lines for further study and analysis.

![image](https://github.com/user-attachments/assets/25527af6-de31-474a-b923-5cf4fc60272e)



### 4. **PGN Game Upload & Analysis**
Upload PGN files of games you've played to Chess Notes and analyze them using the integrated engine.
