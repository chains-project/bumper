```java
protected JFrogPlatformInstance run() throws Exception {
    if (isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = removeEnd(step.url, "/");
    String artifactoryUrl = defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

    String username = step.username;
    String password = step.password;
    String credentialsId = step.credentialsId;

    ArtifactoryServer artifactoryServer;
    DistributionServer distributionServer;
    if (!isEmpty(credentialsId)) {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, credentialsId);
        distributionServer = new DistributionServer(distributionUrl, credentialsId);
    } else {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, username, password);
        distributionServer = new DistributionServer(distributionUrl, username, password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```