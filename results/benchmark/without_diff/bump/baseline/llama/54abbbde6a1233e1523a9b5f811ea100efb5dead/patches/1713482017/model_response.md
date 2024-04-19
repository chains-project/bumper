```
    @Override
    @RetryOnFailure(
        attempts = Tv.SEVEN,
        delay = 1,
        unit = TimeUnit.MINUTES,
        verbose = false,
        types = IOException.class
    )
    protected Session session() throws IOException {
        try {
            JSch.setLogger(new JschLogger());
            final JSch jsch = new JSch();
            Logger.debug(
                this,
                "Opening SSH session to %s@%s:%s (auth with password)...",
                this.getLogin(), this.getAddr(), this.getPort()
            );
            final Session session = jsch.getSession(
                this.getLogin(), this.getAddr(), this.getPort()
            );
            session.setConfig("StrictHostKeyChecking", "no");
            session.setPassword(this.password);
            session.setServerAliveInterval(
                (int) TimeUnit.SECONDS.toMillis(Tv.TEN)
            );
            session.setServerAliveCountMax(Tv.MILLION);
            session.connect((int) TimeUnit.SECONDS.toMillis(10L));
            return session;
        } catch (final JSchException ex) {
            throw new IOException(ex);
        }
    }
```

The error message you provided indicates that the symbol `Tv` cannot be found. This suggests that the `Tv` class is not available in the project's classpath.


To fix this issue, you can replace all occurrences of `Tv` with `TimeUnit` since the values you are using are from the `TimeUnit` class. Here's the modified code:
```
    @Override
    @RetryOnFailure(
        attempts = 7,
        delay = 1,
        unit = TimeUnit.MINUTES,
        verbose = false,
        types = IOException.class
    )
    protected Session session() throws IOException {
        try {
            JSch.setLogger(new JschLogger());
            final JSch jsch = new JSch();
            Logger.debug(
                this,
                "Opening SSH session to %s@%s:%s (auth with password)...",
                this.getLogin(), this.getAddr(), this.getPort()
            );
            final Session session = jsch.getSession(
                this.getLogin(), this.getAddr(), this.getPort()
            );
            session.setConfig("StrictHostKeyChecking", "no");
            session.setPassword(this.password);
            session.setServerAliveInterval(
                (int) TimeUnit.SECONDS.toMillis(10)
            );
            session.setServerAliveCountMax(1000000);
            session.connect((int) TimeUnit.SECONDS.toMillis(10L));
            return session;
        } catch (final JSchException ex) {
            throw new IOException(ex);
        }
    }
```

I replaced `Tv.SEVEN` with `7`, `Tv.TEN` with `10`, and `Tv.MILLION` with `1000000`.

This should fix the error and allow the code to compile.