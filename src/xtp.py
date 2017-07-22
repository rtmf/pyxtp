#!/usr/bin/env python3
# vim: ts=2 sw=2 noet
import re
from html.parser import HTMLParser
from html.entities import html5 as entities, name2codepoint as characters
import types
def dfind(name,dicts,error=None):
	ret=[]
	if type(name)==list:
		for search in name:
			for assoc in dfind(search,dicts,error):
				ret.append(assoc)
	else:
		for assoc in dicts:
			if type(assoc)==dict:
				if name in assoc:
					ret.append(assoc[name])
			elif type(assoc)==list:
				for val in [val for (key,val) in assoc if key==name]:
					ret.append(val)
	if len(ret)==0 and error is not None:
		raise Exception(error%name)
	else:
		return ret
class XTPLogger():
	def log(self,foo):
		from sys import stderr
		stderr.write("%s\n"%foo)
		stderr.flush()
class XTPClassManipulator():
	def addmethod(self,func,name,target=None,source=None):
		setattr(target if target is not None else self,name,self.bindfunc(func,
			source if source is not None else target))
	def bindfunc(self,func,target=None):
		return types.MethodType(func,target if target is not None else self)
	def callifexists(self,target,name,error=None,ret=None,*args,**kwargs):
		if name in dir(target):
			return getattr(target,name)(*args,ret=ret,**kwargs)
		elif error is not None:
			error(target,*args,ret=ret,**kwargs)
			return ret
class XTPAutoGeneric(XTPClassManipulator,XTPLogger):
	def __init__(self,target,generics=[]):
		self.__generic_target__=target
		self._genfuncs=list(map(self.generic,generics))
	def generic(self,generic):
		listname,funclist=self.genlist(generic)
		generr=self.addgenerr(generic)
		self.addmethod(self.getgenfunc(generic,generr,listname),generic,self.__generic_target__)
		return(generic,generr)
	def getgenfunc(self,generic,generr,listname):
		return (lambda self,child,alt,*args,**kwargs:
			([funclist[child]  for funclist in
				[getattr(self,listname)]
				if child in funclist] + [
					alt if alt is not None else getattr(self,generr)]
				)[0](*args, **kwargs))
	def addgenerr(self,generic):
		generr='generic_error__'+generic
		self.addmethod(self.getgenerr(generic),generr,self.__generic_target__)
		return generr
	def getgenerr(self,generic):
		autogen=self
		return (lambda self,child,**kwargs:
				(autogen.log('No alt, no impl, generic:%s, child:%s'%(generic,child))
				and None))
	def genlist(self,generic):
		listname='_%s__funcs'%generic
		if listname not in dir(self.__generic_target__):
			setattr(self.__generic_target__,listname,{ impl.__name__[len(generic)+1:] : impl for impl in
				[ func for func in [
					getattr(self.__generic_target__,name) for name in dir(self.__generic_target__)
					if name.startswith(generic+'_')
					] if type(func).__name__=='method' ] })
		#print(listname,getattr(self.__generic_target__,listname))
		return listname,getattr(self.__generic_target__,listname)
class XTPAutoHandlers(XTPClassManipulator,XTPLogger):
	def __init__(self,source,target,funcs):
		self.__auto_source__=source
		self.__auto_target__=target
		for func,base in [(func,"handle_%s"%func) for func in funcs]:
			self.addmethod(self.genhandler(base),func,source,source)
			self.addmethod(self.genhandler(base),func,target,target)
	def handlermissing(self,obj,func):
		return lambda self,*args,ret=None,**kwargs: self.log(
				"Could not find function %s on %s object."%(func,obj)) and ret
	def callmethod(self,func,ret=None,*args,**kwargs):
		return self.callifexists(
				target=self.__auto_target__,name=func,error=self.handlermissing("target",func),*args,**kwargs,ret=
				self.callifexists(target=self.__auto_source__,name=func,error=self.handlermissing("source",func),
					*args,**kwargs,ret=ret))
	def genhandler(self,func):
		autohandler=self
		return (lambda self,*args,ret=None,**kwargs:
				autohandler.callmethod(func,*args,**kwargs,ret=
					autohandler.callmethod("%s_pre"%func,*args,**kwargs,ret=ret)))
class XTPAutoStack(XTPLogger,XTPClassManipulator):
	__statelist__=[]
	__stack__=[]
	def __init__(self,target,statelist=[]):
		self.__stack_target__=target
		self.__statelist__=statelist
		self.__autogeneric__=XTPAutoGeneric(self,["set","get"])
		self.__handlers__=XTPAutoHandlers(self,self.__stack_target__,["push","pop"])
		self.addmethod(self.depth,"depth",self.__stack_target__)
	def depth(self,other):
		return len(self.__stack__)
	def handle_push_pre(self,ret=None):
		return ret
	def handle_pop_pre(self,ret=None):
		return ret
	def handle_push(self,ret=None,statelist=[]):
		self.__stack__.append(self.state(statelist+self.__statelist__))
		return ret
	def handle_pop(self,ret=None):
		for attr,value in self.__stack__.pop().items():
			self.set(type(attr).__name__,self.bindfunc(setattr,self.__stack_target__),attr,value)
		return ret
	def get_list(self,attr):
		return {*getattr(self.__stack_target__,attr)}
	def set_list(self,attr,value):
		setattr(self.__stack_target__,{*value})
	def get_dict(self,attr):
		return {**getattr(self.__stack_target__,attr)}
	def set_dict(self,attr,value):
		setattr(self.__stack_target__,{**value})
	def state(self,statelist=[]):
		return {attr: self.get(type(attr).__name__,self.bindfunc(getattr,self.__stack_target__),attr)
			for attr in statelist+self.__statelist__}
class XTPExpansion(XTPLogger):
	def __init__(self,dlist):
		self._dlist=dlist
	def submatch(self,match):
		return self.expand(**match.groupdict())
	def expand(self,param,everything,flags=None,index=None,sflag=None,mode=None,expn=None,trinary=None,true=None,false=None):
		value=''
		values=dfind(param,self._dlist)
		if len(values)==0:
			if trinary=='?':
				value=false
			elif mode=='-':
				value=expn
			else:
				value=''
		else:
			if trinary=='?':
				value=true
			elif mode=='+':
				value=expn
			elif mode=='.':
				value=expn.join(map(str,values))
			else:
				value=str(values[0])
		if not len(value):
			self.log("could not find %s or result is empty string"%(everything))
		#else:
		#	self.log("substituted %s with %s"%(everything,value))
		return value
	def subst(self,text):
		count=1
		while count>0:
			text,count=re.subn(
					r"(?msux)(?#turn on multiline, enable comments,"
					r"allow . to match anything, enable unicode support)"
					r"(?#match leading ${)(?P<everything>\$\{"
					r"(?#optional expansion flags)(?P<flags>\([^\)]*\))?"
					r"(?#parameter name to expand)(?P<param>[^$:{}\[\]]*)"
					r"(?#optional subscript index)(?P<index>\["
					r"(?#optional subscript flags)(?P<sflag>\([^\)]*\))?"
					r"(?#close optional subscript)[^\]]*\])?"
					r"(?#optional expansion modes)(:(?P<mode>[.+-])(?P<expn>[^${}]*))?"
					r"(?#optional alternate modes)(:(?P<trinary>\?)(?P<true>[^${}\|]*)\|(?P<false>[^${}]*))?"
					r"(?#match trailing })\})", self.submatch, text)
		return text

class XTP(XTPLogger):
	noindent=["link","img","input","meta","br"]
	autoclose=["link","img","input","meta","br"]
	truthy=["yes","on","1","true"]
	def __init__(self,templates,template=None,iterlist=None,attrs=[],**kwargs):
		self.__auto__=XTPAutoGeneric(self,["render_xtp"])
		self.__stack__=XTPAutoStack(self,[
			"_kwargs",
			"_attrs",
			"_buffer",
			"_indent",
			"_template",
			"_iterlist",
			"_templates",
			"_opentag",
			"_parser",
			])
		self._buffer=''
		self._indent=0
		self._opentag=['',[]]
		self._templates=templates
		self._iterlist=iterlist
		self._kwargs=kwargs
		self._template=template
		self._attrs=attrs
		self._indentby=' '
		self._parser=None
	def render(self,template,attrs=[],iterlist=None,**kwargs):
		self.push()
		self.open()
		self._template=template
		self._kwargs={**self._kwargs,**kwargs}
		self._attrs=attrs
		self._template=template
		self._buffer=''
		depth=self.depth()
		if iterlist is None:
			if self._template in self._templates:
				self._parser.feed(self.subst(self._templates[self._template]))
			else:
				raise Exception('No such template: %s'%self._template)
		else:
			stride=self.attr('stride')
			if len(stride) and int(stride[0])>0:
				curlist=[]
				while len(iterlist):
					curlist+=[iterlist[0:int(stride[0])]]
					iterlist=iterlist[int(stride[0]):]
				iterlist=curlist
			for iteritem in iterlist:
				if type(iteritem)==dict:
					self.append(self.render(self._template,**iteritem))
				elif type(iteritem)==list:
					subtemp=self.attr('subtemp')
					sublist=self.attr('sublist')
					if len(sublist)==0 or sublist[0].lower() in self.truthy:
						subitem={}
						itersublist=iteritem
						if len(subtemp)==0:
							template=self._template
						else:
							subtemp=subtemp[0].lower()
							if subtemp in self.truthy or subtemp=='first':
								subitem=iteritem[0]
								template=subitem['template']
								itersublist=iteritem[1:]
							else:
								template=subtemp
						subitem['template']=template
						self.append(self.render(**subitem,iterlist=None,itersublist=itersublist,attrs=self._attrs))
					else:
						raise(Exception('Sublist passed instead of dict but sublist is not enabled!'))
		self.close()
		return self.xtp_wrap("xtp::render[%s]"%template,self.pop())
	def open(self):
		self._parser=XTPParser(self)
		self._buffer=''
	def close(self):
		depth=self.depth()
		self._parser.close()
		if (depth!=self.depth()):
			raise Exception('Error in template: %s (child not closed properly)'%template)
	def xtp_wrap(self,name,data):
		return self.indent(data)
	def subst(self,text):
		return XTPExpansion([self._attrs,self._kwargs]).subst(text)
	def indent(self,data):
		return ''.join([
				self._indentby*self._indent+line.strip()+'\n'
					for line in data.split('\n')
					if line.strip() != ''
					])
	def append(self,data):
		for line in (data.split('\n')):
			if line.strip() != '':
				self._buffer+=''+line+'\n'
	def render_attrs(self,attrs):
		return ['%s="%s"'%(name,value) for (name,value) in attrs if value is not None]
	def render_tag(self,tag,attrs,endtag=False,startendtag=False):
		startendtag=startendtag or (tag in self.autoclose)
		return self.indent("<%s%s%s>"%("/" if endtag else "",
				tag if endtag else " ".join([tag]+self.render_attrs(attrs)),
				" /" if startendtag else ""))
	def parm(self,name):
		return dfind(name,[self._attrs,self._kwargs],'No such parameter: %s')[0]
	def attr(self,name):
		return dfind(name,[self._attrs])
	def render_xtp_template(self,tag,attrs):
		return self.render(dfind('name',[attrs])[0],attrs=attrs)
	def render_xtp_foreach(self,tag,attrs):
		return self.render(dfind('name',[attrs])[0],attrs=attrs,iterlist=self.parm(dfind('list',[attrs])[0]))
	def render_xtp_parm(self,tag,attrs):
		return self.parm(dfind('name',[attrs])[0])
	def render_comment(self,data):
		return "<!-- %s -->"%data
	def handle_pop_pre(self,ret=None):
		return self._buffer
	def handle_pop(self,ret=None):
		return ret
	def handle_push_pre(self,ret=None):
		return ret
	def handle_push(self,ret=None):
		return ret
	def handle_comment(self,data):
		self.append(self.indent(self.render_comment(data)))
	def handle_entityref(self,name):
		self.append(''.join(dfind(name,[self._attrs,self._kwargs,entities])))
	def handle_charref(self,name):
		self.append(''.join(dfind(name,[self._attrs,self._kwargs,characters])))
	def isdef(self,tag):
		return (tag in self._render_xtp__funcs or tag in self._templates)
	def ifdef(self,tag,render,simple):
		return render if self.isdef(tag) else simple
	def render_xtp_tag(self,tag,attrs):
		items=[self.parm(name) for name in dfind(["__","_items_"],[attrs])] or None
		self.log(repr((tag,len(attrs),len(items or []))))
		return self.render(template=tag,attrs=attrs,iterlist=items)
	def handle_xtp(self,tag,attrs):
		if tag in self._templates:
			self.append(self.render_xtp_tag(tag,attrs))
		else:
			self.append(self.render_xtp(tag,self.render_tag,tag,attrs))
	def enter_subtag(self,tag,attrs):
		self._opentag=(tag,attrs)
		self.push()
		self.open()
	def enter_tag(self,tag,attrs):
		self.handle_tag(tag,attrs,startendtag=False,endtag=False)
		if tag not in self.noindent:
			self._indent+=1
	def handle_tag(self,tag,attrs,startendtag=True,endtag=False):
		self.append(self.render_tag(tag,attrs,startendtag,endtag))
	def handle_starttag(self,tag,attrs):
		self.ifdef(tag,self.enter_subtag,self.enter_tag)(tag,attrs)
	def handle_startendtag(self,tag,attrs):
		self.ifdef(tag,self.handle_xtp,self.handle_tag)(tag,attrs)
	def leave_subtag(self,tag):
		self.close()
		body=self.pop()
		oldtag,attrs=self._opentag
		if tag==oldtag:
			self.handle_xtp(tag,attrs=list(attrs)+[("_",body),("_body_",body)])
		else:
			raise Exception('Mismatched closing tag, expected %s, got %s.'%(oldtag,tag))
	def leave_tag(self,tag):
		if tag not in self.noindent:
			self._indent-=1
		if tag not in self.autoclose:
			self.handle_tag(tag,[],endtag=True)
	def handle_endtag(self,tag):
		self.ifdef(tag,self.leave_subtag,self.leave_tag)(tag)
	def handle_data(self,data):
		self.append(self.indent(data))
	def handle_decl(self,decl):
		self.append(self.indent("<!%s>"%decl))
	def handle_pi(self,pi):
		self.append(self.indent("<?%s>"%pi))
	def unknown_decl(self,decl):
		self.append(self.indent("<![%s]>"%decl))

class XTPParser(HTMLParser):
	def __init__(self,engine):
		super().__init__(convert_charrefs=False)
		self._engine=engine
		for (handler,handled) in [(handler,getattr(self._engine,handler)) for handler in dir(self._engine) if handler.startswith('handle_')]:
			setattr(self,handler,handled)
		self.unknown_decl=self._engine.unknown_decl
	def feed(self,data):
		super().feed(data)

def render_file(filename):
	sitemodule = import_module(filename)
	xtp = XTP(templates=sitemodule.templates,
			__all_data__=sitemodule.data,__all_pages__=sitemodule.pages)
	for target,config in sitemodule.pages.items():
		pagedata={}
		if target in sitemodule.data:
			pagedata={**sitemodule.data[target]}
		if "data" in config:
			for data in config["data"]:
				if data in sitemodule.data:
					pagedata={**pagedata, **sitemodule.data[data]}
		open("./%s"%target,"w").write(
				xtp.render(template=config["template"],**pagedata))

def import_module(filename):
	import importlib.util
	import os.path
	spec = importlib.util.spec_from_file_location(os.path.basename(filename)[:-3], filename)
	sitemodule = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(sitemodule)
	return sitemodule

if __name__=='__main__':
	import sys
	#print(sys.argv)
	for filename in sys.argv[1:]:
		render_file(filename)
