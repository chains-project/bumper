```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.ssh.Ssh;

  public class Ssh {

    public Ssh(String host, String user, String pass) {
      this(new Tv(host, user, pass));
    }

    public Ssh(Tv tv) {
      this.tv = tv;
    }

    private final Tv tv;

    public Ssh exec(String command) {
      tv.exec(command);
      return this;
    }

    public String exec(String command, String[] args) {
      return tv.exec(command, args);
    }

    public int exec(String command, String[] args, String[] env) {
      return tv.exec(command, args, env);
    }

    public Ssh sudo(String command) {
      return exec("sudo", command);
    }

    public String sudo(String command, String[] args) {
      return exec("sudo", command, args);
    }

    public int sudo(String command, String[] args, String[] env) {
      return exec("sudo", command, args, env);
    }

    public Ssh put(String path, String content) {
      tv.put(path, content);
      return this;
    }

    public Ssh get(String path, String destination) {
      tv.get(path, destination);
      return this;
    }

    public Ssh get(String path, String destination, long offset) {
      tv.get(path, destination, offset);
      return this;
    }

    public Ssh get(String path, String destination, long offset, long length) {
      tv.get(path, destination, offset, length);
      return this;
    }

    public Ssh close() {
      tv.close();
      return this;
    }

  }
```