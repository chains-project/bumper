```
private void checkInputs(ArtifactoryServer server) throws IOException {
    if (isAllBlank(server.getUrl(), step.getUrl())) {
        throw new IOException("Server URL is missing");
    }
    if (isNotBlank(step.getCredentialsId())) {
        if (isNotBlank(step.getUsername())) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (isNotBlank(step.getPassword())) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```