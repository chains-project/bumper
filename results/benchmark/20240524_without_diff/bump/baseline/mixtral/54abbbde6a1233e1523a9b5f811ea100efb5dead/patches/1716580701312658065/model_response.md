Here's the proposed patch for the failing client code:

```java
import com.jcabi.ssh.Ssh;

@Tv({"0.15.2"})
public class SshByPassword {
    // existing code...

    @Override
    public Ssh connect(String host, int port, String username, String password) throws IOException, URISyntaxException {
        // use Ssh.create(host, port, username, password) instead of deprecated Ssh.via(host, port, username, password)
        return Ssh.create(host, port, username, password);
    }

    // existing code...
}
```

The patch replaces the deprecated `Ssh.via()` method with the recommended `Ssh.create()` method. This should resolve the "cannot find symbol" error caused by the dependency update.