%include('header')
                        <script src="static/home.js"></script>
				<form id="actionForm" action="/action" method="post">
					<input type="hidden" name="exsecutionAction" value="">
					<div class="success" align="center">
					<img src="static/check.png" style="vertical-align:middle" height="30">
					Rule added successfully
					</div>
					<div class="block">
						<table border="1" width="100%">
								<tbody>
									<tr>
										<td width="11%" height="23"><button onclick="setActionHome('AddV4')" name="btnAddV4">Add a rule set (IP v4)</button></td>
										<td width="11%" height="23"><button onclick="setActionHome('AddV6')" name="btnAddV6">Add a rule set (IP v6)</button></td>
										<td width="11%" height="23"><button onclick="setActionHome('Index')" name="btnStartTC">Home</button></td>
									</tr>
								</tbody>
						</table>
					</div>
				</form>
%include('footer')
