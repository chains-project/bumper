```java
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    if (server.getUrl().isEmpty() && server.getArtifactory().getUrl().isEmpty() && server.getDistribution().getUrl().isEmpty() &&
            step.url.isEmpty() && step.artifactoryUrl.isEmpty() && step.distributionUrl.isEmpty()) {
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