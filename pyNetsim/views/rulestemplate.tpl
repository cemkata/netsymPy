%include('header')
<style>
        table, th, td {
                       border: 1px solid black;
                       border-collapse: collapse;
        }
        th, td {
                padding: 5px;
                text-align: left;
        }
		.show {
			position: absolute;
			background-color:#C0C0C0;
			border: 1px solid blue;
			padding: 2px;
			display: block;
			margin: 0;
			list-style-type: none;
			list-style: none;
		}

		.hide {
			display: none;
		}
		tr:nth-child(even) {
			background-color: #f1f1f1;
		}
		.selected {
			border-style:dashed;
		}
</style>
	<form id="actionForm" action="/editHandler" method="post" onsubmit="return false;">
		<input type="hidden" name="editFormAction" value="">
		<input type="hidden" name="ruleID" value="">
		<div class="buttons">
			<button name="btnDel" onclick="setActionEdit('delete')" disabled="">Delete rule(s)</button>
			<button name="btnEdit" onclick="setActionEdit('edit')" disabled="">Edit rule</button>
			<button name="btnStop" onclick="setActionEdit('disable')" disabled="">Disable rule(s)</button>
			<button name="btnCopy" onclick="setActionEdit('copy')" disabled="">Copy rule</button>
			<button name="btnCopyDifIPVer" onclick="setActionEdit('changeIp')" disabled="">Change rule (different IP version)</button>
		</div>
	</form>
	</br>
	<table id="rules">
		<tbody>
			<tr>
				<td><input type="checkbox" name="deletAll" onclick="selectAll();"></td>
				<td>Active</td>
				<td>Interface</td>
				<td>Buffer Limit</td>
				<td>Bandwidth</td>
				<td>Distribution</td>
				<td>Delay time</td>
				<td>Delay Jitter</td>
				<td>Delay Correlation</td>
				<td>Reordering</td>
				<td>Reordering Correlation</td>
				<td>Gap</td>
				<td>Loss</td>
				<td>Loss Correlation</td>
				<td>Duplication</td>
				<td>Duplication Correlation</td>
				<td>Corruption</td>
				<td>Corruption Correlation</td>
				<td>IP source</td>
				<td>Source subnet</td>
				<td>IP destination</td>
				<td>Destination subnet</td>
				<td>Source port</td>
				<td>Destination port</td>
				<td>TOS/Flowlabel</td>
				<td colspan="2"> <center>Transport Protocol</center></td>
				<td>MAC source</td>
				<td>MAC destination</td>
			</tr>
			%for i in filter:
				<tr>
					<td><input type="checkbox" name="selectedCheckbox" onclick="checkAll();" id='{{i['ruleID']}}'></td>
						%if i['rulestatus']=='On':
							<td><img src="static/check.png" style="vertical-align:middle" id='disabled' height="30"></td>
						%else:
							<td><img src="static/disabled.png" style="vertical-align:middle" id='enabled' height="30"></td>
						%end
					<td>{{i['selIntface']}}</td>
					<td>{{i['txtBufferLimit']}}</td>
					<td>{{i['txtBandwidth']}}</td>
					<td>{{i['distribution']}}</td>
					<td>{{i['txtDelay']}}</td>
					<td>{{i['txtDelayJitter']}}</td>
					<td>{{i['txtDelayCorrelation']}}</td>
					<td>{{i['txtReorder']}}</td>
					<td>{{i['txtReorderCorrelation']}}</td>
					<td>{{i['txtGap']}}</td>
					<td>{{i['txtLoss']}}</td>
					<td>{{i['txtLossCorrelation']}}</td>
					<td>{{i['txtDup']}}</td>
					<td>{{i['txtDupCorrelation']}}</td>
					<td>{{i['txtCurp']}}</td>
					<td>{{i['txtCurptionCorrelation']}}</td>
					<td name = '{{i['ipVersion']}}'>{{i['ipSrc']}}</td>
					<td>{{i['ipSrcSub']}}</td>
					<td>{{i['ipDest']}}</td>
					<td>{{i['ipDestSub']}}</td>
					<td>{{i['portSrc']}}</td>
					<td>{{i['portDst']}}</td>
					<td>{{i['flowlabelTOS']}}</td>
					<td>{{i['transport']}}</td><td>{{i['transportPrtc']}}</td>
					<td>{{i['macSrc']}}</td>
					<td>{{i['macDest']}}</td>
				</tr>
			%end
		</tbody>
	</table>

	<div class="hide" id="rmenu">
				<button onclick="hidemenu();" style="font-size: 8px; background-color: #555555; float: right;">X</button><br>
				<button onclick="showAll(); hidemenu();" style="font-size: 12px; background-color: #e7e7e7; color: black; float: left;">Show all</button><br>
				<button onclick="show_hide_column(selecteCell, false); hidemenu();" style="font-size: 12px; background-color: #e7e7e7; color: black; float: left;">Hide colum</button><br>
				<button onclick="sortTable(selecteCell, true); hidemenu();" style="font-size: 12px; background-color: #e7e7e7; color: black; float: left;">Sort A-Z</button><br>
				<button onclick="sortTable(selecteCell, false); hidemenu();" style="font-size: 12px; background-color: #e7e7e7; color: black; float: left;">Sort Z-A</button><br>
	</div>

<script src="static/editrules.js"></script>
<script src="static/home.js"></script>
<script>
var selecteCell=-1;
var formArray = [];

addRowHandlers();
checkboxHandler();
</script>

%include('footer')
