```java
import com.jcabi.aspects.Tv;

import java.io.IOException;
import java.net.InetAddress;
import java.net.UnknownHostException;

public class SshByPassword extends SshByConfig {

    private final String host;
    private final String username;
    private final String password;

    public SshByPassword(String host, String username, String password) throws IOException {
        super(new SshConfig().setSession(new SshSession(host, username, password)));
        this.host = host;
        this.username = username;
        this.password = password;
    }

    @Override
    public Tv tv() {
        return new Tv(this);
    }

    public String host() {
        return host;
    }

    public String username() {
        return username;
    }

    public String password() {
        return password;
    }

    public static SshByPassword connect(String host, String username, String password) throws IOException {
        return new SshByPassword(host, username, password);
    }

    public static SshByPassword connect(InetAddress host, String username, String password) throws IOException {
        return new SshByPassword(host.getHostAddress(), username, password);
    }

    public static SshByPassword connect(InetAddress host, int port, String username, String password) throws IOException {
        return new SshByPassword(host.getHostAddress(), port, username, password);
    }

    public static SshByPassword connect(String host, int port, String username, String password) throws IOException {
        return new SshByPassword(host, port, username, password);
    }

    private SshByPassword(String host, int port, String username, String password) throws IOException {
        super(new SshConfig().setSession(new SshSession(host, port, username, password)));
        this.host = host;
        this.username = username;
        this.password = password;
    }

    public SshByPassword exec(String command) throws IOException {
        this.get().exec(command);
        return this;
    }

    public SshByPassword exec(String command, String... args) throws IOException {
        this.get().exec(command, args);
        return this;
    }

    public SshByPassword exec(String... command) throws IOException {
        this.get().exec(command);
        return this;
    }

    public SshByPassword put(String local, String remote) throws IOException {
        this.get().put(local, remote);
        return this;
    }

    public SshByPassword get(String remote, String local) throws IOException {
        this.get().get(remote, local);
        return this;
    }

    public SshByPassword close() throws IOException {
        this.get().close();
        return this;
    }

    private static class SshSession extends Session {

        private final String host;
        private final String username;
        private final String password;

        private SshSession(String host, String username, String password) throws UnknownHostException {
            super(InetAddress.getByName(host), 22, username, password);
            this.host = host;
            this.username = username;
            this.password = password;
        }

        private SshSession(String host, int port, String username, String password) throws UnknownHostException {
            super(InetAddress.getByName(host), port, username, password);
            this.host = host;
            this.username = username;
            this.password = password;
        }

        @Override
        public String toString() {
            return String.format("ssh://%s@%s:%d", username, host, port);
        }
    }
}
```