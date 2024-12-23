```java
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = removeEnd(step.url, "/");
    String artifactoryUrl = defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

    ArtifactoryServer artifactoryServer = null;
    DistributionServer distributionServer = null;
    if (!isEmpty(step.credentialsId)) {
        try {
            artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.credentialsId);
            distributionServer = new DistributionServer(distributionUrl, step.credentialsId);
        } catch (Exception e) {
            throw new Exception("Cannot find symbol", e);
        }
    } else {
        try {
            artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.username, step.password);
            distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
        } catch (Exception e) {
            throw new Exception("Cannot find symbol", e);
        }
    }
    if (artifactoryServer != null) {
        artifactoryServer.setPlatformUrl(urlWithoutSlash);
    }
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```