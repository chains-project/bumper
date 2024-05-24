```java
import com.jcabi.aspects.Tv;

public class Ssh {

    private final Tv tv;

    public Ssh(Tv tv) {
        this.tv = tv;
    }

    public void execute(String command) {
        // Execute the command on the remote server.
        tv.execute(command);
    }
}
```