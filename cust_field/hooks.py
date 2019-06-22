# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cust_field"
app_title = "cust_field"
app_publisher = "Indictrans"
app_description = "Add Custom Field"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "indic@indictrans.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cust_field/css/cust_field.css"
# app_include_js = "/assets/cust_field/js/cust_field.js"

# include js, css files in header of web template
# web_include_css = "/assets/cust_field/css/cust_field.css"
# web_include_js = "/assets/cust_field/js/cust_field.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

#include js in doctype views
doctype_js = {
	"Customer" : "cust_field/customer/email_custom.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "cust_field.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cust_field.install.before_install"
# after_install = "cust_field.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cust_field.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Customer": {
		"validate": "cust_field.cust_field.customer.email_custom.cre_custm"
		 
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cust_field.tasks.all"
# 	],
# 	"daily": [
# 		"cust_field.tasks.daily"
# 	],
# 	"hourly": [
# 		"cust_field.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cust_field.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cust_field.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "cust_field.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cust_field.event.get_events"
# }

fixtures=["Custom Field"]