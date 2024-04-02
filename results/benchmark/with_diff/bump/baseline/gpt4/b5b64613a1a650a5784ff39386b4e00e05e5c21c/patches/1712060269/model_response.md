```java
/**
 * Validate step's inputs.
 *
 * @param server - The server to check
 * @throws IOException if there is an illegal step configuration.
 */
private void checkInputs(ArtifactoryServer server) throws IOException {
    if (server.getUrl().isEmpty() || step.url.isEmpty()) {
        throw new IOException("Server URL is missing");
    }
    if (!step.credentialsId.isEmpty()) {
        if (!step.username.isEmpty()) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (!step.password.isEmpty()) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```