```java
import com.jcabi.aspects.Tv;
import com.jcabi.ssh.SshByPassword;

import java.io.IOException;

public class SshByPasswordFixed extends SshByPassword {

    public SshByPasswordFixed(String host, String user, String pass) throws IOException {
        super(host, user, pass);
    }

    @Override
    public Tv tv() {
        return new Tv() {
            @Override
            public void play(String show) throws IOException {
                exec().sh("echo 'Playing " + show + "'").await();
            }
        };
    }
}
```