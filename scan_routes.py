from flask import Flask, render_template, request, redirect, url_for
import nmap
app = Flask(__name__)

@app.route('/scan')
def scan_network():
    # สแกนเครือข่ายในช่วง IP (เช่น 192.168.1.0/24)
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.1.0/24', arguments='-sn')  # เปลี่ยนช่วง IP ให้ตรงกับเครือข่ายของคุณ

    hosts = nm.all_hosts()
    devices = []

    for host in hosts:
        device_info = {
            'ip': host,
            'hostname': nm[host].hostname(),
            'state': nm[host].state()
        }
        devices.append(device_info)

    return render_template('results.html', devices=devices)
