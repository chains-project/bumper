```java
/**
 * Validate step's inputs.
 *
 * @param server - The server to check
 * @throws IOException if there is an illegal step configuration.
 */
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    if (server.getUrl().isBlank() && server.getArtifactory().getUrl().isBlank() && server.getDistribution().getUrl().isBlank() &&
        step.url.isBlank() && step.artifactoryUrl.isBlank() && step.distributionUrl.isBlank()) {
        throw new IOException("Server URL is missing");
    }
    if (!step.credentialsId.isBlank()) {
        if (!step.username.isBlank()) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (!step.password.isBlank()) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```