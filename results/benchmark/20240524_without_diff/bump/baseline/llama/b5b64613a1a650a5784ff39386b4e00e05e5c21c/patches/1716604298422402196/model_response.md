```java
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    String url = server.getUrl();
    String artifactoryUrl = server.getArtifactory() != null ? server.getArtifactory().getUrl() : null;
    String distributionUrl = server.getDistribution() != null ? server.getDistribution().getUrl() : null;
    if (isAllBlank(url, artifactoryUrl, distributionUrl, step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IOException("Server URL is missing");
    }
    if (isNotBlank(step.credentialsId)) {
        if (isNotBlank(step.username)) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (isNotBlank(step.password)) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```