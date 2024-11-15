```java
  import org.jetbrains.annotations.NotNull;

  import java.io.IOException;
  import java.net.InetAddress;
  import java.net.InetSocketAddress;
  import java.net.Socket;
  import java.net.SocketAddress;
  import java.util.concurrent.TimeUnit;

  import com.jcabi.aspects.Tv;

  public class SshByPassword extends AbstractSsh {

      private final String password;

      public SshByPassword(@NotNull final InetAddress host, final int port, @NotNull final String user, @NotNull final String password) {
          super(host, port, user);
          this.password = password;
      }

      public SshByPassword(@NotNull final InetAddress host, @NotNull final String user, @NotNull final String password) {
          super(host, user);
          this.password = password;
      }

      public SshByPassword(@NotNull final String host, final int port, @NotNull final String user, @NotNull final String password) {
          super(host, port, user);
          this.password = password;
      }

      public SshByPassword(@NotNull final String host, @NotNull final String user, @NotNull final String password) {
          super(host, user);
          this.password = password;
      }

      public SshByPassword(@NotNull final SocketAddress address, @NotNull final String user, @NotNull final String password) {
          super(address, user);
          this.password = password;
      }

      public SshByPassword(@NotNull final InetSocketAddress address, @NotNull final String user, @NotNull final String password) {
          super(address, user);
          this.password = password;
      }

      @Override
      protected void connect() throws IOException {
          final Socket socket = new Socket();
          final SocketAddress address = this.address();
          socket.connect(address, this.connectTimeout());
          socket.setSoTimeout(this.readTimeout());
          this.session(new Session(socket, this.in(), this.out(), this.err()));
          this.auth(new PasswordAuth(this.user(), this.password));
          if (!this.isShellOpen()) {
              this.openShell();
          }
      }

      public static void main(final String... args) throws IOException {
          final SshByPassword ssh = new SshByPassword("localhost", 2222, "user", "password");
          final Tv tv = ssh.tv();
          tv.send("pwd");
          final String current = tv.receive();
          System.out.println("Current directory: " + current);
          tv.send("exit");
          ssh.close();
      }

      @Override
      public void close() throws IOException {
          this.session().close();
          this.session().socket().close();
          super.close();
      }

      @Override
      public void close(final long timeout, final TimeUnit unit) throws IOException {
          this.session().close(timeout, unit);
          this.session().socket().close();
          super.close(timeout, unit);
      }

  }
```