```java
    // @checkstyle ProtectedMethodInFinalClassCheck (10 lines)
    @RetryOnFailure(
        attempts = Tv.SEVEN,
        delay = 1,
        unit = TimeUnit.MINUTES,
        verbose = false,
        types = IOException.class
    )
    protected Session session() throws IOException {
        try {
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