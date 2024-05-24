```java
import com.jcabi.aspects.Tv;

import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.concurrent.TimeUnit;

public class SshByPassword implements Ssh {
    private final String host;
    private final int port;
    private final String user;
    private final String pass;
    private final transient long timeout;
    private final transient TimeUnit unit;

    public SshByPassword(final String host, final String user, final String pass) {
        this(host, 22, user, pass);
    }

    public SshByPassword(final String host, final int port, final String user, final String pass) {
        this(host, port, user, pass, 30L, TimeUnit.SECONDS);
    }

    public SshByPassword(final String host, final int port, final String user, final String pass, final long timeout, final TimeUnit unit) {
        this.host = host;
        this.port = port;
        this.user = user;
        this.pass = pass;
        this.timeout = timeout;
        this.unit = unit;
    }

    @Override
    public Socket connect() throws IOException {
        InetAddress addr = InetAddress.getByName(this.host);
        return new Socket(addr, this.port);
    }

    @Override
    public String user() {
        return this.user;
    }

    @Override
    public String pass() {
        return this.pass;
    }

    @Override
    public long timeout() {
        return this.timeout;
    }

    @Override
    public TimeUnit unit() {
        return this.unit;
    }
}
```