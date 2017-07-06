%include('header')
                        <script src="static/changeValue.js"></script>
		%if defined('ruleID'):
				<form action="/UpdateRule" onsubmit="return validateForm()" method="post">
		%else:
			%if filter['ipVer'] == 'ipV4':
				<form action="/AddV4" onsubmit="return validateForm()" method="post">
			%else:
				<form action="/AddV6" onsubmit="return validateForm()" method="post">
			%end
		%end
					%if defined('emptyRule'):
						<div class="info">The rule is empty.</div>
					%end
					%if defined('showErrors'):
						<div class="error">Please check the marked fields!</div>
					%end
					<div class="block">
						<table border="1" width="100%">
							<tr>

						%if defined('ruleID'):
							<input type="hidden" name="ruleID" value="{{ruleID}}">
						%end

								<td width="100%" colspan="10" height="13" align="center">
									<p align="center"><b>Interface:
										<select size="1" name="selIntface">
											  %for intf in interfaces:
												%if intf == filter['selIntface']:
													<option selected>{{intf}}</option>
												%else:
													<option>{{intf}}</option>
												%end
											  %end
										</select>
										</b>
									</p>
								</td>
							</tr>
						%if filter['ipVer'] == 'ipV4': #change the Ip fields depending on the version
							<input type="hidden" name="ipVer" value="ipV4">
						%else:
							<input type="hidden" name="ipVer" value="ipV6">
						%end
							<tr>
								<td width="50%"  colspan="4" height="19" align="left">
									Buffer Limit(Packets)
							%if 'bufferLimitErr' in errors:
									<input type="text" id="error" name="txtBufferLimit" size="9" value={{filter['txtBufferLimit']}} onblur="testDigit('txtBufferLimit')">
							%else:
									<input type="text" name="txtBufferLimit" size="9" value={{filter['txtBufferLimit']}} onblur="testDigit('txtBufferLimit')">
							%end
									Default=1000
								</td>
								<td width="50%" colspan="4" height="19" align="left">
									Bandwidth(Kb/s)
							%if 'bandwidthErr' in errors:
									<input type="text" id="error" name="txtBandwidth" size="9" value={{filter['txtBandwidth']}} onblur="testDigit('txtBufferLimit')">
							%else:
									<input type="text" name="txtBandwidth" size="10" value={{filter['txtBandwidth']}} onblur="testDigit('txtBandwidth')">
							%end
								</td>
								<td width="11%" height="28">Distribution</td>
								<td width="9%" height="28">
									<select size="1" name="selDelayDistribution">
										%for dstrbution in ['-N/A-', 'Normal', 'Pareto', 'Paretonormal']:
											%if dstrbution == filter['selDelayDistribution']:
												<option selected>{{dstrbution}}</option>
											%else:
												<option>{{dstrbution}}</option>
											%end
										%end
									</select>
								</td>
							</tr>
							<tr>
								<td width="16%" colspan="2" height="19">
									<p align="center"><b>Delay</b></p>
								</td>
								<td width="16%" colspan="2" height="19">
									<p align="center"><b>Packet reordering</b></p>
								</td>
								<td width="16%" colspan="2" height="19">
									<p align="center"><b>Loss</b></td></p>
								<td width="16%" colspan="2" height="19">
									<p align="center"><b>Duplication</b></p>
								</td>
								<td width="16%" colspan="2" height="19">
									<p align="center"><b>Corruption</b></p>
								</td>
							</tr>
							<tr>
								<td width="11%" height="23">Delay time(ms) </td>
							%if 'delayErr' in errors:
								<td width="9%" height="23"><input type="text" id="error" name="txtDelay" size="9" value={{filter['txtDelay']}} onblur="testDigit('txtDelay')"></td>
							%else:
								<td width="9%" height="23"><input type="text" name="txtDelay" size="9" value={{filter['txtDelay']}} onblur="testDigit('txtDelay')"></td>
							%end
								<td width="9%" height="23">Reordering(%)</td>
							%if 'reorderErr' in errors:
								<td width="9%" height="23"><input type="text" id="error" name="txtReorder" size="9" value={{filter['txtReorder']}} onblur="testFloat('txtReorder')"></td>
							%else:
								<td width="9%" height="23"><input type="text" name="txtReorder" size="9" value={{filter['txtReorder']}} onblur="testFloat('txtReorder')"></td>
							%end
								<td width="11%" height="23">Loss(%)</td>
							%if 'lossErr' in errors:
								<td width="9%" height="23"><input type="text" id="error" name="txtLoss" size="9" value={{filter['txtLoss']}} onblur="testFloat('txtLoss')"></td>
							%else:
								<td width="9%" height="23"><input type="text" name="txtLoss" size="9" value={{filter['txtLoss']}} onblur="testFloat('txtLoss')"></td>
							%end
								<td width="11%" height="23">Duplication(%)</td>
							%if 'dupErr' in errors:
								<td width="9%" height="23"><input type="text" id="error" name="txtDup" size="9" value={{filter['txtDup']}} onblur="testFloat('txtDup')"></td>
							%else:
								<td width="9%" height="23"><input type="text" name="txtDup" size="9" value={{filter['txtDup']}} onblur="testFloat('txtDup')"></td>
							%end
								<td width="11%" height="23">Duplication(%)</td>
							%if 'curpErr' in errors:
								<td width="9%" height="23"><input type="text" id="error" name="txtCurp" size="9" value={{filter['txtCurp']}} onblur="testFloat('txtCurp')"></td>
							%else:
								<td width="9%" height="23"><input type="text" name="txtCurp" size="9" value={{filter['txtCurp']}} onblur="testFloat('txtCurp')"></td>
							%end
							</tr>
							<tr>
								<td width="11%" height="1">Jitter(ms)</td>
							%if 'delayJitterErr' in errors:
								<td width="9%" height="1"><input type="text" id="error" name="txtDelayJitter" size="9" value={{filter['txtDelayJitter']}} onblur="testDigit('txtDelayJitter')"></td>
							%else:
								<td width="9%" height="1"><input type="text" name="txtDelayJitter" size="9" value={{filter['txtDelayJitter']}} onblur="testDigit('txtDelayJitter')"></td>
							%end
								<td width="11%" height="1">Correlation(%)</td>
							%if 'reorderCorrelationErr' in errors:
								<td width="9%" height="1"><input type="text" id="error" name="txtReorderCorrelation" size="9" value={{filter['txtReorderCorrelation']}} onblur="testFloat('txtReorderCorrelation')"></td>
							%else:
								<td width="9%" height="1"><input type="text"  name="txtReorderCorrelation" size="9" value={{filter['txtReorderCorrelation']}} onblur="testFloat('txtReorderCorrelation')"></td>
							%end
								<td width="11%" height="1">Correlation(%)</td>
							%if 'lossCorreErr' in errors:
								<td width="9%" height="1"><input type="text" id="error" name="txtLossCorrelation" size="9" value={{filter['txtLossCorrelation']}} onblur="testFloat('txtLossCorrelation')"></td>
							%else:
								<td width="9%" height="1"><input type="text"  name="txtLossCorrelation" size="9" value={{filter['txtLossCorrelation']}} onblur="testFloat('txtLossCorrelation')"></td>
							%end
								<td width="11%" height="1">Correlation(%)</td>
							%if 'dupCorrelationErr' in errors:
								<td width="9%" height="1"><input type="text" id="error" name="txtDupCorrelation" size="9" value={{filter['txtDupCorrelation']}} onblur="testFloat('txtDupCorrelation')"></td>
							%else:
								<td width="9%" height="1"><input type="text"  name="txtDupCorrelation" size="9" value={{filter['txtDupCorrelation']}} onblur="testFloat('txtDupCorrelation')"></td>
							%end
								<td width="11%" height="3">Correlation(%)</td>
							%if 'curptionCorrelationErr' in errors:
								<td width="9%" height="3"><input type="text" id="error" name="txtCurptionCorrelation" size="9" value={{filter['txtCurptionCorrelation']}} onblur="testFloat('txtCurptionCorrelation')"></td>
							%else:
								<td width="9%" height="3"><input type="text"  name="txtCurptionCorrelation" size="9" value={{filter['txtCurptionCorrelation']}} onblur="testFloat('txtCurptionCorrelation')"></td>
							%end
							</tr>
							<tr>
								<td width="11%" height="27">Correlation(%)</td>
							%if 'delayCorrelationErr' in errors:
								<td width="9%" height="27"><input type="text" id="error" name="txtDelayCorrelation" size="9" value={{filter['txtDelayCorrelation']}} onblur="testFloat('txtDelayCorrelation')"></td>
							%else:
								<td width="9%" height="27"><input type="text"  name="txtDelayCorrelation" size="9" value={{filter['txtDelayCorrelation']}} onblur="testFloat('txtDelayCorrelation')"></td>
							%end
								<td width="11%" height="27">Gap(packets)</td>
							%if 'gapErr' in errors:
								<td width="9%" height="27"><input type="text" id="error" name="txtGap" size="9" value={{filter['txtGap']}} onblur="testDigit('txtGap')"></td>
							%else:
								<td width="9%" height="27"><input type="text"  name="txtGap" size="9" value={{filter['txtGap']}} onblur="testDigit('txtGap')"></td>
							%end
							</tr>
							<tr>
							</tr>
							<tr>
								<td colspan="6">
									<table style="width:100%">
										<tbody>
											<tr>
											%if filter['ipVer'] == 'ipV4':
												<td class="leftText">IP source addr</td>
												%if 'ipV4SrcErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="ipSrc" size="13" value={{filter['ipSrc']}} onblur="checkipV4('ipSrc')"></td>
												%else:
													<td class="leftInput"><input type="text"  name="ipSrc" size="13" value={{filter['ipSrc']}} onblur="checkipV4('ipSrc')"></td>
												%end
												<td class="leftText">Ip source subnet</td>
												%if 'ipV4SrcSubErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="ipSrcSub" size="13" value={{filter['ipSrcSub']}} onblur="checkipV4('ipSrcSub')"></td>
												%else:
													<td class="leftInput"><input type="text"  name="ipSrcSub" size="13" value={{filter['ipSrcSub']}} onblur="checkipV4('ipSrcSub')"></td>
												%end
											%else:
												<td class="leftText">IP source addr</td>
												%if 'ipV6SrcErr' in errors:
													<td class="leftInput"><input type="text"  id="error" name="ipSrcV6" size="32" value={{filter['ipSrc']}} onblur="checkIPv6('ipSrcV6')"></td>
												%else:
													<td class="leftInput"><input type="text" name="ipSrcV6" size="32" value={{filter['ipSrc']}} onblur="checkIPv6('ipSrcV6')"></td>
												%end
												<td class="leftText">Ip source subnet</td>
												%if 'ipV6SrcSubErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="ipSrcSubV6" size="13" value={{filter['ipSrcSub']}} onblur="testDigit('ipSrcSubV6')"></td>
												%else:
													<td class="leftInput"><input type="text" name="ipSrcSubV6" size="13" value={{filter['ipSrcSub']}} onblur="testDigit('ipSrcSubV6')"></td>
												%end
											%end
											</tr>
											<tr>
											%if filter['ipVer'] == 'ipV4':
												<td class="leftText">IP destination addr</td>
												%if 'ipV4DestErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="ipDest" size="13" value={{filter['ipDest']}} onblur="checkipV4('ipDest')"></td>
												%else:
													<td class="leftInput"><input type="text"  name="ipDest" size="13" value={{filter['ipDest']}} onblur="checkipV4('ipDest')"></td>
												%end
												<td class="leftText">IP destination subnet</td>
												%if 'ipV4DestSubErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="ipDestSub" size="13" value={{filter['ipDestSub']}} onblur="checkipV4('ipDestSub')"></td>
												%else:
													<td class="leftInput"><input type="text"  name="ipDestSub" size="13" value={{filter['ipDestSub']}} onblur="checkipV4('ipDestSub')"></td>
												%end
											%else:
												<td class="leftText">IP destination addr</td>
												%if 'ipV6DestErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="ipDestV6" size="32" value={{filter['ipDest']}} onblur="checkIPv6('ipDestV6')"></td>
												%else:
													<td class="leftInput"><input type="text" name="ipDestV6" size="32" value={{filter['ipDest']}} onblur="checkIPv6('ipDestV6')"></td>
												%end
												<td class="leftText">IP destination subnet</td>
												%if 'ipV6DestSubErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="ipDestSubV6" size="13" value={{filter['ipDestSub']}} onblur="testDigit('ipDestSubV6')"></td>
												%else:
													<td class="leftInput"><input type="text" name="ipDestSubV6" size="13" value={{filter['ipDestSub']}} onblur="testDigit('ipDestSubV6')"></td>
												%end
											%end
											</tr>
											<tr>
												<td class="leftText">Source port</td>
												%if 'portSrcErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="portSrc" size="13" value={{filter['portSrc']}} onblur="testDigit('portSrc')"></td>
												%else:
													<td class="leftInput"><input type="text" name="portSrc" size="13" value={{filter['portSrc']}}  onblur="testDigit('portSrc')"></td>
												%end
												<td class="leftText">Destination port</td>
												%if 'portDstErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="portDst" size="13" value={{filter['portDst']}} onblur="testDigit('portDst')"></td>
												%else:
													<td class="leftInput"><input type="text" name="portDst" size="13" value={{filter['portDst']}}  onblur="testDigit('portDst')"></td>
												%end
											</tr>
											<tr>
											%if filter['ipVer'] == 'ipV4':
												<td class="leftText">TOS</td>
												%if 'flowlabelTOSErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="tos" size="13" value={{filter['flowlabelTOS']}} onblur="testDigit('tos')"></td>
												%else:
													<td class="leftInput"><input type="text" name="tos" size="13" value={{filter['flowlabelTOS']}} onblur="testDigit('tos')"></td>
												%end
											%else:
												<td class="leftText">Flowlabel</td>
												%if 'flowlabelTOSErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="flowlabel" size="13" value={{filter['flowlabelTOS']}} onblur="testDigit('flowlabel')"></td>
												%else:
													<td class="leftInput"><input type="text" name="flowlabel" size="13" value={{filter['flowlabelTOS']}} onblur="testDigit('flowlabel')"></td>
												%end
											%end
												<td class="leftText">Transport Protocol</td>
												<td class="leftInput">
													<select name="transport" onChange="changeValue('transportPrtc', this.selectedIndex)">
														% for transp in ['ALL', 'UDP', 'TCP', 'Custom']:
															%if transp == filter['transport']:
																<option selected>{{transp}}</option>
															%else:
																<option>{{transp}}</option>
															%end
														% end
													</select>
													%if filter['transport'] == "Custom":
														%if 'transportPrtcErr' in errors:
															<input type="text" id="error" name="transportPrtc" size="4" value={{filter['transportPrtc']}} onblur="testDigit('transportPrtc')">
														%else:
															<input type="text" name="transportPrtc" size="4" value={{filter['transportPrtc']}} onblur="testDigit('transportPrtc')">
														%end
													%else:
														<input type="text" name="transportPrtc" size="4" disabled="disabled" value={{filter['transportPrtc']}} onblur="testDigit('transportPrtc')">
													%end
												</td>
											</tr>
											<tr>
												<td class="leftText">MAC source addr</td>
												%if 'macSrcErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="macSrc" size="13" value={{filter['macSrc']}} onblur="checkMAC('macSrc')"></td>
												%else:
													<td class="leftInput"><input type="text" name="macSrc" size="13" value={{filter['macSrc']}} onblur="checkMAC('macSrc')"></td>
												%end
												<td class="leftText">MAC destination addr</td>
												%if 'macDestErr' in errors:
													<td class="leftInput"><input type="text" id="error" name="macDest" size="13" value={{filter['macDest']}} onblur="checkMAC('macDest')"></td>
												%else:
													<td class="leftInput"><input type="text" name="macDest" size="13" value={{filter['macDest']}} onblur="checkMAC('macDest')"></td>
												%end
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</table>
					</div>
					<div class="buttons">
						<a href="/">&lt; Return to index page</a>

                                                %if defined('ruleID'):
                                                        <input type="submit" value="Update rule set" name="btnAdd">
                                                %else:
							<input type="submit" value="Add a rule set" name="btnAdd">
                                                %end

					</div>
				</form>
%include('footer')
