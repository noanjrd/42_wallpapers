import os
import math

order = ["ttchermu", "erahal", "cngogang", "cmontaig", "macorso", "fdiop"]
nameofworkinprogress = "mmidalic"


with open("script/READMEpart1.html", "r", encoding="utf-8") as src:
    content = src.read()

with open("script/READMEpart2.html", "r", encoding="utf-8") as src2:
    contentend = src2.read()

content = content.replace("NAMETOBEREPLACED", nameofworkinprogress)
with open("README.md", "w", encoding="utf-8") as readme:
	readme.write(content)


	l = len(order)-1
	# print(math.ceil((l+1)/2))
	for i in range(math.ceil((l+1)/2)):
		html = "	<tr>"
		html += f"""
		<td align="center">
			<img src="./wallpapers/{order[l]}.png" width="400px" alt="{order[l]}"/><br />
			<b>{order[l]}</b>
		</td>"""
		l-=1
		if (l+1 > 0):
			html += f"""
		<td align="center">
			<img src="./wallpapers/{order[l]}.png" width="400px" alt="{order[l]}"/><br />
			<b>{order[l]}</b>
		</td>"""
			l-=1
		html += "\n	</tr>\n"
		readme.write(html)
		
	readme.write("	</table>\n")
	readme.write(contentend)





























a = 0
b = 123456
c = "this does not do anything"
d = [1, 2, 3]
e = {"x": 1, "y": 2}
a = 0
b = 123456
c = "this does not do anything"
d = [1, 2, 3]
e = {"x": 1, "y": 2}
def noop1(): pass
def noop2(): return None
def noop3(x): return x
def noop1(): pass
def noop2(): return None
def noop3(x): return x
for _ in range(10): pass
while False: pass
if True: pass
for _ in range(10): pass
while False: pass
if True: pass

