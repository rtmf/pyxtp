#!/usr/bin/env python3
# vim: ts=2 sw=2 noet
import re
from html.parser import HTMLParser
from html.entities import html5 as entities, name2codepoint as characters
class TemplateEngine(HTMLParser):
	truthy=["yes","on","1","true"]
	def __init__(self,templates,template,iterlist=None,attrs=[],**kwargs):
		super().__init__(convert_charrefs=False)
		self._templates=templates
		self._iterlist=iterlist
		self._kwargs=kwargs
		self._template=template
		self._attrs=attrs
		self._indentby=' '
	def render(self,indent=0):
		self._indent=indent
		self._buffer=''
		if self._iterlist is None:
			if self._template in self._templates:
				super().feed(self.subst(self._templates[self._template]))
			else:
				raise Exception('No such template: %s'%name)
		else:
			for iteritem in self._iterlist:
				if type(iteritem)==dict:
					self._buffer+=self.template(self._template,**iteritem)
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
						self._buffer+=self.template(**subitem,iterlist=None,itersublist=itersublist)
					else:
						raise(Exception('Sublist passed instead of dict but sublist is not enabled!'))
		return self._buffer
	def template(self,template,**kwargs):
		return TemplateEngine(
				self._templates,
				template,
				**{**kwargs,**self._kwargs}).render(self._indent)
	def subst(self,text):
		data=text
		while True:
			parm=re.search(pattern=r"\$\{([^${}:]*):([^${}:])\}",string=data,flags=re.MULTILINE)
			if parm is not None:
				name,mods=parm.groups()
			else:
				parm=re.search(pattern=r"\$\{([^${}]*)\}",string=data,flags=re.MULTILINE)
				if parm is not None:
						name=parm.groups()[0]
						mods=''
						if name.find(':')>-1:
							name,mods=name.split(':',1)
			if parm is None:
				return data
			value=''
			values=self.dfind(name,[self._attrs,self._kwargs])
			if len(values)==0 and len(mods)>0:
				if mods[0]=='-':
					value=mods[1:]
				elif mods[0]=='|':
					value='${%s}'%(mods[1:])
			elif len(values)>0:
				if len(mods)>0:
					if mods[0]=='+':
						value=mods[1:]
					elif mods[0]=='.':
						value=mods[1:].join(values)
				else:
					value=values[0]
			if not len(value):
				print("could not find ${%s:%s} or result is empty string"%(name,mods))
			else:
				print("substituted ${%s:%s} with %s"%(name,mods,value))
			data=data[0:parm.start()]+value+data[parm.end():]
	def append(self,data):
		for line in data.split('\n'):
			if line.strip()!="":
				self._buffer=self._buffer+(self._indentby*self._indent)+line.strip()+'\n'
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
	def handle_comment(self,data):
		return self.append('<!--%s-->'%data)
	def handle_entityref(self,name):
		self.append(''.join(self.dfind(name,[self._attrs,self._kwargs,entities])))
	def handle_charref(self,name):
		self.append(''.join(self.dfind(name,[self._attrs,self._kwargs,characters])))
	def handle_startendtag(self,tag,attrs):
		if tag=='template':
			self._buffer+=self.template(self.dfind('name',[attrs])[0],attrs=attrs)
		elif tag=='foreach':
			self._buffer+=self.template(self.dfind('name',[attrs])[0],attrs=attrs,iterlist=self.parm(self.dfind('list',[attrs])[0]))
		elif tag=='parm':
			self.append(self.parm(self.dfind('name',[attrs])[0]))
		else:
			self.append("<%s />"%self.render_tag(tag,attrs))
	def handle_starttag(self,tag,attrs):
		self.append("<%s>"%self.render_tag(tag,attrs))
		self._indent+=1
	def handle_endtag(self,tag):
		self._indent-=1
		self.append("</%s>"%tag)
	def handle_data(self,data):
		self.append(data)

def render(templates, template, iterlist=None, **kwargs):
	return TemplateEngine(templates,template,iterlist=iterlist,**kwargs).render()
