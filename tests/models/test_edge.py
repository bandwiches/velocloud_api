from velocloud.models import edge


EDGE_TEMPLATE = {
    "id": 12345,
    "created": "2019-04-30T15:45:37.000Z",
    "enterpriseId": 1234,
    "siteId": 12345,
    "activationKey": "FFFF-FFFF-FFFF-FFFF",
    "activationKeyExpires": "2019-05-30T15:45:37.000Z",
    "activationState": "ACTIVATED",
    "activationTime": "2019-04-30T16:14:04.000Z",
    "softwareVersion": "1.1.1",
    "buildNumber": "1234-12345678-12-1234567890",
    "factorySoftwareVersion": "1.1.1",
    "factoryBuildNumber": "1234-123456789-12-123",
    "softwareUpdated": "2020-08-08T14:30:35.000Z",
    "selfMacAddress": "00:00:00:00:00:00",
    "deviceId": "12345678-1234-1234-1234-123456789012",
    "logicalId": "12345678-1234-1234-1234-123456789012",
    "serialNumber": "0012345678901",
    "modelNumber": "edge000",
    "deviceFamily": "EDGE0X0",
    "name": "Fake Name",
    "dnsName": None,
    "description": None,
    "alertsEnabled": 1,
    "operatorAlertsEnabled": 1,
    "edgeState": "CONNECTED",
    "edgeStateTime": "2021-01-21T22:49:45.000Z",
    "isLive": 0,
    "systemUpSince": "2021-02-19T20:28:32.000Z",
    "serviceUpSince": "2021-02-19T20:29:12.000Z",
    "lastContact": "2021-04-22T14:15:03.000Z",
    "serviceState": "IN_SERVICE",
    "endpointPkiMode": "CERTIFICATE_DISABLED",
    "haState": "READY",
    "haPreviousState": "FAILED",
    "haLastContact": "2021-02-19T20:30:24.000Z",
    "haSerialNumber": "0012345678901",
    "modified": "2021-04-22T14:15:03.000Z",
    "customInfo": None
}


class TestEdge(object):
    def test_edge(self):
        e = edge.Edge.from_dict(EDGE_TEMPLATE)


class TestEdgeProvision(object):
    def test_edge_provision(self):
        e = edge.EdgeProvision(
            configurationId=0,
            modelNumber=edge.ModelNumber('edge6x0')
        )
