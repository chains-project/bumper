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
        com.jcraft.jsch.Logger.setLogger(new JschLogger());
        final com.jcraft.jsch.JSch jsch = new com.jcraft.jsch.JSch();
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
        jsch.setHostKeyRepository(new com.jcraft.jsch.HostKeyRepository() {
            @Override
            public int check(String host, byte[] key) {
                return com.jcraft.jsch.HostKeyRepository.OK;
            }
            @Override
            public void add(com.jcraft.jsch.HostKey hostkey, com.jcraft.jsch.UIKeyboardInteractive ui) throws Exception {
            }
            @Override
            public void remove(String host, com.jcraft.jsch.HostKey hk) {
            }
            @Override
            public void remove(String host) {
            }
            @Override
            public String getKnownHostsRepositoryID() {
                return "";
            }
        });
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