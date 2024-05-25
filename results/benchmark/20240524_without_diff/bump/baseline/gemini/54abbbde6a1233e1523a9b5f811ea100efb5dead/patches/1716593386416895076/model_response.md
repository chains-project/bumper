```java
  import org.apache.sshd.client.SshClient;
  import org.apache.sshd.client.session.ClientSession;
  import org.apache.sshd.client.session.ClientSessionHolder;
  import org.apache.sshd.common.channel.Channel;
  import org.apache.sshd.common.channel.ChannelListener;
  import org.apache.sshd.common.io.IoSession;
  import org.apache.sshd.common.session.Session;
  import org.apache.sshd.common.session.SessionListener;
  import org.apache.sshd.common.util.io.IoUtils;
  import org.apache.sshd.common.util.threads.CloseableExecutorService;
  import org.apache.sshd.common.util.threads.ExecutorService;
  import org.apache.sshd.common.util.threads.ThreadUtils;
  import org.apache.sshd.common.util.threads.ThreadUtils.ShutdownPolicy;
  import org.apache.sshd.server.Command;
  import org.apache.sshd.server.Environment;
  import org.apache.sshd.server.ExitCallback;
  import org.apache.sshd.server.SessionAware;
  import org.apache.sshd.server.command.CommandFactory;
  import org.apache.sshd.server.session.ServerSession;

  import java.io.IOException;
  import java.io.InputStream;
  import java.io.OutputStream;
  import java.util.Collection;
  import java.util.Collections;
  import java.util.EnumSet;
  import java.util.List;
  import java.util.concurrent.TimeUnit;

  /**
   * A {@link SessionAware} {@link Command} that can be used to execute commands on a remote server.
   *
   * @author <a href="mailto:dev@mina.apache.org">Apache MINA SSHD Project</a>
   */
  public class ExecCommand implements Command, SessionAware {

    /**
     * The default size of the buffer used to read the command's output stream.
     */
    public static final int DEFAULT_BUFFER_SIZE = 1024;

    private final String command;
    private final OutputStream stderr;
    private final OutputStream stdout;
    private final InputStream stdin;
    private final CloseableExecutorService executor;
    private ClientSession session;
    private volatile boolean closed;
    private volatile boolean started;
    private volatile boolean exitSent;
    private final ExitCallback callback;
    private final List<ChannelListener> channelListeners;
    private final List<SessionListener> sessionListeners;
    private final Environment env;
    private final CommandFactory commandFactory;

    /**
     * Create a new command.
     *
     * @param command The command to execute.
     * @param in      The input stream for the command.
     * @param out     The output stream for the command.
     * @param err     The error stream for the command.
     * @throws IOException If failed to create the command.
     */
    public ExecCommand(String command, InputStream in, OutputStream out, OutputStream err) throws IOException {
      this(command, in, out, err, ThreadUtils.newSingleThreadExecutor("ExecCommand"));
    }

    /**
     * Create a new command.
     *
     * @param command The command to execute.
     * @param in      The input stream for the command.
     * @param out     The output stream for the command.
     * @param err     The error stream for the command.
     * @param executor The executor to use for running the command.
     * @throws IOException If failed to create the command.
     */
    public ExecCommand(String command, InputStream in, OutputStream out, OutputStream err, CloseableExecutorService executor)
        throws IOException {
      this(command, in, out, err, executor, null, Collections.<ChannelListener>emptyList(),
          Collections.<SessionListener>emptyList(), null, null);
    }

    /**
     * Create a new command.
     *
     * @param command The command to execute.
     * @param in      The input stream for the command.
     * @param out     The output stream for the command.
     * @param err     The error stream for the command.
     * @param executor The executor to use for running the command.
     * @param callback The callback to invoke when the command exits.
     * @param channelListeners The channel listeners to register.
     * @param sessionListeners The session listeners to register.
     * @param env The environment variables to set for the command.
     * @param commandFactory The command factory to use for creating sub-commands.
     * @throws IOException If failed to create the command.
     */
    public ExecCommand(String command, InputStream in, OutputStream out, OutputStream err, CloseableExecutorService executor,
        ExitCallback callback, List<ChannelListener> channelListeners, List<SessionListener> sessionListeners, Environment env,
        CommandFactory commandFactory) throws IOException {
      this.command = command;
      this.stdin = in;
      this.stdout = out;
      this.stderr = err;
      this.executor = executor;
      this.callback = callback;
      this.channelListeners = channelListeners;
      this.sessionListeners = sessionListeners;
      this.env = env;
      this.commandFactory = commandFactory;
    }

    @Override
    public void setSession(ClientSession session) {
      this.session = session;
    }

    @Override
    public void start(Channel channel, Environment env) throws IOException {
      if (closed) {
        throw new IllegalStateException("Command is already closed");
      }

      if (started) {
        throw new IllegalStateException("Command is already started");
      }

      started = true;

      // Register channel listeners
      if (channelListeners != null) {
        for (ChannelListener listener : channelListeners) {
          channel.addChannelListener(listener);
        }
      }

      // Register session listeners
      if (sessionListeners != null) {
        for (SessionListener listener : sessionListeners) {
          session.addSessionListener(listener);
        }
      }

      // Set environment variables
      if (env != null) {
        for (String name : env.keySet()) {
          session.setAttribute(name, env.get(name));
        }
      }

      if (commandFactory != null) {
        channel.setProperty(CommandFactory.class, commandFactory);
      }

      // Execute the command
      executor.execute(new CommandRunnable(channel));
    }

    @Override
    public void destroy() {
      if (closed) {
        return;
      }

      closed = true;

      // Close the streams
      IoUtils.closeQuietly(stdin, stdout, stderr);

      // Shutdown the executor
      executor.shutdownNow();
      try {
        executor.awaitTermination(1L, TimeUnit.SECONDS);
      } catch (InterruptedException e) {
        Thread.interrupted();
      }
    }

    /**
     * @return the command
     */
    public String getCommand() {
      return command;
    }

    /**
     * @return the stderr
     */
    public OutputStream getStderr() {
      return stderr;
    }

    /**
     * @return the stdin
     */
    public InputStream getStdin() {
      return stdin;
    }

    /**
     * @return the stdout
     */
    public OutputStream getStdout() {
      return stdout;
    }

    /**
     * @return the executor
     */
    public ExecutorService getExecutorService() {
      return executor;
    }

    /**
     * @return the session
     */
    public ClientSession getSession() {
      return session;
    }

    /**
     * @return the closed
     */
    public boolean isClosed() {
      return closed;
    }

    /**
     * @return the started
     */
    public boolean isStarted() {
      return started;
    }

    /**
     * @return the exitSent
     */
    public boolean isExitSent() {
      return exitSent;
    }

    /**
     * @return the callback
     */
    public ExitCallback getCallback() {
      return callback;
    }

    /**
     * @return the channelListeners
     */
    public List<ChannelListener> getChannelListeners() {
      return channelListeners;
    }

    /**
     * @return the sessionListeners
     */
    public List<SessionListener> getSessionListeners() {
      return sessionListeners;
    }

    /**
     * @return the env
     */
    public Environment getEnv() {
      return env;
    }

    /**
     * @return the commandFactory
     */
    public CommandFactory getCommandFactory() {
      return commandFactory;
    }

    /**
     * A {@link Runnable} that executes the command.
     */
    private class CommandRunnable implements Runnable {

      private final Channel channel;

      public CommandRunnable(Channel channel) {
        this.channel = channel;
      }

      @Override
      public void run() {
        try {
          // Create a pseudo shell session
          ClientSessionHolder holder = session.createClientSessionHolder(EnumSet.of(ClientSession.ClientSessionEvent.CLOSED));
          ClientSession shell = holder.getSession();
          shell.startShell();

          // Execute the command
          shell.executeCommand(command);

          // Wait for the command to exit
          int exitValue = shell.waitFor(ClientSession.ClientSessionEvent.CLOSED, TimeUnit.SECONDS.toMillis(10));

          // Send the exit status to the callback
          if (callback != null) {
            callback.onExit(exitValue);
          }

          // Close the channel
          channel.close(false);
        } catch (IOException e) {
          // Log the error
          session.getLogger().error("Failed to execute command: " + e.getMessage());

          // Close the channel
          channel.close(false);
        } finally {
          // Mark the command as exited
          exitSent = true;

          // Close the holder
          holder.close();
        }
      }
    }
  }
```