```java
  import com.jcabi.aspects.Tv;
import com.jcabi.ssh.SshByPassword;

  public class SshByPassword {

    public SshByPassword(String host, String user, String pass) {
      this(host, 22, user, pass);
    }

    public SshByPassword(String host, int port, String user, String pass) {
      this(host, port, user, pass, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset) {
      this(host, port, user, pass, charset, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config) {
      this(host, port, user, pass, charset, config, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost) {
      this(host, port, user, pass, charset, config, proxyHost, 0);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, proxyPass, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass, String proxyCharset) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, proxyPass, proxyCharset, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass, String proxyCharset, String proxyConfig) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, proxyPass, proxyCharset, proxyConfig, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass, String proxyCharset, String proxyConfig, String proxyTv) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, proxyPass, proxyCharset, proxyConfig, proxyTv, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass, String proxyCharset, String proxyConfig, String proxyTv, String localConfig) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, proxyPass, proxyCharset, proxyConfig, proxyTv, localConfig, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass, String proxyCharset, String proxyConfig, String proxyTv, String localConfig, Integer timeout) {
      this.host = host;
      this.port = port;
      this.user = user;
      this.pass = pass;
      this.charset = charset;
      this.config = config;
      this.proxy = new Proxy(proxyHost, proxyPort, proxyUser, proxyPass, proxyCharset, proxyConfig, proxyTv);
      this.localConfig = localConfig;
      this.timeout = timeout;
    }

    public final String host;

    public final int port;

    public final String user;

    public final String pass;

    public final String charset;

    public final String config;

    public final Proxy proxy;

    public final String localConfig;

    public final Integer timeout;

    public SshByPassword(String host, String user, String pass, String charset) {
      this(host, 22, user, pass, charset);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset) {
      this(host, port, user, pass, charset, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config) {
      this(host, port, user, pass, charset, config, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost) {
      this(host, port, user, pass, charset, config, proxyHost, 0);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, proxyPass, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass, String proxyCharset) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, proxyPass, proxyCharset, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass, String proxyCharset, String proxyConfig) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, proxyPass, proxyCharset, proxyConfig, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass, String proxyCharset, String proxyConfig, String proxyTv) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, proxyPass, proxyCharset, proxyConfig, proxyTv, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass, String proxyCharset, String proxyConfig, String proxyTv, String localConfig) {
      this(host, port, user, pass, charset, config, proxyHost, proxyPort, proxyUser, proxyPass, proxyCharset, proxyConfig, proxyTv, localConfig, null);
    }

    public SshByPassword(String host, int port, String user, String pass, String charset, String config, String proxyHost, int proxyPort, String proxyUser, String proxyPass, String proxyCharset, String proxyConfig, String proxyTv, String localConfig, Integer timeout) {
      this.host = host;
      this.port = port;
      this.user = user;
      this.pass = pass;
      this.charset = charset;
      this.config = config;
      this.proxy = new Proxy(proxyHost, proxyPort, proxyUser, proxyPass, proxyCharset, proxyConfig, proxyTv);
      this.localConfig = localConfig;
      this.timeout = timeout;
    }

    public final String host;

    public final int port;

    public final String user;

    public final String pass;

    public final String charset;

    public final String config;

    public final Proxy proxy;

    public final String localConfig;

    public final Integer timeout;

  }
```