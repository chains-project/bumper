```java
    // @checkstyle ProtectedMethodInFinalClassCheck (10 lines)
    @Override
    @RetryOnFailure(
        attempts = Tv.SEVEN,
        delay = 1,
        unit = TimeUnit.MINUTES,
        verbose = false,
        types = IOException.class
    )
    protected Session session() throws IOException {
        Session session = null;
        try {
            final JSch jsch = new JSch();
            JSch.setLogger(new JschLogger());
            Logger.debug(
                this,
                "Opening SSH session to %s@%s:%s (auth with password)...",
                this.getLogin(), this.getAddr(), this.getPort()
            );
            session = jsch.getSession(
                this.getLogin(), this.getAddr(), this.getPort()
            );
            session.setConfig("StrictHostKeyChecking", "no");
            session.setPassword(this.password);
            session.setServerAliveInterval(
                (int) TimeUnit.SECONDS.toMillis(Tv.TEN)
            );
            session.setServerAliveCountMax(Tv.MILLION);
            session.connect((int) TimeUnit.SECONDS.toMillis(10L));
        } catch (final JSchException ex) {
            throw new IOException(ex);
        }
        return session;
    }
```