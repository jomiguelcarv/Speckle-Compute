#py 3.7.7
import compute_rhino3d
import compute_rhino3d.Util
import base64

def send_to_compute():
    #Credentials
    compute_rhino3d.Util.url = "http://3.78.144.62/"
    compute_rhino3d.Util.apiKey = "SpeckleCompute02"
    send_to_compute_stream = "https://macad.speckle.xyz/streams/28a211b286/models/c6a5549e3b" #check for stream or projects??
    sendModel_to_compute_stream = "https://macad.speckle.xyz/streams/28a211b286/models/4e98b63e56" 
    receive_from_compute_stream = "https://macad.speckle.xyz/streams/28a211b286/models/f2dd4b4cca" #check for stream or projects??
    gh_definition = "HyperB_Data_GH_Residential-metrics_RA.ghx"

    gh_data = open(gh_definition, mode="r", encoding="utf-8-sig").read()
    data_bytes = gh_data.encode("utf-8")
    encoded = base64.b64encode(data_bytes)
    decoded = encoded.decode("utf-8")

    json_data={
        "algo": decoded,
        "pointer": None,
        "values": [
            {
                "ParamName": "RH_IN:SendData",
                "InnerTree": {
                    "{ 0; }": [
                        {
                            "type": "String",
                            "data": send_to_compute_stream
                        }
                    ]
                }
            }, 
                        {
                "ParamName": "RH_IN:SendGeo",
                "InnerTree": {
                    "{ 0; }": [
                        {
                            "type": "String",
                            "data": sendModel_to_compute_stream
                        }
                    ]
                }
            }, 
            {
                "ParamName": "RH_IN:Receive",
                "InnerTree": {
                    "{ 0; }": [
                        {
                            "type": "String",
                            "data": receive_from_compute_stream
                        }
                    ]
                }
            }, 
        ] 
    }


    response = compute_rhino3d.Util.ComputeFetch("grasshopper", json_data)