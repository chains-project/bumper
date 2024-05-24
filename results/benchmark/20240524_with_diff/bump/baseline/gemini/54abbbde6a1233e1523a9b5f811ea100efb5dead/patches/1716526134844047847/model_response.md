```java
import com.jcabi.aspects.Tv;
import org.apache.commons.lang3.StringUtils;

public class SshByPassword {

    private final String user;
    private final String host;
    private final int port;
    private final String password;
    private final Tv tv;

    public SshByPassword(String user, String host, int port, String password, Tv tv) {
        this.user = user;
        this.host = host;
        this.port = port;
        this.password = password;
        this.tv = tv;
    }

    public String user() {
        return user;
    }

    public String host() {
        return host;
    }

    public int port() {
        return port;
    }

    public String password() {
        return password;
    }

    public Tv tv() {
        return tv;
    }

    @Override
    public String toString() {
        return "SshByPassword{" +
            "user='" + user + '\'' +
            ", host='" + host + '\'' +
            ", port=" + port +
            ", password='" + StringUtils.repeat("*", password.length()) + '\'' +
            ", tv=" + tv +
            '}';
    }
}
```