import os

all_files = os.listdir(".");
mods = []

for fl in all_files:
	if fl.endswith(".jar"):
		mods.append(fl)

with open("mods.txt", "w") as f:
	f.write("\n".join(mods))
