"""
Part - 1
Reliable Data Transfer
Problem: Implement a simple stop-and-wait Reliable Data Transfer 2.2 protocol. A simulated data
        channel can be used for data transfer which has an associated packet loss probability
        as given in the baseline.py file. Implementation should cover sending data and
        displaying the received data, receiving ACK for successful transmission, and
        retransmission in case the packet is not received/ suitable ACK is not received. Print
        statements must be given as mentioned in the baseline.py file and the output must be
        documented in the report.
"""

import random

class SimulatedChannel:
	def __init__(self, loss_rate=0.3):
		self.loss_rate = loss_rate
		self.packet = None

	def send(self, packet):
		if random.random() >= self.loss_rate:
			self.packet = packet
		else:
			self.packet = None

	def receive(self):
		if random.random() >= self.loss_rate:
			return self.packet
		return None

class RDTSender:
	def __init__(self, channel):
		self.channel = channel
		self.seq_num = 0

	def rdt_send(self, data, receiver):
		packet = self.make_packet(data)
		self.send_packet(packet)
		while True:
			ack_rcv = receiver.rdt_receive(packet)
			if ack_rcv:
				break
			else:
				print("\nSENDER: \nTimeout: Retransmitting the packet having sequence number = {}".format(packet['sequence_number']))
				self.send_packet(packet)
	
	def send_packet(self, packet):
		self.channel.send(packet)

	def make_packet(self, data):
		packet = {"sequence_number": self.seq_num, "data": data}
		self.seq_num = 1 - self.seq_num
		return packet

class RDTReceiver:
	def __init__(self, channel):
		self.channel = channel
	
	def rdt_receive(self, sender_packet):
		rcvd_pkt = self.receive_packet()
		if rcvd_pkt and rcvd_pkt["sequence_number"] == sender_packet["sequence_number"]:
			print("\nRECEIVER: \nReceived {} having sequence number {}".format((rcvd_pkt["data"]), rcvd_pkt["sequence_number"]))
			self.send_acknowledgement(rcvd_pkt["sequence_number"])
			return True
		else:
			return False

	def receive_packet(self):
		return self.channel.receive()

	def send_acknowledgement(self, seq_num):
		ack = {"ack_num": seq_num}
		print("\nRECEIVER: \nACK SENT : {}".format(seq_num))
		self.channel.send(ack)

def main():
    channel = SimulatedChannel()
    sender = RDTSender(channel)
    receiver = RDTReceiver(channel)

    with open("test_rdt.txt", "r") as file:
            for line in file:
                data, content = line.strip().split(' ', 1)
                sender.rdt_send((data, content), receiver)

if __name__ == '__main__':
    main()