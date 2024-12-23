```java
import com.jcabi.aspects.Tv;
import com.jcabi.ssh.Shell;
import com.jcabi.ssh.SshByPassword;
import org.apache.sshd.client.SshClient;
import org.apache.sshd.client.channel.ClientChannel;
import org.apache.sshd.client.channel.ClientChannelEvent;
import org.apache.sshd.client.future.ConnectFuture;
import org.apache.sshd.client.session.ClientSession;
import org.apache.sshd.common.io.IoSession;
import org.apache.sshd.common.io.IoWriteFuture;
import org.apache.sshd.common.session.Session;
import org.apache.sshd.common.util.buffer.Buffer;
import org.apache.sshd.common.util.buffer.ByteArrayBuffer;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;

public class SshByPassword implements Ssh {

    private final String host;
    private final int port;
    private final String user;
    private final char[] password;
    private final int timeout;
    private final AtomicReference<ConnectFuture> connectFuture = new AtomicReference<>();
    private final AtomicReference<ClientChannel> channel = new AtomicReference<>();
    private final AtomicReference<ClientSession> session = new AtomicReference<>();
    private final CountDownLatch latch = new CountDownLatch(1);
    private final AtomicBoolean isClosed = new AtomicBoolean();
    private final AtomicInteger exitStatus = new AtomicInteger(-1);

    public SshByPassword(String host, int port, String user, char[] password, int timeout) {
        this.host = host;
        this.port = port;
        this.user = user;
        this.password = password;
        this.timeout = timeout;
    }

    @Override
    public void exec(String... command) throws IOException {
        if (isClosed.get()) {
            throw new IOException("SSH connection is closed");
        }
        ClientChannel ch = channel.get();
        if (ch == null) {
            throw new IOException("SSH connection is not established");
        }
        ch.write(String.join(" ", command) + "\n").addListener(future -> {
            if (future.isFailure()) {
                latch.countDown();
            }
        });
    }

    @Override
    public Shell shell() throws IOException {
        if (isClosed.get()) {
            throw new IOException("SSH connection is closed");
        }
        ClientChannel ch = channel.get();
        if (ch == null) {
            throw new IOException("SSH connection is not established");
        }
        return new Shell(ch.getInvertedIn(), ch.getInvertedOut(), ch.getInvertedErr());
    }

    @Override
    public int exitValue() throws IOException {
        if (isClosed.get()) {
            throw new IOException("SSH connection is closed");
        }
        ClientChannel ch = channel.get();
        if (ch == null) {
            throw new IOException("SSH connection is not established");
        }
        if (exitStatus.get() == -1) {
            ch.waitFor(ClientChannelEvent.CLOSED, timeout, TimeUnit.SECONDS);
            exitStatus.set(ch.getExitStatus());
        }
        return exitStatus.get();
    }

    @Override
    public void close() throws IOException {
        if (isClosed.compareAndSet(false, true)) {
            ClientChannel ch = channel.getAndSet(null);
            if (ch != null) {
                ch.close(false);
            }
            ClientSession ses = session.getAndSet(null);
            if (ses != null) {
                ses.close(false);
            }
            ConnectFuture fut = connectFuture.getAndSet(null);
            if (fut != null) {
                fut.cancel();
            }
        }
    }

    private void connect() throws IOException {
        SshClient client = SshClient.setUpDefaultClient();
        client.start();
        ConnectFuture future = client.connect(user, host, port);
        future.await(timeout, TimeUnit.SECONDS);
        if (!future.isConnected()) {
            throw new IOException("Failed to connect to SSH server");
        }
        ClientSession ses = future.getSession();
        ses.addPasswordIdentity(password);
        ses.auth().verify(timeout, TimeUnit.SECONDS);
        ClientChannel ch = ses.createShellChannel();
        ch.open().verify(timeout, TimeUnit.SECONDS);
        connectFuture.set(future);
        session.set(ses);
        channel.set(ch);
        latch.countDown();
    }

    public static class Shell implements com.jcabi.aspects.Shell {
        private final InputStream in;
        private final OutputStream out;
        private final OutputStream err;
        private final AtomicBoolean isClosed = new AtomicBoolean();
        private final CountDownLatch latch = new CountDownLatch(1);
        private final AtomicReference<ClientChannel> channel = new AtomicReference<>();
        private final AtomicReference<ConnectFuture> connectFuture = new AtomicReference<>();
        private final AtomicReference<ClientSession> session = new AtomicReference<>();
        private final AtomicBoolean isConnected = new AtomicBoolean();
        private final AtomicInteger exitStatus = new AtomicInteger(-1);
        private final List<String> history = new ArrayList<>();
        private final int timeout;

        public Shell(InputStream in, OutputStream out, OutputStream err) {
            this.in = in;
            this.out = out;
            this.err = err;
            this.timeout = 10;
        }

        @Override
        public void exec(String... command) throws IOException {
            if (isClosed.get()) {
                throw new IOException("SSH connection is closed");
            }
            ClientChannel ch = channel.get();
            if (ch == null) {
                throw new IOException("SSH connection is not established");
            }
            ch.write(String.join(" ", command) + "\n").addListener(future -> {
                if (future.isFailure()) {
                    latch.countDown();
                }
            });
            history.addAll(Arrays.asList(command));
        }

        @Override
        public int exitValue() throws IOException {
            if (isClosed.get()) {
                throw new IOException("SSH connection is closed");
            }
            ClientChannel ch = channel.get();
            if (ch == null) {
                throw new IOException("SSH connection is not established");
            }
            if (exitStatus.get() == -1) {
                ch.waitFor(ClientChannelEvent.CLOSED, timeout, TimeUnit.SECONDS);
                exitStatus.set(ch.getExitStatus());
            }
            return exitStatus.get();
        }

        @Override
        public void close() throws IOException {
            if (isClosed.compareAndSet(false, true)) {
                ClientChannel ch = channel.getAndSet(null);
                if (ch != null) {
                    ch.close(false);
                }
                ClientSession ses = session.getAndSet(null);
                if (ses != null) {
                    ses.close(false);
                }
                ConnectFuture fut = connectFuture.getAndSet(null);
                if (fut != null) {
                    fut.cancel();
                }
            }
        }

        @Override
        public InputStream in() {
            return in;
        }

        @Override
        public OutputStream out() {
            return out;
        }

        @Override
        public OutputStream err() {
            return err;
        }

        @Override
        public List<String> history() {
            return Collections.unmodifiableList(history);
        }

        @Override
        public void connect(String host, int port, String user, char[] password) throws IOException {
            if (isConnected.compareAndSet(false, true)) {
                SshClient client = SshClient.setUpDefaultClient();
                client.start();
                ConnectFuture future = client.connect(user, host, port);
                future.await(timeout, TimeUnit.SECONDS);
                if (!future.isConnected()) {
                    throw new IOException("Failed to connect to SSH server");
                }
                ClientSession ses = future.getSession();
                ses.addPasswordIdentity(password);
                ses.auth().verify(timeout, TimeUnit.SECONDS);
                ClientChannel ch = ses.createShellChannel();
                ch.open().verify(timeout, TimeUnit.SECONDS);
                connectFuture.set(future);
                session.set(ses);
                channel.set(ch);
                latch.countDown();
            }
        }

        @Override
        public boolean isConnected() {
            return isConnected.get();
        }
    }
}
```