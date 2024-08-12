# Helper script to paste a formatted log string into separate files

upd = '''[2024-05-24]: Downlinking single-frame images stored in memory from previous CASPR location!  Began downlink of Santo Domingo burst!
[2024-05-31]: Began downlink of San Juan burst!  Tested image conversion commands for coming app upload.
[2024-06-06]: Successfully uploaded CNNJPEG image compression app for on-orbit study!  Shout out to Diego and Tyler for their hard work!
[2024-06-14]: Began downlink of Merritt Island burst!  Collected another round of radiation-effects data.
[2024-06-21]: Completed downlink of Santo Domingo burst!  Unique cityscape with multiple airports!
[2024-06-28]: Completed downlink of San Juan burst!  Unexpected parts of denser urban area visible further down the frame!
[2024-07-19]: Downlinking second half of Merritt Island burst!
[2024-07-26]: Acquired last few lost segments of first half of Merritt Island burst!  Halfway there!
[2024-08-02]: Debugging a slight anomaly with second half of Merritt Island burst.  This one is worth the fight, though!
[2024-08-09]: Completed downlink of Merritt Island burst!  Began downlink of Palermo, Italy burst!'''

for line in upd.split('\n'):
    date = line.split(']')[0].split('[')[1]
    with open(f"_commandlog/{date}.md", "w") as F:
        F.write(f'---\npubdate: {date}\n---\n\n')
        F.write(line.split(': ')[1])
        F.write('\n')
        