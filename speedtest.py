import speedtest as suraj_speedtest
def speedtest():
        test = suraj_speedtest.Speedtest()
        print("Downloading Speed test ....")
        download = test.download()
        download = round(download / 10**6,2)
        print(f"The Download Speed is : {download} Mbps..")
        print("Uploading Speed test ....")
        upload = test.upload()
        upload = round(upload/ 10**6,2)
        print(f"The Upload speed is : {upload} Mbps..")

        ping = test.results.ping
        print(f"The Ping is : {ping} ms")
speedtest()
