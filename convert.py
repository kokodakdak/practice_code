r = nuke.nodes.Read(file="/project/circle/in/aces_exr/A005C301_160120_R51F/A005C031_160120_R51F.%04d.exr")
w = nuke.nodes.Write(file="/project/circle/in/aces_exr/A005C301_160120_R51F/A005C031_160120_R51F.%04d.jpg")
nuke.execute("Write1",001771,002947)
quit()
