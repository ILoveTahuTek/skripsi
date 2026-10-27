#!/usr/bin/env python3
"""Patch footer PAGE field dengan format switch (WPS compat) + hapus pgNumType kosong.
Footer romawi (rata tengah) -> PAGE \\* roman; footer arab (rata kanan) -> PAGE \\* arabic."""
import re, shutil, zipfile

path = '/home/z/my-project/download/translator-sibi-docx/Proposal-Penerjemah-Dua-Arah-SIBI-CSI-ESP32S3.docx'
tmp = path + '.tmp'

zin = zipfile.ZipFile(path, 'r')
zout = zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED)
patched = []

for item in zin.infolist():
    data = zin.read(item.filename)
    if item.filename.startswith('word/footer') and item.filename.endswith('.xml'):
        xml = data.decode('utf-8')
        if 'PAGE' in xml:
            if 'w:val="center"' in xml:
                xml2 = re.sub(r'(<w:instrText[^>]*>)\s*PAGE\s*(</w:instrText>)',
                              r'\1 PAGE \\* roman \\* MERGEFORMAT \2', xml)
                tag = 'roman'
            elif 'w:val="right"' in xml:
                xml2 = re.sub(r'(<w:instrText[^>]*>)\s*PAGE\s*(</w:instrText>)',
                              r'\1 PAGE \\* arabic \\* MERGEFORMAT \2', xml)
                tag = 'arabic'
            else:
                xml2, tag = xml, None
            if xml2 != xml:
                patched.append((item.filename, tag))
                data = xml2.encode('utf-8')
    elif item.filename == 'word/document.xml':
        xml = data.decode('utf-8')
        n = xml.count('<w:pgNumType/>')
        if n:
            xml = xml.replace('<w:pgNumType/>', '')
            patched.append(('document.xml', f'pgNumType-kosong-dihapus x{n}'))
            data = xml.encode('utf-8')
    zout.writestr(item, data)

zin.close()
zout.close()
shutil.move(tmp, path)
print('Dipatch:', patched if patched else 'tidak ada perubahan')
