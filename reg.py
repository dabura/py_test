import re
import io

#2016.11.18. 22:20:58: ERROR: A00332985729: System.Exception: NFW hiba (Warning): ErrorOperationFailed
lines = io.open(r'log_sbsvc_20161118_ERROR.log')
i = 0
for line in lines:
    regex = r"(.*): ERROR: (.*): System.Exception:.*ErrorOperationFailed"
    matches = re.findall(regex, line)
    for match in matches:
         i += 1
         print('idopont: %s, sorszam: %s, tksz: %s' % (match[0], i, match[1]))
