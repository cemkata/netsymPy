%include('header')
                        <script src="static/home.js"></script>
				<form id="actionForm" action="/action" method="post">
					<input type="hidden" name="exsecutionAction" value="">
					<div class="success" align="center">
					<img src="static/check.png" style="vertical-align:middle" height="30">
					Done!
					</div>
					<div class="block">
						<table border="1" width="100%">
								<tbody>
									<tr>
										<td width="11%" height="23"><button onclick="setAction('Index')" name="btnStartTC">Home</button></td>
									</tr>
								</tbody>
						</table>
					</div>
				</form>
				<script>
					function redirectIndex(){
						window.location.replace("/")
					}
					window.onload = function() { setTimeout(redirectIndex, 5000)};
				</script>
%include('footer')
