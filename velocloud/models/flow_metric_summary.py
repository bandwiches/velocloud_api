from dataclasses import dataclass


@dataclass
class FlowMetricSummary:
    """Flow Metric Summary"""
    bytesRx: int = None
    bytesTx: int = None
    flowCount: int = None
    packetsRx: int = None
    packetsTx: int = None
    totalBytes: int = None
    totalPackets: int = None
