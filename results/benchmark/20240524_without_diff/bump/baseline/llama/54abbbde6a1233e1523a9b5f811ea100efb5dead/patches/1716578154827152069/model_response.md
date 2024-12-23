```java
@RetryOnFailure(
    attempts = 7,
    delay = 1,
    unit = TimeUnit.MINUTES,
    verbose = false,
    types = IOException.class
)
protected Session session() throws IOException {
    try {
        com.jcraft.jsch.Logger.setDefaultLogger(new JschLogger());
        final com.jcraft.jsch.JSch jsch = new com.jcraft.jsch.JSch();
        Logger.debug(
            this,
            "Opening SSH session to %s@%s:%s (auth with password)...",
            this.getLogin(), this.getAddr(), this.getPort()
        );
        final com.jcraft.jsch.Session session = jsch.getSession(
            this.getLogin(), this.getAddr(), this.getPort()
        );
        java.util.Properties config = new java.util.Properties();
        config.put("StrictHostKeyChecking", "no");
        session.setConfig(config);
        session.setPassword(this.password);
        session.setServerAliveInterval(
            (int) TimeUnit.SECONDS.toMillis(10L)
        );
        session.setServerAliveCountMax(1000000);
        session.connect((int) TimeUnit.SECONDS.toMillis(10L));
        return session;
    } catch (final com.jcraft.jsch.JSchException ex) {
        throw new IOException(ex);
    }
}
```