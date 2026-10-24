import re, sys
src = open('/home/z/my-project/materials/sempro/dpj4-sibi-csi/bab3-metodologi.md').read()
blocks = re.findall(r'```mermaid\n(.*?)```', src, re.S)
for i, b in enumerate(blocks, 1):
    open(f'gambar-3.{i}.mmd', 'w').write(b)
    print(f'gambar-3.{i}.mmd: {len(b)} chars')
