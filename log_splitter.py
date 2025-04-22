# Helper script to paste a formatted log string into separate files

upd = '''[2025-03-28]: Working to resolve an issue with SSP1 and grainy image burst capture.  Also performed some diagnostics on SGPU swap space for CNNJPEG!
[2025-03-31]: Conducted extensive flatsat testing to help resolve a CNNJPEG bug dealing with limited storage memory and swap size.
[2025-04-03]: Demonstrated CASPR operations to SHREC Members from Northrup Grumman!  Thank you very much for your visit and support!
[2025-04-07]: Members of the CASPR team attended the National Conference on Undergraduate Research in Pittsburgh to help recruit the next incoming class of Pitt Space graduate engineers!
[2025-04-08]: Showcased CASPR commanding to Pitt ECE Distinguished Speaker Dr. Don Tan!  Thank you very much for sharing your time and knowledge with SHREC!
[2025-04-10]: Provided CASPR data and experiment updates to Pitt Space Distinguished Speaker Dr. Andrew Horchler!  Thank you very much for your visit and insight!
[2025-04-18]: Resolved limited storage issue for CNNJPEG processing!  Successfully completed first three layers of compression!'''

for line in upd.split('\n'):
    date = line.split(']')[0].split('[')[1]
    with open(f"_commandlog/{date}.md", "w") as F:
        F.write(f'---\npubdate: {date}\n---\n\n')
        F.write(line.split(': ')[1])
        F.write('\n')
        