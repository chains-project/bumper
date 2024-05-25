```java
@RetryOnFailure(
    attempts = 7,
    delay = 1,
    unit = TimeUnit.MINUTES,
    verbose = false,
    types = IOException.class
)
protected Session session() throws IOException {
    final File file = File.createTempFile("jcabi-ssh", ".key");
    try {
        com.jcraft.jsch.Logger jschLogger = new com.jcraft.jsch.Logger() {
            @Override
            public void log(String message) {
                Logger.debug(this, message);
            }
        };
        JSch.setLogger(jschLogger);
        final JSch jsch = new JSch();
        new Unchecked<>(
            new LengthOf(
                new TeeInput(
                    this.key.replaceAll("\r", "")
                        .replaceAll("\n\\s+|\n{2,}", "\n")
                        .trim(),
                    file
                )
            )
        ).value();
        jsch.setHostKeyRepository(new EasyRepo());
        if (this.passphrase == null) {
            jsch.addIdentity(file.getAbsolutePath());
        } else {
            jsch.addIdentity(
                this.getLogin(),
                this.key.getBytes(StandardCharsets.UTF_8),
                null,
                this.passphrase.getBytes(StandardCharsets.UTF_8)
            );
        }
        Logger.debug(
            this,
            "Opening SSH session to %s@%s:%s (%d bytes in RSA key)...",
            this.getLogin(), this.getAddr(), this.getPort(),
            file.length()
        );
        return this.session(jsch);
    } catch (final JSchException ex) {
        throw new IOException(ex);
    } finally {
        Files.deleteIfExists(file.toPath());
    }
}
```