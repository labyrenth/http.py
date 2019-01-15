
import pyshark

out_string=""
cap=pyshark.LiveCapture(interface='eth0',only_summaries="ip")
cap.sniff(timeout=10)
#cap=sniff()
i=1
for pkt in cap:
    out_file=open("date.txt","w")
    out_string += str(pkt)
    out_string += "\n"
    out_file.write(out_string)
    i = i + 1
cap.close()
