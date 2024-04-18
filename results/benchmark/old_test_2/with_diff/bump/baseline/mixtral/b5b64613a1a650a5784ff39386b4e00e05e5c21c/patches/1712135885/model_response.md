Here's a fixed version of the `run()` method that should resolve the compilation error:

```java
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (StringUtils.isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = StringUtils.removeEnd(step.url, "/");
    String artifactoryUrl = StringUtils.defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = StringUtils.defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

    ArtifactoryServer artifactoryServer;
    DistributionServer distributionServer;
    if (!StringUtils.isEmpty(step.credentialsId)) {
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

The changes made are:

1. Imported `org.apache.commons.lang3.StringUtils` to replace the removed `isAllBlank`, `removeEnd`, `defaultIfBlank`, and `isEmpty` methods.
2. Replaced the removed `isAllBlank` method with `StringUtils.isAllBlank`.
3. Replaced the removed `removeEnd` method with `StringUtils.removeEnd`.
4. Replaced the removed `defaultIfBlank` method with `StringUtils.defaultIfBlank`.
5. Replaced the removed `isEmpty` method with `StringUtils.isEmpty`.