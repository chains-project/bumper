```java
/**
 * Validate step's inputs.
 *
 * @param server - The server to check
 * @throws IOException if there is an illegal step configuration.
 */
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    boolean isAllBlank = server.getUrl().isEmpty() && server.getArtifactory().getUrl().isEmpty() &&
            server.getDistribution().getUrl().isEmpty() && step.url.isEmpty() && step.artifactoryUrl.isEmpty() &&
            step.distributionUrl.isEmpty();

    if (isAllBlank) {
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