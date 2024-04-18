```java
import com.jcabi.aspects.Tv;

import java.io.IOException;

public class SshByPassword {

    private final String host;
    private final int port;
    private final String user;
    private final String password;

    public SshByPassword(String host, int port, String user, String password) {
        this.host = host;
        this.port = port;
        this.user = user;
        this.password = password;
    }

    public Tv tv() throws IOException {
        return new Tv(host, port, user, password);
    }
}
```