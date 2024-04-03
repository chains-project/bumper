Here's the fixed `run()` method with the error resolved:

```java
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (StringUtils.isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = urlWithoutSlash(step.url);
    String artifactoryUrl = defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

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

private String urlWithoutSlash(String url) {
    return url != null ? url.endsWith("/") ? url.substring(0, url.length() - 1) : url : url;
}
```

The changes include:

1. Imported `org.apache.commons.lang3.StringUtils` to use `StringUtils.isAllBlank` and `StringUtils.isEmpty`.
2. Imported `org.apache.commons.lang3.StringUtils` to use `StringUtils.defaultIfBlank`.
3. Replaced the custom `isAllBlank` method with `StringUtils.isAllBlank`.
4. Replaced the custom `isEmpty` method with `StringUtils.isEmpty`.
5. Replaced the custom `defaultIfBlank` method with `StringUtils.defaultIfBlank`.
6. Added a new utility method `urlWithoutSlash` to replace the `removeEnd` method.