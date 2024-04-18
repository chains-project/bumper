Here's a proposed patch to fix the error:

```java
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = removeEnd(step.url, "/");
    String artifactoryUrl = defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

    ArtifactoryServer artifactoryServer;
    DistributionServer distributionServer;
    if (!isEmpty(step.credentialsId)) {
        artifactoryServer = new ArtifactoryServerImpl(artifactoryUrl, step.credentialsId);
        distributionServer = new DistributionServerImpl(distributionUrl, step.credentialsId);
    } else {
        artifactoryServer = new ArtifactoryServerImpl(artifactoryUrl, step.username, step.password);
        distributionServer = new DistributionServerImpl(distributionUrl, step.username, step.password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```

The only change made to the code is to replace `ArtifactoryServer` and `DistributionServer` with `ArtifactoryServerImpl` and `DistributionServerImpl`, respectively. This assumes that the missing symbol is a class that was removed from the external dependency and replaced with a new implementation.