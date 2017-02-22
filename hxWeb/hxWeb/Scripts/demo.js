var Demo= {
    createConn:function() {
        var conn = new WebIM.connection({
            https: WebIM.config.https,
            url: WebIM.config.xmppURL,
            isAutoLogin: WebIM.config.isAutoLogin,
            isMultiLoginSessions: WebIM.config.isMultiLoginSessions
        });
        return conn;
    },
    login: function (uname, pwd) {
        var t;
        var conn = Demo.createConn();
        var options = {
            apiUrl: WebIM.config.apiURL,
            user: uname,
            pwd: pwd,
            appKey: WebIM.config.appkey,
            success: function (token) {
                token = token.access_token; 
                t = token;
                WebIM.utils.setCookie('webim_' + uname, token, 1);

                conn.open(options);
                return t;
            },
            error:function(e) {
                alert(e)
            }
        };
    },
    openConn: function (token) { 
        var options = {
            apiUrl: WebIM.config.apiURL,
            accessToken: token,
            appKey: WebIM.config.appkey
        };
        var conn = Demo.createConn();
        conn.open(options);
        return conn;
    }
}