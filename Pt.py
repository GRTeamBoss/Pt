#!usr/bin/env python3
#-*- encoding: utf-8 -*-
import time
import os
# PL == Programming Language


class Pt:
	"""docstring for Pt:\nINFO\n---\nINTRO:\nMain("[PATH]")\nPATH\n--\nUbuntu: /home/$USER/path/to/folder/\nWindows: [Logical Disk]:/path/to/folder/\nMacOS: I don't know, because I not have MacBook and iMac and MacOS\nResult: $[YOUR_PATH]site.txt\n--\n---\n[1] {\nself.conf_hash_src_[PL] = []\n}\n[2] {\nself.conf_hash_src_[PL].append(self.conf_hash_src_node[count])\n}\n[3] {\n...\nos.system("echo [PL] Success")\nself.[PL]_edit()\n...\n#[PL]\nfor elem in self.conf_hash_src_[PL]:\nif len(self.conf_hash_src_[PL]) == 1:\nif elem == "[PL](off)":\nos.system("rm -rf " + self.path_dist + "[PL]/")\nos.system("cp " + self.path_src + "[PL]/ " + self.path_dist)\nelse:\npass\nelif len(self.conf_hash_src_[PL]) >= 1:\nos.system("cd " + self.path_dist + " && mkdir [PL]/ && cd [PL]/ && touch *.[PL]")\nfor add in self.conf_hash_src_[PL]:\nwith open(self.path_src + add, "r") as file_get:\nfile_get_read = file_get.read()\nwith open(self.path_dist + "[PL]/*.[PL]", "a") as file_post:\nfile_post.write(file_get_read)\nelse:\nprint("[PL] error!")\nprint("[PL] Success")\n}"""
	
	def __init__(self, way):
		self.conf_hash_src = []
		self.conf_hash_src_node = []
		self.conf_hash_src_html = []
		self.conf_hash_src_css = []
		self.conf_hash_src_js = []
		# [1]
		self.conf_hash_dist = []
		self.conf_hash_path = []
		self.path_site_txt = way
		self.status = ''
		self.err = ''
		self.path_dist = ''
		self.path_src = ''
		self.path_main = ''
		self.head_hash = ''
		self.header_hash = ''
		self.footer_hash = ''
		self.index_title = ''
	
	def edit(self):
		# hash_conf
		self.path_dist = self.path_site_txt + "dist/"
		self.path_src = self.path_site_txt + "src/"
		self.path_main = self.path_site_txt
		try:
			with open(self.path_site_txt + "site.txt", "r") as conf_open:
				self.conf_hash_src = conf_open.read().split(">>>")
		except Exception as error:
			self.err = error
			self.status = "false"
			self.log_file()
			os.system("echo '%s'" % self.err)
		else:
			self.conf_hash_src_html.append(self.conf_hash_src[1])
			self.conf_hash_src_css.append(self.conf_hash_src[2])
			self.conf_hash_src_js.append(self.conf_hash_src[3])
			# [2]
		finally:
			pass
		# hash_file
		with open(self.path_src + "path/head.html", "r") as head_file:
			self.head_hash = head_file.read().split()
		with open(self.path_src + "path/header.html", "r") as header_file: 
			self.header_hash = header_file.read().split()
		with open(self.path_src + "path/footer.html", "r") as footer_file:
			self.footer_hash = footer_file.read().split()
		self.index_title = [self.head_hash.index(x) for x in self.head_hash if x == r"{{>title}}"]
		os.system("cd " + self.path_main)
		# html
		for elem in self.conf_hash_src_html:
			os.system("rm " + self.path_dist + elem)
			os.system("touch " + self.path_dist + elem + " && " + "cp " + self.path_src + "layouts/default.html " + self.path_dist + elem)		
		for elem in self.conf_hash_src_html:
			with open(self.path_src + elem, "r") as index_open:
				index_hash = index_open.read().split("---")
			index_hash_title = index_hash[1].split("|")
			index_hash_title = index_hash_title[1].split(":")			
			index_hash_title = index_hash_title[1].split(" ")
			html_title = index_hash_title[1]
			self.head_hash[self.index_title[0]] = html_title
			with open(self.path_dist + elem, "r") as html_open:
				html_hash = html_open.read().split()
			html_hash[html_hash.index('{{>head}}')] = " ".join(self.head_hash)
			os.system("echo 'head SUCCESS!'")
			html_hash[html_hash.index('{{>header}}')] = " ".join(self.header_hash)
			os.system("echo 'header SUCCESS!'")
			html_hash[html_hash.index('{{>body}}')] = " ".join(index_hash[2:])
			os.system("echo 'body SUCCESS!'")
			html_hash[html_hash.index('{{>footer}}')] = " ".join(self.footer_hash)
			os.system("echo 'footer SUCCESS!'")	
			with open(self.path_dist + elem, "w+") as file_post:
				file_post.write(" ".join(html_hash))
		os.system("echo 'HTML Success'")
		self.status = "true"
		# css
		for elem in self.conf_hash_src_css:
			if len(self.conf_hash_src_css) == 1:
				if elem == "css(off)":
					os.system("rm -rf " + self.path_dist + "css/")
					os.system("cp -r " + self.path_src + "css/ " + self.path_dist)
				else:
					pass
			elif len(self.conf_hash_src_css) >= 1:
				os.system("rm -rf " + self.path_dist + "css/")
				os.system("cd " + self.path_dist + " && mkdir css/ && cd css/ && touch main.css")
				for add in self.conf_hash_src_css:
					with open(self.path_src + add, "r") as file_get:
						file_get_read = file_get.read()
					with open(self.path_dist + "css/main.css", "a+") as file_post:
						file_post.write(file_get_read)
			else:
				os.system("echo 'CSS error!'")
		os.system("echo 'CSS Success'")
		# js
		for elem in self.conf_hash_src_js:
			if len(self.conf_hash_src_js) == 1:
				if elem == "js(off)":
					os.system("rm -rf " + self.path_dist + "js/")
					os.system("cp -r " + self.path_src + "js/ " + self.path_dist)
				else:
					pass
			elif len(self.conf_hash_src_js) >= 1:
				os.system("rm -rf " + self.path_dist + "js/")
				os.system("cd " + self.path_dist + " && mkdir js/ && cd js/ && touch app.js")
				for add in self.conf_hash_src_js:
					with open(self.path_src + add, "r") as file_get:
						file_get_read = file_get.read()
					with open(self.path_dist + "js/app.js", "a+") as file_post:
						file_post.write(file_get_read)
			else:
				os.system("echo 'JS error!'")
		os.system("echo 'JS Success'")
		# [3]
		# logs
		if self.status == "true":
			with open(self.path_main + "log_success.txt", "a") as success_log:
				success_log.write(time.ctime() + ":\n" + self.path_main + " - SUCCESS\n")
				os.system("echo 'success'")
		elif self.status == "false":
			with open(self.path_main + "log_fail.txt", "a") as fail_log:
				fail_log.write(time.ctime() + ":\n" + str(self.err) + " - FAIL\n")
				os.system("echo 'fail'")
		else:
			pass