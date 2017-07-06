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

        pre {
             display: block;
             font-family: monospace;
             white-space: pre;
             margin: 1em 0;
             font-size: 1.5em;
        }
</style>

%if defined('tcnotrun'):
</br>
</br>
<b>tc is not running</b>
</br>
</br>
<a href="/">Home</a>
%else:
%for item in tcstatistic:
</br>
</br>
	<table>
		<tr>
			<td><b>{{item['interface']}}<b></td>
		</tr>
		<tr>
			<td></td><td><i>Filter</i></td>
		</tr>
		<tr>
			<td></td><td></td><td><pre>{{item['filterstatistic']}}</pre></td>
		</tr>
		<tr>
			<td></td><td><i>Queue(Qdisc)</i></td>
		</tr>
		<tr>
			<td></td><td></td><td><pre>{{item['qdiscstatistic']}}</pre></td>
		</tr>
	</table>
%end
</br>
</br>
<table>
	<tbody>
		<tr>
			<td><a href="/">Home</a></td>
			<td><a href="/Statistic">Refresh</a></td>
		</tr>
	</tbody>
</table>
%end
%include('footer')
