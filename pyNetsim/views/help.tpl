%include('header')
<style>
p.main {
    text-align: justify;
}
</style>

<h1>Help page <img src="static/question.png"  height="45" width="45"><h1>

<h2>Add a rule</h2>
<p class="main">
   <b>limit packets</b>
      limits the effect of selected options to the indicated number of next packets.
</br>
   <b>delay</b>
       adds the chosen delay to the packets outgoing to chosen network
       interface. The optional parameters allows to introduce a delay
       variation and a correlation.  Delay and jitter values are expressed
       in ms while correlation is percentage.
</br>
   <b>distribution</b>
       allow the user to choose the delay distribution. If not specified,
       the default distribution is Normal. Additional parameters allow to
       consider situations in which network has variable delays depending on
       traffic flows concurring on the same path, that causes several delay
       peaks and a tail.
</br>
   <b>loss random</b>
       adds an independent loss probability to the packets outgoing from the
       chosen network interface. It is also possible to add a correlation,
       but this option is now deprecated due to the noticed bad behavior.
</br>
   <b>corrupt</b>
       allows the emulation of random noise introducing an error in a random
       position for a chosen percent of packets. It is also possible to add
       a correlation through the proper parameter.
</br>
   <b>duplicate</b>
       using this option the chosen percent of packets is duplicated before
       queuing them. It is also possible to add a correlation through the
       proper parameter.
</br>
   <b>reorder</b>
       to use reordering, a delay option must be specified. There are two
       ways to use this option (assuming 'delay 10ms' in the options list).
</br>
       <b>reorder </b><i>25% 50%</i> <b>gap </b><i>5</i>
       in this first example, the first 4 (gap - 1) packets are delayed by
       10ms and subsequent packets are sent immediately with a probability
       of 0.25 (with correlation of 50% ) or delayed with a probability of
       0.75. After a packet is reordered, the process restarts i.e. the next
       4 packets are delayed and subsequent packets are sent immediately or
       delayed based on reordering probability. To cause a repeatable
       pattern where every 5th packet is reordered reliably, a reorder
       probability of 100% can be used.
</br>
       <b>reorder </b><i>25% 50%</i>
       in this second example 25% of packets are sent immediately (with
       correlation of 50%) while the others are delayed by 10 ms.
</br>
   <b>rate</b>
       delay packets based on packet size and is a replacement for <i>TBF</i>.
       Rate can be specified in common units (e.g. 100kbit).
</br>
       <b>ip </b><i>IP</i>
       <b>ip6 </b><i>IP6</i>
              Assume packet starts with an IPv4 ( <b>ip</b>) or IPv6 ( <b>ip6</b>) header.
              <i>IP</i>/<i>IP6</i> then allows to match various header fields:
</br>
</br>              <b>src </b><i>ADDR</i>
</br>              <b>dst </b><i>ADDR</i>
</br>
                     Compare Source or Destination Address fields against
                     the value of <i>ADDR</i>.  The reserved words <b>default</b>, <b>any </b>and
                     <b>all </b>effectively match any address. Otherwise an IP
                     address of the particular protocol is expected,
                     optionally suffixed by a prefix length to match whole
                     subnets. In case of IPv4 a netmask may also be given.
</br>
</br>
               <b>protocol </b>
                     Match the Protocol (IPv4) or Next Header (IPv6) field
                     value, e.g. 6 for TCP.
</br>
</br>              <b>sport </b>
</br>              <b>dport </b>
</br>
             Match layer four source or destination ports. This is
             dangerous as well, as it assumes a suitable layer four
             protocol is present (which has Source and Destination
             Port fields right at the start of the header and 16bit
             in size).  Also minimal header size for IPv4 and lack
             of IPv6 extension headers is assumed.
</br>
</br>
             <b>flowlabel </b>
</br>
                     IPv6 only. Match the Flow Label field's value. Note
                     that Flow Label itself is only 20bytes long, which are
                     the least significant ones here. The remaining upper
                     12bytes match Version and Traffic Class fields.
</p>

<h2>Statistic <img src="static/important.png" height="30" width="30"></h2>
<p class="main">
</br><b>qdisc</b> — A queue discipline (qdisc) is a set of rules that determine the order in which arrivals are serviced. It is a packet queue with an algorithm that decides when to send each packet. This show all rules regarding delay, loss, reorder and bandwidth limitation.
</br>
</br><b>filter</b> — Classification can be performed using filters. This shows all IP, port and MAC address filters.

</p>

<h2>Edit Rules<img src="static/info.png" height="30" width="30"></h2>
<p class="main">
</br>If you click on the first row with the deification of the fields and you can hide columns or order field.

</p>
%include('footer')
