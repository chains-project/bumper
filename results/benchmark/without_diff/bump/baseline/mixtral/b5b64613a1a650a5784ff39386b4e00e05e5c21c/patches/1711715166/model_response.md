Here is a fixed version of the `run` method that should resolve the "cannot find symbol" error:

```java
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
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.credentialsId);
        distributionServer = new DistributionServer(distributionUrl, step.credentialsId);
    } else {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.username, step.password);
        distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
    }
    artifactoryServer.setUrl(urlWithoutSlash); // changed to 'setUrl' instead of 'setPlatformUrl'
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```

The error message suggests that the `ArtifactoryServer` class is missing a `setPlatformUrl` method. I replaced the call to `setPlatformUrl` with `setUrl` instead, which should resolve the issue.

If this change still does not resolve the issue, it is possible that the `ArtifactoryServer` and `DistributionServer` classes have been removed or renamed in the external dependency. In this case, you may need to update the external dependency to a compatible version.