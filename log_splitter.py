# Helper script to paste a formatted log string into separate files

upd = '''[2024-03-20]: Manually completed last few segments of Geelong and Plymouth bursts!  Started downlink of Constitucion burst.  Two more burst targets programmed!
[2024-03-22]: Downlinked new round of radiation-effects data!  Beginning downlink of San Salvador burst!  Two more bursts scheduled!
[2024-03-26]: Down to only four segments remaining for San Salvador burst!  Started downlink of burst near Sanxenxo, Spain!  12 bursts stored onboard!
[2024-03-27]: Lots of burst capture data movement.  Began downlink of Melbourne burst!  Two more burst targets this evening!
[2024-03-29]: Back-to-back manual burst successes near San Juan, Puerto Rico and Cape Canaveral, Florida!  Lots of data operations!  Additional burst attempt scheduled for this evening!'''

for line in upd.split('\n'):
    date = line.split(']')[0].split('[')[1]
    with open(f"_commandlog/{date}.md", "w") as F:
        F.write(f'---\npubdate: {date}\n---\n\n')
        F.write(line.split(': ')[1])
        F.write('\n')
        