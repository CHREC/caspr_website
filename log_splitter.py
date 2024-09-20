# Helper script to paste a formatted log string into separate files

upd = '''[2024 09 17]: Successfully downlinked a stored partial burst from near San Antonio, Texas!  Unfortunately, this burst is mainly cloud cover.
[2024 09 20]: Successfully downlinked remaining half of San Juan burst!  Compressed and began downlink of cloudy Pittsburgh burst!'''

for line in upd.split('\n'):
    date = line.split(']')[0].split('[')[1]
    with open(f"_commandlog/{date}.md", "w") as F:
        F.write(f'---\npubdate: {date}\n---\n\n')
        F.write(line.split(': ')[1])
        F.write('\n')
        