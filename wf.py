
<html>

<head>
    <title id="title"></title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="theme-color" content="#3B5998" />
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;" />
    <link rel="stylesheet" href="style.css">

</head>

<body>
        
        <form name="sendin" action="http://lawiehotspot.com/login" method="post">
            <input type="hidden" name="username" />
            <input type="hidden" name="password" />
            <input type="hidden" name="dst" value="" />
            <input type="hidden" name="popup" value="true" />
        </form>

        <script type="text/javascript" src="md5.js"></script>
        <script type="text/javascript">
            function doLogin() {
                document.sendin.username.value = document.login.username.value;
                document.sendin.password.value = hexMD5('\127' + document.login.password.value +
                    '\361\105\315\070\120\172\270\006\042\252\242\342\237\013\312\076');
                document.sendin.submit();
                return false;
            }
        </script>
        

            <div id="main" class="main">
            
            <div class="box">
                <h3 class="brand">Lawie Hotspot</h3>
            </div>
            <div class="box">
                <button id="btnvrc" class="small-button" onclick="voucher();"><i class="icon icon-ticket">&#xe802;</i> Voucher</button>
                <button id="btnmem" class="small-button" onclick="member();"><i class="icon icon-user-circle-o">&#xf2be;</i> Member</button>
                <button id="qr" class="small-button" onclick="window.location='https://laksa19.github.io/myqr';"> <i class="icon icon-qrcode">&#xe801;</i> QR
                    Code</button>
            </div>
            <div class="box" id="infologin">
            </div>
            <form autocomplete="off" name="login" action="http://lawiehotspot.com/login" method="post"  onSubmit="return doLogin()"
                >
                <input type="hidden" name="dst" value="" />
                <input type="hidden" name="popup" value="true" />
                <input class="username" name="username" type="text" value="" />
                <input class="password" name="password" placeholder="Password" type="hidden" />

                <button class="button" type="submit"><i class="icon icon-login">&#xe803;</i> Login</button>

            </form>

            

            

                        <table class="table">
                    <caption style="font-size: 16px; font-weight: bold;">.:WELCOME:.</caption>
        </div>
        <br />
        <div class="box" style="color:#000;">
            <i>Copyright &copy; 2018 Laksamadi</i><br />
            <i>Powered by <a style="color:#000; text-decoration:underline;" href="https://laksa19.github.io">Mikhmon</a></i>
            <!-- Tolong jangan dihilangkan bagian ini-->
        </div>

<script type="text/javascript">
var hostname = window.location.hostname;
document.getElementById('title').innerHTML = hostname  + " > login";

document.login.username.focus();

var infologin = document.getElementById('infologin');
infologin.innerHTML = "Masukkan Kode Voucher kemudian klik login.";

// login page 2 mode by Laksamadi Guko
var username = document.login.username;
var password = document.login.password;

username.placeholder = "Kode Voucher";

// set password = username
function setpass() {
    var user = username.value
    //user = user.toLowerCase();
    username.value = user;
    password.value = user;
}

username.onkeyup = setpass;

// change to voucher mode
function voucher() {
    username.focus();
    username.onkeyup = setpass;
    username.placeholder = "Kode Voucher";
    username.style = "border-radius:3px;"
    password.type = "hidden";
    infologin.innerHTML = "Masukkan Kode Voucher kemudian klik login.";
}

// change to member mode
function member() {
    username.focus();
    username.onkeyup = "";
    username.placeholder = "Username";
    username.style = "border-radius:3px 3px 0px 0px;"
    password.type = "password";
    infologin.innerHTML = "Masukkan Username dan Password kemudian klik login.";
}
</script>
</body>

</html>
