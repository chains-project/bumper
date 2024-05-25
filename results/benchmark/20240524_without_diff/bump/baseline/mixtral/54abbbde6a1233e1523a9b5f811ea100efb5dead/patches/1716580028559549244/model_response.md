Here's the proposed patch for the failing client code:

```java
import com.jcabi.ssh.Ssh;

@Tv({"0.15.2"})
public class SshByPassword {
    // existing code...

    @Override
    public Ssh ssh(String host, int port, String username, String password) {
        return Ssh.create(host, port, username, password);
    }

    // existing code...
}
```

In this patch, I've replaced the import statement with the correct one for the `Ssh` class. I've also replaced the usage of the removed `SshByPassword` constructor with the new `Ssh.create` method, which is an added method in the external dependency.