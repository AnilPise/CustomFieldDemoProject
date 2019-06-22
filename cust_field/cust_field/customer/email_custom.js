frappe.ui.form.on('Customer', {
	refresh: function(frm) {
       //frm.set_value("customer_name","AAAAA");
	//   frm.set_value("account_name", data.account_name);
	},
	 
	email: function(frm){
		var email_id = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
		console.log("============email function called")
        console.log(email_id.test(frm.doc.email));
		if (email_id.test(frm.doc.email) == false)
			{
				frm.set_value(`email`,``)
				frappe.throw("Incorrect Email")
			}
	},
	onload_post_render: function(frm) {
		 
        console.log("onload_post_render called...................");
    },
    validate:function(frm){
    	console.log("Validate^^^^^^^^^^^^^^...................");
    	frm.set_df_property("email","read_only",1);
    }   

});