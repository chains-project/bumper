```java
import com.jcabi.aspects.Tv;
import com.jcabi.aspects.Tv.Channel;

public class SshByPassword {

    public SshByPassword(String host, String user, String password) {
        this(host, user, password, 22);
    }

    public SshByPassword(String host, String user, String password, int port) {
        this(host, port, user, password);
    }

    public SshByPassword(String host, int port, String user, String password) {
        this(new Tv(host, port, user, password));
    }

    public SshByPassword(Tv tv) {
        this.tv = tv;
    }

    private final Tv tv;

    public void exec(String command) {
        tv.exec(command);
    }

    public void exec(String command, Channel channel) {
        tv.exec(command, channel);
    }

    public void exec(String command, String[] args) {
        tv.exec(command, args);
    }

    public void exec(String command, String[] args, Channel channel) {
        tv.exec(command, args, channel);
    }

    public void exec(String command, String[] args, String[] env) {
        tv.exec(command, args, env);
    }

    public void exec(String command, String[] args, String[] env, Channel channel) {
        tv.exec(command, args, env, channel);
    }

    public void close() {
        tv.close();
    }

}
```