# vim: set syntax=python ts=2 sw=2 noet:
pages														= {  
		"resume.fodt"								:	{
				"template"							:	"o:resume",
				"data"									:	[
						"resume"						,
					]											,
			}													,
		"index.html"								: {
				"template"							:	"h:index",
				"data"									: [
						"resume"						,
					]											,
			}													,
		"resume.html"								: {
				"template"							:	"h:resume",
				"data"									: [
						"resume"						,
					]											,
			}													,
	}															# end of pages
data														= {
		"resume"										: {
				"fullname"							:	"Quinn Morrighan Storm",
				"phone"									:	[
						"+1.415.756.6327"		,
						"+1.702.550.2984"		,
										],
				"email"			: [
						"rtmf@beautifulsunrise.org"		,
						"quinn@tymestl.org"		,
						"livinglatexkali@gmail.com"		,
						],
				"bullets"		: [
					{
						"title"	:	"Core Competencies",
						"items"	:	[
							"Project Management"		,
							"Systems Administration"		,
							"Software Development"		,
							"Networking"		,
							"Dev/OPS"		,
							"IT Support"		,
							"Community Management"		,
							"Hardware Engineering"		,
							]
						},
					{
						"title"	:	"Languages",
						"items"	:	[
							"Python"		,
							"C, C++, Objective-C"		,
							"Bash, ZSH, sed, awk, grep, etc."		,
							"HTML, XHTML, CSS"		,
							"Java"		,
							"PHP"		,
							"Javascript, JQuery, Node"		,
							"MySQL"		,
							]
						},
					{
						"title"	:	"Software Packages",
						"items"	:	[
							"GDB, Valgrind, strace"		,
							"CVS, SVN, GIT, Gitlab"		,
							"Apache"		,
							"Postfix, Dovecot, Cyrus"		,
							"OpenVPN, StrongSwan"		,
							"Systemd"		,
							"APT, dpkg, pacman, makepkg"		,
							"Autotools"		,
							]
						},
					],
				"experience": [
						{
							"name"	:	"Beautiful Sunrise Solutions",
							"title"	:	"Founder",
							"from"	:	"December, 2013",
							"until"	:	"Present",
							"duties": [
							"Under this name, I have begun building a business centered around F/OSS consulting, seeking to offer comprehensive services as a true generalist. "		,
							"So far, my clients have included tasks ranging from Dev/Ops for growing e-commerce site written in django, java for android for a telepresence robot, migrating a microfactory from windows to linux and more."		,
								],
							},
						{
							"name"	:	"Robots Everywhere",
							"title"	:	"Minion",
							"from"	:	"November, 2012",
							"until"	:	"Present",
							"desc": [
								"I&apos;ve been engaged as a consultant with this small NASA contractor based out of San Rafael California, a staunch supporter of Open Hardware and Software specializing in automation itself and therefore the research, development, and just-in-time manufacturing of almost anything imaginable." 
								],
							"duties":[
							"Electronic design, prototyping, and assembly (Analog/audio and digital), PCB layout"		,
							"Micro-controller hardware design and software development (MSP430, Arduino, Propeller)"		,
							"3D printer maintenance and operation, Android software in Java, Linux/Windows Desktop Software in C with GTK"		,
							"Custom software integration including hardware support and implementation of reverse engineered protocols"		,
								],
							},
						{
							"name"	:	"Concordia Collective",
							"title"	:	"Co-Founder",
							"from"	:	"October, 2009",
							"until"	:	"Present",
							"desc": [
							"A collection of improbable people working together to design a more interesting future for us all"		,
								],
							},
						{
							"name"	:	"Bluepulse",
							"title"	:	"Production Engineer",
							"from"	:	"July, 2008",
							"until"	:	"October, 2008",
							"desc": [
							"Sole administrator responsible for the entire production infrastructure of this social messaging provider."		,
							],
							"duties": [
							"Linux system administration on Ubuntu"		,
							"General IT work, set up office wireless network, set up Ubuntu desktop machines, etc."		,
							"Tool development in Bash/sed/AWK/grep for general systems administration and infrastructure"		,
								],
							},
						{
								"name"	:	"Everex",
								"title"	:	"F/OSS Advocate",
								"from"	:	"November, 2007",
								"until"	:	"April, 2008",
								"desc"	: [
							"Lead in-house developer and all-around advocate for the PC manufacturer&apos;s debut in the Linux-based netbook market"		,
							],
								"duties": [
							"Created Linux drivers in C to support wifi hardware from x86 disassembly alone"		,
							"Custom integration and systems deployment for Linux-based netbook product, one of the first to sell in Wal*Mart"		,
									],
								},
						{
								"name"	:	"VMware",
								"title"	:	"Software Engineer",
								"from"	:	"July, 2007",
								"until"	:	"October, 2007",
								"desc"	:	[
									"Member of the tools team supporting internal development and process for the virtualization giant"		,
									],
								"duties": [
							"Build and install system development in C, Perl, Bash"		,
							"Internal development infrastructure tools creation support and integration"		,
									],
								},
						{
								"name"	:	"Beryl",
								"title"	:	"BDFL",
								"from"	:	"May, 2006",
								"until"	:	"April, 2007",
								"desc"	:	[
							"Creator and leader of the team responsible for this Compiz fork that finally brought the wobbly windows out of the shadows and onto your desktop!"		,
							],
								"duties": [
							"Managed an international team of open source software developers via IRC, e-mail and XMPP"		,
							"Created the modular Emerald window decorator and accompanying Emerald Theme Manager frontend"		,
							"Created configuration architecture library libberylsettings and autogenerated frontend application//"		,
							"Created and maintained Debian style APT repositories containing Ubuntu packages, with automated package generation scripts"		,
							"Hosted and managed development infrastructure, including source control through CVS, SVN and GIT and custom tools"		,
							"Read each new post on the Beryl forums and replied to over 90% of them personally to provide individual support"		,
									]
							},
					],
				},
		"resume.fodt"		:	{
				"officedoc"	:	"""
												xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" 
												xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" 
												xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" 
												xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" 
												xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" 
												xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" 
												xmlns:xlink="http://www.w3.org/1999/xlink" 
												xmlns:dc="http://purl.org/dc/elements/1.1/"
												xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0"
												xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0"
												xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0"
												xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0"
												xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0"
												xmlns:math="http://www.w3.org/1998/Math/MathML"
												xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0"
												xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0"
												xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0"
												xmlns:ooo="http://openoffice.org/2004/office"
												xmlns:ooow="http://openoffice.org/2004/writer"
												xmlns:oooc="http://openoffice.org/2004/calc"
												xmlns:dom="http://www.w3.org/2001/xml-events"
												xmlns:xforms="http://www.w3.org/2002/xforms"
												xmlns:xsd="http://www.w3.org/2001/XMLSchema"
												xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
												xmlns:rpt="http://openoffice.org/2005/report"
												xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2"
												xmlns:xhtml="http://www.w3.org/1999/xhtml"
												xmlns:grddl="http://www.w3.org/2003/g/data-view#"
												xmlns:officeooo="http://openoffice.org/2009/office"
												xmlns:tableooo="http://openoffice.org/2009/table"
												xmlns:drawooo="http://openoffice.org/2010/draw"
												xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0"
												xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0"
												xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0"
												xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0"
												xmlns:css3t="http://www.w3.org/TR/css3-text/" 
												office:version="1.2" 
												office:mimetype="application/vnd.oasis.opendocument.text"
											""",
			}
		}
templates   = {
		"h:level"		:	"""
										<style>
											.level${level} {
												font-size:${size};
												flex-direction:column;
												}
											${extra:+.level${level}.${extra}}${_}
										</style>
									""",
			"h:validation":"""
					<a style="margin:0;border:0;padding:0" href="http://validator.w3.org/check/referer">
						<img style="margin:0;border:0;padding:0;width:88px;height:31px"
							src="http://tymestl.org/~rtmf/images/valid-html5-blue.svg"
							alt="Valid HTML5!" />
					</a>
					<a style="margin:0;border:0;padding:0" href="http://jigsaw.w3.org/css-validator/check/referer">
						<img style="margin:0;border:0;padding:0;width:88px;height:31px"
							src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
							alt="Valid CSS!" />
					</a>
			""",
		"h:head"		:	"""
										<head>
											<meta charset="utf-8" />
											<title>${title}</title>
											<style type="text/css">
												html {
													position:relative;
													margin:0;
													padding:0;
													border:0;
													float:none;
													font-style:normal;
													font-family:Sans;
													box-sizing:border-box;
													display:flex;
												}
													body {
													height:100%;
													}
												.underborder {
													border-top:0px;
													border-left:0px;
													border-right:0px;
													border-bottom:1.5px;
													border-color:#000000;
													border-style:solid;
													width:100%;
												}
												.right {
													text-align:right;
													float:right;
													margin-left:auto
													}
												.header {
													font-size:150%;
													font-weight:bold;
													flex-direction:row;
													flex-grow:0;
													}
												.paperdoc {
													margin-right:0.5in;
													margin-right:0.5in;
													width:8.5in;
													height:11in;
													}
												.viewport {
													flex-direction:column;
													overflow:scroll;	
													}
												.section {
													flex-direction:column;
													}
												.block {
													flex-grow:1;
													margin:0.125in;
													}
												.dot {
													width:0.3in;
													text-align:right;
													}
												.one {
													width:100%;
													margin-right:auto;
													display:flex;
													flex-direction:row;
													}
												.half {
													width:50%;
													display:inline-flex;
													flex-direction:row;
													}
												.quarter {
													width:25%;
													display:inline-flex;
													flex-direction:row;
													}
											</style>
											<h:level level="0" size="14pt" />
											<h:level level="1" size="10pt" extra="header">
												 {
													margin-left:auto;
													margin-right:auto;
													text-align:center;
													}
											</h:level>
											<h:level level="2" size="8pt" extra="header">
												 {
													font-style:italic;
													margin:0px;
													text-align:left;
													}
											</h:level>
											<h:level level="3" size="8pt"/>
										</head>
									""",
		"h:html"		:	"""
		<!DOCTYPE html>
		<html lang="en">${_}</html>""",
		"h:doc"			:	"""
										<h:html>
											<h:head title="${fullname}'s Resume" />
											<body>
												<div>
													${_}
												</div>
											</body>
										</h:html>
									""",
									"h:resume":"""
										<h:doc title="${fullname}'s Resume">
		<div class="paperdoc">
				<h:block level="1" title="${fullname}">
															<h:block level="2" title="Contact Information">
																<h:1>
																	<h:quarter><h:a div="half" scheme="tel" __="phone" /></h:quarter>
																	<h:a div="quarter" scheme="mailto" __="email" />
																</h:1>
															</h:block>
															<h:bulletlist __="bullets" />
															<h:position __="experience" />
														</h:block>
											</div>
											</h:doc>
									""",
		"h:paper"		:	"""
										<iframe src="resume.html" style="width:100%;height:100%">
																				</iframe>
									""",
		"h:block"		:	"""
										<div class="level${level:-0} section">
											<div class="level${level:-0} underborder">
												<div class="level${level:-0} header">
													${title}
													${right:+<div class="level${level:-0} right header">${right}</div>}
												</div>
											</div>
											<div class="level${level:-0} block">
												${_}
											</div>
										</div>
									""",
		"h:div"			:	"""<div class="${class}">${_}${__}</div>""",
		"h:half"				:	"""<h:div class="half">${_}${__}</h:div>""",
		"h:quarter"				:	"""<h:div class="quarter">${_}${__}</h:div>""",
		"h:1"				:	"""<h:div class="one">${_}</h:div>""",
		"h:section"	:	"""
										<h:block level="2" ${right:+right="${right}"} title="${title}">
											${_}
										</h:block>
									""",
		"h:duty"		:	"""<h:1>${‣:+<span class="dot">${‣}</span>}${.}</h:1>
									""",
		"h:position": """
										<h:section title="${name} — ${title}" right="${from} — ${until}">
											<h:duty __="duties" />
										</h:section>
									""",
		"h:bullet"	:	"""<h:quarter />""",
		"h:bullets"	:	"""
										<h:1><h:bullet __="___" /></h:1>
									""",
		"h:bulletlist"	: """
										<h:section title="${title}">
											<h:bullets __="items" _#_="4"/>
										</h:section>
									""",
					"h:a"	:	"""
										<h:div class="${div}">
												<a href="${scheme}${__}">
														${__}
												</a>
										</h:div>
										""",
		"h:index"	: """
										<h:doc title="${fullname}'s Resume">
											<h:block level="1" title="${fullname}'s Resume">
												<h:block level="2" title="Available Formats">
													The following are generated with 
													<a href="https://github.com/rtmf/pyxtp">PyXTP</a> 
													and LibreOffice, 
													PyXTP generates both resume.html and resume.fodt,
													LibreOffice is used to convert these to various formats.
												</h:block>
												<h:block level="2" title="Preview Display">
													<h:paper>
										
													</h:paper>
												</h:block>
												<h:block level="2" title="Validation">
													<h:validation />
												</h:block>`
											</h:block>
										</h:doc>
									""",
		"o:dtd"			: """<?xml version="1.0" encoding="UTF-8"?>\n""",
		"o:meta"			: """
										<office:meta>
										<meta:generator>
										LibreOffice/5.3.2.2$Linux_X86_64 LibreOffice_project/30m0$Build-2</meta:generator>
										<dc:title/>
										<dc:description/>
										<dc:subject/>
										<meta:initial-creator/>
										<dc:creator/>
										<meta:creation-date>
										2017-05-02T05:50:00Z</meta:creation-date>
										<dc:date>
										2017-05-02T05:50:00Z</dc:date>
										<meta:print-date>
										1900-01-01T00:00:00Z</meta:print-date>
										<meta:editing-cycles>
										23</meta:editing-cycles>
										<meta:editing-duration>
										PT1080S</meta:editing-duration>
										<meta:document-statistic meta:character-count="3856" meta:non-whitespace-character-count="3287" meta:page-count="1" meta:paragraph-count="7" meta:row-count="27" meta:word-count="576"/>
										<meta:template xlink:type="simple" xlink:actuate="onRequest" xlink:title="" xlink:href="resume.odt/Normal.dotm"/>
										</office:meta>
									""",
		"o:settings"	: """
									 <office:settings>
										<config:config-item-set config:name="ooo:view-settings">
										 <config:config-item config:name="ViewAreaTop" config:type="long">0</config:config-item>
										 <config:config-item config:name="ViewAreaLeft" config:type="long">0</config:config-item>
										 <config:config-item config:name="ViewAreaWidth" config:type="long">22156</config:config-item>
										 <config:config-item config:name="ViewAreaHeight" config:type="long">14501</config:config-item>
										 <config:config-item config:name="ShowRedlineChanges" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="InBrowseMode" config:type="boolean">false</config:config-item>
										 <config:config-item-map-indexed config:name="Views">
											<config:config-item-map-entry>
											 <config:config-item config:name="ViewId" config:type="string">view2</config:config-item>
											 <config:config-item config:name="ViewLeft" config:type="long">9620</config:config-item>
											 <config:config-item config:name="ViewTop" config:type="long">1822</config:config-item>
											 <config:config-item config:name="VisibleLeft" config:type="long">0</config:config-item>
											 <config:config-item config:name="VisibleTop" config:type="long">0</config:config-item>
											 <config:config-item config:name="VisibleRight" config:type="long">22154</config:config-item>
											 <config:config-item config:name="VisibleBottom" config:type="long">14499</config:config-item>
											 <config:config-item config:name="ZoomType" config:type="short">0</config:config-item>
											 <config:config-item config:name="ViewLayoutColumns" config:type="short">1</config:config-item>
											 <config:config-item config:name="ViewLayoutBookMode" config:type="boolean">false</config:config-item>
											 <config:config-item config:name="ZoomFactor" config:type="short">75</config:config-item>
											 <config:config-item config:name="IsSelectedFrame" config:type="boolean">false</config:config-item>
											 <config:config-item config:name="AnchoredTextOverflowLegacy" config:type="boolean">false</config:config-item>
											</config:config-item-map-entry>
										 </config:config-item-map-indexed>
										</config:config-item-set>
										<config:config-item-set config:name="ooo:configuration-settings">
										 <config:config-item config:name="PrintProspect" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="PrintLeftPages" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="PrintPageBackground" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="PrintControls" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="PrintAnnotationMode" config:type="short">0</config:config-item>
										 <config:config-item config:name="PrintGraphics" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="PrintRightPages" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="PrintFaxName" config:type="string"/>
										 <config:config-item config:name="PrintPaperFromSetup" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="PrintTextPlaceholder" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="ApplyParagraphMarkFormatToNumbering" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="PrintReversed" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="TabOverMargin" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="EmbedFonts" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="SurroundTextWrapSmall" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="BackgroundParaOverDrawings" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="ClippedPictures" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="FloattableNomargins" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="EmbedSystemFonts" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="TabOverflow" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="PrintTables" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="PrintSingleJobs" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="SmallCapsPercentage66" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="CollapseEmptyCellPara" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="RsidRoot" config:type="int">2002116</config:config-item>
										 <config:config-item config:name="TreatSingleColumnBreakAsPageBreak" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="MathBaselineAlignment" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="AddFrameOffsets" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="IsLabelDocument" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="PrinterName" config:type="string"/>
										 <config:config-item config:name="OutlineLevelYieldsNumbering" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="IgnoreFirstLineIndentInNumbering" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="UpdateFromTemplate" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="PrintBlackFonts" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="TableRowKeep" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="EmbeddedDatabaseName" config:type="string"/>
										 <config:config-item config:name="IgnoreTabsAndBlanksForLineCalculation" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="UseOldPrinterMetrics" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="InvertBorderSpacing" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="SaveGlobalDocumentLinks" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="TabsRelativeToIndent" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="Rsid" config:type="int">2002116</config:config-item>
										 <config:config-item config:name="PrintProspectRTL" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="PrintEmptyPages" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="ApplyUserData" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="PrintHiddenText" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="AddParaTableSpacingAtStart" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="FieldAutoUpdate" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="UseOldNumbering" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="AddParaTableSpacing" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="CharacterCompressionType" config:type="short">0</config:config-item>
										 <config:config-item config:name="SaveVersionOnClose" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="ChartAutoUpdate" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="PrinterIndependentLayout" config:type="string">high-resolution</config:config-item>
										 <config:config-item config:name="IsKernAsianPunctuation" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="UseFormerObjectPositioning" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="AddVerticalFrameOffsets" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="UnbreakableNumberings" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="AllowPaddingWithoutBorders" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="StylesNoDefault" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="LinkUpdateMode" config:type="short">1</config:config-item>
										 <config:config-item config:name="AlignTabStopPosition" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="DoNotJustifyLinesWithManualBreak" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="SubtractFlysAnchoredAtFlys" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="AddParaSpacingToTableCells" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="AddExternalLeading" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="CurrentDatabaseDataSource" config:type="string"/>
										 <config:config-item config:name="AllowPrintJobCancel" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="ProtectForm" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="UseFormerLineSpacing" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="PrintDrawings" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="UseFormerTextWrapping" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="UnxForceZeroExtLeading" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="TabAtLeftIndentForParagraphsInList" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="RedlineProtectionKey" config:type="base64Binary"/>
										 <config:config-item config:name="PropLineSpacingShrinksFirstLine" config:type="boolean">true</config:config-item>
										 <config:config-item config:name="ConsiderTextWrapOnObjPos" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="DoNotResetParaAttrsForNumFont" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="CurrentDatabaseCommandType" config:type="int">0</config:config-item>
										 <config:config-item config:name="LoadReadonly" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="DoNotCaptureDrawObjsOnPage" config:type="boolean">false</config:config-item>
										 <config:config-item config:name="CurrentDatabaseCommand" config:type="string"/>
										 <config:config-item config:name="PrinterSetup" config:type="base64Binary"/>
										 <config:config-item config:name="ClipAsCharacterAnchoredWriterFlyFrames" config:type="boolean">false</config:config-item>
										</config:config-item-set>
									 </office:settings>
									""",
		"o:scripts"		: """
 <office:scripts>
  <office:script script:language="ooo:Basic">
   <ooo:libraries xmlns:ooo="http://openoffice.org/2004/office" xmlns:xlink="http://www.w3.org/1999/xlink"/>
  </office:script>
 </office:scripts>
									""",
		"o:fonts"			: """
									 <office:font-face-decls>
										<style:font-face style:name="Wingdings 2" svg:font-family="&apos;Wingdings 2&apos;" style:font-family-generic="roman" style:font-pitch="variable" style:font-charset="x-symbol"/>
										<style:font-face style:name="Wingdings" svg:font-family="Wingdings" style:font-family-generic="system" style:font-pitch="variable" style:font-charset="x-symbol"/>
										<style:font-face style:name="StarSymbol" svg:font-family="StarSymbol" style:font-family-generic="system"/>
										<style:font-face style:name="Times New Roman" svg:font-family="&apos;Times New Roman&apos;" style:font-family-generic="roman" style:font-pitch="variable"/>
										<style:font-face style:name="Arial" svg:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable"/>
										<style:font-face style:name="Lucida Sans Unicode" svg:font-family="&apos;Lucida Sans Unicode&apos;" style:font-family-generic="swiss" style:font-pitch="variable"/>
										<style:font-face style:name="Tahoma" svg:font-family="Tahoma" style:font-family-generic="swiss" style:font-pitch="variable"/>
										<style:font-face style:name="Verdana" svg:font-family="Verdana" style:font-family-generic="swiss" style:font-pitch="variable"/>
										<style:font-face style:name="Lucida Grande" svg:font-family="&apos;Lucida Grande&apos;" style:font-family-generic="system" style:font-pitch="variable"/>
									 </office:font-face-decls>
									""",
		"o:styles"		: """
									 <office:styles>
										<style:default-style style:family="graphic">
										 <style:graphic-properties draw:stroke="solid" svg:stroke-width="0.0138in" svg:stroke-color="#2f528f" draw:stroke-linejoin="miter" svg:stroke-linecap="butt" draw:fill-color="#4472c4" fo:wrap-option="wrap" draw:shadow-offset-x="0.1181in" draw:shadow-offset-y="0.1181in" draw:start-line-spacing-horizontal="0.1114in" draw:start-line-spacing-vertical="0.1114in" draw:end-line-spacing-horizontal="0.1114in" draw:end-line-spacing-vertical="0.1114in" style:flow-with-text="false"/>
										 <style:paragraph-properties fo:line-height="100%" fo:text-align="start" style:text-autospace="ideograph-alpha" style:line-break="strict" style:writing-mode="lr-tb" style:font-independent-line-spacing="false">
											<style:tab-stops/>
										 </style:paragraph-properties>
										 <style:text-properties fo:font-variant="normal" fo:text-transform="none" style:use-window-font-color="true" style:text-outline="false" style:text-line-through-style="none" style:text-line-through-type="none" style:text-position="0% 100%" style:font-name="Times New Roman" fo:font-size="10pt" fo:letter-spacing="normal" fo:language="en" fo:country="US" fo:font-style="normal" style:text-underline-style="none" fo:font-weight="normal" style:letter-kerning="false" style:font-name-asian="Times New Roman" style:font-size-asian="10pt" style:language-asian="en" style:country-asian="US" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-name-complex="Times New Roman" style:font-size-complex="10pt" style:language-complex="ar" style:country-complex="SA" style:font-style-complex="normal" style:font-weight-complex="normal" style:text-emphasize="none" style:text-scale="100%" style:font-relief="none"/>
										</style:default-style>
										<style:default-style style:family="paragraph">
										 <style:paragraph-properties fo:line-height="100%" fo:text-align="start" style:justify-single-word="false" fo:keep-together="auto" fo:orphans="2" fo:widows="2" fo:hyphenation-ladder-count="no-limit" fo:break-before="auto" fo:break-after="auto" fo:background-color="transparent" fo:padding="0in" fo:border="none" style:shadow="none" fo:keep-with-next="auto" text:number-lines="true" text:line-number="0" style:text-autospace="ideograph-alpha" style:punctuation-wrap="hanging" style:line-break="strict" style:tab-stop-distance="0.75in" style:snap-to-layout-grid="true" style:writing-mode="lr-tb">
											<style:background-image/>
										 </style:paragraph-properties>
										 <style:text-properties fo:font-variant="normal" fo:text-transform="none" style:use-window-font-color="true" style:text-outline="false" style:text-line-through-style="none" style:text-line-through-type="none" style:text-position="0% 100%" style:font-name="Times New Roman" fo:font-size="10pt" fo:letter-spacing="normal" fo:language="en" fo:country="US" fo:font-style="normal" style:text-underline-style="none" fo:font-weight="normal" style:letter-kerning="false" fo:background-color="transparent" style:font-name-asian="Times New Roman" style:font-size-asian="10pt" style:language-asian="en" style:country-asian="US" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-name-complex="Times New Roman" style:font-size-complex="10pt" style:language-complex="ar" style:country-complex="SA" style:font-style-complex="normal" style:font-weight-complex="normal" style:text-emphasize="none" style:text-combine="none" style:text-scale="100%" style:font-relief="none" fo:hyphenate="true"/>
										</style:default-style>
										<style:default-style style:family="table">
										 <style:table-properties table:border-model="collapsing"/>
										</style:default-style>
										<style:default-style style:family="table-row">
										 <style:table-row-properties fo:keep-together="auto"/>
										</style:default-style>
										<style:style style:name="Standard" style:family="paragraph" style:class="text"/>
										<style:style style:name="Heading" style:family="paragraph" style:parent-style-name="Normal" style:next-style-name="Body_20_Text" style:class="text">
										 <style:paragraph-properties fo:margin-top="0.1665in" fo:margin-bottom="0.0835in" loext:contextual-spacing="false" fo:hyphenation-ladder-count="no-limit" fo:keep-with-next="always"/>
										 <style:text-properties style:font-name="Arial" fo:font-family="Arial" style:font-family-generic="swiss" style:font-pitch="variable" fo:font-size="14pt" style:font-size-asian="14pt" style:font-size-complex="14pt" fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Text_20_body" style:display-name="Text body" style:family="paragraph" style:parent-style-name="Standard" style:class="text">
										 <style:paragraph-properties fo:margin-top="0in" fo:margin-bottom="0.0972in" loext:contextual-spacing="false" fo:line-height="120%"/>
										</style:style>
										<style:style style:name="Heading_20_1" style:display-name="Heading 1" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Body_20_Text" style:default-outline-level="1" style:class="text">
										 <style:paragraph-properties fo:hyphenation-ladder-count="no-limit"/>
										 <style:text-properties fo:font-size="18pt" fo:font-weight="bold" style:font-size-asian="18pt" style:font-weight-asian="bold" style:font-size-complex="18pt" style:font-weight-complex="bold" fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Heading_20_2" style:display-name="Heading 2" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Body_20_Text" style:default-outline-level="2" style:class="text">
										 <style:paragraph-properties fo:margin-top="0.139in" fo:margin-bottom="0in" loext:contextual-spacing="false" fo:hyphenation-ladder-count="no-limit"/>
										 <style:text-properties fo:font-size="16pt" fo:font-weight="bold" style:font-size-asian="16pt" style:font-weight-asian="bold" style:font-size-complex="16pt" style:font-weight-complex="bold" fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Heading_20_3" style:display-name="Heading 3" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Body_20_Text" style:default-outline-level="3" style:class="text">
										 <style:paragraph-properties fo:margin-top="0.0972in" fo:margin-bottom="0in" loext:contextual-spacing="false" fo:hyphenation-ladder-count="no-limit"/>
										 <style:text-properties fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Normal" style:family="paragraph">
										 <style:paragraph-properties fo:orphans="0" fo:widows="0" fo:hyphenation-ladder-count="no-limit"/>
										 <style:text-properties fo:font-size="12pt" style:font-name-asian="Lucida Sans Unicode" style:font-family-asian="&apos;Lucida Sans Unicode&apos;" style:font-family-generic-asian="swiss" style:font-pitch-asian="variable" style:font-size-asian="12pt" style:font-name-complex="Tahoma" style:font-family-complex="Tahoma" style:font-family-generic-complex="swiss" style:font-pitch-complex="variable" style:font-size-complex="12pt" style:language-complex="en" style:country-complex="US" fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Body_20_Text" style:display-name="Body Text" style:family="paragraph" style:parent-style-name="Normal">
										 <style:paragraph-properties fo:margin-top="0in" fo:margin-bottom="0.0835in" loext:contextual-spacing="false" fo:hyphenation-ladder-count="no-limit"/>
										 <style:text-properties fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="List" style:family="paragraph" style:parent-style-name="Body_20_Text" style:class="list">
										 <style:paragraph-properties fo:hyphenation-ladder-count="no-limit"/>
										 <style:text-properties fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Caption" style:family="paragraph" style:parent-style-name="Normal" style:class="extra">
										 <style:paragraph-properties fo:margin-top="0.0835in" fo:margin-bottom="0.0835in" loext:contextual-spacing="false" fo:hyphenation-ladder-count="no-limit" text:number-lines="false" text:line-number="0"/>
										 <style:text-properties fo:font-style="italic" style:font-style-asian="italic" style:font-style-complex="italic" fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Index" style:family="paragraph" style:parent-style-name="Normal" style:class="index">
										 <style:paragraph-properties fo:hyphenation-ladder-count="no-limit" text:number-lines="false" text:line-number="0"/>
										 <style:text-properties fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Table_20_Contents" style:display-name="Table Contents" style:family="paragraph" style:parent-style-name="Normal" style:class="extra">
										 <style:paragraph-properties fo:hyphenation-ladder-count="no-limit" text:number-lines="false" text:line-number="0"/>
										 <style:text-properties fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Table_20_Heading" style:display-name="Table Heading" style:family="paragraph" style:parent-style-name="Table_20_Contents" style:class="extra">
										 <style:paragraph-properties fo:text-align="center" style:justify-single-word="false" fo:hyphenation-ladder-count="no-limit"/>
										 <style:text-properties fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold" fo:hyphenate="false"/>
										</style:style>

										<style:style style:name="Quotations" style:family="paragraph" style:parent-style-name="Normal" style:class="html">
										 <style:paragraph-properties fo:margin-left="0.3937in" fo:margin-right="0.3937in" fo:margin-top="0in" fo:margin-bottom="0.1965in" loext:contextual-spacing="false" fo:hyphenation-ladder-count="no-limit" fo:text-indent="0in" style:auto-text-indent="false">
											<style:tab-stops/>
										 </style:paragraph-properties>
										 <style:text-properties fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Title" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Body_20_Text" style:class="chapter">
										 <style:paragraph-properties fo:text-align="center" style:justify-single-word="false" fo:hyphenation-ladder-count="no-limit"/>
										 <style:text-properties fo:font-size="28pt" fo:font-weight="bold" style:font-size-asian="28pt" style:font-weight-asian="bold" style:font-size-complex="28pt" style:font-weight-complex="bold" fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Subtitle" style:family="paragraph" style:parent-style-name="Heading" style:next-style-name="Body_20_Text" style:class="chapter">
										 <style:paragraph-properties fo:margin-top="0.0417in" fo:margin-bottom="0in" loext:contextual-spacing="false" fo:text-align="center" style:justify-single-word="false" fo:hyphenation-ladder-count="no-limit"/>
										 <style:text-properties fo:font-size="18pt" style:font-size-asian="18pt" style:font-size-complex="18pt" fo:hyphenate="false"/>
										</style:style>
										<style:style style:name="Default_20_Paragraph_20_Font" style:display-name="Default Paragraph Font" style:family="text"/>
										<style:style style:name="WW8Num1z0" style:family="text">
										 <style:text-properties style:font-name="Lucida Grande" fo:font-family="&apos;Lucida Grande&apos;" style:font-family-generic="system" style:font-pitch="variable" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num1z1" style:family="text">
										 <style:text-properties style:font-name="Wingdings 2" fo:font-family="&apos;Wingdings 2&apos;" style:font-family-generic="roman" style:font-pitch="variable" style:font-charset="x-symbol" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num1z2" style:family="text">
										 <style:text-properties style:font-name="StarSymbol" fo:font-family="StarSymbol" style:font-family-generic="system" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num1z3" style:family="text">
										 <style:text-properties style:font-name="Wingdings" fo:font-family="Wingdings" style:font-family-generic="system" style:font-pitch="variable" style:font-charset="x-symbol" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num2z0" style:family="text">
										 <style:text-properties style:font-name="Lucida Grande" fo:font-family="&apos;Lucida Grande&apos;" style:font-family-generic="system" style:font-pitch="variable" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num2z1" style:family="text">
										 <style:text-properties style:font-name="Wingdings 2" fo:font-family="&apos;Wingdings 2&apos;" style:font-family-generic="roman" style:font-pitch="variable" style:font-charset="x-symbol" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num2z2" style:family="text">
										 <style:text-properties style:font-name="StarSymbol" fo:font-family="StarSymbol" style:font-family-generic="system" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num2z3" style:family="text">
										 <style:text-properties style:font-name="Wingdings" fo:font-family="Wingdings" style:font-family-generic="system" style:font-pitch="variable" style:font-charset="x-symbol" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num3z0" style:family="text"/>
										<style:style style:name="WW8Num3z1" style:family="text"/>
										<style:style style:name="WW8Num3z2" style:family="text"/>
										<style:style style:name="WW8Num3z3" style:family="text"/>
										<style:style style:name="WW8Num3z4" style:family="text"/>
										<style:style style:name="WW8Num3z5" style:family="text"/>
										<style:style style:name="WW8Num3z6" style:family="text"/>
										<style:style style:name="WW8Num3z7" style:family="text"/>
										<style:style style:name="WW8Num3z8" style:family="text"/>
										<style:style style:name="WW8Num4z0" style:family="text">
										 <style:text-properties style:font-name="Lucida Grande" fo:font-family="&apos;Lucida Grande&apos;" style:font-family-generic="system" style:font-pitch="variable" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num4z1" style:family="text">
										 <style:text-properties style:font-name="Wingdings 2" fo:font-family="&apos;Wingdings 2&apos;" style:font-family-generic="roman" style:font-pitch="variable" style:font-charset="x-symbol" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num4z2" style:family="text">
										 <style:text-properties style:font-name="StarSymbol" fo:font-family="StarSymbol" style:font-family-generic="system" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num4z3" style:family="text">
										 <style:text-properties style:font-name="Wingdings" fo:font-family="Wingdings" style:font-family-generic="system" style:font-pitch="variable" style:font-charset="x-symbol" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num5z0" style:family="text">
										 <style:text-properties style:font-name="Lucida Grande" fo:font-family="&apos;Lucida Grande&apos;" style:font-family-generic="system" style:font-pitch="variable" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num5z1" style:family="text">
										 <style:text-properties style:font-name="Wingdings 2" fo:font-family="&apos;Wingdings 2&apos;" style:font-family-generic="roman" style:font-pitch="variable" style:font-charset="x-symbol" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num5z2" style:family="text">
										 <style:text-properties style:font-name="StarSymbol" fo:font-family="StarSymbol" style:font-family-generic="system" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num5z3" style:family="text">
										 <style:text-properties style:font-name="Wingdings" fo:font-family="Wingdings" style:font-family-generic="system" style:font-pitch="variable" style:font-charset="x-symbol" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num6z0" style:family="text">
										 <style:text-properties style:font-name="Lucida Grande" fo:font-family="&apos;Lucida Grande&apos;" style:font-family-generic="system" style:font-pitch="variable" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num6z1" style:family="text">
										 <style:text-properties style:font-name="Wingdings 2" fo:font-family="&apos;Wingdings 2&apos;" style:font-family-generic="roman" style:font-pitch="variable" style:font-charset="x-symbol" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num6z2" style:family="text">
										 <style:text-properties style:font-name="StarSymbol" fo:font-family="StarSymbol" style:font-family-generic="system" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="WW8Num6z3" style:family="text">
										 <style:text-properties style:font-name="Wingdings" fo:font-family="Wingdings" style:font-family-generic="system" style:font-pitch="variable" style:font-charset="x-symbol" fo:font-size="9pt" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="Bullet_20_Symbols" style:display-name="Bullet Symbols" style:family="text">
										 <style:text-properties style:font-name="StarSymbol" fo:font-family="StarSymbol" style:font-family-generic="system" fo:font-size="9pt" style:font-name-asian="StarSymbol" style:font-family-asian="StarSymbol" style:font-family-generic-asian="system" style:font-size-asian="9pt" style:font-name-complex="StarSymbol" style:font-family-complex="StarSymbol" style:font-family-generic-complex="system" style:font-size-complex="9pt"/>
										</style:style>
										<style:style style:name="Hyperlink" style:family="text">
										 <style:text-properties fo:color="#000080" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" style:text-underline-mode="continuous" style:text-overline-mode="continuous" style:text-line-through-mode="continuous"/>
										</style:style>
										<style:style style:name="Numbering_20_Symbols" style:display-name="Numbering Symbols" style:family="text"/>
										<text:outline-style style:name="Outline">
										 <text:outline-level-style text:level="1" style:num-format="">
											<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
											 <style:list-level-label-alignment text:label-followed-by="nothing" fo:text-indent="-0.3in" fo:margin-left="0.3in"/>
											</style:list-level-properties>
										 </text:outline-level-style>
										 <text:outline-level-style text:level="2" style:num-format="">
											<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
											 <style:list-level-label-alignment text:label-followed-by="nothing" fo:text-indent="-0.4in" fo:margin-left="0.4in"/>
											</style:list-level-properties>
										 </text:outline-level-style>
										 <text:outline-level-style text:level="3" style:num-format="">
											<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
											 <style:list-level-label-alignment text:label-followed-by="nothing" fo:text-indent="-0.5in" fo:margin-left="0.5in"/>
											</style:list-level-properties>
										 </text:outline-level-style>
										 <text:outline-level-style text:level="4" style:num-format="">
											<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
											 <style:list-level-label-alignment text:label-followed-by="listtab"/>
											</style:list-level-properties>
										 </text:outline-level-style>
										 <text:outline-level-style text:level="5" style:num-format="">
											<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
											 <style:list-level-label-alignment text:label-followed-by="listtab"/>
											</style:list-level-properties>
										 </text:outline-level-style>
										 <text:outline-level-style text:level="6" style:num-format="">
											<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
											 <style:list-level-label-alignment text:label-followed-by="listtab"/>
											</style:list-level-properties>
										 </text:outline-level-style>
										 <text:outline-level-style text:level="7" style:num-format="">
											<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
											 <style:list-level-label-alignment text:label-followed-by="listtab"/>
											</style:list-level-properties>
										 </text:outline-level-style>
										 <text:outline-level-style text:level="8" style:num-format="">
											<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
											 <style:list-level-label-alignment text:label-followed-by="listtab"/>
											</style:list-level-properties>
										 </text:outline-level-style>
										 <text:outline-level-style text:level="9" style:num-format="">
											<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
											 <style:list-level-label-alignment text:label-followed-by="listtab"/>
											</style:list-level-properties>
										 </text:outline-level-style>
										 <text:outline-level-style text:level="10" style:num-format="">
											<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">
											 <style:list-level-label-alignment text:label-followed-by="listtab"/>
											</style:list-level-properties>
										 </text:outline-level-style>
										</text:outline-style>
										<text:notes-configuration text:note-class="footnote" style:num-format="1" text:start-value="0" text:footnotes-position="page" text:start-numbering-at="document"/>
										<text:notes-configuration text:note-class="endnote" style:num-format="i" text:start-value="0"/>
										<text:linenumbering-configuration text:number-lines="false" text:offset="0.1965in" style:num-format="1" text:number-position="left" text:increment="5"/>
										<style:default-page-layout>
										 <style:page-layout-properties fo:border="none" fo:padding="0in" style:writing-mode="lr-tb" style:layout-grid-standard-mode="true"/>
										</style:default-page-layout>
									 </office:styles>
									""",
		"o:automatic"	:	"""
										<office:automatic-styles>
											<style:style style:name="Table1" style:family="table" style:master-page-name="MP0">
											 <style:table-properties style:width="7.6979in" fo:margin-left="0.0201in" style:page-number="auto" table:align="left"/>
											</style:style>
											<style:style style:name="Table1.A" style:family="table-column">
											 <style:table-column-properties style:column-width="7.6979in"/>
											</style:style>
											<style:style style:name="Table1.A1" style:family="table-cell">
											 <style:table-cell-properties fo:padding="0.0201in" fo:border="none" style:writing-mode="lr-tb"/>
											</style:style>
											<style:style style:name="Table1.3" style:family="table-row">
											 <style:table-row-properties style:min-row-height="2.1785in" style:use-optimal-row-height="false"/>
											</style:style>
											<style:style style:name="Table2" style:family="table">
											 <style:table-properties style:width="7.6576in" fo:margin-left="0in" table:align="left"/>
											</style:style>
											<style:style style:name="Table2.A" style:family="table-column">
											 <style:table-column-properties style:column-width="0.125in"/>
											</style:style>
											<style:style style:name="Table2.B" style:family="table-column">
											 <style:table-column-properties style:column-width="0.4236in"/>
											</style:style>
											<style:style style:name="Table2.C" style:family="table-column">
											 <style:table-column-properties style:column-width="0.8021in"/>
											</style:style>
											<style:style style:name="Table2.D" style:family="table-column">
											 <style:table-column-properties style:column-width="0.8021in"/>
											</style:style>
											<style:style style:name="Table2.E" style:family="table-column">
											 <style:table-column-properties style:column-width="1.6042in"/>
											</style:style>
											<style:style style:name="Table2.F" style:family="table-column">
											 <style:table-column-properties style:column-width="1.6042in"/>
											</style:style>
											<style:style style:name="Table2.G" style:family="table-column">
											 <style:table-column-properties style:column-width="2.0278in"/>
											</style:style>
											<style:style style:name="Table2.H" style:family="table-column">
											 <style:table-column-properties style:column-width="0.1229in"/>
											</style:style>
											<style:style style:name="Table2.A1" style:family="table-cell">
											 <style:table-cell-properties style:vertical-align="bottom" fo:padding="0.0201in" fo:border="none" style:writing-mode="lr-tb"/>
											</style:style>
											<style:style style:name="Table2.2" style:family="table-row">
											 <style:table-row-properties style:min-row-height="0.2069in" style:use-optimal-row-height="false"/>
											</style:style>
											<style:style style:name="Table3" style:family="table">
											 <style:table-properties style:width="7.6576in" fo:margin-left="0in" table:align="left"/>
											</style:style>
											<style:style style:name="Table3.A" style:family="table-column">
											 <style:table-column-properties style:column-width="0.125in"/>
											</style:style>
											<style:style style:name="Table3.B" style:family="table-column">
											 <style:table-column-properties style:column-width="0.4264in"/>
											</style:style>
											<style:style style:name="Table3.C" style:family="table-column">
											 <style:table-column-properties style:column-width="1.6042in"/>
											</style:style>
											<style:style style:name="Table3.D" style:family="table-column">
											 <style:table-column-properties style:column-width="1.6042in"/>
											</style:style>
											<style:style style:name="Table3.E" style:family="table-column">
											 <style:table-column-properties style:column-width="1.6042in"/>
											</style:style>
											<style:style style:name="Table3.F" style:family="table-column">
											 <style:table-column-properties style:column-width="1.6042in"/>
											</style:style>
											<style:style style:name="Table3.G" style:family="table-column">
											 <style:table-column-properties style:column-width="0.4236in"/>
											</style:style>
											<style:style style:name="Table3.H" style:family="table-column">
											 <style:table-column-properties style:column-width="0.1229in"/>
											</style:style>
											<style:style style:name="Table3.A1" style:family="table-cell">
											 <style:table-cell-properties style:vertical-align="bottom" fo:padding="0.0201in" fo:border="none" style:writing-mode="lr-tb"/>
											</style:style>
											<style:style style:name="Table3.2" style:family="table-row">
											 <style:table-row-properties style:min-row-height="0.2069in" style:use-optimal-row-height="false"/>
											</style:style>
											<style:style style:name="Table4" style:family="table">
											 <style:table-properties style:width="7.6576in" fo:margin-left="0in" table:align="left"/>
											</style:style>
											<style:style style:name="Table4.A" style:family="table-column">
											 <style:table-column-properties style:column-width="0.125in"/>
											</style:style>
											<style:style style:name="Table4.B" style:family="table-column">
											 <style:table-column-properties style:column-width="0.4264in"/>
											</style:style>
											<style:style style:name="Table4.C" style:family="table-column">
											 <style:table-column-properties style:column-width="1.6042in"/>
											</style:style>
											<style:style style:name="Table4.D" style:family="table-column">
											 <style:table-column-properties style:column-width="1.6042in"/>
											</style:style>
											<style:style style:name="Table4.E" style:family="table-column">
											 <style:table-column-properties style:column-width="1.6042in"/>
											</style:style>
											<style:style style:name="Table4.F" style:family="table-column">
											 <style:table-column-properties style:column-width="1.6042in"/>
											</style:style>
											<style:style style:name="Table4.G" style:family="table-column">
											 <style:table-column-properties style:column-width="0.4236in"/>
											</style:style>
											<style:style style:name="Table4.H" style:family="table-column">
											 <style:table-column-properties style:column-width="0.1229in"/>
											</style:style>
											<style:style style:name="Table4.A1" style:family="table-cell">
											 <style:table-cell-properties style:vertical-align="bottom" fo:padding="0.0382in" fo:border="none" style:writing-mode="lr-tb"/>
											</style:style>
											<style:style style:name="Table4.2" style:family="table-row">
											 <style:table-row-properties style:min-row-height="0.2069in" style:use-optimal-row-height="false"/>
											</style:style>
											<style:style style:name="P1" style:family="paragraph" style:parent-style-name="Normal">
											 <style:paragraph-properties fo:text-align="center" style:justify-single-word="false" fo:break-before="page"/>
											</style:style>
											<style:style style:name="___" style:display-name="___" style:family="table-cell" style:parent-style-name="Normal">
											 <style:table-cell-properties fo:margin-top="0in" fo:margin-bottom="0in" loext:contextual-spacing="false" fo:hyphenation-ladder-count="no-limit" style:border-line-width-bottom="0.0071in 0.0071in 0.0071in" fo:padding="0in" fo:border-left="none" fo:border-right="none" fo:border-top="none" fo:border-bottom="1.5pt double #808080" style:shadow="none" text:number-lines="false" text:line-number="0" />
											</style:style>
											<style:style style:name="P2" style:family="paragraph" style:parent-style-name="Normal">
											 <style:paragraph-properties fo:margin-left="0in" fo:margin-right="-0.0071in" fo:text-indent="0in" style:auto-text-indent="false">
												<style:tab-stops>
												 <style:tab-stop style:position="0.75in"/>
												 <style:tab-stop style:position="2.5in"/>
												 <style:tab-stop style:position="4.25in"/>
												</style:tab-stops>
											 </style:paragraph-properties>
											</style:style>
											<style:style style:name="P3" style:family="paragraph" style:parent-style-name="Normal">
											 <style:paragraph-properties>
												<style:tab-stops>
												 <style:tab-stop style:position="0.75in"/>
												 <style:tab-stop style:position="2.5in"/>
												 <style:tab-stop style:position="4.25in"/>
												</style:tab-stops>
											 </style:paragraph-properties>
											</style:style>
											<style:style style:name="P4" style:family="paragraph" style:parent-style-name="Normal">
											 <style:paragraph-properties fo:text-align="end" style:justify-single-word="false">
												<style:tab-stops>
												 <style:tab-stop style:position="0.75in"/>
												 <style:tab-stop style:position="2.5in"/>
												 <style:tab-stop style:position="4.25in"/>
												</style:tab-stops>
											 </style:paragraph-properties>
											</style:style>
											<style:style style:name="P5" style:family="paragraph" style:parent-style-name="Normal">
											 <style:text-properties style:font-name="Arial" fo:font-size="8pt" fo:font-style="italic" style:font-size-asian="8pt" style:font-style-asian="italic" style:font-name-complex="Verdana" style:font-size-complex="8pt" style:font-style-complex="italic"/>
											</style:style>
											<style:style style:name="P6" style:family="paragraph" style:parent-style-name="Normal">
											 <style:paragraph-properties>
												<style:tab-stops>
												 <style:tab-stop style:position="0.9in"/>
												</style:tab-stops>
											 </style:paragraph-properties>
											 <style:text-properties style:font-name="Arial" fo:font-size="8pt" style:font-size-asian="8pt" style:font-name-complex="Verdana" style:font-size-complex="8pt"/>
											</style:style>
											<style:style style:name="P7" style:family="paragraph" style:parent-style-name="Normal">
											 <style:paragraph-properties>
												<style:tab-stops>
												 <style:tab-stop style:position="0.9in"/>
												</style:tab-stops>
											 </style:paragraph-properties>
											</style:style>
											<style:style style:name="P8" style:family="paragraph" style:parent-style-name="Normal">
											 <style:text-properties style:font-name="Verdana" fo:font-size="7pt" style:font-size-asian="7pt" style:font-name-complex="Verdana" style:font-size-complex="7pt" fo:color="#000080" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" style:text-underline-mode="continuous" style:text-overline-mode="continuous" style:text-line-through-mode="continuous"/>
											</style:style>
											<style:style style:name="T1" style:family="text">
											 <style:text-properties style:font-name="Arial" fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-name-complex="Verdana" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
											</style:style>
											<style:style style:name="T2" style:family="text">
											 <style:text-properties style:font-name="Arial" fo:font-size="7pt" style:font-size-asian="7pt" style:font-name-complex="Verdana" style:font-size-complex="7pt"/>
											</style:style>
											<style:style style:name="T3" style:family="text">
											 <style:text-properties style:font-name="Arial" fo:font-size="8pt" style:font-size-asian="8pt" style:font-size-complex="8pt"/>
											</style:style>
											<style:style style:name="T4" style:family="text">
											 <style:text-properties style:font-name="Arial" fo:font-size="8pt" style:font-size-asian="8pt" style:font-name-complex="Verdana" style:font-size-complex="8pt"/>
											</style:style>
											<style:style style:name="T5" style:family="text">
											 <style:text-properties style:font-name="Arial" fo:font-size="8pt" fo:font-style="italic" style:font-size-asian="8pt" style:font-style-asian="italic" style:font-name-complex="Verdana" style:font-size-complex="8pt" style:font-style-complex="italic"/>
											</style:style>
											<style:style style:name="T6" style:family="text">
											 <style:text-properties fo:color="#000000" style:font-name="Arial" fo:font-size="8pt" fo:font-style="italic" fo:font-weight="bold" style:font-name-asian="Verdana" style:font-size-asian="8pt" style:font-style-asian="italic" style:font-weight-asian="bold" style:font-name-complex="Verdana" style:font-size-complex="8pt" style:font-style-complex="italic" style:font-weight-complex="bold"/>
											</style:style>
											<style:style style:name="T7" style:family="text">
											 <style:text-properties fo:color="#000000" style:font-name="Arial" fo:font-size="8pt" style:font-name-asian="Verdana" style:font-size-asian="8pt" style:font-name-complex="Verdana" style:font-size-complex="8pt"/>
											</style:style>
											<style:page-layout style:name="pm1">
											<style:style style:name="T8" style:family="text">
											 <style:text-properties style:font-name="Arial" fo:font-size="7pt" style:font-size-asian="7pt" style:font-size-complex="7pt" fo:color="#000080" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" style:text-underline-mode="continuous" style:text-overline-mode="continuous" style:text-line-through-mode="continuous"/>
										  </style:style>
											 <style:page-layout-properties fo:page-width="8.5in" fo:page-height="11in" style:num-format="1" style:print-orientation="portrait" fo:margin-top="0.7874in" fo:margin-bottom="0.7874in" fo:margin-left="0.7874in" fo:margin-right="0.7874in" style:writing-mode="lr-tb" style:footnote-max-height="0in">
												<style:footnote-sep style:width="0.0071in" style:distance-before-sep="0.0398in" style:distance-after-sep="0.0398in" style:line-style="solid" style:adjustment="left" style:rel-width="25%" style:color="#000000"/>
											 </style:page-layout-properties>
											 <style:header-style/>
											 <style:footer-style/>
											</style:page-layout>
											<style:page-layout style:name="pm2">
											 <style:page-layout-properties fo:page-width="8.5in" fo:page-height="11in" style:num-format="1" style:print-orientation="portrait" fo:margin-top="0.5in" fo:margin-bottom="0.5in" fo:margin-left="0.5in" fo:margin-right="0.5in" style:writing-mode="lr-tb" style:footnote-max-height="0in">
												<style:footnote-sep style:width="0.0071in" style:line-style="solid" style:adjustment="left" style:rel-width="33%" style:color="#000000"/>
											 </style:page-layout-properties>
											 <style:header-style/>
											 <style:footer-style/>
											</style:page-layout>
										</office:automatic-styles>
									""",
		"o:master"		:	"""
									 <office:master-styles>
										<style:master-page style:name="Standard" style:page-layout-name="pm1"/>
										<style:master-page style:name="MP0" style:page-layout-name="pm2"/>
									 </office:master-styles>
									""",

		"o:office"		:	"""
										<office:document ${officedoc}>
											<o:meta />
											<o:fonts />
											<o:styles />
											<o:scripts />
											<o:automatic />
											<o:master />
											<office:body>
												<office:text>
													<text:sequence-decls>
														<text:sequence-decl text:display-outline-level="0" text:name="Illustration"/>
														<text:sequence-decl text:display-outline-level="0" text:name="Table"/>
														<text:sequence-decl text:display-outline-level="0" text:name="Text"/>
														<text:sequence-decl text:display-outline-level="0" text:name="Drawing"/>
													</text:sequence-decls>
													<table:table table:name="Table1" table:style-name="Table1">
														<table:table-column table:style-name="Table1.A"/>
														${_}
													</table:table>
													<text:p text:style-name="P8"/>
												</office:text>
											</office:body>
										</office:document>
									""",
		"o:t1row"			:	"""
										<table:table-row table:style-name="Table1.A#{rn:-1}">
											<table:table-cell table:style-name="${style:-Table1.A${rn:-1}}" office:value-type="string">
												${_}
											</table:table-cell>
										</table:table-row>
									""",
		"o:table"	:	"""
										<table:table table:name="Table${tn}" table:style-name="Table${tn}">
											<table:table-column table:style-name="Table${tn}.A"/>
											<table:table-column table:style-name="Table${tn}.B"/>
											<table:table-column table:style-name="Table${tn}.C"/>
											<table:table-column table:style-name="Table${tn}.D"/>
											<table:table-column table:style-name="Table${tn}.E"/>
											<table:table-column table:style-name="Table${tn}.F"/>
											<table:table-column table:style-name="Table${tn}.G"/>
											<table:table-column table:style-name="Table${tn}.H"/>
											${_}
										</table:table>
									""",
		"o:text:p"	:	"""
										<text:p text:style-name="${p}">
											<text:span text:style-name="${s:-T2}">
												<text:span text:style-name="${t}">
													${_}
												</text:span>
											</text:span>
										</text:p>
									""",
		"o:trow" 	:	"""
										<table:table-row table:style-name="Table${tn}.${s:-A1}">
											<o:titem tn="${tn}"/>
											${_}
											<o:titem tn="${tn}"/>
										</table:table-row>
									""",
		"o:tcell"	:	"""
										<table:table-cell table:style-name="${style:-Table${tn}.${s:-A1}}" office:value-type="string" ${cs:+table:number-columns-spanned="${cs}"}>
											${_}
										</table:table-cell>
									""",
		"o:titem"		:	"""
										<o:tcell ${cs:+cs="${cs}"} tn="${tn}" s="A1" style="${style}">
											<o:text:p p="${p:-P2}" t="${t:-T2}" style="${style}">
												${_}
											</o:text:p>
										</o:tcell>
									""",
		"o:thead"		:	"""
										<o:trow tn="${tn}">
											<o:tcell tn="${tn}" style="___" cs="${cs:-6}">
												<o:text:p p="${p:-P2}" t="${t:-T6}">
													${_}
												</o:text:p>
											</o:tcell>
										</o:trow>
									""",
		"o:bullet"	:	"""
										<o:tcell tn="3">
											<o:text:p t="T3">${__}</o:text:p>
										</o:tcell>
									""",
		"o:brow"	:	"""
										<o:trow tn="3">
											<o:titem />
											<o:bullet __="___" />
											<o:titem />
										</o:trow>
									""",
		"o:blist"		:	"""
										<o:thead tn="3" cs="6">${title}</o:thead>
										<o:brow __="items" _#_="4" />
									""",
		"o:bullets"	:	"""
										<o:t1row>
											<o:table tn="3">
												<o:blist __="bullets" />
											</o:table>
										</o:t1row>
									""",
		"o:name"		:	"""
										<o:t1row style="___">
											<o:text:p p="P1" t="T1">
												${fullname}
											</o:text:p>
										</o:t1row>
									""",
		"o:phone"		:	"""
										<o:titem tn="2" t="T2">${.}</o:titem>
									""",
		"o:email"		:	"""
										<o:titem tn="2" t="T8" p="P8" style="">${.}</o:titem>
									""",
		"o:contact"	:	"""
										<o:t1row>
											<o:table tn="2">
												<o:thead cs="6" t="T6">
													Contact Information
												</o:thead>
												<o:trow tn="2" s="2">
													<o:titem />
													<o:phone __="phone" />
													<o:email __="email" />
													<o:titem />
												</o:trow>
											</o:table>
										</o:t1row>
									""",
		"o:desc"		:	"""
										<o:trow tn="4">
											<o:titem tn="4" cs="6" P="P5" t="T5"}>${.}</o:titem>
											<o:titem tn="4" />
										</o:trow>
										""",
		"o:duty"		: """
										<o:trow tn="4">
											<o:titem tn="4" p="P2" t="$T2">‣</o:titem>
											<o:titem tn="4" cs="5" p="P2" t="T2">${__}</o:titem>
											<o:titem tn="4" />
										</o:trow>
									""",
		"o:position": """
										<o:t1row>
											<o:table tn="4">
												<o:trow tn="4">
													<o:titem tn="4" cs="3" style="___" p="P3" t="T6">
														${name} — ${title}
													</o:titem>
													<o:titem tn="4" cs="3" style="___" p="P4" t="T6">
														${from} — ${until}
													</o:titem>
												</o:trow>
												<o:desc __="desc" />
												<o:duty __="duties" />
											</o:table>
										</o:t1row>
									""",
		"o:work"		: """
										<o:position __="experience" />
									""",
		"o:resume"		:	"""<o:dtd />
										<o:office>
											<o:name />
											<o:contact />
											<o:bullets />
											<o:work />
										</o:office>
									""",
				}
