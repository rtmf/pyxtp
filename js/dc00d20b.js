window.Fonticons||(window.Fonticons={}),function(e,n,t){function o(e,t){var o,i="IE",d=n.createElement("B"),s=n.documentElement;return e&&(i+=" "+e,t&&(i=t+" "+i)),d.innerHTML="<!--[if "+i+']><b id="fitest"></b><![endif]-->',s.appendChild(d),o=!!n.getElementById("fitest"),s.removeChild(d),o}function i(){for(var e=[/.*/],t=n.location.hostname,i=0;i<e.length;i++)if(e[i].test(t)){var d=n.createElement("link"),s=o(8,"lte")?"dc00d20b-sd":"dc00d20b";d.href="https://fonticons-free-fonticons.netdna-ssl.com/kits/dc00d20b/"+s+".css",d.media="all",d.rel="stylesheet",n.getElementsByTagName("head")[0].appendChild(d);break}}e.Fonticons.load=i}(this,document),window.Fonticons.load();