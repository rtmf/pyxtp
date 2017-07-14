<p>
To build the demo site, resite, simply run:
<ul><li>make</li></ul>
This will produce several files of interest:
<ul><li><b>build/index.html</b> - this is the actual site, which should function live from the build path</li></ul>
<ul><li><b>build/resite.zip</b> - this contains all the files to deploy the site wherever you might like!</li></ul>
</p>
<p>
if you are in windows:
c:\python3\python.exe .\src\xtp.py .\resite\resite.py
this will generate an index.html wherever you are in the filesystem, the makefile keeps things neat in build/
eventually I'll write a .bat or something
</p>
