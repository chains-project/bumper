```java
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (step.url == null && step.artifactoryUrl == null && step.distributionUrl == null) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = step.url != null ? step.url.replaceFirst("/$", "") : null;
    String artifactoryUrl = step.artifactoryUrl != null ? step.artifactoryUrl : (urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = step.distributionUrl != null ? step.distributionUrl : (urlWithoutSlash + "/" + "distribution");

    ArtifactoryServer artifactoryServer;
    DistributionServer distributionServer;
    if (step.credentialsId != null && !step.credentialsId.isEmpty()) {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.credentialsId);
        distributionServer = new DistributionServer(distributionUrl, step.credentialsId);
    } else {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.username, step.password);
        distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```