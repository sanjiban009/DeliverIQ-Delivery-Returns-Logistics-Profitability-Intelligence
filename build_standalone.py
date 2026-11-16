from pathlib import Path
r=Path(__file__).resolve().parents[1]
s=(r/'index.html').read_text()
s=s.replace('<link rel="stylesheet" href="style.css">','<style>'+(r/'style.css').read_text()+'</style>')
for file in ['data/data.js','app.js']:
 s=s.replace('<script src="'+file+'"></script>','<script>'+r.joinpath(file).read_text().replace('</script','<\\/script')+'</script>')
r.joinpath('DeliverIQ_Standalone.html').write_text(s)
print('Standalone HTML rebuilt')
