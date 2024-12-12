# Helper script to paste a formatted log string into separate files

upd = '''[2024-12-10]: Downlinked another round of radiation-effects data from CSP and SSPs!  Preparing for on-orbit CNNJPEG tests, but this has been delayed slightly due to high beta angle and resultant high temperatures.'''

for line in upd.split('\n'):
    date = line.split(']')[0].split('[')[1]
    with open(f"_commandlog/{date}.md", "w") as F:
        F.write(f'---\npubdate: {date}\n---\n\n')
        F.write(line.split(': ')[1])
        F.write('\n')
        