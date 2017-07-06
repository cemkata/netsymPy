%include('header')
                        <script src="static/home.js"></script>
				<form id="actionForm" action="/action" method="post" onsubmit="return false;">
					<input type="hidden" name="exsecutionAction" value="">
					<div name='jsEnabled' class="block" style="display: none;">
						<table border="1" width="100%">
							<tr>
								%if tcCheck == True:
									<td width="11%" height="23"><button onclick="setActionHome('AddV4')" name="btnAddV4" >Add a rule set (IP v4)</button></td>
									<td width="11%" height="23"><button onclick="setActionHome('AddV6')" name="btnAddV6" >Add a rule set (IP v6)</button></td>
									<td width="11%" height="23"><button onclick="setActionHome('StartTC')" name="btnStartTC" disabled >Start netem (TC)</button></td>
									<td width="11%" height="23"><button onclick="setActionHome('StopTC')" name="btnStopTC">Stop netem (TC)</button></td>
								%else:
									<td width="11%" height="23"><button onclick="setActionHome('AddV4')" name="btnAddV4" disabled >Add a rule set (IP v4)</button></td>
									<td width="11%" height="23"><button onclick="setActionHome('AddV6')" name="btnAddV6" disabled>Add a rule set (IP v6)</button></td>
									<td width="11%" height="23"><button onclick="setActionHome('StartTC')" name="btnStartTC">Start netem (TC)</button></td>
									<td width="11%" height="23"><button onclick="setActionHome('StopTC')" name="btnStopTC" disabled >Stop netem (TC)</button></td>
								%end
							</tr>
							<tr>
								<td width="11%" height="23"><button onclick="setActionHome('ClearRules')" name="btnClearRules">Clear rules</button></td>
								<td width="11%" height="23"><button onclick="setActionHome('EditRules')" name="btnShowRules">Edit rules</button></td>
							%if tcCheck == True:
								<td width="11%" height="23"><button onclick="setActionHome('Statistic')" name="btnStatus">tc Statistic</button></td>
							%else:
								<td width="11%" height="23"><button onclick="setActionHome('Statistic')" name="btnStatus" disabled>tc Statistic</button></td>
							%end
								<td width="11%" height="23"><button onclick="setActionHome('Help')" name="btnShowHelp">Help</button></td>
							</tr>
						</table>
					</div>
					<div name='jsDisabled' style="display: inline;">
						<b>Please enable Javascript (JS).</b>
						</br>
						<b>This is needed for the work of this tool.</b>
					</div>
					<script type="text/javascript">
					   checkJS()
					</script>
				</form>
%include('footer')


