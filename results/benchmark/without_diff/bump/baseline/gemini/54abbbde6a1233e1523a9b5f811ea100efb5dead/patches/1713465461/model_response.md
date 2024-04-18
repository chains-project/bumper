```java
import com.jcabi.aspects.Tv;

public class SshByPassword {

    public SshByPassword(String host, String user, String password) {
        this(host, user, password, 22);
    }

    public SshByPassword(String host, String user, String password, int port) {
        this(host, port, () -> new Tv(user, password));
    }

    private SshByPassword(String host, int port, Tv tv) {
        // TODO Auto-generated constructor stub
    }
}
```