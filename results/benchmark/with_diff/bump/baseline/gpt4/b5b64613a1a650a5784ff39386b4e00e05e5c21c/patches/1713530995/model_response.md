```java
/**
 * Validate step's inputs.
 *
 * @param server - The server to check
 * @throws IOException if there is an illegal step configuration.
 */
private void checkInputs(ArtifactoryServer server) throws IOException {
    if (server.getUrl() == null || server.getUrl().isBlank() || step.url == null || step.url.isBlank()) {
        throw new IOException("Server URL is missing");
    }
    if (step.credentialsId != null && !step.credentialsId.isBlank()) {
        if (step.username != null && !step.username.isBlank()) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (step.password != null && !step.password.isBlank()) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```