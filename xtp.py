#!/usr/bin/env python3
# vim: ts=2 sw=2 noet
import re
from html.parser import HTMLParser
from html.entities import html5 as entities, name2codepoint as characters
import types
class TemplateEngine():
	truthy=["yes","on","1","true"]
	xtptags=["template","foreach","parm"]
	statelist=[
			"_kwargs",
			"_attrs",
			"_buffer",
			"_indent",
			"_template",
			"_iterlist",
			"_templates",
			"_opentag",
			"_parser",
			]
	generics=[
			"render_xtp",
			"get",
			"set",
			]
	def __init__(self,templates,template=None,iterlist=None,attrs=[],**kwargs):
		self._buffer=''
		self._indent=0
		self._opentag=['',[]]
		self._templates=templates
		self._iterlist=iterlist
		self._kwargs=kwargs
		self._template=template
		self._attrs=attrs
		self._indentby=' '
		self._stack=[]
		self._genfuncs=list(map(self.generic,self.generics))
		self._parser=None
	def log(*args,**kwargs):
		pass
	def generic(self,generic):
		listname,funclist=self.genlist(generic)
		generr='generic_error__'+generic
		self.addmethod((lambda self,child,**kwargs:
				self.log('No alt, no impl, generic:%s, child:%s'%(generic,child))
				and None),generr)
		self.addmethod(lambda self,child,alt,*args,**kwargs:
				([funclist[child]  for funclist in 
					[getattr(self,listname)]
					if child in funclist] + [
				alt if alt is not None else getattr(self,generr)]
					)[0](*args, **kwargs),
				generic)
		return(generic,generr)
	def addmethod(self,func,name):
		setattr(self,name,self.bindfunc(func))
	def bindfunc(self,func):
		return types.MethodType(func,self)
	def genlist(self,generic):
		listname='_'+generic+'__funcs'
		if listname not in dir(self):
			setattr(self,listname,{ impl.__name__[len(generic)+1:] : impl for impl in
				[ func for func in [ 
					getattr(self,name) for name in dir(self) 
					if name.startswith(generic+'_') 
					] if type(func).__name__=='method' ] })
		return listname,getattr(self,listname)

	def render(self,template,attrs=[],iterlist=None,**kwargs):
		self.push()
		self._parser=TemplateParser(self)
		self._template=template
		self._kwargs={**kwargs,**self._kwargs}
		self._attrs=attrs
		self._template=template
		self._buffer=''
		if iterlist is None:
			if self._template in self._templates:
				self._parser.feed(self.subst(self._templates[self._template]))
			else:
				raise Exception('No such template: %s'%name)
		else:
			for iteritem in iterlist:
				if type(iteritem)==dict:
					self.append(self.render(self._template,**iteritem))
				elif type(iteritem)==list:
					subtemp=self.attr('subtemp')
					sublist=self.attr('sublist')
					if len(sublist)==0 or sublist[0].lower() in self.truthy:
						subitem=None
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
						self.append(self.render(**subitem,iterlist=None,itersublist=itersublist))
					else:
						raise(Exception('Sublist passed instead of dict but sublist is not enabled!'))
		self._parser.close()
		return self.pop()
	def submatch(self,match):
		return self.expand(**match.groupdict())
	def expand(self,param,flags=None,index=None,sflag=None,expn=None):
		value=''
		values=self.dfind(param,[self._attrs,self._kwargs])
		if expn and len(expn)>0:
			mode=expn[0]
			data=expn[1:]
		else:
			mode=''
			data=''
		if len(values)==0:
			if mode=='-':
				value=data
			elif mode=='|':
				value=self.subst('${'+data+'}')
		else:
			if mode=='+':
				value=data
			elif mode=='.':
				value=data.join(values)
			else:
				value=values[0]
		if not len(value):
			self.log("could not find ${%s:%s} or result is empty string"%(param,expn))
		else:
			self.log("substituted ${%s:%s} with %s"%(param,expn,value))
		return value
	def subst(self,text):
		count=1
		while count>0:
			text,count=re.subn(
					r"(?msux)(?#turn on multiline, enable comments,"
					r"allow . to match anything, enable unicode support)"
					r"(?#match leading ${)\$\{"
					r"(?#optional expansion flags)(?P<flags>\([^\)]*\))?"
					r"(?#parameter name to expand)(?P<param>[^$:{}\[\]]*)"
					r"(?#optional subscript index)(?P<index>\["
					r"(?#optional subscript flags)(?P<sflag>\([^\)]*\))?"
					r"(?#close optional subscript)[^\]]*\])?"
					r"(?#optional expansion modes)(:(?P<expn>[^${}]*))?"
					r"(?#match trailing })\}", self.submatch, text)
		return text

	def indent(self,data):
		return ''.join([
				self._indentby*self._indent+line.strip()+'\n'
					for line in data.split('\n') 
					if line.strip() != ''
					])
	def append(self,data):
		self._buffer+=self.subst(data)
	def render_attrs(self,attrs): 
		return ["%s='%s'"%(name,value) for (name,value) in attrs if value is not None]
	def render_tag(self,tag,attrs):
		return " ".join([tag]+self.render_attrs(attrs))
	def dfind(self,name,dicts,error=None):
		ret=[]
		for assoc in dicts:
			if type(assoc)==dict:
				if name in assoc:
					ret+=[assoc[name]]
			elif type(assoc)==list:
				ret+=[val for (key,val) in assoc if key==name]
		if len(ret)==0 and error is not None:
			raise Exception(error%name)
		else:
			return ret
	def parm(self,name):
		return self.dfind(name,[self._attrs,self._kwargs],'No such parameter: %s')[0]
	def attr(self,name):
		return self.dfind(name,[self._attrs])
	
	def render_xtp_template(self,tag,attrs):
		return self.render(self.dfind('name',[attrs])[0],attrs=attrs)
	def render_xtp_foreach(self,tag,attrs):
		return self.render(self.dfind('name',[attrs])[0],attrs=attrs,iterlist=self.parm(self.dfind('list',[attrs])[0]))
	def render_xtp_parm(self,tag,attrs):
		return self.parm(self.dfind('name',[attrs])[0])
	def render_startendtag(self,tag,attrs):
		return self.indent("<%s />"%self.render_tag(tag,attrs))
	def get_list(self,attr):
		return {*getattr(self,attr)}
	def set_list(self,attr,value):
		setattr(self,{*value})
	def get_dict(self,attr):
		return {**getattr(self,attr)}
	def set_dict(self,attr,value):
		setattr(self,{**value})
	def state(self,statelist=[]):
		return {attr: self.get(type(attr).__name__,self.bindfunc(getattr),attr)
			for attr in statelist+self.statelist}
	def push(self,statelist=[]):
		self._stack.append(self.state())
		self._buffer=''
	def pop(self):
		result=self._buffer
		for attr,value in self._stack.pop().items():
			self.set(type(attr).__name__,self.bindfunc(setattr),attr,value)
		return result
	def handle_comment(self,data):
		self.append(self.indent('<!--%s-->'%data))
	def handle_entityref(self,name):
		self.append(''.join(self.dfind(name,[self._attrs,self._kwargs,entities])))
	def handle_charref(self,name):
		self.append(''.join(self.dfind(name,[self._attrs,self._kwargs,characters])))
	def handle_startendtag(self,tag,attrs):
		self.append(self.render_xtp(tag,self.render_startendtag,tag,attrs)) 
	def handle_starttag(self,tag,attrs):
		if tag in self._render_xtp__funcs:
			self._opentag=[tag,attrs]
			self.push()
		else:
			self.append(self.indent("<%s>"%self.render_tag(tag,attrs)))
			self._indent+=1
	def handle_endtag(self,tag):
		if tag in self._render_xtp__funcs:
			body=self.pop()
			tag,attrs=self._opentag
			attrs.append(('_body_',body),('_',body))
			self.append(self.render_xtp(tag,self.render_startendtag,tag,attrs))
		else:
			self._indent-=1
			self.append(self.indent("</%s>"%tag))
	def handle_data(self,data):
		self.append(self.indent(data))

class TemplateParser(HTMLParser):
	def __init__(self,engine):
		super().__init__(convert_charrefs=False)
		self._engine=engine
		for (handler,handled) in [(handler,getattr(self._engine,handler)) for handler in dir(self._engine) if handler.startswith('handle_')]:
			setattr(self,handler,handled)
#			self.addmethod(
#					(lambda self,*args,**kwargs:(
#					self.log(args) and self.log(kwargs) and
#					self.log(handler) and self.log(handled) and
#					handled(*args,**kwargs))),handler)
	def addmethod(self,func,name):
		setattr(self,name,self.bindfunc(func))
	def bindfunc(self,func):
		return types.MethodType(func,self)
	def feed(self,data):
		super().feed(data)
