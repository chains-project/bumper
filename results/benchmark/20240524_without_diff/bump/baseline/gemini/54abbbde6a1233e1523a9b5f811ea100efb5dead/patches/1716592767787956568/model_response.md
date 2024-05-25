```java
import com.jcabi.aspects.Tv;

public class SshByPassword extends SshByCredentials {

    public SshByPassword(final String host, final int port, final String user, final String pass) {
        super(host, port, user, pass);
    }

    @Override
    public Tv root() {
        return new Tv(this, "root", this.password());
    }

    @Override
    public Tv user(final String user) {
        return new Tv(this, user, this.password());
    }

    @Override
    public Tv user(final String user, final String pass) {
        return new Tv(this, user, pass);
    }

    private String password() {
        return this.credentials().get(1);
    }
}
```