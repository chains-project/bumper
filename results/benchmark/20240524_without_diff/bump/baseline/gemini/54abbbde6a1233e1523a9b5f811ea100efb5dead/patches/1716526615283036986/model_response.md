```java
import com.jcabi.aspects.Tv;
import com.jcabi.ssh.Ssh;

public class Ssh {

    public Ssh(Tv tv) {
        this.tv = tv;
    }

    private final Tv tv;

    public void exec(String command) {
        tv.watch(command);
    }
}
```