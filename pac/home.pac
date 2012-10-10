// This is a Proxy Auto Config (PAC) file for Y! geeks to work from home with
// a iPad, iOS cannot connect the corp VPN server (I believe it's a hacked
// version)
//
// Configure your wifi network to use this PAC, then create a local socks
// proxy with a ssh client e.g. iSSH
//
//      iSSH -L1080:corp-socks:1080 corp-proxy
//
function FindProxyForURL(url, host)
{
    if (shExpMatch(url, "*yahoo*")) {
        return "SOCKS localhost:1080";
    } else {
        return "DIRECT";
    }
}
