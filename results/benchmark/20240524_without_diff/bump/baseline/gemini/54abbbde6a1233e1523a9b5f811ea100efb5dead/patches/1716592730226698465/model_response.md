```java
import com.jcabi.aspects.Tv;
import com.jcabi.ssh.Shell;
import com.jcabi.ssh.Ssh;
import com.jcabi.ssh.SshByPassword;

import java.io.IOException;

public class SshByPassword {

    private final Shell shell;

    public SshByPassword(final String host, final int port, final String user, final String pass) throws IOException {
        this.shell = new SshByPassword(host, port, user, pass).shell();
    }

    public String exec(final String cmd) throws IOException {
        return this.shell.exec(cmd);
    }

    public String exec(final String cmd, final Tv.Output out) throws IOException {
        return this.shell.exec(cmd, out);
    }

    public void close() throws IOException {
        this.shell.close();
    }

    public static void main(final String[] args) throws IOException {
        final Ssh ssh = new SshByPassword("localhost", 22, "user", "pass");
        final String out = ssh.exec("ls -l");
        System.out.println(out);
        ssh.close();
    }
}
```