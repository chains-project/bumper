```java
/**
 * Validate step's inputs.
 *
 * @param server - The server to check
 * @throws IOException if there is an illegal step configuration.
 */
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    if (server == null || step == null) {
        throw new IOException("Server or Step is null");
    }

    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(),
            step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IOException("Server URL is missing");
    }

    if (isNotBlank(step.credentialsId)) {
        if (isNotBlank(step.getUsername())) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }

        if (isNotBlank(step.getPassword())) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```