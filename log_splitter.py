# Helper script to paste a formatted log string into separate files

upd = '''[2024-03-05]: Completed the Chattanooga burst downlink and began another!  One target programmed!
[2024-03-08]: Completed manual downlink of last few segments of coastal burst near Tokyo!  Two more targets programmed!
[2024-03-12]: Poor downlink window today.  Conducting manual imaging and storing on SGPU for use on future ML/CV apps after the move!
[2024-03-13]: Race track near Melbourne, Australia visible in one of the 3/8 bursts!  Began downlink of burst near Plymouth, Massachusetts!  Two more bursts scheduled!'''

for line in upd.split('\n'):
    date = line.split(']')[0].split('[')[1]
    with open(f"_commandlog/{date}.md", "w") as F:
        F.write(f'---\npubdate: {date}\n---\n\n')
        F.write(line.split(': ')[1])
        F.write('\n')
        