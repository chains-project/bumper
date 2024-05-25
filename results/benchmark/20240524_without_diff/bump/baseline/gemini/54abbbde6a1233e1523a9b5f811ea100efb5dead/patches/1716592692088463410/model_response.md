```java
import com.jcabi.aspects.Tv;

public class SshByPassword {

    public SshByPassword(String host, String user, String password) {
        // Use the Tv class to create a new SSH connection
        Tv tv = new Tv(host, user, password);
        // Set the timeout for the connection
        tv.setTimeout(30000);
        // Set the port for the connection
        tv.setPort(22);
        // Connect to the SSH server
        tv.connect();
    }

    // ... other methods
}
```