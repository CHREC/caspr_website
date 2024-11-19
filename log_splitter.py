# Helper script to paste a formatted log string into separate files

upd = '''[2024-10-31]: Demonstrated CASPR operations to visitors from Sandia National Laboratories!
[2024-11-01]: Successfully split compressed Palermo burst on orbit, recompressed in smaller halves, and began downlink!
[2024-11-05]: Began downlink of NIR/R half of Palermo burst!
[2024-11-07]: Demonstrated CASPR operations to visitor from Lockheed Martin!  A few manual transfers of Palermo burst segments.
[2024-11-08]: Completed, recombined, and decompressed Palermo burst on the ground!  Cleared space on GPU system for further experiments, including CNNJPEG!
[2024-11-14]: Successfully decompressed, split, and recompressed New Guinea burst onboard and began downlink!'''

for line in upd.split('\n'):
    date = line.split(']')[0].split('[')[1]
    with open(f"_commandlog/{date}.md", "w") as F:
        F.write(f'---\npubdate: {date}\n---\n\n')
        F.write(line.split(': ')[1])
        F.write('\n')
        