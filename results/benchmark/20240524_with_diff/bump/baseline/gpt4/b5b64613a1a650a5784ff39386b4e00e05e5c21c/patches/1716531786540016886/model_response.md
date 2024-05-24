```java
private void checkInputs(ArtifactoryServer server) throws IOException {
    if (server.getUrl() == null || server.getUrl().isEmpty() || step.url == null || step.url.isEmpty()) {
        throw new IOException("Server URL is missing");
    }
    if (step.credentialsId != null && !step.credentialsId.isEmpty()) {
        if (step.username != null && !step.username.isEmpty()) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (step.password != null && !step.password.isEmpty()) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```