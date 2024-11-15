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
        com.jcraft.jsch.Logger logger = new com.jcraft.jsch.Logger() {
            public boolean isEnabled(int level) {
                return true;
            }
            public void log(int level, String message) {
                Logger.debug(this, message);
            }
        };
        com.jcraft.jsch JSch = new com.jcraft.jsch();
        JSch.setLogger(logger);
        final String key = this.key.replaceAll("\r", "")
                .replaceAll("\n\\s+|\n{2,}", "\n")
                .trim();
        new Unchecked<>(
            new LengthOf(
                new TeeInput(
                    key,
                    file
                )
            )
        ).value();
        JSch.setHostKeyRepository(new com.jcraft.jsch.UserInfo() {
            public String getPassword() {
                return null;
            }
            public String getPassphrase() {
                return this.passphrase;
            }
        });
        if (this.passphrase == null) {
            JSch.addIdentity(file.getAbsolutePath());
        } else {
            JSch.addIdentity(
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
        return this.session(JSch);
    } catch (final JSchException ex) {
        throw new IOException(ex);
    } finally {
        Files.deleteIfExists(file.toPath());
    }
}
```