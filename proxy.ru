require 'net/http'

proxies = [
    "138.2.61.140:88",
    "123.182.58.221:8089",
    "185.189.199.75:23500",
    "164.132.170.100:80",
    "153.92.214.224:80",
    "120.196.207.10:80",
    "31.40.27.214:3128",
    "153.92.214.224:80",
    "177.185.92.193:3128",
    "170.81.241.14:999",
    "185.189.199.75:23500",
    "177.185.92.193:3128"
    # Add more proxy servers as needed
]

def write_callback(response, contents)
    response << contents
    contents.length
end

def make_network_request(url)
    proxies.each do |proxy|
        uri = URI(url)
        http = Net::HTTP.new(uri.host, uri.port, proxy.split(':')[0], proxy.split(':')[1])
        request = Net::HTTP::Get.new(uri.request_uri)
        response = ""
        http.request(request) do |res|
            res.read_body do |chunk|
                response << chunk
            end
        end
        if response.code == "200"
            return response
        end
    end
    raise "Failed to make a successful request using any proxy server."
end
