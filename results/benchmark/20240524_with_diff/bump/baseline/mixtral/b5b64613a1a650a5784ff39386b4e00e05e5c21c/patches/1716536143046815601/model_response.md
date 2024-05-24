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

The changes include:

* Importing the `StringUtils` class from `org.apache.commons.lang3` package.
* Replacing the `isAllBlank` method with `StringUtils.isAllBlank`.
* Replacing the `removeEnd` method with `StringUtils.removeEnd`.
* Replacing the `defaultIfBlank` method with `StringUtils.defaultIfBlank`.
* Replacing the `isEmpty` method with `StringUtils.isEmpty`.