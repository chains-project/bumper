```java
import com.jcabi.aspects.Tv;

public class SshByPassword {

    private final String host;
    private final String user;
    private final String password;

    public SshByPassword(String host, String user, String password) {
        this.host = host;
        this.user = user;
        this.password = password;
    }

    public Tv tv() {
        return new Tv();
    }

}
```